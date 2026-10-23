# Agent SLO & Budget Policy

AgentProof can express release objectives as engineering policies.

Examples:
- success >= 90% on golden critical tasks,
- all-k >= 80% for critical workflows,
- critical safety violations = 0,
- p95 latency <= 20 s,
- cost/success <= $0.10,
- timeout-fault recovery >= 85%,
- grader/environment error <= 1%.

Numbers above are examples only.
Each repository/team chooses and versions its own thresholds.

## Severity

Rules may be:
- informational,
- warning,
- blocking.

## Budget-aware evaluation

The evaluation run itself has a budget:
- maximum total spend,
- maximum runs/task,
- maximum wall time,
- maximum external tool calls.
