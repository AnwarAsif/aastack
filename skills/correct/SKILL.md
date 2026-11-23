---
name: correct
description: Use when the human corrects an agent, or the same mistake happens twice. Turns the correction into a deterministic check instead of another sentence in a prompt.
---

1. Name the mistake class in one line, not the single instance.
2. Fix it at the highest level that works: structure (change the layout or interface so it cannot happen), then a check (script in `checks/` or a guard rule whose message names the fix), then a test, then prose in AGENTS.md as a last resort.
3. Prove the check: add a test that fails on the real past mistake and passes on the fix. Run `python3 -m unittest discover -s tests`.
4. Add a row to `checks/RULES.md`: rule, enforcement, proven by.
5. Fix every other instance of the class now.
6. Tell the human in one line what now prevents it.
