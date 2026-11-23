---
name: architect
description: Use before building something non-trivial: new tables, modules or pipeline stages. Sketches two shapes, picks the one with a single owner for each piece of state.
disable-model-invocation: true
---

1. Name the data shape first: entities, keys, grain of each table.
2. Sketch two structures (tables or modules, inputs and outputs) in 15 lines each.
3. Pick the one where each piece of state has one owner and the fewest moving parts. Say why in one line.
4. Write the chosen shape into the ticket or docs/research.md. Then build.
