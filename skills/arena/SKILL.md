---
name: arena
description: Use when two or three approaches compete and the choice is not obvious. Runs each on the same input, scores them on one rubric, and picks one.
disable-model-invocation: true
---

1. Write the rubric first: 3 to 5 criteria and the one metric that decides ties.
2. Run each option on the same data and the same split. Same effort for each.
3. Score in one pass, with the options labelled A, B, C so the judge is blind to which is which.
4. Report a table, the winner and the cost of each option in tokens. Graft a loser's good part only if it passes the same check.
