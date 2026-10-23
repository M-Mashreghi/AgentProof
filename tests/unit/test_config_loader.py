from pathlib import Path

import pytest

from agentproof.config import (
    ConfigError,
    ConfigKind,
    load_config,
    load_research_study,
)
from agentproof.config.models import AgentConfig, BenchmarkConfig, ConfidenceChannel

ROOT = Path(__file__).resolve().parents[2]
TYPED_DIRS = [
    "benchmarks", "agents", "reliability", "perturbations", "faults", "recovery", "research",
]
REPO_CONFIGS = sorted(p for d in TYPED_DIRS for p in (ROOT / "configs" / d).glob("*.yaml"))

AGENT_YAML = """\
agent_id: a
agent_version: 1
model: {provider: mock, model_id: m}
scaffold: {name: s, version: 1}
confidence: {channel: self_reported, schema: probability_0_1}
memory: {cross_run_memory: false}
tools: {source: tools.json}
"""
BENCHMARK_YAML = """\
benchmark_id: b
benchmark_version: 1
adapter: jsonl
task_source: tasks.jsonl
grader_source: gold.jsonl
"""
STUDY_YAML = """\
name: study
benchmark_config: configs/benchmarks/b.yaml
agent_config: configs/agents/a.yaml
runs_per_task: 3
"""


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    (tmp_path / "pyproject.toml").write_text("[project]\nname='x'\n")
    for name in ["tools.json", "tasks.jsonl", "gold.jsonl"]:
        (tmp_path / name).write_text("{}\n")
    write(tmp_path, "configs/agents/a.yaml", AGENT_YAML)
    write(tmp_path, "configs/benchmarks/b.yaml", BENCHMARK_YAML)
    write(tmp_path, "configs/research/study.yaml", STUDY_YAML)
    return tmp_path


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


@pytest.mark.parametrize("path", REPO_CONFIGS, ids=lambda p: p.relative_to(ROOT).as_posix())
def test_repository_configs_load(path):
    loaded = load_config(path)
    assert loaded.provenance.path == path.relative_to(ROOT).as_posix()
    assert len(loaded.provenance.content_sha256) == 64


def test_every_typed_kind_present_in_repository():
    kinds = {load_config(p).provenance.kind for p in REPO_CONFIGS}
    assert kinds == set(ConfigKind)


def test_repository_research_studies_resolve():
    multirun = load_research_study(ROOT / "configs/research/multirun_mvp.yaml")
    assert multirun.runs_per_task == 5
    assert multirun.benchmark.config.benchmark_id == "synthetic_reliability"
    assert multirun.agent.config.memory.cross_run_memory is False

    robustness = load_research_study(ROOT / "configs/research/robustness_study.yaml")
    assert robustness.perturbation is not None and robustness.fault is not None
    assert set(robustness.provenance()) == {
        "research", "benchmark", "agent", "reliability", "perturbation", "fault",
    }

    recovery = load_research_study(ROOT / "configs/research/recovery_study.yaml")
    assert recovery.recovery is not None
    assert recovery.recovery.config.verifier.gold_answer_access is False


def test_agent_settings_stay_separate(repo):
    agent = load_config(repo / "configs/agents/a.yaml").config
    assert isinstance(agent, AgentConfig)
    assert agent.model.model_id == "m"
    assert agent.scaffold.name == "s"
    assert agent.confidence is not None
    assert agent.confidence.channel is ConfidenceChannel.SELF_REPORTED


def test_kind_inference_and_explicit_kind(repo):
    outside = write(repo, "other/b.yaml", BENCHMARK_YAML)
    with pytest.raises(ConfigError, match="cannot infer"):
        load_config(outside)
    assert isinstance(load_config(outside, kind="benchmark").config, BenchmarkConfig)


def test_relative_path_resolves_against_root(repo):
    loaded = load_config("configs/agents/a.yaml", root=repo)
    assert loaded.provenance.path == "configs/agents/a.yaml"


def test_provenance_is_deterministic_and_canonical(repo):
    path = repo / "configs/agents/a.yaml"
    first = load_config(path).provenance
    assert load_config(path).provenance == first

    path.write_text("# comment\n" + AGENT_YAML.replace("agent_id: a", "agent_id:   a"))
    reformatted = load_config(path).provenance
    assert reformatted.content_sha256 != first.content_sha256
    assert reformatted.canonical_sha256 == first.canonical_sha256

    path.write_text(AGENT_YAML.replace("agent_version: 1", "agent_version: 2"))
    assert load_config(path).provenance.canonical_sha256 != first.canonical_sha256


@pytest.mark.parametrize(
    ("old", "new", "message"),
    [
        ("tools.json", "missing.json", "referenced file does not exist"),
        ("tools.json", "/etc/passwd", "repo-relative"),
        ("tools.json", "../tools.json", "escape the repository"),
        ("tools.json", "dir\\\\tools.json", "repo-relative"),
        ("agent_version: 1", "agent_version: 0", "greater than or equal to 1"),
        ("agent_version: 1", "agent_version: '1'", "valid integer"),
        ("cross_run_memory: false", "cross_run_memory: true", "repeated runs must be independent"),
        ("self_reported", "vibes", "channel"),
        ("agent_id: a", "agent_id: a\nagent_name: typo", "Extra inputs are not permitted"),
        ("agent_id: a", "agent_id: a\nagent_id: b", "duplicate key"),
        ("agent_id: a", "agent_id: [a", "invalid YAML"),
    ],
)
def test_agent_config_rejections(repo, old, new, message):
    path = write(repo, "configs/agents/bad.yaml", AGENT_YAML.replace(old, new))
    with pytest.raises(ConfigError, match=message):
        load_config(path)


