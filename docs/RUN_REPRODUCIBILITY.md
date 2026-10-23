# Run Reproducibility

Evaluation unit:
benchmark + task + environment + model + scaffold + system prompt + tool schema + memory/retrieval + reasoning/effort + recovery policy.

Fresh runs must not inherit hidden memory, prior final answers, prior successful trajectories, or task-specific solution caches.

Hash task version, environment hash, agent config hash, seed, perturbation, fault, and recovery ids.
