---
name: show-me-your-work
description: Use after a long or unattended run to audit what happened. Checks docs/decisions.tsv against the transcript and flags gaps.
disable-model-invocation: true
---

Read docs/decisions.tsv (ts, ticket, decision, why, evidence). For each row verify the evidence exists. List decisions made without a row, rows without evidence, and any step that skipped a gate. Report in a table with `NEXT:`.
