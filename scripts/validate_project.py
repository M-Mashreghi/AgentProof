"""Repository integrity validator for AgentProof.

Checks required files, config/fixture parseability, agent-visible vs grader-only
data separation, referenced paths, task-graph consistency, markdown links,
stale terms, and private-artifact hygiene. Exits non-zero on the first failure.
"""

import json
import re
import sys
import tomllib
from collections.abc import Iterator
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print(f"PyYAML import failed: {exc}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]

# Local environments and tool caches are not part of the repository surface.
EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "build",
    "dist",
}

REQUIRED = [
    "README.md",
    "CLAUDE.md",
    "PROJECT_STRUCTURE.md",
    "pyproject.toml",
    "docs/PROJECT_PHASES_AND_TASKS.md",
    "docs/TASK_DEPENDENCIES.md",
    "docs/TASKS.md",
    "docs/BENCHMARK_INTEGRITY_POLICY.md",
    "docs/RELIABILITY_METRICS.md",
    "docs/EVALUATION_PROTOCOL.md",
    "docs/GIT_WORKFLOW.md",
    "docs/FINAL_AUDIT.md",
    "src/agentproof/__init__.py",
    "src/agentproof/cli.py",
]
GOLD_KEYS = {"expected", "gold", "gold_answer", "reference_answer", "winning_outcome"}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".toml", ".json", ".jsonl", ".sh"}
REF_PATTERNS = [
    re.compile(r"(configs/[A-Za-z0-9_./-]+\.(?:yaml|yml))(?![A-Za-z0-9])"),
    re.compile(r"(examples/[A-Za-z0-9_./-]+\.(?:jsonl|json|yaml|yml|md))(?![A-Za-z0-9])"),
]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BAD_TERMS = [
    "TODO", "TBD", "FIXME", "CHANGEME", "your-repo", "example.com", "MacroSignal",
    "FlowBook", "MicroEdge", "CaseMind", "QuizForge", "FedTone", "ImpactLens",
    "EquityDesk", "FilingLens",
]


def fail(message: str) -> None:
    print(message)
    sys.exit(1)


def iter_files(*suffixes: str) -> Iterator[Path]:
    """Yield repository files (sorted), skipping local environments and caches."""
    for path in sorted(ROOT.rglob("*")):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts[:-1]):
            continue
        if not path.is_file():
            continue
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def rel(path: Path) -> Path:
    return path.relative_to(ROOT)


def check_required_files() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail(f"Missing required files: {missing}")


def check_pyproject() -> None:
    with open(ROOT / "pyproject.toml", "rb") as f:
        project = tomllib.load(f)
    if project["project"]["name"] != "agentproof":
        fail("Unexpected project name")
    if project["project"]["scripts"].get("agentproof") != "agentproof.cli:app":
        fail("Broken CLI entry point")


