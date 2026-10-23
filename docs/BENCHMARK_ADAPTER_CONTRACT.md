# Benchmark Adapter Contract

Required:
- benchmark_metadata()
- list_tasks(split)
- load_task(task_id)
- reset_environment(task_id, seed)
- task_context(task_id)
- grade(run_artifact)
- cleanup()

Capabilities:
- deterministic_reset
- exact_grader
- prompt_perturbation
- structural_perturbation
- fault_injection
- environment_snapshot
- tool_schema_instrumentation
- cost_capture
- trajectory_capture

Unsupported capabilities must fail/skip clearly, never be faked.
