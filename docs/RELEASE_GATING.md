# Candidate vs Baseline Release Gating

## Comparison unit

A candidate and baseline must be compared on compatible:
- task set/version,
- benchmark/environment,
- grader,
- perturbation/fault schedule,
- run-count policy.

## Gate dimensions

Possible policies:
- minimum success/non-regression,
- all-k reliability non-regression,
- robustness floor,
- zero new critical safety violations,
- maximum cost/success increase,
- maximum p95 latency increase,
- minimum task coverage,
- maximum grader/environment error rate.

## Result

Each policy rule returns:
- PASS
- WARN
- BLOCK
- NOT_EVALUABLE

Overall release status follows explicit severity rules, not an opaque weighted score.

## Statistical support

Where sample sizes permit, include paired task deltas and confidence intervals.
A gate can require both a magnitude threshold and statistical evidence, but the policy must declare this explicitly.
