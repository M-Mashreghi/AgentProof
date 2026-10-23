# Git & GitHub Workflow

Implement → Test → Benchmark-integrity checks → Update docs → git diff --check → Stage task files only → Commit → Push → Verify → STOP.

Commit: `task(<task-id>): <short imperative summary>`.

If push fails, keep local verified commit, mark `[!]`, report blocker, stop. Never force-push.

## Workflow checks

`scripts/check_git_workflow.py` enforces the read-only parts of this workflow
(logic in `src/agentproof/workflow/git_workflow.py`):

```bash
python scripts/check_git_workflow.py message "task(1.2): add git workflow checks"
python scripts/check_git_workflow.py pre-commit          # branch, behind-upstream, staged scope
python scripts/check_git_workflow.py post-push --task 1.2  # HEAD subject + upstream in sync
```

- Commit subjects must match `task(<id>): <summary>`, reference a task id from
  `docs/PROJECT_PHASES_AND_TASKS.md`, stay within 72 characters, and not end with a period.
- Secrets, local environments, and private benchmark/trace directories must never be staged.
- A missing `origin` is a warning (push blocked, mark `[!]`); the checker never creates,
  renames, or replaces remotes and never pushes.
- Exit codes: `0` ok, `1` workflow violation, `3` git/infrastructure error.

## Ledger

`docs/TASKS.md` records each task's commit. Because a commit cannot contain its own
hash, the hash of task N is recorded by the next commit (task N+1, or a follow-up
`docs(<id>)` commit for the last task in a session).
