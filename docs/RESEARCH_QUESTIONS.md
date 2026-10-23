# Research Questions

## Product question

Can a multi-run, trace-aware release gate detect meaningful agent regressions that ordinary single-run accuracy misses?

## Research questions

1. How large is the gap between pass@k capability and all-k reliability?
2. Does robustness under controlled perturbations predict later incident-prone behavior better than base success alone?
3. Does confidence calibration enable useful selective abstention before failure?
4. Which partial-trajectory signals predict failure early enough for intervention?
5. When do retry/verifier policies improve success enough to justify their cost and latency?
6. Do model upgrades and scaffold/tool changes affect different reliability dimensions differently?
7. How often do tool contract/schema changes create regressions even when model quality is unchanged?
8. Can incident-derived golden cases reduce recurrence across later agent versions?
9. Which release-gate dimensions best correlate with real/shadow evaluation failures?
10. What is the reliability–cost–latency Pareto frontier across agent configurations?
11. How sensitive are conclusions to benchmark/grader quality?
12. How stable are reliability profiles across benchmark and production-like task distributions?
