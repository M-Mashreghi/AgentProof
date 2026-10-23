# Benchmark Integrity Policy

Do not:
- expose hidden test answers;
- persist gold labels in agent-visible cache;
- retrieve public solutions during test;
- reuse successful test trajectories as memory;
- mutate graders silently;
- redistribute protected traces.

Cross-version comparisons must be labeled. Grader changes create a new evaluation version.

## Agent-visible input vs hidden grader state

Agent-visible task files must not contain canonical expected answers, gold labels,
or grader-only state.

For local fixtures, repository storage may contain separate gold files for
deterministic testing, but the agent adapter receives only the configured
`task_source`. The grader receives the separate `grader_source`.

This separation is enforced by the release validator for configured JSONL task
sources.
