---
name: handoff
description: Use when the context is nearly full, a quota runs out, or work moves to another agent or tool. Writes a resume note so a fresh agent continues without rereading the chat.
---

Write `docs/handoff.md` (overwrite): goal, current ticket and state, what is done with evidence, what is next as one concrete first action, open decisions waiting on the human, files that matter (paths only), commands to resume. Redact secrets. Stop at a safe boundary first: no half-written outputs, ticket status accurate in PLAN.md.

To resume: read docs/handoff.md, verify its claims against the real files, then continue with the first action. Do not redo finished work.
