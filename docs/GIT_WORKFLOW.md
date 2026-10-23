# Git & GitHub Workflow

Implement → Test → Benchmark-integrity checks → Update docs → git diff --check → Stage task files only → Commit → Push → Verify → STOP.

Commit: `task(<task-id>): <short imperative summary>`.

If push fails, keep local verified commit, mark `[!]`, report blocker, stop. Never force-push.
