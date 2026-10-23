# Pull Request Release Report

A PR report should be decision-oriented rather than a wall of benchmark metrics.

## Header

```text
AgentProof Gate: BLOCK
Candidate: pr-184
Baseline: main@abc123
Suite: supportops-critical-v3
```

## Required table

| Dimension | Baseline | Candidate | Delta | Rule | Status |
|---|---:|---:|---:|---|---|
| Success | ... | ... | ... | >= floor | PASS |
| All-k | ... | ... | ... | max regression | PASS/BLOCK |
| Robustness | ... | ... | ... | max regression | PASS/BLOCK |
| Safety | ... | ... | ... | no new critical | PASS/BLOCK |
| Cost/success | ... | ... | ... | max increase | WARN/BLOCK |
| p95 latency | ... | ... | ... | max increase | WARN/BLOCK |

## Blocking reasons

Use explicit statements, e.g.:

```text
BLOCK: timeout-fault robustness fell 7.2 percentage points; policy allows 5.0.
```

## Drilldowns

Link/path to:
- failed critical tasks,
- new safety violations,
- trace diffs,
- cost outliers,
- grader/environment errors,
- full immutable evaluation manifest.