@pytest.mark.parametrize(
    ("old", "new", "message"),
    [
        ("benchmark_version: 1\n", "", "must pin benchmark_version"),
        ("grader_source: gold.jsonl", "grader_source: tasks.jsonl", "must be separate files"),
        ("adapter: jsonl", "adapter: jsonl\ncapabilities: {teleport: true}", "Extra inputs"),
    ],
)
def test_benchmark_config_rejections(repo, old, new, message):
    path = write(repo, "configs/benchmarks/bad.yaml", BENCHMARK_YAML.replace(old, new))
    with pytest.raises(ConfigError, match=message):
        load_config(path)


def test_disabled_external_benchmark_needs_no_local_sources(repo):
    text = "benchmark_id: ext\nadapter: x\nenabled: false\n"
    path = write(repo, "configs/benchmarks/ext.yaml", text)
    cfg = load_config(path).config
    assert cfg.capabilities.fault_injection is False


@pytest.mark.parametrize(
    ("rel", "text", "message"),
    [
        (
            "configs/reliability/r.yaml",
            "version: 1\nruns_per_task: 5\ndimensions: {capability: true, consistency: true,"
            " predictability: true, robustness: true, recovery: true, safety: true,"
            " economics: true}\naggregate: {enabled: true}\n",
            "formula and normalization",
        ),
        (
            "configs/reliability/r.yaml",
            "version: 1\nruns_per_task: 5\ndimensions: {capability: true}\n",
            "Field required",
        ),
        (
            "configs/perturbations/p.yaml",
            "version: 1\nsemantics_preserving: [prompt_paraphrase]\n"
            "semantics_changing: {enabled: true, variants: [prompt_paraphrase]}\n",
            "both semantics-preserving and -changing",
        ),
        (
            "configs/perturbations/p.yaml",
            "version: 1\nsemantics_changing: {enabled: false, variants: [negate]}\n",
            "listed while disabled",
        ),
        (
            "configs/perturbations/p.yaml",
            "version: 1\nsemantics_preserving: [prompt_paraphrase, prompt_paraphrase]\n",
            "duplicate entries",
        ),
        (
            "configs/faults/f.yaml",
            "version: 1\nfaults: [timeout_once]\nguards: {do_not_corrupt_grader: false}\n",
            "do_not_corrupt_grader",
        ),
        ("configs/faults/f.yaml", "version: 1\nfaults: [meteor_strike]\n", "faults"),
        ("configs/faults/f.yaml", "version: 1\nfaults: []\n", "at least 1"),
        (
            "configs/recovery/rc.yaml",
            "version: 1\npolicies: [retry_once]\nverifier: {gold_answer_access: true}\n",
            "never receive gold answers",
        ),
        ("configs/research/s.yaml", "- not\n- a mapping\n", "top level must be a mapping"),
        (
            "configs/research/s.yaml",
            STUDY_YAML + "run_isolation: {cross_run_memory: true}\n",
            "repeated runs must be independent",
        ),
        (
            "configs/research/s.yaml",
            STUDY_YAML + "budget: {max_cost_usd: -1, max_wall_minutes: 10}\n",
            "greater than or equal to 0",
        ),
        (
            "configs/research/s.yaml",
            STUDY_YAML + "matched_baseline: true\n",
            "requires a perturbation_config or fault_config",
        ),
    ],
)
def test_other_kind_rejections(repo, rel, text, message):
    with pytest.raises(ConfigError, match=message):
        load_config(write(repo, rel, text))


def test_research_study_resolves_references(repo):
    study = load_research_study(repo / "configs/research/study.yaml")
    assert study.runs_per_task == 3
    assert study.reliability is None
    assert study.provenance()["agent"].path == "configs/agents/a.yaml"


def test_research_study_rejects_missing_reference(repo):
    path = write(
        repo, "configs/research/s.yaml", STUDY_YAML.replace("agents/a.yaml", "agents/none.yaml")
    )
    with pytest.raises(ConfigError, match="referenced file does not exist"):
        load_research_study(path)


def test_research_study_rejects_wrong_kind_reference(repo):
    path = write(
        repo,
        "configs/research/s.yaml",
        STUDY_YAML.replace("configs/benchmarks/b.yaml", "configs/agents/a.yaml"),
    )
    with pytest.raises(ConfigError, match="expected a benchmark config"):
        load_research_study(path)


def test_research_study_propagates_nested_errors(repo):
    write(repo, "configs/agents/a.yaml", AGENT_YAML.replace("false", "true"))
    with pytest.raises(ConfigError, match="configs/agents/a.yaml"):
        load_research_study(repo / "configs/research/study.yaml")


def test_config_outside_root_rejected(repo, tmp_path_factory):
    elsewhere = tmp_path_factory.mktemp("elsewhere") / "a.yaml"
    elsewhere.write_text(AGENT_YAML)
    with pytest.raises(ConfigError, match="inside the repository"):
        load_config(elsewhere, kind="agent", root=repo)
