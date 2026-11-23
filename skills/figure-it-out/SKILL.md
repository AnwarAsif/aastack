---
name: figure-it-out
description: Use for large or ambiguous work where no playbook fits. Designs a phased playbook, runs a hypothesis loop, and keeps an audit trail.
disable-model-invocation: true
---

1. Frame: goal, constraints, what is unknown.
2. Design 3 to 6 phases, each ending in a checkable result. Write them to PLAN.md as tickets.
3. Loop per unknown: hypothesis, cheapest test, result, keep or drop. Log each in docs/decisions.tsv.
4. Gate with the human after the plan and before the last phase.
