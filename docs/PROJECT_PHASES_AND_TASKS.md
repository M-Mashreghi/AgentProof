# AgentProof — Project Phases & Atomic Tasks

**Single source of truth.**

Status: `[ ]` Not Started · `[-]` In Progress · `[x]` Completed · `[!]` Push Blocked

## Global Definition of Done

Every task must preserve benchmark integrity, independent repeated runs, hidden-answer protection, grader/environment separation, typed confidence channels, valid perturbation semantics, gold-free recovery, versioned costs, sandboxed safety, synchronized documentation, one task-scoped commit, verified push, and STOP.

---

## Phase 1 — Foundation, Benchmark Integrity & Research Protocol

### Task 1.1: Python Package Scaffold & Development Tooling

**Status:** `[ ]` Not Started  
**Depends on:** `None`

**Task Contract**
- Create installable src-layout package, CLI smoke test, and dev tooling without research logic.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.2: GitHub Remote & Per-Task Workflow Baseline

**Status:** `[ ]` Not Started  
**Depends on:** `1.1`

**Task Contract**
- Validate branch/remote/staging/commit/push workflow without inventing or replacing origin.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.3: Typed Configuration Loader

**Status:** `[ ]` Not Started  
**Depends on:** `1.2`

**Task Contract**
- Load and validate benchmark/agent/reliability/perturbation/fault/recovery/research YAML and referenced paths.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.4: BenchmarkMetadata & Task Domain Models

**Status:** `[ ]` Not Started  
**Depends on:** `1.3`

**Task Contract**
- Represent benchmark/split/task/environment/grader versions while separating public task context from hidden grading state.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.5: AgentEvaluationUnit Model

**Status:** `[ ]` Not Started  
**Depends on:** `1.4`

**Task Contract**
- Represent model, scaffold, prompt, tools, memory, and reasoning settings as a canonical hashed evaluation unit.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.6: RunIdentity & Seed Model

**Status:** `[ ]` Not Started  
**Depends on:** `1.5`

**Task Contract**
- Create deterministic run ids from task, environment, agent, seed, perturbation, fault, and recovery condition.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.7: Trajectory & Event Domain Models

**Status:** `[ ]` Not Started  
**Depends on:** `1.6`

**Task Contract**
- Implement normalized observable trajectory events with timing, tools, errors, retries, confidence, and usage.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.8: GraderOutcome & FailureSource Model

**Status:** `[ ]` Not Started  
**Depends on:** `1.7`

**Task Contract**
- Keep agent failure, grader error, environment error, ambiguity, and success as distinct outcomes.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.9: CostUsage Domain Model

**Status:** `[ ]` Not Started  
**Depends on:** `1.8`

**Task Contract**
- Represent tokens, tool/API usage, retries, wall time, pricing table id, and unknown costs explicitly.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.10: Perturbation / Fault / Recovery Condition Models

**Status:** `[ ]` Not Started  
**Depends on:** `1.9`

**Task Contract**
- Represent condition provenance, semantic class, triggers, seeds, and matched baseline ids.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.11: Research Protocol Registry

**Status:** `[ ]` Not Started  
**Depends on:** `1.10`

**Task Contract**
- Freeze hypotheses, metrics, run counts, budgets, perturbations, and exploratory/confirmatory status per study.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 1.12: Artifact Registry & Repository Validator

**Status:** `[ ]` Not Started  
**Depends on:** `1.11`

