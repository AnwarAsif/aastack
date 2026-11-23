---
name: token-budget
description: Use at session start, when planning tickets, or when a run feels expensive. Sets per-role models and turn caps, reads docs/usage.tsv, and compares spend to ticket budgets.
---

1. Roles: cheap model for researcher and mechanical work, strongest model for lead and verifier. Set `model`, `effort` and `maxTurns` in each agent file.
2. Budget: every PLAN.md ticket has a Budget (tokens). Estimate before starting; a ticket over 2x its budget stops and asks.
3. Log: the SubagentStop hook appends to `docs/usage.tsv` (input, output, cache read, cache create per subagent). Read it at each gate and write the ticket total in the report as tokens, not money.
4. Trim: keep always-loaded context small (short AGENTS.md, slash-only skills with `disable-model-invocation: true`), send bulk output to subagents and take back summaries, use file pointers not pasted context.
5. Other tools: Claude Code `/usage` and `/context`; Copilot premium-request analytics; Cursor dashboard. They have no hooks, so log spend by hand in docs/usage.tsv.
