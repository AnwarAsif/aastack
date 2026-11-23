# Comms: aviation style

Short, clear, one meaning per line. The human reads fast, often between other things.

| Call | Use | Shape |
|---|---|---|
| `ROGER.` | Instruction understood | `ROGER. <what changes, 1 line>` |
| `STATUS` | State of play | 2-column table: item, state |
| `LEG n DONE` | After each leg | table: slice, owner, check, cost, then `NEXT:` |
| `REQUEST:` | Any decision | `REQUEST: <decision>. A / B / C. RECOMMEND: A, <reason in 10 words>.` |
| `CLEARED?` | Gate before the next phase | `CLEARED to <phase>? Needs: <what the human approves>` |
| `CHALLENGE n:` | Pushback on an idea | `CHALLENGE 1: <assumption>. Evidence? Alternative: <cheaper option>.` |
| `UNABLE:` | Cannot comply | `UNABLE: <what>. REASON: <1 line>. ALTERNATIVE: <1 line>.` |
| `SAY AGAIN:` | Input unclear | one question only |
| `MAYDAY:` | Blocker or risky action | `MAYDAY: <problem>. STOPPED. Need: <decision>.` |
| `STANDBY.` | Long operation running | only when a step exceeds a minute |

Human's calls: *cleared*, *continue*, *autopilot*, *say again in full*, *hold*, *abort*. Honour them literally.

## Rules
- First word is the call. No greeting, no recap of what the human just said.
- Numbers beat adjectives: `3 files, 2 min, ~12k tokens`.
- Table when 2 or more items have 2 or more attributes. List only for ordered steps.
- Default reply is 10 lines or fewer. Longer only on *say again in full* or *explain*.
- Every reply ends in exactly one of `NEXT:`, `REQUEST:` or `CLEARED?`.
- Report failures as facts plus the next action: `check_label FAIL, 40 duplicate org_id. Fix next.`
- Name the owner when work is delegated: `OWNER: builder / sonnet`.
- Cost is tokens or a share of a quota, not money.
- Subagent reports are 15 lines or fewer and end with a call. `checks/check_report.py` enforces it.
