import subprocess
from pathlib import Path

import pytest

from agentproof.workflow.git_workflow import (
    GitError,
    check_post_push,
    check_pre_commit,
    forbidden_staged_paths,
    inspect_repo,
    known_task_ids,
    validate_commit_subject,
)

ROOT = Path(__file__).resolve().parents[2]
IDS = ["1.1", "1.2", "1.3"]


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    ).stdout


def make_repo(tmp_path: Path, with_origin: bool = True) -> Path:
    repo = tmp_path / "work"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.name", "Test")
    git(repo, "config", "user.email", "test@invalid")
    git(repo, "config", "commit.gpgsign", "false")
    (repo / "README.md").write_text("x\n")
    git(repo, "add", "README.md")
    git(repo, "commit", "-q", "-m", "task(1.1): seed repository")
    if with_origin:
        bare = tmp_path / "origin.git"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
        git(repo, "remote", "add", "origin", str(bare))
        git(repo, "push", "-q", "-u", "origin", "main")
    return repo


@pytest.mark.parametrize(
    "subject",
    ["task(1.2): add workflow checks", "task(1.3): load typed configs"],
)
def test_valid_commit_subjects(subject):
    assert validate_commit_subject(subject, IDS) == []


@pytest.mark.parametrize(
    "subject",
    [
        "add workflow checks",
        "task 1.2: add workflow checks",
        "task(1.2):add workflow checks",
        "Task(1.2): add workflow checks",
        "task(1.2): ",
    ],
)
def test_malformed_commit_subjects(subject):
    assert validate_commit_subject(subject, IDS)


def test_commit_subject_rules():
    assert validate_commit_subject("task(9.9): fix thing", IDS) == ["unknown task id '9.9'"]
    assert validate_commit_subject("task(1.2): x", IDS, "1.3") == [
        "commit is for task 1.2, expected 1.3"
    ]
    assert validate_commit_subject("task(1.2): add workflow checks.", IDS)
    assert validate_commit_subject("task(1.2): " + "a" * 80, IDS)


def test_known_task_ids_follow_plan_order():
    ids = known_task_ids(ROOT / "docs" / "PROJECT_PHASES_AND_TASKS.md")
    assert ids[:3] == IDS
    assert len(ids) == len(set(ids)) == 108


def test_forbidden_staged_paths():
    staged = [".env", ".env.example", "config/.env.local", "private_traces/a.json", "src/x.py"]
    assert forbidden_staged_paths(staged) == [".env", "config/.env.local", "private_traces/a.json"]


def test_inspect_rejects_non_repo(tmp_path):
    with pytest.raises(GitError):
        inspect_repo(tmp_path)


def test_clean_pushed_repo_passes_post_push(tmp_path):
    repo = make_repo(tmp_path)
    state = inspect_repo(repo)
    assert state.branch == "main"
    assert state.upstream == "origin/main"
    assert (state.ahead, state.behind) == (0, 0)
    report = check_post_push(state, IDS, "1.1")
    assert report.ok, report.errors


def test_unpushed_commit_fails_post_push(tmp_path):
    repo = make_repo(tmp_path)
    (repo / "a.txt").write_text("a\n")
    git(repo, "add", "a.txt")
    git(repo, "commit", "-q", "-m", "task(1.2): add a")
    report = check_post_push(inspect_repo(repo), IDS, "1.2")
    assert not report.ok
    assert any("1 ahead" in e for e in report.errors)


def test_missing_origin_is_warning_and_never_created(tmp_path):
    repo = make_repo(tmp_path, with_origin=False)
    (repo / "a.txt").write_text("a\n")
    git(repo, "add", "a.txt")
    state = inspect_repo(repo)
    pre = check_pre_commit(state)
    post = check_post_push(state, IDS)
    assert pre.ok and post.ok
    assert any("origin" in w for w in pre.warnings + post.warnings)
    assert git(repo, "remote").strip() == ""


def test_pre_commit_staging_rules(tmp_path):
    repo = make_repo(tmp_path)
    assert "nothing is staged" in check_pre_commit(inspect_repo(repo)).errors

    (repo / "a.txt").write_text("a\n")
    (repo / "b.txt").write_text("b\n")
    git(repo, "add", "a.txt")
    state = inspect_repo(repo)
    assert state.staged == ("a.txt",)
    assert state.untracked == ("b.txt",)
    assert check_pre_commit(state).ok

    (repo / ".env").write_text("SECRET=1\n")
    git(repo, "add", "-f", ".env")
    report = check_pre_commit(inspect_repo(repo))
    assert any(".env" in e for e in report.errors)


def test_detached_head_fails_pre_commit(tmp_path):
    repo = make_repo(tmp_path)
    git(repo, "checkout", "-q", "--detach")
    (repo / "a.txt").write_text("a\n")
    git(repo, "add", "a.txt")
    state = inspect_repo(repo)
    assert state.branch is None
    assert any("detached" in e for e in check_pre_commit(state).errors)
