"""Check the per-task Git workflow (see docs/GIT_WORKFLOW.md).

Usage:
    python scripts/check_git_workflow.py pre-commit
    python scripts/check_git_workflow.py post-push [--task 1.2]
    python scripts/check_git_workflow.py message "task(1.2): add workflow checks"

Exit codes: 0 ok (warnings allowed), 1 workflow violation, 3 git/infrastructure error.
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentproof.workflow.git_workflow import (  # noqa: E402
    GitError,
    WorkflowReport,
    check_post_push,
    check_pre_commit,
    inspect_repo,
    known_task_ids,
    validate_commit_subject,
)


def emit(report: WorkflowReport) -> int:
    for warning in report.warnings:
        print(f"WARN  {warning}")
    for error in report.errors:
        print(f"ERROR {error}")
    print("git workflow: OK" if report.ok else "git workflow: FAILED")
    return 0 if report.ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("pre-commit")
    post = sub.add_parser("post-push")
    post.add_argument("--task", help="expected task id of HEAD commit")
    msg = sub.add_parser("message")
    msg.add_argument("subject")
    args = parser.parse_args()

    ids = known_task_ids(ROOT / "docs" / "PROJECT_PHASES_AND_TASKS.md")
    if args.command == "message":
        report = WorkflowReport(errors=validate_commit_subject(args.subject, ids))
        return emit(report)
    try:
        state = inspect_repo(ROOT)
    except GitError as exc:
        print(f"ERROR {exc}")
        return 3
    if args.command == "pre-commit":
        return emit(check_pre_commit(state))
    return emit(check_post_push(state, ids, args.task))


if __name__ == "__main__":
    sys.exit(main())