**Task Contract**
- Create immutable run layout plus repository/config/link/task validation suitable for CI.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(1.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 2 — Benchmark / Agent Adapters, Grading & Run Orchestration

### Task 2.1: BenchmarkAdapter Interface

**Status:** `[ ]` Not Started  
**Depends on:** `1.12`

**Task Contract**
- Define task listing/loading, environment reset, grading, cleanup, metadata, and explicit capability declarations.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.2: Synthetic Benchmark Adapter

**Status:** `[ ]` Not Started  
**Depends on:** `2.1`

**Task Contract**
- Implement deterministic public fixture tasks plus a separate hidden grader/gold fixture, exact structured grading, reset, and tool schema for API-free development.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.3: Custom JSONL / YAML Task Adapter

**Status:** `[ ]` Not Started  
**Depends on:** `2.2`

**Task Contract**
- Load agent-visible custom tasks from a public task source plus separate hidden grader/gold state, with stable ids/versions and structured grader configuration.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.4: AgentAdapter Interface

**Status:** `[ ]` Not Started  
**Depends on:** `2.3`

**Task Contract**
- Define agent setup/run/confidence/trajectory hooks and explicit model/scaffold/tool capability metadata.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.5: Deterministic Mock Agent

**Status:** `[ ]` Not Started  
**Depends on:** `2.4`

**Task Contract**
- Implement seeded fixture agent with scripted success, failure, tool use, and confidence behavior.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.6: Tool Instrumentation Layer

**Status:** `[ ]` Not Started  
**Depends on:** `2.5`

**Task Contract**
- Log tool arguments/results hashes, latency, errors, retries, cost, and support controlled fault injection.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.7: Environment Reset / Snapshot Contract

**Status:** `[ ]` Not Started  
**Depends on:** `2.6`

**Task Contract**
- Verify clean task reset, optional environment hash, and absence of cross-run hidden state.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.8: Grader Interface & Structured Grader

**Status:** `[ ]` Not Started  
**Depends on:** `2.1, 2.2, 2.3`

**Task Contract**
- Implement deterministic exact/structured grading with versioned grader logic and explicit grader errors.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.9: Grader Quality Fixture Tests

**Status:** `[ ]` Not Started  
**Depends on:** `2.8`

**Task Contract**
- Verify positive/negative/ambiguous fixtures, deterministic reruns, and no hidden grader leakage.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.10: Single-Run Orchestrator

**Status:** `[ ]` Not Started  
**Depends on:** `2.4, 2.6, 2.7, 2.8`

**Task Contract**
- Execute one task condition through clean environment, agent, trajectory, grader, cost collector, and immutable artifact.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.11: Run Isolation Guard

**Status:** `[ ]` Not Started  
**Depends on:** `2.5, 2.7, 2.10`

**Task Contract**
- Detect/reset cross-run memory, task-specific caches, prior final answers, and leaked successful trajectories.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 2.12: Budget / Timeout / Parallel Scheduler

**Status:** `[ ]` Not Started  
**Depends on:** `2.11`

**Task Contract**
- Enforce run/study budgets, timeouts, concurrency/rate limits, explicit retries, and independent run state.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(2.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 3 — Multi-Run Evaluation, Trajectories & Consistency

### Task 3.1: Repeated-Run Study Builder

**Status:** `[ ]` Not Started  
**Depends on:** `2.12`

**Task Contract**
- Generate K independent run specs per task/agent condition with matched inputs and no answer sharing.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.2: Capability Metrics

**Status:** `[ ]` Not Started  
**Depends on:** `2.10`

**Task Contract**
- Compute success, pass@1, pass@k-style capability, completion rate, and completion time with coverage.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.3: All-K Repeated Success Reliability

**Status:** `[ ]` Not Started  
**Depends on:** `3.2`

**Task Contract**
- Compute all-k/pass^k-style repeated success separately from pass@k and test hand-computed cases.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.4: Outcome Consistency Metrics

**Status:** `[ ]` Not Started  
**Depends on:** `3.3`

**Task Contract**
- Measure success frequency and final structured-output agreement across repeated runs.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.5: Resource Consistency Metrics

**Status:** `[ ]` Not Started  
**Depends on:** `3.4`

**Task Contract**
- Measure variance/CV in tokens, tools, retries, wall time, and cost across runs.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.6: Normalized Trajectory Action Vocabulary

**Status:** `[ ]` Not Started  
**Depends on:** `3.5`

**Task Contract**
- Map framework-specific observable events into versioned normalized action categories.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.7: Trajectory Action-Distribution Similarity

**Status:** `[ ]` Not Started  
**Depends on:** `3.6`

**Task Contract**
- Measure documented action-distribution divergence/similarity across repeated runs.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.8: Trajectory Sequence Similarity

**Status:** `[ ]` Not Started  
**Depends on:** `3.7`

**Task Contract**
- Measure normalized observable action-sequence edit/LCS-style similarity without chain-of-thought.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.9: Loop / Retry / Tool-Churn Diagnostics

**Status:** `[ ]` Not Started  
**Depends on:** `3.8`

**Task Contract**
- Detect repeated actions, retry loops, excessive tool churn, and long trajectories as diagnostics.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.10: Per-Task Reliability Profile

**Status:** `[ ]` Not Started  
**Depends on:** `3.2, 3.3, 3.4, 3.5, 3.7, 3.8`

**Task Contract**
- Assemble capability, consistency, resources, and trajectory diagnostics while keeping components visible.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.11: Benchmark Reliability Summary

**Status:** `[ ]` Not Started  
**Depends on:** `3.10`

**Task Contract**
- Aggregate task profiles with explicit weighting, coverage, and uncertainty-ready output.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 3.12: Deterministic Multi-Run Regression Fixture

**Status:** `[ ]` Not Started  
**Depends on:** `3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8`

**Task Contract**
- Freeze expected repeated-run metrics/hashes so CI detects unexplained reliability drift.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(3.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 4 — Predictability, Perturbations & Fault Robustness

### Task 4.1: Self-Reported Confidence Protocol

**Status:** `[ ]` Not Started  
**Depends on:** `3.12`

**Task Contract**
- Implement standardized 0–1 confidence collection with timing/type validation and no post-grader confidence.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.2: Brier & Calibration Metrics

**Status:** `[ ]` Not Started  
**Depends on:** `4.1, 3.2`

**Task Contract**
- Compute Brier score, reliability bins, calibration diagnostics, and sample counts.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.3: Success Discrimination AUROC

**Status:** `[ ]` Not Started  
**Depends on:** `4.2`

**Task Contract**
- Measure whether confidence distinguishes success/failure, handling degenerate samples explicitly.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.4: Risk-Coverage / Selective Prediction

**Status:** `[ ]` Not Started  
**Depends on:** `4.1, 4.2`

**Task Contract**
- Compute risk-coverage and E-AURC-style diagnostics plus validation-selected abstention simulation.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.5: PerturbationGenerator Interface

**Status:** `[ ]` Not Started  
**Depends on:** `4.4`

**Task Contract**
- Define base task, semantic class, changed fields, invariant, seed, and grader-update contract.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.6: Prompt Paraphrase Perturbations

**Status:** `[ ]` Not Started  
**Depends on:** `4.5`

**Task Contract**
- Generate/version semantics-preserving instruction paraphrases and validate expected outcome invariance.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.7: Structural Input Perturbations

**Status:** `[ ]` Not Started  
**Depends on:** `4.6`

**Task Contract**
- Implement harmless field reordering, optional metadata, formatting, and schema variants where supported.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.8: Distractor / Irrelevant Context Perturbations

**Status:** `[ ]` Not Started  
**Depends on:** `4.7`

**Task Contract**
- Inject controlled non-semantic distractors while preserving required information and grader truth.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.9: Perturbation Invariant Validator

**Status:** `[ ]` Not Started  
**Depends on:** `4.5, 4.6, 4.7, 4.8`

**Task Contract**
- Block variants that violate declared semantics or fail deterministic/reference checks.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.10: Matched Robustness Study Builder

**Status:** `[ ]` Not Started  
**Depends on:** `4.9`

**Task Contract**
- Pair base and perturbed conditions on matched tasks/seeds to avoid selection bias.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.11: Fault Injector & Transport Faults

**Status:** `[ ]` Not Started  
**Depends on:** `4.10`

**Task Contract**
- Implement observable, reproducible timeout/HTTP500/rate-limit fault injection without corrupting graders.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 4.12: Payload / Delay Faults & Robustness Report

**Status:** `[ ]` Not Started  
**Depends on:** `4.10, 4.11`

**Task Contract**
- Inject malformed/missing/stale/delayed tool responses and compute matched robustness degradation.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(4.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 5 — Failure Analysis, Recovery & Selective Intervention

### Task 5.1: Failure Evidence / Taxonomy Model

**Status:** `[ ]` Not Started  
**Depends on:** `4.12`

**Task Contract**
- Represent failure categories, evidence event ids, classifier confidence, reviewer status, and contributing causes.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.2: Rule-Based Failure Diagnostics

**Status:** `[ ]` Not Started  
**Depends on:** `5.1`

**Task Contract**
- Detect observable tool errors, loops, timeouts, premature finalization, and repeated failed actions.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.3: Optional LLM-Assisted Failure Classifier

**Status:** `[ ]` Not Started  
**Depends on:** `5.2`

**Task Contract**
- Classify redacted trajectories with cited event ids and review low-confidence/high-impact cases.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.4: Human Review / Adjudication Schema

**Status:** `[ ]` Not Started  
**Depends on:** `5.3`

**Task Contract**
- Track ambiguous grading/failure review separately from automatic suggestions and allow blinded review labels.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.5: Partial-Trajectory Failure-Prediction Features

**Status:** `[ ]` Not Started  
**Depends on:** `3.9, 4.1`

**Task Contract**
- Build causal checkpoint features from errors, repeats, elapsed time, usage, and confidence only up to checkpoint.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.6: Offline Failure Predictor Baseline

**Status:** `[ ]` Not Started  
**Depends on:** `5.5`

**Task Contract**
- Train leakage-safe logistic/boosting baseline to predict eventual failure from partial trajectory features.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.7: Checkpointed Risk Estimation

**Status:** `[ ]` Not Started  
**Depends on:** `5.6`

**Task Contract**
- Estimate failure risk over time and measure warning lead time without using future events.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.8: RecoveryPolicy Interface

**Status:** `[ ]` Not Started  
**Depends on:** `5.7`

**Task Contract**
- Define retry/replan/verifier/rollback/abstention inputs while explicitly prohibiting gold-answer access.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.9: Retry / Replan Recovery

**Status:** `[ ]` Not Started  
**Depends on:** `5.8`

**Task Contract**
- Implement capped fresh retry and evidence-limited replanning with cost/latency accounting.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.10: Verifier-Then-Retry Recovery

**Status:** `[ ]` Not Started  
**Depends on:** `5.9`

**Task Contract**
- Use independent verifier on allowed output/trajectory evidence and track false alarms/missed failures.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.11: Selective Abstention / Escalation

**Status:** `[ ]` Not Started  
**Depends on:** `5.10`

**Task Contract**
- Trigger abstention/escalation using validation-selected risk thresholds and report coverage vs risk.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 5.12: Matched Recovery Experiment & Metrics

**Status:** `[ ]` Not Started  
**Depends on:** `5.8, 5.9, 5.10, 5.11`

**Task Contract**
- Compare base/recovery on matched conditions and compute recovered success, intervention precision, cost, and latency overhead.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(5.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 6 — Cost, Safety, Statistics & Comparative Evaluation

### Task 6.1: Provider Pricing Table Model

**Status:** `[ ]` Not Started  
**Depends on:** `5.12`

**Task Contract**
- Version model/provider pricing snapshots by effective date and usage dimension.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.2: Model / Tool / Runtime Cost Calculator

**Status:** `[ ]` Not Started  
**Depends on:** `6.1`

**Task Contract**
- Compute model, tool/API, retry, wall-time, and optional runtime costs with unknowns explicit.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.3: Cost / Reliability Pareto Analysis

**Status:** `[ ]` Not Started  
**Depends on:** `3.11, 4.12, 5.12, 6.2`

**Task Contract**
- Identify non-dominated systems across capability, reliability, cost, and latency rather than arbitrary single ranking.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.4: Safety Constraint & Sandbox Guard

**Status:** `[ ]` Not Started  
**Depends on:** `6.3`

**Task Contract**
- Represent benchmark/domain constraints and block real irreversible transaction endpoints.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.5: Safety Violation Metrics

**Status:** `[ ]` Not Started  
**Depends on:** `6.4`

**Task Contract**
- Compute violation rate, severity, safe failure, escalation behavior, and coverage separately from reliability.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.6: Task-Level Bootstrap Confidence Intervals

**Status:** `[ ]` Not Started  
**Depends on:** `3.11`

**Task Contract**
- Bootstrap tasks, respecting repeated runs nested within tasks, for benchmark-level uncertainty.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.7: Paired Agent / Policy Comparison

**Status:** `[ ]` Not Started  
**Depends on:** `6.6`

**Task Contract**
- Compare matched task/condition differences and coverage without pairing incompatible benchmark versions.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.8: Multiple-Comparison / Search Registry

**Status:** `[ ]` Not Started  
**Depends on:** `6.7`

**Task Contract**
- Register agents, scaffolds, thresholds, perturbations, and policies searched and disclose selection breadth.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.9: Task Difficulty / Length Stratification

**Status:** `[ ]` Not Started  
**Depends on:** `6.8`

**Task Contract**
- Stratify results by valid task difficulty/length metadata while keeping sample sizes and avoiding test-driven tuning.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.10: Benchmark / Grader Quality Audit

**Status:** `[ ]` Not Started  
**Depends on:** `6.9`

**Task Contract**
- Summarize invalid tasks, grader errors, ambiguous outcomes, reset failures, and verified-subset status.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.11: Model-vs-Scaffold Comparison

**Status:** `[ ]` Not Started  
**Depends on:** `1.5, 6.7`

**Task Contract**
- Support matched descriptive comparisons and label confounded changes rather than attributing scaffold gains to model.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 6.12: Research Table / Figure / Report Builder

**Status:** `[ ]` Not Started  
**Depends on:** `6.8, 6.9, 6.10, 6.11`

**Task Contract**
- Generate reproducible capability, reliability, robustness, recovery, safety, cost, uncertainty, and limitation outputs.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(6.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 7 — Real Benchmark Integrations & Longitudinal Tracking

### Task 7.1: GAIA Adapter Skeleton

**Status:** `[ ]` Not Started  
**Depends on:** `6.12`

**Task Contract**
- Implement version-pinned GAIA task/context/grading hooks while keeping hidden labels out of agent context.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.2: GAIA Multi-Run Reliability Study Config

**Status:** `[ ]` Not Started  
**Depends on:** `7.1, 3.12, 4.4`

**Task Contract**
- Create pre-specified repeated-run/calibration study slice and valid perturbation policy.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.3: SWE-bench Verified Adapter Skeleton

**Status:** `[ ]` Not Started  
**Depends on:** `7.2`

**Task Contract**
- Integrate the 500-instance verified subset with isolated repo/container and pinned harness/scaffold metadata.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.4: SWE-bench Trajectory / Cost Instrumentation

**Status:** `[ ]` Not Started  
**Depends on:** `7.3, 2.10`

**Task Contract**
- Capture patch/test outcome, runtime, model usage, observable trajectory, and distinguish setup/test failures.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.5: τ-bench-Style Tool Environment Adapter

**Status:** `[ ]` Not Started  
**Depends on:** `7.4`

**Task Contract**
- Support stateful tool-policy environments with tool schema, policy constraints, faults, and safety capabilities.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.6: OSWorld / OSWorld 2.0 Adapter Contract

**Status:** `[ ]` Not Started  
**Depends on:** `7.5`

**Task Contract**
- Define optional GUI environment snapshots, app/image versions, trajectories, and execution graders without base-install dependency.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.7: TUA-Bench Adapter Contract

**Status:** `[ ]` Not Started  
**Depends on:** `7.6`

**Task Contract**
- Define optional terminal-use integration with pinned containers and repeated-run/all-k evaluation.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.8: ALE / ALE-CLI Adapter Contract

**Status:** `[ ]` Not Started  
**Depends on:** `7.7`

**Task Contract**
- Define optional long-horizon professional-task integration with access rules, domain, duration, and outcome grading.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.9: Benchmark Capability Matrix

**Status:** `[ ]` Not Started  
**Depends on:** `7.1, 7.3, 7.5, 7.6, 7.7, 7.8`

**Task Contract**
- Generate which adapters support reset, exact grading, perturbations, faults, safety, cost, trajectories, and recovery.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.10: Cross-Benchmark Reliability Comparison

**Status:** `[ ]` Not Started  
**Depends on:** `7.9, 6.12`

**Task Contract**
- Compare dimension profiles without blindly averaging incompatible benchmark/task structures.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.11: Longitudinal Evaluation / Drift Registry

**Status:** `[ ]` Not Started  
**Depends on:** `7.10`

**Task Contract**
- Register stable task slices, dates, model/agent versions, environment changes, and temporal reliability/cost drift.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 7.12: Dynamic Parameterized Benchmark Generator

**Status:** `[ ]` Not Started  
**Depends on:** `4.9, 7.9`

**Task Contract**
- Generate controlled task families with exact grader state, novelty/duplicate checks, and invariant-quality audit.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(7.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Phase 8 — Dashboard, CLI, CI/CD & Portfolio Release

### Task 8.1: Streamlit Run / Evaluation Selector

**Status:** `[ ]` Not Started  
**Depends on:** `7.12`

**Task Contract**
- Create read-only dashboard shell over immutable evaluations with benchmark/agent/protocol integrity metadata.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.2: Capability & Multi-Run Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `8.1`

**Task Contract**
- Show pass@1/pass@k/all-k, outcome consistency, resource variance, and repeated-run drilldown.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.3: Trajectory Comparison Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `3.8, 8.2`

**Task Contract**
- Visualize observable action sequences, tools, loops, and resource differences without chain-of-thought.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.4: Predictability / Calibration Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `4.4`

**Task Contract**
- Show Brier, calibration, AUROC, risk-coverage, abstention simulation, channel type, and sample counts.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.5: Robustness Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `4.12`

**Task Contract**
- Show matched base vs prompt/structural/fault results and degradation heatmaps with provenance.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.6: Failure Explorer Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `5.4`

**Task Contract**
- Show one run trajectory, failure evidence/category, grader/environment status, and review state without secrets.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.7: Recovery / Safety Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `5.12, 6.5`

**Task Contract**
- Compare retry/replan/verifier/abstention outcomes, overhead, safety violations, severity, and safe failure.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.8: Cost / Pareto / Drift Dashboard

**Status:** `[ ]` Not Started  
**Depends on:** `6.3, 7.11`

**Task Contract**
- Show cost/task, cost/success, pricing version, reliability-cost frontier, and longitudinal drift.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.9: Full Run Audit Trail

**Status:** `[ ]` Not Started  
**Depends on:** `2.10, 1.12`

**Task Contract**
- Expose exact task/env/agent/prompt/tool hashes, seed, conditions, trajectory, grader, costs, and code commit.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.10: Typer CLI & End-to-End Fixture Demo

**Status:** `[ ]` Not Started  
**Depends on:** `8.9`

**Task Contract**
- Implement eval/reliability/robustness/recovery/report CLI and API-free synthetic demo producing dashboard-ready artifacts.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.11: GitHub Actions CI & Clean-Clone Reproduction

**Status:** `[ ]` Not Started  
**Depends on:** `3.12, 8.10`

**Task Contract**
- Run validation, compile/import smoke, reliability tests, and deterministic fixture pipeline without paid APIs.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 8.12: Secrets / Benchmark Privacy / Portfolio Release Audit

**Status:** `[ ]` Not Started  
**Depends on:** `8.11`

**Task Contract**
- Check keys, hidden answers, private traces, licenses, measured claims, screenshots, and safe tag/release instructions.
- Preserve benchmark/task/environment/agent/grader version provenance.
- Add deterministic tests/fixtures and run applicable integrity checks.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Benchmark/run/reliability invariants pass where applicable.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(8.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---


## Phase 9 — Production Trace Integration, Release Gating & Incident Learning

### Task 9.1: OTLP / OpenTelemetry Trace Ingestion

**Status:** `[ ]` Not Started  
**Depends on:** `1.7, 3.6`

**Task Contract**
- Ingest OTLP JSON traces into the normalized AgentProof observable trajectory model while preserving trace/span ids, parent relationships, timestamps, status, usage, error, and namespaced unknown attributes.
- Implement configurable payload redaction/hash policies before persistence.
- Add deterministic OTLP fixture tests and preserve original source-profile metadata.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Trace provenance/redaction invariants pass.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.1): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.2: OpenAI OTLP Trace Compatibility Profile

**Status:** `[ ]` Not Started  
**Depends on:** `9.1`

**Task Contract**
- Map exported OpenAI agent OTLP trace patterns into AgentProof spans/events without creating a duplicate vendor-specific trace store.
- Preserve agent/model/tool/handoff/status/usage metadata where available and mark unavailable fields explicitly.
- Add fixture tests for agent and tool span normalization.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Vendor-profile mapping is versioned and loss is documented.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.2): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.3: Golden Regression Set Builder

**Status:** `[ ]` Not Started  
**Depends on:** `2.3, 2.8, 2.10`

**Task Contract**
- Build versioned golden task sets from curated fixtures or redacted/minimized historical traces/incidents.
- Keep agent-visible input separate from expected/grader state and record provenance/severity/criticality.
- Add dataset hashing, deduplication, review status, and train/test contamination warnings.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Hidden-answer and privacy checks pass.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.3): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.4: Baseline-vs-Candidate Paired Diff Engine

**Status:** `[ ]` Not Started  
**Depends on:** `3.11, 4.12, 9.3`

**Task Contract**
- Compare compatible baseline/candidate runs on matched task/condition ids across quality, all-k reliability, robustness, recovery, safety, cost, and latency.
- Produce task-level deltas, aggregate deltas, coverage, uncertainty where available, and NOT_EVALUABLE reasons for incompatible comparisons.
- Never hide regressions behind one weighted score.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Compatibility/matching checks pass.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.4): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.5: Release Gate Policy Engine

**Status:** `[ ]` Not Started  
**Depends on:** `9.4`

**Task Contract**
- Evaluate versioned policy rules over candidate-vs-baseline metrics and return PASS, WARN, BLOCK, or NOT_EVALUABLE per rule.
- Support magnitude thresholds, coverage requirements, safety blockers, optional uncertainty criteria, and critical-task rules.
- Produce explicit blocking reasons rather than an opaque aggregate score.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Policy parsing/severity/edge cases pass.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.5): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.6: Agent SLO / Evaluation Budget Policy

**Status:** `[ ]` Not Started  
**Depends on:** `2.12, 9.5`

**Task Contract**
- Add versioned success/all-k/robustness/safety/cost/latency SLO-style rules plus evaluation-spend and wall-time budgets.
- Treat missing/unknown metrics according to explicit policy rather than silently passing.
- Add examples with clearly labeled illustrative thresholds.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Unknown metric and budget-exhaustion behavior is tested.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.6): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.7: MCP Tool Contract Registry

**Status:** `[ ]` Not Started  
**Depends on:** `2.6`

**Task Contract**
- Represent discovered/declared MCP tool names, input schemas, side-effect class, retry/idempotency policy, permissions/approval requirements, and server/version metadata.
- Support owned/test MCP servers and fixtures only for active negative testing.
- Produce contract hashes suitable for regression comparison.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Contract/version/side-effect metadata is preserved.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.7): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.8: MCP Contract Regression & Safe Fuzz Tests

**Status:** `[ ]` Not Started  
**Depends on:** `4.11, 9.7`

**Task Contract**
- Detect tool discovery/schema/required-field/side-effect policy regressions and run safe boundary/invalid-argument tests against local/owned test MCP servers.
- Verify timeout/error behavior, parseability, and declared retry safety without attacking third-party systems.
- Emit blocking contract failures consumable by the release gate.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Test target ownership/sandbox guard passes.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.8): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.9: Incident Import / Redaction / Minimization Workflow

