---
name: grill-spec
description: Use at the start of a new job, when the goal is vague, or when SPEC.md has TBD. Interviews the human one question at a time until the spec is confirmed.
---

Needs a human in the loop. In an autonomous run do not guess: write `BLOCKED.md` with the open questions and stop.

1. **Hypothesis.** State your understanding in one sentence with a confidence number. Below about 70 percent, list what is missing.
2. **Interview.** One question at a time, each with your guessed answer. If the answer is in the files or data, look instead of asking. When an answer sounds like a convention ("the usual way"), ask: what would you want if you did not have to justify it?
3. **Stop test.** Stop asking when you can predict the human's reaction to the next three questions.
4. **Restate** as: Outcome, User, Why now, Success (the checks that prove it), Constraint (time, tokens, access), Out of scope. Add the glossary of terms with exact meanings.
5. **Confirm.** Wait for an explicit yes. "Whatever you think" and "sounds good" are not a yes. Then write SPEC.md in place, replacing every TBD, and set `Status: APPROVED`.
6. Fill PLAN.md from `playbooks/` and ask for *cleared* on the plan.

## Rationalizations
| Excuse | Reality |
|---|---|
| "The goal is obvious, skip the interview" | Misalignment is the main failure; a 5-minute interview is cheaper than a wrong build. |
| "I will fill the TBDs with sensible defaults" | A default the human never saw is an unconfirmed decision. |
