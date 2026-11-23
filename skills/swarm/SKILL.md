---
name: swarm
description: Use when work splits into independent slices that can run in parallel (coverage sweeps, many small checks). Fans out workers and aggregates one report.
disable-model-invocation: true
---

1. State the done-test: what each worker must prove, as PASS, ISSUES or BLOCKED.
2. Write one brief per slice: goal, then "read AGENTS.md and SPEC.md first", then a file pointer. Slices must not write the same file.
3. Start the workers in parallel as plain subagents. Cap turns and budget per worker.
4. Aggregate: one table (slice, result, evidence), dropouts named, then `NEXT:`.
