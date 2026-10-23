# AgentProof — Project Structure

```text
AgentProof/
├── README.md
├── CLAUDE.md
├── PROJECT_STRUCTURE.md
├── pyproject.toml
├── Makefile
├── .env.example
├── .gitignore
├── .claude/rules/
├── docs/
├── configs/
│   ├── benchmarks/
│   ├── agents/
│   ├── reliability/
│   ├── perturbations/
│   ├── faults/
│   ├── recovery/
│   └── research/
├── examples/
├── src/agentproof/
│   ├── config/
│   ├── domain/
│   ├── benchmarks/
│   ├── agents/
│   ├── runs/
│   ├── trajectories/
│   ├── reliability/
│   ├── perturbations/
│   ├── faults/
│   ├── grading/
│   ├── recovery/
│   ├── costs/
│   ├── evaluation/
│   ├── reporting/
│   └── dashboard/
├── tests/
├── reports/
├── scripts/
└── .github/workflows/
```

Release governance: `docs/RELEASE_CHECKLIST.md`.
## V2 Production-Oriented Additions

```text
configs/traces/        # OTLP/OpenAI trace profiles
configs/gates/         # release policies
configs/mcp/           # tool contract tests
configs/demo/          # reference sandbox

src/agentproof/trace_ingest/
src/agentproof/gates/
src/agentproof/mcp/
src/agentproof/incidents/
src/agentproof/golden_sets/

docs/FAST_TRACK_MVP.md
docs/TRACE_INGESTION.md
docs/RELEASE_GATING.md
docs/INCIDENT_TO_EVAL.md
docs/MCP_CONTRACT_TESTING.md
docs/SLO_AND_BUDGET_POLICY.md
docs/REFERENCE_DEMO.md
docs/CLI_SPEC.md
docs/PR_REPORT_SPEC.md
```
