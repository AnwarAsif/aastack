---
name: ui-design
description: Use when designing or reviewing a web or app UI, dashboard or page layout. Short rules for layout, type, spacing, states and accessibility, driven by the project theme.
---

Read `themes/` first: colours, fonts and status colours come from the theme, never hard-coded.

- Layout: one primary action per screen, content width 60 to 80 characters for text, 8-point spacing grid, clear hierarchy by size and weight before colour.
- Type: at most 2 families and 4 sizes. Body 15 to 16 px, line height 1.5.
- Color: text contrast 4.5:1 or better, 3:1 for large text and controls. Do not use color alone to carry meaning.
- States: design empty, loading, error and success for every view. Error text says what happened and what to do.
- Controls: hit targets 44 px or larger on touch, visible focus ring, full keyboard path.
- Responsive: works at phone width with a 16 px gutter and no horizontal scroll. Support light and dark.
- Check with a real render or screenshot, not by reading code. If a frontend-design or artifact-design skill is installed, use it for the visual direction.
