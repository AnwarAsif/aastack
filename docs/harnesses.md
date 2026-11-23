# Using aastack with different tools

| Tool | Reads | Notes |
|---|---|---|
| Claude Code | `CLAUDE.md` (imports AGENTS.md), `.claude/agents`, `.claude/skills`, `.claude/settings.json` | Full support: hooks enforce the checks. Run the lead with `claude --agent lead`. |
| GitHub Copilot | `AGENTS.md`, `.github/copilot-instructions.md`, `.github/skills` | No hooks: run `python3 checks/tree_audit.py` and the ticket checks yourself at each leg end. Subagent support varies, so run tickets one at a time. |
| Cursor | `AGENTS.md`, skills if enabled | No hooks on tool calls. Same manual checks as Copilot. |
| Codex and others | `AGENTS.md` | Rules are in AGENTS.md; the guard does not run. |

Protection from subagents relies on the hook's `agent_type`; where there is no hook, run `python3 checks/check_weakened.py` and `python3 checks/run_checks.py task` yourself at each leg end.

`scripts/link-harness.sh` creates the folder links. Token usage: Claude Code `/usage` and `/context`; Copilot premium-request analytics; Cursor dashboard. Log spend by hand in docs/usage.tsv where there are no hooks.
