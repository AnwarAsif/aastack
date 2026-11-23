# Playbook: build a ticket (one leg)
1. Set the ticket `doing` in PLAN.md. Re-read its Output, Check and Budget.
2. Restate the goal. List the files you will create (they must be the Output).
3. Write the test or check first when a cheap one exists.
4. Build the smallest thing that passes. Throwaway work goes in `.scratch/`.
5. Run the ticket's Check and keep the raw output.
6. Run `python3 checks/tree_audit.py`. Fix strays.
7. Log one line in docs/decisions.tsv, mark the ticket done, report the leg, stop.

## Rationalizations
| Excuse | Reality |
|---|---|
| "I need one extra helper file" | Add it to the ticket Output first, or use .scratch/. |
| "This check is flaky, skip it" | Fix the cause or REQUEST a change from the lead. Do not skip. |
| "I will clean up at the end" | Run tree_audit now, every leg. |
