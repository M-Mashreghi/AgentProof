# Fast-Track MVP

The full project is research-grade; the fast track exists so a useful portfolio product appears early.

## Demo milestone A — working harness

Build enough of Phases 1–2 to run a synthetic/custom task from a clean environment and write a graded trace artifact.

Minimum useful outcomes:
- typed config,
- evaluation unit identity,
- run identity,
- trajectory model,
- structured grader,
- one-run orchestrator,
- run isolation.

## Demo milestone B — multi-run reliability

Add:
- repeated runs,
- pass@k and all-k,
- outcome consistency,
- resource consistency,
- simple trajectory diagnostics.

At this point the product can already demonstrate why single-run accuracy is insufficient.

## Demo milestone C — robustness

Add:
- confidence/calibration,
- one semantics-preserving perturbation family,
- one tool timeout fault,
- matched base-vs-perturbed report.

## Demo milestone D — release gate

Implement the **fast-track subset** of production-oriented Phase 9 early. Tasks 9.3–9.5 are intentionally dependency-light so they can follow the core multi-run/robustness stack without requiring advanced recovery, benchmark integrations, or dashboard work:
- golden regression set,
- baseline-vs-candidate diff,
- release policy,
- PR-style report.

Target demo:

```text
Candidate PR-184
Quality       +2.1 pp   PASS
All-k         -0.4 pp   PASS
Robustness    -7.2 pp   BLOCK
Cost/success +11.0 %    PASS
Safety         0 new    PASS

RELEASE: BLOCK
Reason: robustness regression under timeout faults
```

## Demo milestone E — incident loop

Import a failed trace, redact/minimize it, turn it into a golden case, rerun baseline/candidate, and show the new regression test in the PR gate.

## Advanced scale-up only after MVP

- SWE-bench Verified
- OSWorld
- TUA-Bench
- ALE
- failure prediction ML
- longitudinal drift
- large dynamic benchmark generation

This sequencing prevents the project from becoming a benchmark-integration project before the core product is useful.

## Fast-track dependency rule

The release-gate path must remain implementable without completing the advanced
failure-prediction/recovery, real-benchmark, or dashboard phases.

Core fast-track chain:

```text
Core harness (Phases 1–2 subset)
→ Multi-run summary (Phase 3)
→ Robustness study (Phase 4)
→ 9.3 Golden Regression Set
→ 9.4 Baseline-vs-Candidate Diff
→ 9.5 Release Gate
```

Optional metrics such as advanced safety, recovery, or priced cost dimensions may
return `NOT_EVALUABLE` until their owning modules are implemented. They must not
silently PASS.
