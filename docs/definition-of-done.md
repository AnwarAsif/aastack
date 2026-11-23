# Definition of done

Applies to every ticket on top of its own Check. A ticket is done only when all hold:

1. The ticket's Check ran and its raw output was shown.
2. Tests pass **and** the deliverable was run or opened on real data. Tests passing alone is not done.
3. A new test or check fails without the change (a wrong value must fail it).
4. `python3 checks/run_checks.py task` passes: no stray files, no weakened checks.
5. Every number in the deliverable has its explain-number lines.
6. One row in docs/decisions.tsv; tokens used are within the ticket Budget or the overrun is explained.
7. No dead code, no leftover files in `.scratch/`.
8. Gates that need the human (spec, plan, landing) have an explicit yes.

Last ticket: a fresh verifier also passes (skill `verify`).
