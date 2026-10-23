# Practical MVP

The first useful AgentProof product is **not** a giant benchmark leaderboard.
It is a candidate-vs-baseline release gate.

## MVP demonstration

1. Run a small SupportOps golden suite on baseline configuration.
2. Run the same suite on a candidate prompt/model/tool change.
3. Repeat each critical task multiple times.
4. Inject one timeout and one malformed tool payload condition.
5. Grade quality, reliability, safety, cost, and latency.
6. Compare candidate vs baseline.
7. Apply `configs/gates/pr_gate.yaml`.
8. Produce PASS/WARN/BLOCK with reasons.
9. Open one failed trace in Failure Explorer.
10. Convert that failure into a permanent regression case.

Then scale to GAIA/SWE-bench/OSWorld/TUA-Bench/ALE for research depth.
