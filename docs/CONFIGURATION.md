# Configuration

Configs are versioned YAML files under `configs/`. `agentproof.config` loads them into
typed, frozen Pydantic models and fingerprints each one.

```python
from agentproof.config import load_config, load_research_study

agent = load_config("configs/agents/example_agent.yaml")      # kind inferred from directory
study = load_research_study("configs/research/robustness_study.yaml")
study.benchmark.config.capabilities.fault_injection           # typed access
study.provenance()                                            # per-config path + hashes
```

## Kinds

| Directory | Kind | Model |
|---|---|---|
| `configs/benchmarks/` | `benchmark` | `BenchmarkConfig` |
| `configs/agents/` | `agent` | `AgentConfig` |
| `configs/reliability/` | `reliability` | `ReliabilityConfig` |
| `configs/perturbations/` | `perturbation` | `PerturbationConfig` |
| `configs/faults/` | `fault` | `FaultConfig` |
| `configs/recovery/` | `recovery` | `RecoveryConfig` |
| `configs/research/` | `research` | `ResearchConfig` |

Files elsewhere need an explicit `kind=`. Gate, trace, MCP, and demo configs are loaded
by their owning modules in later tasks.

## Validation

- Unknown keys, duplicate YAML keys, and type coercion (e.g. `"1"` for an integer) are errors.
- Referenced files (`*_source`, `*_config`, `tools.source`) must be repo-relative, stay
  inside the repository, and exist.
- Research studies must reference configs of the matching kind; each is loaded and validated.
- Integrity rules enforced at load time:
  - enabled benchmarks pin `benchmark_version` and keep `task_source` separate from `grader_source`;
  - `cross_run_memory` must be false (agent memory and study run isolation);
  - confidence channels are typed: `self_reported`, `external_predictor`, or `heuristic`;
  - an enabled reliability aggregate must declare `formula` and `normalization`;
  - a perturbation cannot be both semantics-preserving and semantics-changing;
  - fault configs keep `do_not_corrupt_grader: true`;
  - recovery verifiers never get `gold_answer_access`.

Failures raise `ConfigError` with the repo-relative file path and the failing field.

## Provenance

Each `LoadedConfig` carries a `ConfigProvenance`:

- `path`: repo-relative POSIX path;
- `content_sha256`: hash of the raw file bytes;
- `canonical_sha256`: hash of the validated values (sorted-key JSON), stable across
  comments and formatting, so it identifies the effective configuration a run used.
