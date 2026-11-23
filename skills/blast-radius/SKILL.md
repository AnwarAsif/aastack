---
name: blast-radius
description: Use before changing a shared table, schema, definition or interface. Finds what else it could break.
disable-model-invocation: true
---

1. List everything that reads or depends on the thing (grep, lineage, docs).
2. Prove the key safety fact by running something (a query count, a diff of outputs), not by reasoning.
3. Report affected items, the proof, and the cheapest safe order of change.
