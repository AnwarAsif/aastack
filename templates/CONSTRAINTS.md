# CONSTRAINTS

The quality bar. Agents must not lower it. Only the lead or the human edits this file (the guard blocks subagents).
Commands here are run by `python3 checks/run_checks.py <tier>`, so treat this file like code.

## Floor (never lowered)
Tests pass. No stray or unplanned files. No weakened checks. A valid spec.

## Constraints
| ID | Constraint | Command | Threshold | Tier |
|---|---|---|---|---|
| C1 | Spec is valid | python3 checks/check_spec.py | exit 0 | fast |
| C2 | Tests pass | python3 -m unittest discover -s tests | exit 0 | task |
| C3 | No stray files | python3 checks/tree_audit.py | 0 strays | task |
| C4 | No weakened checks | python3 checks/check_weakened.py | 0 findings | task |
| C5 | Skill rules hold | python3 checks/check_skills.py | exit 0 | task |

Tiers: **fast** runs after every edit (under 5 s), **task** when a ticket closes (under 90 s), **full** at verification.
Put slow checks only in `full`. Never put them in `fast`.

## Add at least one external check
Checks that agents also write (their own tests) are circular. Add one that is not: a recompute from the raw source, a row-count reconciliation against the source system, a leakage test, or a tool that is not in this repo. Use `/constraints` to add it, then prove it fails on a known violation and passes on a clean control.

## Ratchets
Numbers that may only improve, recorded from a measurement, never guessed. Format: `ID, metric, current best`.

## Exceptions
| ID | What is waived | Owner | Expires |
|---|---|---|---|
