# AgentProof — AI Agent Reliability & Release-Gating Platform

AgentProof is a **production-oriented evaluation and release-gating platform for AI agents**.
It combines benchmark research with the workflow a real team needs before shipping an agent change.

## Product question

> Did this agent change make the system more capable **without making it less reliable, more expensive, slower, or less safe**?

## Practical workflow

```text
Agent PR / Model / Prompt / Tool Change
                ↓
Replay Golden Regression Suite
                ↓
Repeated Independent Runs
                ↓
Trace Ingestion + Trace Grading
                ↓
Perturbations + Tool Fault Injection
                ↓
Baseline vs Candidate Diff
                ↓
Quality / Reliability / Cost / Latency / Safety Gates
                ↓
            PASS / BLOCK
                ↓
Incident → New Regression Case → Next Release Gate
```

AgentProof therefore has **two modes**:

1. **Research Mode** — multi-run reliability, robustness, failure analysis, benchmark studies.
2. **Release-Gate Mode** — compare a baseline agent with a candidate and decide whether the change is safe to ship under explicit policies.

## Why this is useful

A normal benchmark can say:

```text
Candidate success = 81%
Baseline success  = 79%
```

AgentProof asks the more useful questions:

```text
Did all-k reliability improve?
Did safety violations increase?
Did p95 latency regress?
Did cost per successful task increase?
Did tool-use robustness fall under timeouts?
Is the gain concentrated in a few easy tasks?
Is the candidate calibrated enough to abstain safely?
```

## Core evaluation dimensions

- **Capability:** success, pass@k, completion
- **Consistency:** all-k reliability, outcome/resource variance, trajectory stability
- **Predictability:** calibration, Brier, AUROC, risk-coverage
- **Robustness:** prompt/structural/tool-fault robustness
- **Recovery:** retry, replan, verifier, abstention/escalation
- **Safety:** policy and action-constraint violations
- **Economics:** cost/task, cost/success, tokens, tools, latency
- **Release fitness:** candidate-vs-baseline regression gates

## Production-friendly integrations

### Trace ingestion

AgentProof targets a normalized internal trace schema and can ingest:

- **OpenTelemetry / OTLP JSON** traces,
- exported **OpenAI agent traces** through their OTLP representation,
- native AgentProof traces,
- adapter-specific traces from other frameworks later.

The normalized trace keeps model calls, tool calls, handoffs/actions, errors, duration, token usage, and redaction metadata without relying on hidden chain-of-thought.

### MCP contract testing

MCP tools are treated like an API surface.
AgentProof can test:

- tool schema drift,
- required/optional field changes,
- invalid arguments,
- timeout/error behavior,
- idempotency/safe retry policy,
- side-effect classification,
- tool-result perturbations.

### Regression datasets

Production-like failures can become future eval cases:

```text
Failed trace / incident
        ↓
Redact sensitive data
        ↓
Minimize reproducible task
        ↓
Add expected invariant / grader
        ↓
Golden Regression Set
        ↓
Every future PR
```

## Release gate

Example command target:

```bash
agentproof gate \
  --baseline runs/main \
  --candidate runs/pr-184 \
  --policy configs/gates/pr_gate.yaml
```

Illustrative policy:

```text
quality regression        <= 2 percentage points
all-k reliability drop    <= 2 percentage points
new critical safety       = 0
cost/success increase     <= 20%
p95 latency increase      <= 15%
robustness drop            <= 5 percentage points
```

Thresholds are project-specific and versioned; they are not universal defaults.

## Incident learning loop

```text
Production Incident
→ import trace
→ classify failure
→ redact/minimize
→ create regression case
→ reproduce
→ fix agent/tool/prompt
→ candidate evaluation
→ release gate
```

This makes AgentProof useful after deployment, not only during a benchmark paper.

## Benchmarks

Research adapters include or plan support for:

- synthetic deterministic tasks
- custom JSONL/YAML tasks
- GAIA
- SWE-bench Verified
- τ-bench-style tool environments
- OSWorld / OSWorld 2.0
- TUA-Bench
- Agents' Last Exam / ALE-CLI

Adapters declare capabilities explicitly; AgentProof never pretends all benchmarks support the same reset, grading, perturbation, fault, or safety semantics.

## Reference demo packs

Two complementary mock demos are included:

### SupportOps
A transactional/tool agent that demonstrates policy compliance, side-effect safety, approvals, timeouts, malformed payloads, and escalation.

### ResearchOps
An evidence-grounded research agent that demonstrates citation precision/recall, unsupported-claim detection, conflicting/irrelevant sources, source freshness, and abstention under insufficient evidence.

All actions and data are local/mock; no real accounts or irreversible transactions are used.

## Fast-track MVP

Do **not** implement every advanced benchmark before showing a working product.
Follow `docs/FAST_TRACK_MVP.md` to reach a useful baseline-vs-candidate release gate first.

## Full architecture

```text
Benchmarks / Golden Sets / Production Traces
                    ↓
              Trace Normalization
                    ↓
Agent + Model + Scaffold + Tools
                    ↓
          Repeated / Perturbed Runs
                    ↓
       Grading + Reliability Metrics
                    ↓
       Failure / Recovery / Safety
                    ↓
          Baseline vs Candidate
                    ↓
              Release Policy
                    ↓
       PASS / WARN / BLOCK + Report
```

## Development

Requires Python 3.11+.

```bash
python -m pip install -e ".[dev]"   # or: make install
make ci                              # ruff + mypy + pytest + repository validator
agentproof version                   # also: python -m agentproof version
```

Start implementation with Task 1.1 in `docs/PROJECT_PHASES_AND_TASKS.md`.
