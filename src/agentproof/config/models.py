"""Typed configuration models.

Every model forbids unknown keys so typos fail loudly instead of being silently
ignored. Paths to other repository files are kept as repo-relative POSIX strings
(``RepoPath``); the loader resolves and checks them. Integrity rules from
``CLAUDE.md`` that can be decided from a single file are enforced here.
"""

from __future__ import annotations

from enum import StrEnum
from pathlib import PurePosixPath
from typing import Annotated, Literal

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, model_validator


def _check_repo_path(value: str) -> str:
    path = PurePosixPath(value)
    if "\\" in value or path.is_absolute() or (value[1:2] == ":"):
        raise ValueError(f"path must be repo-relative POSIX, got {value!r}")
    if any(part == ".." for part in path.parts):
        raise ValueError(f"path must not escape the repository, got {value!r}")
    if not path.parts or str(path) == ".":
        raise ValueError("path must not be empty")
    return str(path)


RepoPath = Annotated[str, Field(min_length=1), AfterValidator(_check_repo_path)]
Identifier = Annotated[str, Field(min_length=1, pattern=r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")]
PositiveInt = Annotated[int, Field(ge=1)]


class ConfigKind(StrEnum):
    BENCHMARK = "benchmark"
    AGENT = "agent"
    RELIABILITY = "reliability"
    PERTURBATION = "perturbation"
    FAULT = "fault"
    RECOVERY = "recovery"
    RESEARCH = "research"


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)


# --- benchmark -------------------------------------------------------------


class BenchmarkCapabilities(StrictModel):
    """Capabilities from docs/BENCHMARK_ADAPTER_CONTRACT.md; undeclared means unsupported."""

    deterministic_reset: bool = False
    exact_grader: bool = False
    prompt_perturbation: bool = False
    structural_perturbation: bool = False
    fault_injection: bool = False
    environment_snapshot: bool = False
    tool_schema_instrumentation: bool = False
    cost_capture: bool = False
    trajectory_capture: bool = False


class GraderSpec(StrictModel):
    type: Identifier
    version: PositiveInt | None = None


class BenchmarkConfig(StrictModel):
    benchmark_id: Identifier
    benchmark_version: PositiveInt | None = None
    adapter: Identifier
    enabled: bool = True
    subset: Identifier | None = None
    expected_instances: PositiveInt | None = None
    task_source: RepoPath | None = None
    grader_source: RepoPath | None = None
    grader: GraderSpec | None = None
    capabilities: BenchmarkCapabilities = BenchmarkCapabilities()
    requirements: dict[Identifier, bool] = {}
    guards: dict[Identifier, bool] = {}
    reliability: dict[Identifier, bool | Literal["optional"]] = {}

    @model_validator(mode="after")
    def _integrity(self) -> BenchmarkConfig:
        if self.enabled:
            if self.benchmark_version is None:
                raise ValueError("enabled benchmarks must pin benchmark_version")
            if self.task_source is None:
                raise ValueError("enabled benchmarks must declare task_source")
        if self.task_source is not None and self.task_source == self.grader_source:
            raise ValueError(
                "task_source (agent-visible) and grader_source (hidden) must be separate files"
            )
        return self


# --- agent -----------------------------------------------------------------


class ModelSpec(StrictModel):
    provider: Identifier
    model_id: Identifier
    model_version: str | None = None


class ScaffoldSpec(StrictModel):
    name: Identifier
    version: PositiveInt


class SystemPromptSpec(StrictModel):
    prompt_id: Identifier
    version: PositiveInt
    source: RepoPath | None = None


class ReasoningSpec(StrictModel):
    effort: Identifier | None = None
    max_reasoning_tokens: PositiveInt | None = None


class ConfidenceChannel(StrEnum):
    SELF_REPORTED = "self_reported"
    EXTERNAL_PREDICTOR = "external_predictor"
    HEURISTIC = "heuristic"


class ConfidenceSpec(StrictModel):
    channel: ConfidenceChannel = Field(strict=False)
    schema_: Identifier = Field(alias="schema")

    model_config = ConfigDict(populate_by_name=True)


class MemorySpec(StrictModel):
    cross_run_memory: bool

    @model_validator(mode="after")
    def _independent_runs(self) -> MemorySpec:
        if self.cross_run_memory:
            raise ValueError("cross_run_memory must be false: repeated runs must be independent")
        return self


class ToolsSpec(StrictModel):
    source: RepoPath


class AgentConfig(StrictModel):
    """Model, scaffold, system prompt, tools, memory, and reasoning stay separate fields."""

    agent_id: Identifier
    agent_version: PositiveInt
    model: ModelSpec
    scaffold: ScaffoldSpec
    system_prompt: SystemPromptSpec | None = None
    reasoning: ReasoningSpec | None = None
    confidence: ConfidenceSpec | None = None
    memory: MemorySpec
    tools: ToolsSpec | None = None


# --- reliability -----------------------------------------------------------


class ReliabilityDimensions(StrictModel):
    capability: bool
    consistency: bool
    predictability: bool
    robustness: bool
    recovery: bool
    safety: bool
    economics: bool


class ConsistencySpec(StrictModel):
    outcome: bool = True
    resource_variance: bool = True
    trajectory_action_distribution: bool = True
    trajectory_sequence: bool = True


class PredictabilitySpec(StrictModel):
    brier: bool = True
    auroc: bool = True
    reliability_curve: bool = True
    risk_coverage: bool = True


class AggregateSpec(StrictModel):
    enabled: bool = False
    formula: str | None = None
    normalization: str | None = None

    @model_validator(mode="after")
    def _explicit_formula(self) -> AggregateSpec:
        if self.enabled and not (self.formula and self.normalization):
            raise ValueError("an enabled aggregate must declare its formula and normalization")
        return self


class ReliabilityConfig(StrictModel):
    version: PositiveInt
    runs_per_task: PositiveInt
    dimensions: ReliabilityDimensions
    consistency: ConsistencySpec = ConsistencySpec()
    predictability: PredictabilitySpec = PredictabilitySpec()
    aggregate: AggregateSpec = AggregateSpec()


# --- perturbations ---------------------------------------------------------

SemanticsPreservingPerturbation = Literal[
    "prompt_paraphrase",
    "reorder_independent_fields",
    "add_irrelevant_context",
    "harmless_format_change",
]
StructuralPerturbation = Literal["tool_response_field_order", "optional_metadata_insertion"]


class SemanticsChangingSpec(StrictModel):
    enabled: bool = False
    variants: list[Identifier] = []

    @model_validator(mode="after")
    def _variants_need_enable(self) -> SemanticsChangingSpec:
        if self.variants and not self.enabled:
            raise ValueError("semantics_changing variants listed while disabled")
        return self


class PerturbationValidationSpec(StrictModel):
    require_invariant_check: bool = True


def _no_duplicates(values: list[str], label: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate entries in {label}")


class PerturbationConfig(StrictModel):
    version: PositiveInt
    semantics_preserving: list[SemanticsPreservingPerturbation] = []
    structural: list[StructuralPerturbation] = []
    semantics_changing: SemanticsChangingSpec = SemanticsChangingSpec()
    validation: PerturbationValidationSpec = PerturbationValidationSpec()

    @model_validator(mode="after")
    def _distinct_families(self) -> PerturbationConfig:
        _no_duplicates(list(self.semantics_preserving), "semantics_preserving")
        _no_duplicates(list(self.structural), "structural")
        _no_duplicates(self.semantics_changing.variants, "semantics_changing.variants")
        preserving = set(self.semantics_preserving) | set(self.structural)
        overlap = preserving & set(self.semantics_changing.variants)
        if overlap:
            raise ValueError(
                "perturbations cannot be both semantics-preserving and -changing: "
                f"{sorted(overlap)}"
            )
        return self


# --- faults ----------------------------------------------------------------

FaultKind = Literal[
    "timeout_once",
    "http_500_once",
    "rate_limit_once",
    "malformed_json_once",
    "missing_optional_field",
    "delayed_tool_response",
]


class FaultGuards(StrictModel):
    do_not_corrupt_grader: bool = True
    log_fault_trigger: bool = True

    @model_validator(mode="after")
    def _grader_untouched(self) -> FaultGuards:
        if not self.do_not_corrupt_grader:
            raise ValueError("fault configs must keep do_not_corrupt_grader: true")
        return self


class FaultConfig(StrictModel):
    version: PositiveInt
    faults: list[FaultKind] = Field(min_length=1)
    guards: FaultGuards = FaultGuards()

    @model_validator(mode="after")
    def _unique(self) -> FaultConfig:
        _no_duplicates(list(self.faults), "faults")
        return self


# --- recovery --------------------------------------------------------------

RecoveryPolicyName = Literal[
    "none", "retry_once", "replan_once", "verifier_then_retry", "selective_abstention"
]


class VerifierSpec(StrictModel):
    gold_answer_access: bool = False

    @model_validator(mode="after")
    def _gold_free(self) -> VerifierSpec:
        if self.gold_answer_access:
            raise ValueError("recovery verifiers must never receive gold answers")
        return self


class RecoveryComparisonSpec(StrictModel):
    matched_conditions: bool = True
    report_cost_overhead: bool = True


class RecoveryConfig(StrictModel):
    version: PositiveInt
    policies: list[RecoveryPolicyName] = Field(min_length=1)
    verifier: VerifierSpec = VerifierSpec()
    comparison: RecoveryComparisonSpec = RecoveryComparisonSpec()

    @model_validator(mode="after")
    def _unique(self) -> RecoveryConfig:
        _no_duplicates(list(self.policies), "policies")
        return self


# --- research study --------------------------------------------------------


class BudgetSpec(StrictModel):
    max_cost_usd: Annotated[float, Field(ge=0, strict=False)]
    max_wall_minutes: Annotated[float, Field(gt=0, strict=False)]


class RunIsolationSpec(StrictModel):
    reset_environment: bool = True
    cross_run_memory: bool = False

    @model_validator(mode="after")
    def _independent_runs(self) -> RunIsolationSpec:
        if self.cross_run_memory:
            raise ValueError("cross_run_memory must be false: repeated runs must be independent")
        return self


# Research-study fields that reference another config, with the kind it must be.
RESEARCH_REFERENCES: dict[str, ConfigKind] = {
    "benchmark_config": ConfigKind.BENCHMARK,
    "agent_config": ConfigKind.AGENT,
    "reliability_config": ConfigKind.RELIABILITY,
    "perturbation_config": ConfigKind.PERTURBATION,
    "fault_config": ConfigKind.FAULT,
    "recovery_config": ConfigKind.RECOVERY,
}


class ResearchConfig(StrictModel):
    name: Identifier
    benchmark_config: RepoPath
    agent_config: RepoPath
    reliability_config: RepoPath | None = None
    perturbation_config: RepoPath | None = None
    fault_config: RepoPath | None = None
    recovery_config: RepoPath | None = None
    runs_per_task: PositiveInt | None = None
    budget: BudgetSpec | None = None
    run_isolation: RunIsolationSpec = RunIsolationSpec()
    matched_baseline: bool | None = None
    matched_conditions: bool | None = None
    report_cost_latency_overhead: bool | None = None

    @model_validator(mode="after")
    def _study_shape(self) -> ResearchConfig:
        if self.matched_baseline and not (self.perturbation_config or self.fault_config):
            raise ValueError("matched_baseline requires a perturbation_config or fault_config")
        if self.matched_conditions and not self.recovery_config:
            raise ValueError("matched_conditions requires a recovery_config")
        return self


CONFIG_MODELS: dict[ConfigKind, type[StrictModel]] = {
    ConfigKind.BENCHMARK: BenchmarkConfig,
    ConfigKind.AGENT: AgentConfig,
    ConfigKind.RELIABILITY: ReliabilityConfig,
    ConfigKind.PERTURBATION: PerturbationConfig,
    ConfigKind.FAULT: FaultConfig,
    ConfigKind.RECOVERY: RecoveryConfig,
    ConfigKind.RESEARCH: ResearchConfig,
}
