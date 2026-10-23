# CLI Specification

Target CLI surfaces:

```bash
# Run an evaluation suite
agentproof eval --suite supportops --agent configs/agents/example_agent.yaml --runs 5

# Compare candidate to baseline
agentproof compare --baseline runs/main --candidate runs/pr-184

# Apply release policy
agentproof gate --baseline runs/main --candidate runs/pr-184 --policy configs/gates/pr_gate.yaml

# Ingest external OTLP traces
agentproof trace ingest traces.otlp.json --profile configs/traces/otlp.yaml

# Validate MCP tool contracts against an owned/test server
agentproof mcp check --config configs/mcp/contract_test.yaml

# Turn a reviewed incident into a regression-case proposal
agentproof incident import incident.json

# Build dashboard/report artifacts
agentproof report --evaluation eval_2026_10_23
```

## Exit codes

- `0`: command/evaluation completed; gate did not block.
- `2`: release gate BLOCK.
- `3`: evaluation infrastructure / configuration failure.
- `4`: privacy/benchmark-integrity guard failure.

Exact codes are implementation contracts and must be tested.
