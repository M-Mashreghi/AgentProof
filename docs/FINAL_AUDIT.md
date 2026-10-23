# AgentProof V2 — Architecture / Product Audit

**Product position:** AI Agent Reliability & Release-Gating Platform.

V2 retains research-grade multi-run reliability while adding the practical engineering loop needed before and after deployment:

- OTLP/OpenTelemetry trace ingestion,
- OpenAI OTLP compatibility profile,
- golden regression datasets,
- paired baseline-vs-candidate diffs,
- explicit PASS/WARN/BLOCK release gates,
- SLO and evaluation-budget policies,
- MCP tool-contract regression testing,
- incident-to-eval learning loop,
- PR/CI gate reports,
- shadow/canary evaluation without automatic promotion,
- SupportOps and ResearchOps reference demos.

The project contains **108 atomic tasks across 9 phases**.

## Key design boundary

AgentProof is an evaluation/control plane, not an agent runtime or production deployment service. It does not perform real irreversible transactions and does not collect hidden chain-of-thought.

## Recommended implementation order

Use `FAST_TRACK_MVP.md`: build the harness → multi-run metrics → one perturbation/fault → baseline/candidate diff → release gate → incident regression loop. Heavy benchmark integrations are scale-up work.

## Final V2.1 audit corrections

The final audit found and corrected two implementation-significant issues:

1. The documented Fast-Track release-gate path previously had transitive
   dependencies on advanced recovery/cost modules. Tasks 9.3–9.5 are now
   dependency-light and can be implemented after the core multi-run/robustness
   stack.
2. Synthetic, SupportOps, and ResearchOps agent-visible task files previously
   co-located expected outputs. They now use separate task and grader/gold
   sources, and the validator blocks gold fields in configured agent-visible
   JSONL task sources.

SupportOps and ResearchOps now also include complete local mock state/evidence
fixtures so the reference demos are self-contained.
