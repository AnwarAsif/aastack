---
name: interrogate
description: Use to stress-test a risky result or design ("challenge this", before shipping). Adversarial review where a finding survives only if a rerunnable command proves it.
---

Brief 2 or 3 reviewers (subagents) in fresh context, each with a different angle: correctness, shortcuts and leakage, missing cases. Give each only the artifact and the contract, not the builder's reasoning, and an adversarial instruction: find what is wrong. Each must produce findings as `claim -> command -> output`.

Keep a finding only if you can rerun its command and see the problem. Drop opinions. Reconcile each survivor as real issue, trade-off or noise. At most 3 cycles; stop earlier if two cycles in a row find nothing actionable. Report the surviving findings ranked by impact, each with the command. Apply no fixes in this step.
