# How aastack works

**Roles.** lead plans and gates; researcher answers one question; builder builds one ticket; verifier tries to break the result. Files: `agents/`.

**Loop.** SPEC approved (human gate) -> PLAN tickets with owner, output, check, budget -> per ticket one leg: do, check, audit the tree, log, report, stop -> last ticket verified by a fresh verifier -> `cleanup`.

**Trust order** (from "All Code Is Slop"): deterministic code first (`checks/`, hooks), verification second (verifier, tests), prose last (AGENTS.md, skills). Every correction becomes a check (`correct` skill).

**Skills.** `skills/` has 12 that fire on their own trigger and 23 slash-only (`disable-model-invocation: true`, zero standing context cost). `playbooks/` map a task type to steps the lead copies into its todo list.

**Never lower the bar.** `CONSTRAINTS.md` lists the checks by cost tier. Subagents cannot edit checks, constraints or existing tests, and `check_weakened.py` flags new suppressions, skipped or deleted tests and changed constraints. Fix the work, not the check.

**Waste control.** New files must be Outputs of the `doing` ticket; `.scratch/` is the only free zone; no "final/v2" names; legs and token budgets cap the time.

**Connectors.** `connectors/` documents each outside system: read-only by default, secrets only in env vars, one smoke test.
