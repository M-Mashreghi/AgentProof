# Trajectory Contract

RunTrajectory:
run_id, task_id, started_at, ended_at, agent_version, events[], final_output, confidence, grader_result, cost_summary.

Event:
event_index, timestamp, event_type, model_call_id, tool_name, args/result hashes, action_type, error_type, retry_index, token_usage, latency.

Normalize observable categories only; never expose hidden chain-of-thought.
