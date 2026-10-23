# Reference Demo Packs

AgentProof includes two complementary practical demo concepts.

## 1. SupportOps — transactional/tool agent

### Mock tasks
- look up an order,
- explain shipment state,
- determine refund eligibility,
- update address only when policy permits,
- request approval for restricted refund,
- escalate when required data is missing.

### Reliability scenarios
- timeout,
- malformed payload,
- policy conflict,
- ambiguous order id,
- stale state,
- unsafe retry after side-effect uncertainty.

### Why it matters
Demonstrates tool use, policy compliance, side-effect safety, fault recovery, and human escalation.

---

## 2. ResearchOps — evidence-grounded research agent

### Mock tasks
- search an evidence store,
- compare claims/numbers,
- cite supporting source ids,
- distinguish supported vs unsupported claims,
- abstain when evidence is insufficient.

### Metrics
- answer correctness,
- citation precision,
- citation recall,
- unsupported-claim rate,
- source freshness compliance,
- cost and latency.

### Reliability scenarios
- irrelevant distractor documents,
- conflicting sources,
- missing evidence,
- stale source,
- tool timeout,
- reordered search results.

### Why it matters
Demonstrates LLM/agent evaluation, grounding, trace grading, evidence quality, and hallucination resistance.

All tools/data are mock fixtures; no private accounts or real irreversible actions.

## Fixture completeness

The demo packs include their own local mock environment data:

- SupportOps: `examples/supportops_state.json`
- ResearchOps: `examples/researchops_evidence.json`

Agent-visible task files and grader-only gold files are separate by construction.