**Status:** `[ ]` Not Started  
**Depends on:** `5.1, 5.4, 9.1`

**Task Contract**
- Import failed-run/incident artifacts, redact configured sensitive fields, separate environment/tool outage from agent behavior, and create a minimized reproducible case proposal.
- Record severity, reproduction status, root-cause hypothesis, privacy review, and linkage to the resulting golden task.
- Never auto-publish production trace payloads.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Redaction/privacy and provenance checks pass.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.9): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.10: Incident-to-Eval Regression Loop

**Status:** `[ ]` Not Started  
**Depends on:** `9.3, 9.9`

**Task Contract**
- Convert reviewed/minimized incidents into permanent golden regression cases with versioned expected invariants/grader state.
- Where practical, verify the old configuration reproduces the failure and the fixed candidate resolves it.
- Track fixed-by commit/version and prevent duplicate regression cases.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Reproduction/fix linkage and deduplication work.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.10): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.11: GitHub PR / CI Release-Gate Reporter

**Status:** `[ ]` Not Started  
**Depends on:** `8.10, 9.5`

**Task Contract**
- Generate machine-readable and Markdown PR summaries with candidate/baseline deltas, rule status, blocking reasons, cost/latency/safety changes, and links/paths to detailed artifacts.
- Exit nonzero only according to configured blocking rules and distinguish infrastructure/evaluation failure from candidate regression.
- Keep provider-neutral core output so GitHub reporting is an adapter, not the gate engine itself.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] PASS/WARN/BLOCK/infrastructure-exit behavior is deterministic.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.11): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---
### Task 9.12: Shadow / Canary Evaluation & Production Learning Report

