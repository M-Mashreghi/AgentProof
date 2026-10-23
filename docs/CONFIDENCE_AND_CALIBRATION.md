# Confidence & Calibration

Channels:
- self-reported confidence
- external failure predictor
- heuristic confidence

Do not compare them as identical quantities.

Self-reported schema should be standardized, e.g. probability 0–1.

Metrics: Brier, reliability curve, ECE-style diagnostic, AUROC, risk-coverage.

Failure predictor features may include tool errors, repeated actions, plan changes, elapsed time, token/tool usage, and self-confidence. Use leakage-safe task splits.
