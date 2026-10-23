# Architecture Rules
Canonical flow:
Benchmark Adapter → Frozen Task/Environment → Agent Adapter → Repeated Runs → Trajectory Store → Grader → Reliability Metrics → Perturbation/Fault Runs → Recovery → Cost/Statistics → Dashboard.
Reporting reads immutable run artifacts only.
