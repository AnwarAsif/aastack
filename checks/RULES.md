# Rules and what enforces them

A rule with only "prose" is a smell. When it is violated twice, turn it into a check (skill `correct`).

| Rule | Enforcement | Proven by |
|---|---|---|
| No building before SPEC is APPROVED | `guard.py` hook | tests/test_guard.py |
| SPEC cannot be APPROVED with a TBD left | `check_spec.py` | tests/test_guard.py |
| Fixed file tree, no new top-level files or folders | `guard.py` | tests/test_guard.py |
| No "final", "v2", "copy", "old", "tmp" variants | `guard.py` | tests/test_guard.py |
| New files only as Outputs of the `doing` ticket | `guard.py` | tests/test_guard.py |
| Stray and scratch files are listed | `tree_audit.py` | tests/test_tree_audit.py |
| Subagent report is 15 lines or fewer and ends with a call | `check_report.py` hook | tests/test_report.py |
| Token usage per subagent is logged | `usage.py` hook | tests/test_report.py |
| Subagents cannot edit checks, CONSTRAINTS.md, hook settings or existing tests | `guard.py` (uses the hook's agent_type) | tests/test_constraints.py |
| No weakened checks: new suppressions, skipped or deleted tests, changed constraints | `check_weakened.py` | tests/test_constraints.py |
| Constraints run by tier: fast on edit, task at ticket end, full at verification | `run_checks.py` + CONSTRAINTS.md | tests/test_constraints.py |
| Skill rules: name = folder, description starts with Use, 1024 chars or fewer, 3 sentences or fewer, under 500 lines | `check_skills.py` | tests/test_constraints.py |
| Read-only on source systems | connector grants (human sets up) | not enforced in code |
| Explain every number | skill `explain-number`, verifier item 4 | prose |
| Builder does not verify itself | `verify` skill uses a fresh verifier | prose |

Run all: `python3 -m unittest discover -s tests`.
Known gaps: the guard relies on the hook's `agent_type` field to tell the lead from subagents; if a tool does not send it, every writer counts as the lead. Hooks cover Write, Edit and NotebookEdit; a shell command that writes a file bypasses the guard, so the verifier and `tree_audit.py` list the tree. Hooks run only in Claude Code.
