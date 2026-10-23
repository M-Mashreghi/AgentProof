# Perturbation Protocol

Semantics-preserving examples:
- prompt paraphrase
- reorder independent fields
- harmless field renaming with schema update
- add irrelevant context
- formatting changes

Semantics-changing variants require new expected state/grader.

Every variant records id, base task, generator/version, seed, family, changed fields, semantic class, invariant, grader update id.

Validate invariants before evaluation.
