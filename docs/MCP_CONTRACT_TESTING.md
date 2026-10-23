# MCP Tool Contract Testing

MCP tools are a critical agent dependency and should be tested like APIs.

## Contract checks

- server/tool discovery succeeds,
- expected tool names exist,
- input schema remains compatible,
- output content/schema remains parseable,
- side-effect classification is explicit,
- retry/idempotency policy is declared,
- timeout/error behavior is handled,
- permission/approval requirements are preserved.

## Fuzz/negative tests

Generate invalid or boundary arguments:
- missing required fields,
- wrong enum/type,
- extreme lengths/numbers,
- unknown fields,
- malformed nested objects.

The objective is not to attack third-party systems; tests run only against owned/test MCP servers or local fixtures.

## Release use

A tool-contract regression can block an agent release even if model benchmark accuracy is unchanged.
