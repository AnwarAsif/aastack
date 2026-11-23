# PLAN

One row per ticket, in order. Only a ticket marked `doing` may create new files, and only those listed in Output.
Status: todo, doing, done. Done only when the Check output was shown.

| # | Ticket | Owner | Output | Check | Budget | Status |
|---|---|---|---|---|---|---|
| T0 | Grill the human, fill SPEC, get APPROVED | lead | SPEC.md | python3 checks/check_spec.py | 20k | todo |
| T1 | First real ticket | builder | src/example.py | python3 -m unittest discover -s tests | 50k | todo |
| T9 | Independent verification | verifier | none | all items PASS | 40k | todo |

Every ticket also meets docs/definition-of-done.md.
Done = last ticket passed. Everything else goes to BACKLOG.md.
