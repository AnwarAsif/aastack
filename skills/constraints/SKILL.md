---
name: constraints
description: Use to set or tighten the quality bar of a job. Writes CONSTRAINTS.md with checks placed by cost and proves each check can fail.
disable-model-invocation: true
---

Lead or human only (subagents cannot edit CONSTRAINTS.md).

1. Ask four questions with defaults: what must never break, what is the slowest check you accept per ticket, which external source can verify the result (raw data, a source system, a tool outside this repo), and who may grant exceptions.
2. Write the rows in CONSTRAINTS.md: ID, constraint, command, threshold, tier. Put cheap checks in `fast` (under 5 s), ticket checks in `task` (under 90 s), slow or external checks in `full`.
3. Require at least one external check, because checks the agents wrote themselves are circular.
4. Prove each new check: run it on a known violation (it must fail) and on a clean control (it must pass). Record both in docs/decisions.tsv.
5. Ratchets only from a measurement. Exceptions need an owner and an expiry.
6. Run `python3 checks/run_checks.py full`.
