# Trace Ingestion & Interoperability

## Goal

AgentProof should evaluate agents without requiring every agent framework to be rewritten around AgentProof.

## Canonical approach

External traces → adapter → normalized AgentProof observable trace.

## OTLP / OpenTelemetry

Support OTLP JSON trace ingestion as a primary interoperability path.
Preserve:
- trace/span ids,
- parent-child relationships,
- span names/kinds/status,
- timestamps/duration,
- GenAI model/provider metadata where available,
- token/usage attributes,
- tool/agent operation attributes,
- errors.

Do not assume every vendor uses identical GenAI attributes; retain unknown attributes in a namespaced metadata map.

## OpenAI trace export

OpenAI agent session traces can be exported as OTLP JSON. AgentProof should therefore implement OpenAI support as a thin compatibility/profile layer over the generic OTLP adapter, not a duplicate trace stack.

## Privacy

Raw prompts, tool arguments, or outputs may contain PII/secrets.
Trace adapters support:
- allowlist/denylist attributes,
- field hashing,
- structured redaction,
- payload omission with preserved hashes.
