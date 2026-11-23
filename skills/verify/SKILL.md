---
name: verify
description: Use before saying work is done, or at the last ticket. Starts a fresh verifier and gates completion on its result. Can also write a project-specific verify recipe.
---

1. Have the builder refresh outputs so checks run on current data.
2. Start the `verifier` agent fresh, never the builder's run. Brief: goal, then "read AGENTS.md and SPEC.md first, be adversarial".
3. All PASS: mark done, report, stop. Any FAIL: open a fix ticket for that item only, run the builder, then a new fresh verifier. Two rounds at most, then BLOCKED.md and ask.

To create a project recipe: write `docs/verify.md` with the exact commands that run the deliverable end to end, what evidence each step produces, and how to clean up. Run it once before handing off.

## Fresh context, artifact and contract only
Give the verifier the artifact paths and the contract (SPEC.md plus the ticket's Check), never the builder's reasoning or summary. The lead reconciles each finding as: real issue, trade-off (record it in docs/decisions.tsv), or noise (explain why). At most 3 review cycles; if two cycles in a row find nothing actionable, stop.

## Rationalizations
| Excuse | Reality |
|---|---|
| "Tests pass, so it is done" | Tests are written by the same agent; run the deliverable on real data too. |
| "The builder already checked it" | A builder checking its own work shares its blind spots. Use a fresh run. |
| "The check is too strict, I will relax it" | Fix the work. Weakening a check is a protected action for the lead or the human. |
