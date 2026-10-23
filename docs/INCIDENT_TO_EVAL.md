# Incident → Eval Learning Loop

## Purpose

Production failures are among the highest-value future regression cases.

## Workflow

1. Import incident trace/log.
2. Remove secrets and user-identifying fields.
3. Separate environment/tool outage from agent behavior.
4. Minimize to the smallest reproducible scenario.
5. Define invariant / expected outcome / policy constraint.
6. Create a versioned golden task.
7. Verify the old/bad configuration reproduces the failure where practical.
8. Verify the fix succeeds.
9. Add the case to the release gate permanently.

## Metadata

Store:
- incident id,
- discovery date,
- severity,
- root-cause hypothesis,
- reproduced flag,
- minimized task id,
- fixed-by version/commit,
- privacy/redaction review.

Do not store production secrets or unnecessary user data.
