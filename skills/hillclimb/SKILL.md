---
name: hillclimb
description: Use to improve a measured result (model score, speed, accuracy) without drifting. Frozen harness, one change per attempt, noise floor, stop rule.
disable-model-invocation: true
---

1. Before any change write: metric, direction, stop predicate (target met or N attempts). Never relax it later.
2. Freeze the harness: one script, fixed seed and data split. Run it 5 times on the baseline; the spread is the noise floor.
3. List regression gates that must stay green (leakage check, key segments).
4. Loop: state the mechanism, change one thing, run 5 times, take the median. Keep only if the gain beats the noise floor and gates are green. Log every attempt in docs/experiments.tsv.
5. A suspiciously large gain is a leakage alarm: send it to the verifier.
