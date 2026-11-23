---
name: writing-for-agents
description: Use when creating or editing a skill, agent file, AGENTS.md or any document an agent reads.
disable-model-invocation: true
---

- Descriptions are pointers: front-load the trigger ("Use when ..."), one trigger per distinct branch.
- Keep always-loaded text lean. Put branch-only detail in files the skill points to.
- Every step needs a checkable completion criterion.
- One source of truth per meaning. Do not restate what a file, type or config already shows.
- Say what to do, not why, unless the rule confuses without it. Prefer positive phrasing; keep prohibitions for hard guardrails.
- When in doubt, delete the line. Prune stale lines. Slash-only skills get `disable-model-invocation: true`.
