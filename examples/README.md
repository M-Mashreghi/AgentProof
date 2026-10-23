# Example Fixtures

These fixtures are synthetic, local, and API-free.

## Privacy / benchmark-integrity layout

Agent-visible inputs are deliberately separated from grader-only state:

```text
tasks.jsonl                  ← agent-visible
tasks_gold.jsonl             ← grader-only

supportops_tasks.jsonl       ← agent-visible
supportops_gold.jsonl        ← grader-only
supportops_state.json        ← mock tool/environment state

researchops_tasks.jsonl      ← agent-visible
researchops_gold.jsonl       ← grader-only
researchops_evidence.json    ← mock evidence available through research tools
```

Gold files may live in this public repository because they are synthetic CI/demo
fixtures. The benchmark adapter must never place their contents in the agent
context.

These files are not official benchmark leaderboard data.
