---
name: cleanup
description: Use at the end of a leg or session, before committing, when the tree feels cluttered, or when the user says clean up, land, or wrap up. Removes junk and stray files and keeps commits small.
---

Leave the tree smaller than you found it. Nothing is deleted without the human seeing the list.

1. `python3 checks/tree_audit.py` for strays and scratch files. `python3 scripts/gc.py` for junk files and merged branches.
2. Show one table. `REQUEST: delete N safe items? RECOMMEND: yes`. Safe means junk patterns, scratch files and merged branches. Strays that are real work need a decision: add to a ticket Output, move, or delete.
3. On yes: `python3 scripts/gc.py --apply --yes` and `python3 checks/tree_audit.py --clean-scratch`.
4. Look in files this session touched for unused code, commented-out code, duplicate helpers and stale docs. Delete what is clearly unused, list the rest.
5. Commit small: one logical change, imperative subject of 60 characters or fewer, body only for the why. Never commit outputs, secrets or large binaries. Push only after the human clears it.
6. Update PLAN.md and docs/decisions.tsv. Report `LANDED | n files removed, n commits` and `NEXT:`.

## Rationalizations
| Excuse | Reality |
|---|---|
| "I might need that file later" | If a ticket needs it, it is in Output. Otherwise it is clutter; the log has the decision. |
| "Leave cleanup for the end" | Run the audit every leg; the end is when it is most expensive. |
| "Just delete everything in scratch and src" | Only the safe list, shown to the human first. |
