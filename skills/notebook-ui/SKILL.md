---
name: notebook-ui
description: Use when building or restyling a Jupyter notebook that shows results: consistent theme, colour-coded tables, callouts, KPI row, charts. Reads the project theme.
---

Use `skills/notebook-ui/notebook_ui.py` with a theme from `themes/` (default, or your private brand theme). First cell: `import notebook_ui as ui; T = ui.load_theme(); ui.apply_chart_style(T)`.

Structure: title and one-line answer first (callout), KPI row, then sections with a short markdown lead-in each. Evidence before detail, limits last.

Rules:
- One idea per chart, direct labels over legends, title states the finding.
- Same colour always means the same thing. Status colours (good, warn, bad) only for status. Categorical colours come from the theme palette, in order.
- Tables: format numbers once (`ui.fmt`), colour-code the one column that matters (`ui.style_table`), cap rows, right-align numbers.
- Never rely on colour alone: add a symbol or label.
- Notebook runs top to bottom on a fresh kernel and reads results from stored tables, never recomputes different numbers inline.
