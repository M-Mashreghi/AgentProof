"""Load YAML configs into typed models with provenance.

``load_config`` parses one file, validates it against the model for its kind,
and checks that every referenced repository path exists. ``load_research_study``
also loads each config a research study references, checking that each one is
of the expected kind. Every loaded config carries a ``ConfigProvenance`` with
both a raw-bytes hash and a canonical hash of the validated values, so runs can
pin exactly which configuration they used.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generic, TypeVar, cast

import yaml
from pydantic import BaseModel, ValidationError

from agentproof.config.models import (
    CONFIG_MODELS,
    RESEARCH_REFERENCES,
    AgentConfig,
    BenchmarkConfig,
    ConfigKind,
    FaultConfig,
    PerturbationConfig,
    RecoveryConfig,
    ReliabilityConfig,
    ResearchConfig,
    StrictModel,
)

ModelT = TypeVar("ModelT", bound=StrictModel)

# configs/<directory>/ -> kind, for kind inference.
DIRECTORY_KINDS: dict[str, ConfigKind] = {
    "benchmarks": ConfigKind.BENCHMARK,
    "agents": ConfigKind.AGENT,
    "reliability": ConfigKind.RELIABILITY,
    "perturbations": ConfigKind.PERTURBATION,
    "faults": ConfigKind.FAULT,
    "recovery": ConfigKind.RECOVERY,
    "research": ConfigKind.RESEARCH,
}


class ConfigError(ValueError):
    """A configuration file could not be loaded or failed validation."""


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate mapping keys instead of keeping the last one."""


def _construct_unique_mapping(loader: _UniqueKeyLoader, node: yaml.MappingNode) -> dict[Any, Any]:
    seen: set[Any] = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        seen.add(key)
    return loader.construct_mapping(node)


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)


@dataclass(frozen=True)
class ConfigProvenance:
    kind: ConfigKind
    path: str  # repo-relative POSIX path
    content_sha256: str  # hash of the raw file bytes
    canonical_sha256: str  # hash of the validated values; ignores comments/formatting


@dataclass(frozen=True)
class LoadedConfig(Generic[ModelT]):
    config: ModelT
    provenance: ConfigProvenance


@dataclass(frozen=True)
class ResearchStudy:
    study: LoadedConfig[ResearchConfig]
    benchmark: LoadedConfig[BenchmarkConfig]
    agent: LoadedConfig[AgentConfig]
    reliability: LoadedConfig[ReliabilityConfig] | None
    perturbation: LoadedConfig[PerturbationConfig] | None
    fault: LoadedConfig[FaultConfig] | None
    recovery: LoadedConfig[RecoveryConfig] | None

    @property
    def runs_per_task(self) -> int | None:
        """Study override first, then the reliability config's value."""
        if self.study.config.runs_per_task is not None:
            return self.study.config.runs_per_task
        return self.reliability.config.runs_per_task if self.reliability else None

    def provenance(self) -> dict[str, ConfigProvenance]:
        items: dict[str, LoadedConfig[Any] | None] = {
            "research": self.study,
            "benchmark": self.benchmark,
            "agent": self.agent,
            "reliability": self.reliability,
            "perturbation": self.perturbation,
            "fault": self.fault,
            "recovery": self.recovery,
        }
        return {name: item.provenance for name, item in items.items() if item is not None}


def find_repo_root(start: Path) -> Path:
    """Nearest ancestor of ``start`` containing ``pyproject.toml``."""
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "pyproject.toml").is_file():
            return candidate
    raise ConfigError(f"no repository root (pyproject.toml) found above {start}")


def infer_kind(path: Path, root: Path) -> ConfigKind:
    parts = path.resolve().relative_to(root).parts
    if len(parts) >= 3 and parts[0] == "configs" and parts[1] in DIRECTORY_KINDS:
        return DIRECTORY_KINDS[parts[1]]
    raise ConfigError(f"cannot infer config kind for {path}; pass kind explicitly")


