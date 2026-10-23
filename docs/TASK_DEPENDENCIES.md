# Task Dependencies

| Task | Depends on |
|---|---|
| 1.1 — Python Package Scaffold & Development Tooling | None |
| 1.2 — GitHub Remote & Per-Task Workflow Baseline | 1.1 |
| 1.3 — Typed Configuration Loader | 1.2 |
| 1.4 — BenchmarkMetadata & Task Domain Models | 1.3 |
| 1.5 — AgentEvaluationUnit Model | 1.4 |
| 1.6 — RunIdentity & Seed Model | 1.5 |
| 1.7 — Trajectory & Event Domain Models | 1.6 |
| 1.8 — GraderOutcome & FailureSource Model | 1.7 |
| 1.9 — CostUsage Domain Model | 1.8 |
| 1.10 — Perturbation / Fault / Recovery Condition Models | 1.9 |
| 1.11 — Research Protocol Registry | 1.10 |
| 1.12 — Artifact Registry & Repository Validator | 1.11 |
| 2.1 — BenchmarkAdapter Interface | 1.12 |
| 2.2 — Synthetic Benchmark Adapter | 2.1 |
| 2.3 — Custom JSONL / YAML Task Adapter | 2.2 |
| 2.4 — AgentAdapter Interface | 2.3 |
| 2.5 — Deterministic Mock Agent | 2.4 |
| 2.6 — Tool Instrumentation Layer | 2.5 |
| 2.7 — Environment Reset / Snapshot Contract | 2.6 |
| 2.8 — Grader Interface & Structured Grader | 2.1, 2.2, 2.3 |
| 2.9 — Grader Quality Fixture Tests | 2.8 |
| 2.10 — Single-Run Orchestrator | 2.4, 2.6, 2.7, 2.8 |
| 2.11 — Run Isolation Guard | 2.5, 2.7, 2.10 |
| 2.12 — Budget / Timeout / Parallel Scheduler | 2.11 |
| 3.1 — Repeated-Run Study Builder | 2.12 |
| 3.2 — Capability Metrics | 2.10 |
| 3.3 — All-K Repeated Success Reliability | 3.2 |
| 3.4 — Outcome Consistency Metrics | 3.3 |
| 3.5 — Resource Consistency Metrics | 3.4 |
| 3.6 — Normalized Trajectory Action Vocabulary | 3.5 |
| 3.7 — Trajectory Action-Distribution Similarity | 3.6 |
| 3.8 — Trajectory Sequence Similarity | 3.7 |
| 3.9 — Loop / Retry / Tool-Churn Diagnostics | 3.8 |
| 3.10 — Per-Task Reliability Profile | 3.2, 3.3, 3.4, 3.5, 3.7, 3.8 |
| 3.11 — Benchmark Reliability Summary | 3.10 |
| 3.12 — Deterministic Multi-Run Regression Fixture | 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8 |
| 4.1 — Self-Reported Confidence Protocol | 3.12 |
| 4.2 — Brier & Calibration Metrics | 4.1, 3.2 |
| 4.3 — Success Discrimination AUROC | 4.2 |
| 4.4 — Risk-Coverage / Selective Prediction | 4.1, 4.2 |
| 4.5 — PerturbationGenerator Interface | 4.4 |
| 4.6 — Prompt Paraphrase Perturbations | 4.5 |
| 4.7 — Structural Input Perturbations | 4.6 |
| 4.8 — Distractor / Irrelevant Context Perturbations | 4.7 |
| 4.9 — Perturbation Invariant Validator | 4.5, 4.6, 4.7, 4.8 |
| 4.10 — Matched Robustness Study Builder | 4.9 |
| 4.11 — Fault Injector & Transport Faults | 4.10 |
| 4.12 — Payload / Delay Faults & Robustness Report | 4.10, 4.11 |
| 5.1 — Failure Evidence / Taxonomy Model | 4.12 |
| 5.2 — Rule-Based Failure Diagnostics | 5.1 |
| 5.3 — Optional LLM-Assisted Failure Classifier | 5.2 |
| 5.4 — Human Review / Adjudication Schema | 5.3 |
| 5.5 — Partial-Trajectory Failure-Prediction Features | 3.9, 4.1 |
| 5.6 — Offline Failure Predictor Baseline | 5.5 |
| 5.7 — Checkpointed Risk Estimation | 5.6 |
| 5.8 — RecoveryPolicy Interface | 5.7 |
| 5.9 — Retry / Replan Recovery | 5.8 |
| 5.10 — Verifier-Then-Retry Recovery | 5.9 |
| 5.11 — Selective Abstention / Escalation | 5.10 |
| 5.12 — Matched Recovery Experiment & Metrics | 5.8, 5.9, 5.10, 5.11 |
| 6.1 — Provider Pricing Table Model | 5.12 |
| 6.2 — Model / Tool / Runtime Cost Calculator | 6.1 |
| 6.3 — Cost / Reliability Pareto Analysis | 3.11, 4.12, 5.12, 6.2 |
| 6.4 — Safety Constraint & Sandbox Guard | 6.3 |
| 6.5 — Safety Violation Metrics | 6.4 |
| 6.6 — Task-Level Bootstrap Confidence Intervals | 3.11 |
| 6.7 — Paired Agent / Policy Comparison | 6.6 |
| 6.8 — Multiple-Comparison / Search Registry | 6.7 |
| 6.9 — Task Difficulty / Length Stratification | 6.8 |
| 6.10 — Benchmark / Grader Quality Audit | 6.9 |
| 6.11 — Model-vs-Scaffold Comparison | 1.5, 6.7 |
| 6.12 — Research Table / Figure / Report Builder | 6.8, 6.9, 6.10, 6.11 |
| 7.1 — GAIA Adapter Skeleton | 6.12 |
| 7.2 — GAIA Multi-Run Reliability Study Config | 7.1, 3.12, 4.4 |
| 7.3 — SWE-bench Verified Adapter Skeleton | 7.2 |
| 7.4 — SWE-bench Trajectory / Cost Instrumentation | 7.3, 2.10 |
| 7.5 — τ-bench-Style Tool Environment Adapter | 7.4 |
| 7.6 — OSWorld / OSWorld 2.0 Adapter Contract | 7.5 |
| 7.7 — TUA-Bench Adapter Contract | 7.6 |
| 7.8 — ALE / ALE-CLI Adapter Contract | 7.7 |
| 7.9 — Benchmark Capability Matrix | 7.1, 7.3, 7.5, 7.6, 7.7, 7.8 |
| 7.10 — Cross-Benchmark Reliability Comparison | 7.9, 6.12 |
| 7.11 — Longitudinal Evaluation / Drift Registry | 7.10 |
| 7.12 — Dynamic Parameterized Benchmark Generator | 4.9, 7.9 |
| 8.1 — Streamlit Run / Evaluation Selector | 7.12 |
| 8.2 — Capability & Multi-Run Dashboard | 8.1 |
| 8.3 — Trajectory Comparison Dashboard | 3.8, 8.2 |
| 8.4 — Predictability / Calibration Dashboard | 4.4 |
| 8.5 — Robustness Dashboard | 4.12 |
| 8.6 — Failure Explorer Dashboard | 5.4 |
| 8.7 — Recovery / Safety Dashboard | 5.12, 6.5 |
| 8.8 — Cost / Pareto / Drift Dashboard | 6.3, 7.11 |
| 8.9 — Full Run Audit Trail | 2.10, 1.12 |
| 8.10 — Typer CLI & End-to-End Fixture Demo | 8.9 |
| 8.11 — GitHub Actions CI & Clean-Clone Reproduction | 3.12, 8.10 |
| 8.12 — Secrets / Benchmark Privacy / Portfolio Release Audit | 8.11 |
| 9.1 — OTLP / OpenTelemetry Trace Ingestion | 1.7, 3.6 |
| 9.2 — OpenAI OTLP Trace Compatibility Profile | 9.1 |
| 9.3 — Golden Regression Set Builder | 2.3, 2.8, 2.10 |
| 9.4 — Baseline-vs-Candidate Paired Diff Engine | 3.11, 4.12, 9.3 |
| 9.5 — Release Gate Policy Engine | 9.4 |
| 9.6 — Agent SLO / Evaluation Budget Policy | 2.12, 9.5 |
| 9.7 — MCP Tool Contract Registry | 2.6 |
| 9.8 — MCP Contract Regression & Safe Fuzz Tests | 4.11, 9.7 |
| 9.9 — Incident Import / Redaction / Minimization Workflow | 5.1, 5.4, 9.1 |
| 9.10 — Incident-to-Eval Regression Loop | 9.3, 9.9 |
| 9.11 — GitHub PR / CI Release-Gate Reporter | 8.10, 9.5 |
| 9.12 — Shadow / Canary Evaluation & Production Learning Report | 7.11, 9.10, 9.11 |
