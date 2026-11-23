---
name: reflect
description: Use after a session or ticket to capture lessons. Proposes edits to skills, checks and AGENTS.md, and waits for approval.
disable-model-invocation: true
---

1. List what went wrong or took longer than planned (from docs/decisions.tsv, BLOCKED.md, the chat).
2. For each, pick the fix level: check, then skill, then prose. Use the `correct` skill for repeat mistakes.
3. Propose the edits as a diff list. Apply only what the human approves.
