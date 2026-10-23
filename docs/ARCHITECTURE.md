# Architecture

```mermaid
flowchart LR
    GS[Golden Regression Sets] --> R[Run Orchestrator]
    B[Benchmarks] --> R
    PT[Production / OTLP Traces] --> TI[Trace Ingestion]
    TI --> TS[Normalized Trace Store]

    R --> TS
    TS --> G[Graders]
    G --> M[Reliability Metrics]

    R --> P[Perturbation / Fault Engine]
    P --> M

    M --> F[Failure Analysis]
    F --> RC[Recovery Experiments]

    M --> D[Baseline vs Candidate Diff]
    RC --> D
    D --> GP[Release Gate Policy]
    GP --> PR[PR / Release Report]

    TS --> IL[Incident Learning]
    IL --> GS

    MCP[MCP Tool Contracts] --> CT[Contract / Fuzz Tests]
    CT --> GP
```

## Architectural principle

AgentProof is a **test/evaluation control plane**, not an agent runtime.
It should integrate with existing runtimes through adapters and traces.

## Interoperability

Prefer standards and portable artifacts:
- OTLP/OpenTelemetry for trace interchange,
- explicit benchmark adapters,
- MCP contract metadata for tool interfaces,
- JSON/Parquet run artifacts,
- versioned YAML release policies.
