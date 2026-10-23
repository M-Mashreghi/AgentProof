# Product Specification — AgentProof

## Primary user

An ML/AI engineer or researcher changing an agent's model, prompt, toolset, scaffold, recovery policy, or memory configuration.

## Primary job

Before merge/deploy, answer:

> Is the candidate agent measurably better, or at least non-regressing, on the quality dimensions we care about?

## Core product surfaces

1. **Eval Runner** — repeated/perturbed execution.
2. **Trace Store** — normalized observable trajectories.
3. **Regression Set** — frozen golden tasks.
4. **Diff Engine** — baseline vs candidate paired analysis.
5. **Release Gate** — policy-based PASS/WARN/BLOCK.
6. **Failure Explorer** — evidence-based debugging.
7. **Incident Loop** — turn failures into future tests.
8. **Dashboard / PR Report** — concise engineering decision surface.

## Non-goals for v1

- production agent hosting,
- real financial/booking transactions,
- universal leaderboard,
- hidden chain-of-thought collection,
- fully automated root-cause claims.