def check_parseable() -> None:
    for path in iter_files(".yaml", ".yml"):
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            fail(f"Invalid YAML {rel(path)}: {exc}")
    for path in iter_files(".json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"Invalid JSON {rel(path)}: {exc}")
    for path in iter_files(".jsonl"):
        lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                fail(f"Invalid JSONL {rel(path)}:{lineno}: {exc}")


def check_task_sources() -> None:
    """Agent-visible configured task sources must not contain grader-only gold fields."""
    for cfg_path in iter_files(".yaml", ".yml"):
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        if not isinstance(cfg, dict):
            continue
        task_source = cfg.get("task_source")
        if not task_source:
            continue
        task_path = ROOT / task_source
        if not task_path.exists():
            fail(f"Configured task_source does not exist: {task_source}")
        if task_path.suffix == ".jsonl":
            lines = task_path.read_text(encoding="utf-8").splitlines()
            for lineno, line in enumerate(lines, start=1):
                if not line.strip():
                    continue
                leaked = sorted(GOLD_KEYS.intersection(json.loads(line)))
                if leaked:
                    fail(
                        f"Gold/grader fields leaked into agent-visible task source "
                        f"{task_source}:{lineno}: {leaked}"
                    )
        grader_source = cfg.get("grader_source")
        if grader_source and not (ROOT / grader_source).exists():
            fail(f"Configured grader_source does not exist: {grader_source}")


def check_referenced_paths() -> None:
    for path in iter_files(*TEXT_SUFFIXES):
        content = read_text(path)
        if content is None:
            continue
        for pattern in REF_PATTERNS:
            for ref in pattern.findall(content):
                if not (ROOT / ref).exists():
                    fail(f"Missing referenced file {ref} from {rel(path)}")


def check_task_graph() -> list[str]:
    task_text = (ROOT / "docs/PROJECT_PHASES_AND_TASKS.md").read_text(encoding="utf-8")
    ids = re.findall(r"^### Task (\d+\.\d+):", task_text, flags=re.MULTILINE)
    if len(ids) != len(set(ids)):
        fail("Duplicate task IDs")
    order = {tid: i for i, tid in enumerate(ids)}
    graph: dict[str, list[str]] = {tid: [] for tid in ids}
    dep_pattern = r"^### Task (\d+\.\d+):.*?^\*\*Depends on:\*\* `([^`]+)`"
    for m in re.finditer(dep_pattern, task_text, flags=re.MULTILINE | re.DOTALL):
        tid, depstr = m.group(1), m.group(2)
        if depstr == "None":
            continue
        for dep in [x.strip() for x in depstr.split(",")]:
            if dep not in order:
                fail(f"Unknown dependency {tid}->{dep}")
            if order[dep] >= order[tid]:
                fail(f"Forward dependency {tid}->{dep}")
            graph[tid].append(dep)

    state = dict.fromkeys(ids, 0)

    def visit(node: str) -> None:
        if state[node] == 1:
            raise RuntimeError(f"Dependency cycle involving {node}")
        if state[node] == 2:
            return
        state[node] = 1
        for dep in graph[node]:
            visit(dep)
        state[node] = 2

    try:
        for node in ids:
            visit(node)
    except RuntimeError as exc:
        fail(str(exc))

    ledger = (ROOT / "docs/TASKS.md").read_text(encoding="utf-8")
    ledger_ids = re.findall(r"\*\*Task (\d+\.\d+)\*\*", ledger)
    if ledger_ids != ids:
        fail("TASKS.md mismatch")
    return ids


def check_markdown_links() -> None:
    for md in iter_files(".md"):
        content = md.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(content):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (md.parent / file_part).resolve().exists():
                fail(f"Broken link {rel(md)} -> {target}")


def check_stale_terms() -> None:
    this_file = Path(__file__).resolve()
    for path in iter_files(*TEXT_SUFFIXES):
        if path.resolve() == this_file:
            continue
        content = read_text(path)
        if content is None:
            continue
        for term in BAD_TERMS:
            if term in content:
                fail(f"Stale/forbidden term {term!r} in {rel(path)}")


def check_private_artifacts() -> None:
    if (ROOT / ".env").exists():
        fail(".env must not be committed")
    for name in ["private_benchmarks", "private_traces", "encrypted_traces"]:
        p = ROOT / name
        if p.exists() and any(x.is_file() for x in p.rglob("*")):
            fail(f"Private artifact files found in {name}")


def check_package_inits() -> None:
    for d in sorted((ROOT / "src/agentproof").rglob("*")):
        if not d.is_dir() or d.name in EXCLUDED_DIRS:
            continue
        if not (d / "__init__.py").exists():
            fail(f"Missing __init__.py: {rel(d)}")


def main() -> None:
    check_required_files()
    check_pyproject()
    check_parseable()
    check_task_sources()
    check_referenced_paths()
    ids = check_task_graph()
    check_markdown_links()
    check_stale_terms()
    check_private_artifacts()
    check_package_inits()
    print(
        f"AgentProof release validation passed: {len(ids)} unique tasks, "
        "configs/links/dependencies clean."
    )


if __name__ == "__main__":
    main()
