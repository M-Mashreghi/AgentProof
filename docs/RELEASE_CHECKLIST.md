# Public Release Checklist

- [ ] Choose/confirm repository software license.
- [ ] Confirm benchmark/data licenses and redistribution rules.
- [ ] Remove credentials, private traces, and hidden answers.
- [ ] Run `python scripts/validate_project.py`.
- [ ] Run `ruff check .`.
- [ ] Run `python -m pytest`.
- [ ] Run API-free fixture evaluation.
- [ ] Pin benchmark, harness, environment, model, scaffold, tool, and grader versions.
- [ ] Version pricing tables used for cost claims.
- [ ] Separate grader/environment errors from agent failures.
- [ ] Report task/run counts and uncertainty.
- [ ] Keep safety separately visible.
- [ ] Report recovery gains with cost/latency overhead.
- [ ] Keep negative/null findings and limitations.
## V2 release-gate checks

- [ ] Golden regression set is versioned and reviewed.
- [ ] Baseline and candidate use compatible task/environment/grader versions.
- [ ] Release-gate policy is versioned.
- [ ] Unknown metrics do not silently pass blocking rules.
- [ ] MCP negative tests target only owned/local test servers.
- [ ] OTLP trace payloads are redacted before public artifacts.
- [ ] Incident-derived cases are privacy-reviewed and minimized.
- [ ] PR report distinguishes candidate regression from evaluation infrastructure failure.

