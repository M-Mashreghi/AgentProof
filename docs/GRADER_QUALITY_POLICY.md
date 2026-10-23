# Grader Quality Policy

Where possible:
- deterministic rerun
- known positive/negative fixtures
- environment reset repeatability
- manual spot-check
- verified benchmark subset

Outcome classes:
agent_success, agent_failure, grader_error, environment_error, ambiguous.

Any grader code/config change increments grader version/hash.