**Status:** `[ ]` Not Started  
**Depends on:** `7.11, 9.10, 9.11`

**Task Contract**
- Define offline/shadow evaluation ingestion for sampled real traces where permitted, compare reliability/cost/drift to release baselines, and surface candidate incident/regression cases.
- Do not route real irreversible actions or automatically promote a candidate to production.
- Generate an end-to-end production-learning report: release gate → observed drift/incidents → new golden cases → next gate.

**Definition of Done**
- [ ] Implementation exists.
- [ ] Relevant tests pass.
- [ ] Privacy, sampling, drift, and no-auto-promotion guards pass.
- [ ] Docs/task status are synchronized.
- [ ] `git diff --check` passes.
- [ ] Dedicated `task(9.12): ...` commit exists.
- [ ] Push is verified when `origin` exists.
- [ ] Claude stops before next task.

---

## Progress Summary

| Phase | Tasks | Completed |
|---|---:|---:|
| 1 — Foundation, Benchmark Integrity & Research Protocol | 12 | 0 |
| 2 — Benchmark / Agent Adapters, Grading & Run Orchestration | 12 | 0 |
| 3 — Multi-Run Evaluation, Trajectories & Consistency | 12 | 0 |
| 4 — Predictability, Perturbations & Fault Robustness | 12 | 0 |
| 5 — Failure Analysis, Recovery & Selective Intervention | 12 | 0 |
| 6 — Cost, Safety, Statistics & Comparative Evaluation | 12 | 0 |
| 7 — Real Benchmark Integrations & Longitudinal Tracking | 12 | 0 |
| 8 — Dashboard, CLI, CI/CD & Portfolio Release | 12 | 0 |
| 9 — Production Trace Integration, Release Gating & Incident Learning | 12 | 0 |
| **Total** | **108** | **0** |
