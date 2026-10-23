# AgentProof — Claude Code Instructions

AgentProof evaluates AI agents for reliability, robustness, predictability, recovery, safety, and cost.

## Read before every task

Read:
1. `docs/PROJECT_PHASES_AND_TASKS.md`
2. `docs/PRACTICAL_MVP.md`
3. `docs/BENCHMARK_ADAPTER_CONTRACT.md`
4. `docs/BENCHMARK_INTEGRITY_POLICY.md`
5. `docs/RUN_REPRODUCIBILITY.md`
6. `docs/MULTIRUN_PROTOCOL.md`
7. `docs/TRAJECTORY_CONTRACT.md`
8. `docs/RELIABILITY_METRICS.md`
9. `docs/PERTURBATION_PROTOCOL.md`
10. `docs/FAULT_INJECTION.md`
11. `docs/CONFIDENCE_AND_CALIBRATION.md`
12. `docs/FAILURE_TAXONOMY.md`
13. `docs/RECOVERY_POLICY.md`
14. `docs/COST_ACCOUNTING.md`
15. `docs/EVALUATION_PROTOCOL.md`
16. `docs/GIT_WORKFLOW.md`
17. `docs/FAST_TRACK_MVP.md`
18. `docs/TRACE_INGESTION.md`
19. `docs/RELEASE_GATING.md`
20. `docs/INCIDENT_TO_EVAL.md`
21. `docs/MCP_CONTRACT_TESTING.md`
22. `docs/CLI_SPEC.md`

## Mandatory task workflow

1. Read exact task scope/dependencies.
2. Inspect Git status/branch/remote.
3. Implement only the requested task.
4. Add deterministic tests/fixtures.
5. Run relevant tests and integrity checks.
6. Update task docs.
7. Run `git diff --check`.
8. Stage only task files.
9. Commit `task(<task-id>): <short imperative summary>`.
10. Push and verify upstream.
11. STOP.

## Critical integrity rules

- Never leak hidden benchmark answers or prior successful trajectories into fresh runs.
- Represent model, scaffold, system prompt, tools, memory, and reasoning settings separately.
- Repeated runs must be independent.
- Keep grader/environment failures separate from agent failures.
- Confidence channels must be typed: self-reported, external predictor, or heuristic.
- Semantics-preserving and semantics-changing perturbations are distinct.
- Recovery systems never receive gold answers.
- Safety uses sandbox/mock tools; never perform real irreversible actions.
- Cost tables are versioned by provider/model/effective date.
- Do not publish private/encrypted benchmark traces.
- Reliability dimensions remain separately visible; do not hide everything behind one score.
## Product Priority

AgentProof is not only a benchmark runner. Treat baseline-vs-candidate release gating, regression sets, trace interoperability, and incident-to-eval learning as first-class product requirements.

Prefer standards-based integration:
- OTLP/OpenTelemetry for external trace ingestion;
- MCP-aware tool contract testing where applicable;
- versioned YAML release policies.

A candidate release must never be declared safe from one aggregate score. Preserve explicit blocking reasons and dimension-level evidence.