def canonical_hash(model: BaseModel) -> str:
    payload = json.dumps(
        model.model_dump(mode="json", by_alias=True), sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _referenced_paths(value: Any, field_path: str = "") -> list[tuple[str, str]]:
    """(field, path) pairs for every repo-path field, found by name convention."""
    found: list[tuple[str, str]] = []
    if isinstance(value, BaseModel):
        for name in type(value).model_fields:
            child = getattr(value, name)
            dotted = f"{field_path}.{name}" if field_path else name
            if isinstance(child, str) and (
                name.endswith(("_source", "_config")) or name == "source"
            ):
                found.append((dotted, child))
            else:
                found.extend(_referenced_paths(child, dotted))
    return found


def _resolve_in_root(root: Path, rel_path: str, origin: str) -> Path:
    resolved = (root / rel_path).resolve()
    if not resolved.is_relative_to(root):
        raise ConfigError(f"{origin}: {rel_path!r} resolves outside the repository")
    if not resolved.is_file():
        raise ConfigError(f"{origin}: referenced file does not exist: {rel_path}")
    return resolved


def load_config(
    path: str | Path,
    kind: ConfigKind | str | None = None,
    root: str | Path | None = None,
) -> LoadedConfig[Any]:
    """Load, validate, and fingerprint one config file."""
    file_path = Path(path)
    repo_root = Path(root).resolve() if root is not None else find_repo_root(file_path.parent)
    if not file_path.is_absolute():
        file_path = repo_root / file_path
    file_path = file_path.resolve()
    if not file_path.is_relative_to(repo_root):
        raise ConfigError(f"{path}: config must live inside the repository {repo_root}")
    rel = file_path.relative_to(repo_root).as_posix()
    if not file_path.is_file():
        raise ConfigError(f"{rel}: file does not exist")

    resolved_kind = ConfigKind(kind) if kind is not None else infer_kind(file_path, repo_root)
    raw = file_path.read_bytes()
    try:
        data = yaml.load(raw.decode("utf-8"), Loader=_UniqueKeyLoader)  # noqa: S506
    except (yaml.YAMLError, UnicodeDecodeError) as exc:
        raise ConfigError(f"{rel}: invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"{rel}: top level must be a mapping")

    model_cls = CONFIG_MODELS[resolved_kind]
    try:
        model = model_cls.model_validate(data)
    except ValidationError as exc:
        raise ConfigError(f"{rel}: invalid {resolved_kind.value} config:\n{exc}") from exc

    for field_name, ref in _referenced_paths(model):
        _resolve_in_root(repo_root, ref, f"{rel}:{field_name}")

    provenance = ConfigProvenance(
        kind=resolved_kind,
        path=rel,
        content_sha256=hashlib.sha256(raw).hexdigest(),
        canonical_sha256=canonical_hash(model),
    )
    return LoadedConfig(config=model, provenance=provenance)


def load_research_study(path: str | Path, root: str | Path | None = None) -> ResearchStudy:
    """Load a research study and every config it references, checking their kinds."""
    file_path = Path(path)
    repo_root = Path(root).resolve() if root is not None else find_repo_root(file_path.parent)
    study = cast(LoadedConfig[ResearchConfig], load_config(path, ConfigKind.RESEARCH, repo_root))

    loaded: dict[str, LoadedConfig[Any] | None] = {}
    for field_name, expected_kind in RESEARCH_REFERENCES.items():
        ref = getattr(study.config, field_name)
        if ref is None:
            loaded[field_name] = None
            continue
        ref_path = repo_root / ref
        try:
            inferred = infer_kind(ref_path, repo_root)
        except ConfigError:
            inferred = expected_kind
        if inferred is not expected_kind:
            raise ConfigError(
                f"{study.provenance.path}:{field_name}: expected a {expected_kind.value} "
                f"config, but {ref} is a {inferred.value} config"
            )
        loaded[field_name] = load_config(ref_path, expected_kind, repo_root)

    return ResearchStudy(
        study=study,
        benchmark=cast(LoadedConfig[BenchmarkConfig], loaded["benchmark_config"]),
        agent=cast(LoadedConfig[AgentConfig], loaded["agent_config"]),
        reliability=cast(LoadedConfig[ReliabilityConfig] | None, loaded["reliability_config"]),
        perturbation=cast(LoadedConfig[PerturbationConfig] | None, loaded["perturbation_config"]),
        fault=cast(LoadedConfig[FaultConfig] | None, loaded["fault_config"]),
        recovery=cast(LoadedConfig[RecoveryConfig] | None, loaded["recovery_config"]),
    )
