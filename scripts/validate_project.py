from pathlib import Path
import re, sys, tomllib
try:
    import yaml
except Exception as exc:
    print(f"PyYAML import failed: {exc}"); sys.exit(1)
ROOT=Path(__file__).resolve().parents[1]
required=["README.md","CLAUDE.md","PROJECT_STRUCTURE.md","pyproject.toml","docs/PROJECT_PHASES_AND_TASKS.md","docs/TASK_DEPENDENCIES.md","docs/TASKS.md","docs/BENCHMARK_INTEGRITY_POLICY.md","docs/RELIABILITY_METRICS.md","docs/EVALUATION_PROTOCOL.md","docs/GIT_WORKFLOW.md","docs/FINAL_AUDIT.md","src/agentproof/__init__.py","src/agentproof/cli.py"]
missing=[p for p in required if not (ROOT/p).exists()]
if missing: print("Missing required files:",missing); sys.exit(1)
with open(ROOT/"pyproject.toml","rb") as f: project=tomllib.load(f)
if project["project"]["name"]!="agentproof": print("Unexpected project name"); sys.exit(1)
if project["project"]["scripts"].get("agentproof")!="agentproof.cli:app": print("Broken CLI entry point"); sys.exit(1)
for path in sorted(ROOT.rglob("*.yaml"))+sorted(ROOT.rglob("*.yml")):
    try: yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc: print(f"Invalid YAML {path.relative_to(ROOT)}: {exc}"); sys.exit(1)

# Parse JSON / JSONL fixtures.
for path in sorted(ROOT.rglob("*.json")):
    try:
        import json
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Invalid JSON {path.relative_to(ROOT)}: {exc}"); sys.exit(1)

for path in sorted(ROOT.rglob("*.jsonl")):
    import json
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except Exception as exc:
            print(f"Invalid JSONL {path.relative_to(ROOT)}:{lineno}: {exc}"); sys.exit(1)

# Agent-visible configured task sources must not contain grader-only gold fields.
gold_keys = {"expected", "gold", "gold_answer", "reference_answer", "winning_outcome"}
for cfg_path in sorted(ROOT.rglob("*.yaml")) + sorted(ROOT.rglob("*.yml")):
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    if not isinstance(cfg, dict):
        continue
    task_source = cfg.get("task_source")
    if not task_source:
        continue
    task_path = ROOT / task_source
    if not task_path.exists():
        print(f"Configured task_source does not exist: {task_source}"); sys.exit(1)
    if task_path.suffix == ".jsonl":
        import json
        for lineno, line in enumerate(task_path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            obj = json.loads(line)
            leaked = sorted(gold_keys.intersection(obj))
            if leaked:
                print(
                    f"Gold/grader fields leaked into agent-visible task source "
                    f"{task_source}:{lineno}: {leaked}"
                )
                sys.exit(1)
    grader_source = cfg.get("grader_source")
    if grader_source and not (ROOT / grader_source).exists():
        print(f"Configured grader_source does not exist: {grader_source}"); sys.exit(1)
suffixes={".md",".yaml",".yml",".py",".toml",".json",".jsonl",".sh"}
patterns=[re.compile(r"(configs/[A-Za-z0-9_./-]+\.(?:yaml|yml))(?![A-Za-z0-9])"),re.compile(r"(examples/[A-Za-z0-9_./-]+\.(?:jsonl|json|yaml|yml|md))(?![A-Za-z0-9])")]
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in suffixes: continue
    try: content=path.read_text(encoding="utf-8")
    except UnicodeDecodeError: continue
    for pattern in patterns:
        for ref in pattern.findall(content):
            if not (ROOT/ref).exists(): print(f"Missing referenced file {ref} from {path.relative_to(ROOT)}"); sys.exit(1)
task_text=(ROOT/"docs/PROJECT_PHASES_AND_TASKS.md").read_text(encoding="utf-8")
ids=re.findall(r"^### Task (\d+\.\d+):",task_text,flags=re.M)
if len(ids)!=len(set(ids)): print("Duplicate task IDs"); sys.exit(1)
order={tid:i for i,tid in enumerate(ids)}; graph={tid:[] for tid in ids}
for m in re.finditer(r"^### Task (\d+\.\d+):.*?^\*\*Depends on:\*\* `([^`]+)`",task_text,flags=re.M|re.S):
    tid,depstr=m.group(1),m.group(2)
    if depstr=="None": continue
    for dep in [x.strip() for x in depstr.split(",")]:
        if dep not in order: print(f"Unknown dependency {tid}->{dep}"); sys.exit(1)
        if order[dep]>=order[tid]: print(f"Forward dependency {tid}->{dep}"); sys.exit(1)
        graph[tid].append(dep)
state={tid:0 for tid in ids}
def visit(n):
    if state[n]==1: raise RuntimeError(f"Dependency cycle involving {n}")
    if state[n]==2: return
    state[n]=1
    for d in graph[n]: visit(d)
    state[n]=2
try:
    for n in ids: visit(n)
except RuntimeError as exc: print(exc); sys.exit(1)
ledger=(ROOT/"docs/TASKS.md").read_text(encoding="utf-8")
ledger_ids=re.findall(r"\*\*Task (\d+\.\d+)\*\*",ledger)
if ledger_ids!=ids: print("TASKS.md mismatch"); sys.exit(1)
link_pat=re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for md in ROOT.rglob("*.md"):
    content=md.read_text(encoding="utf-8")
    for target in link_pat.findall(content):
        if target.startswith(("http://","https://","mailto:","#")): continue
        file_part=target.split("#",1)[0]
        if file_part and not (md.parent/file_part).resolve().exists(): print(f"Broken link {md.relative_to(ROOT)} -> {target}"); sys.exit(1)
bad_terms=["TODO","TBD","FIXME","CHANGEME","your-repo","example.com","MacroSignal","FlowBook","MicroEdge","CaseMind","QuizForge","FedTone","ImpactLens","EquityDesk","FilingLens"]
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in suffixes: continue
    if path.resolve() == Path(__file__).resolve():
        continue
    try: content=path.read_text(encoding="utf-8")
    except UnicodeDecodeError: continue
    for term in bad_terms:
        if term in content: print(f"Stale/forbidden term {term!r} in {path.relative_to(ROOT)}"); sys.exit(1)
if (ROOT/".env").exists(): print(".env must not be committed"); sys.exit(1)
for name in ["private_benchmarks","private_traces","encrypted_traces"]:
    p=ROOT/name
    if p.exists() and any(x.is_file() for x in p.rglob("*")): print(f"Private artifact files found in {name}"); sys.exit(1)
for d in (ROOT/"src/agentproof").rglob("*"):
    if not d.is_dir():
        continue
    if d.name in {"__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"}:
        continue
    if not (d/"__init__.py").exists():
        print(f"Missing __init__.py: {d.relative_to(ROOT)}"); sys.exit(1)
print(f"AgentProof release validation passed: {len(ids)} unique tasks, configs/links/dependencies clean.")
