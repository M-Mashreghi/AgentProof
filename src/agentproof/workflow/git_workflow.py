"""Per-task Git workflow checks.

Implements the read-only guards behind ``docs/GIT_WORKFLOW.md``: commit message
format, branch/remote/upstream state, staged-file hygiene, and push
verification. Nothing here creates, renames, or replaces a remote, and nothing
pushes; missing ``origin`` is reported as a push blocker, never "fixed".
"""

from __future__ import annotations

import fnmatch
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

# ``task(<id>)`` for task work; ``docs(<id>)`` for ledger follow-ups that record a hash.
COMMIT_SUBJECT_RE = re.compile(
    r"^(?P<type>task|docs)\((?P<task_id>\d+\.\d+)\): (?P<summary>\S.*)$"
)
MAX_SUBJECT_LENGTH = 72
TASK_HEADING_RE = re.compile(r"^### Task (\d+\.\d+):", flags=re.MULTILINE)

# Paths that must never be staged in a task commit.
FORBIDDEN_STAGED_PATTERNS = (
    ".env",
    ".env.*",
    ".venv/*",
    "private_benchmarks/*",
    "private_traces/*",
    "encrypted_traces/*",
    "*.pem",
    "*.key",
)
ALLOWED_STAGED_EXCEPTIONS = (".env.example",)


class GitError(RuntimeError):
    """Raised when a git command fails or the path is not a repository."""


@dataclass(frozen=True)
class GitState:
    branch: str | None  # None when HEAD is detached
    origin_url: str | None
    upstream: str | None
    ahead: int
    behind: int
    staged: tuple[str, ...]
    unstaged: tuple[str, ...]
    untracked: tuple[str, ...]
    head_subject: str | None


@dataclass
class WorkflowReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def _git_optional(repo: Path, *args: str) -> str | None:
    try:
        return _git(repo, *args).strip() or None
    except GitError:
        return None


def known_task_ids(plan_path: Path) -> list[str]:
    """Task ids in plan order, read from ``docs/PROJECT_PHASES_AND_TASKS.md``."""
    return TASK_HEADING_RE.findall(plan_path.read_text(encoding="utf-8"))


def validate_commit_subject(
    subject: str,
    known_ids: list[str] | None = None,
    expected_task_id: str | None = None,
) -> list[str]:
    """Return problems with a commit subject; empty list means it is valid."""
    errors: list[str] = []
    match = COMMIT_SUBJECT_RE.match(subject)
    if match is None:
        return [
            "commit subject must match 'task(<id>): <summary>' or "
            f"'docs(<id>): <summary>', got {subject!r}"
        ]
    task_id = match.group("task_id")
    if len(subject) > MAX_SUBJECT_LENGTH:
        errors.append(f"commit subject exceeds {MAX_SUBJECT_LENGTH} characters")
    if subject.rstrip() != subject or match.group("summary").endswith("."):
        errors.append("commit subject must not end with whitespace or a period")
    if known_ids is not None and task_id not in known_ids:
        errors.append(f"unknown task id {task_id!r}")
    if expected_task_id is not None and task_id != expected_task_id:
        errors.append(f"commit is for task {task_id}, expected {expected_task_id}")
    return errors


def forbidden_staged_paths(paths: tuple[str, ...] | list[str]) -> list[str]:
    bad = []
    for path in paths:
        name = Path(path).name
        if path in ALLOWED_STAGED_EXCEPTIONS or name in ALLOWED_STAGED_EXCEPTIONS:
            continue
        if any(
            fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(name, pat)
            for pat in FORBIDDEN_STAGED_PATTERNS
        ):
            bad.append(path)
    return bad


def inspect_repo(repo: Path) -> GitState:
    """Read branch/remote/upstream/working-tree state without modifying anything."""
    if _git_optional(repo, "rev-parse", "--is-inside-work-tree") != "true":
        raise GitError(f"{repo} is not a git work tree")
    branch = _git_optional(repo, "symbolic-ref", "--quiet", "--short", "HEAD")
    origin_url = _git_optional(repo, "remote", "get-url", "origin")
    upstream = _git_optional(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    ahead = behind = 0
    if upstream:
        counts = _git(repo, "rev-list", "--left-right", "--count", "HEAD...@{u}").split()
        ahead, behind = int(counts[0]), int(counts[1])

    staged: list[str] = []
    unstaged: list[str] = []
    untracked: list[str] = []
    for line in _git(repo, "status", "--porcelain=v1", "--untracked-files=all").splitlines():
        code, path = line[:2], line[3:]
        if code == "??":
            untracked.append(path)
            continue
        if code[0] not in (" ", "?"):
            staged.append(path)
        if code[1] not in (" ", "?"):
            unstaged.append(path)

    head_subject = _git_optional(repo, "log", "-1", "--format=%s")
    return GitState(
        branch=branch,
        origin_url=origin_url,
        upstream=upstream,
        ahead=ahead,
        behind=behind,
        staged=tuple(staged),
        unstaged=tuple(unstaged),
        untracked=tuple(untracked),
        head_subject=head_subject,
    )


def check_pre_commit(state: GitState) -> WorkflowReport:
    """Checks before committing a task: branch, remote, and staged scope."""
    report = WorkflowReport()
    if state.branch is None:
        report.errors.append("HEAD is detached; check out a branch before committing")
    if state.origin_url is None:
        report.warnings.append(
            "no 'origin' remote: commit locally, mark the task [!] Push Blocked; "
            "do not invent a remote"
        )
    if state.behind:
        report.errors.append(f"branch is {state.behind} commit(s) behind {state.upstream}")
    if not state.staged:
        report.errors.append("nothing is staged")
    bad = forbidden_staged_paths(state.staged)
    if bad:
        report.errors.append(f"forbidden paths staged: {bad}")
    return report


def check_post_push(
    state: GitState,
    known_ids: list[str] | None = None,
    expected_task_id: str | None = None,
) -> WorkflowReport:
    """Checks after committing/pushing a task: HEAD message and upstream sync."""
    report = WorkflowReport()
    if state.head_subject is None:
        report.errors.append("repository has no commits")
    else:
        report.errors.extend(
            validate_commit_subject(state.head_subject, known_ids, expected_task_id)
        )
    if state.origin_url is None:
        report.warnings.append("no 'origin' remote: push blocked, mark the task [!]")
    elif state.upstream is None:
        report.errors.append("branch has no upstream; push with 'git push -u origin <branch>'")
    elif state.ahead or state.behind:
        report.errors.append(
            f"push not verified: {state.ahead} ahead / {state.behind} behind {state.upstream}"
        )
    return report
