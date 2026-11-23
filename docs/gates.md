# Gates, legs, autopilot

## Gates
| Gate | Before | Human says | Then |
|---|---|---|---|
| Spec | any building | *cleared* | SPEC.md `Status: APPROVED` (guard unlocks building) |
| Plan | first ticket | *cleared* | PLAN.md tickets have owner, output, check, budget |
| Leg | next leg | *continue* | run one more leg |
| Land | commit and push | *cleared* | run `cleanup`, then push |

A change to an approved SPEC reopens its gate: REQUEST before editing.

## Legs
A leg is one ticket slice, or about 8 tool calls, or about 5 minutes, whichever ends first. Then: update PLAN.md and docs/decisions.tsv, run `tree_audit.py`, report, stop. Nothing runs unattended without *autopilot*.

## Autopilot
Human says *autopilot* or *continue until done*: keep flying legs back to back. Stop at the first of:
- a failing check that one fix attempt did not clear
- an ambiguity the SPEC does not answer
- any deletion outside files this session created
- a needed change to SPEC
- a ticket over 2x its token budget
- 20 legs without a check-in
On stop send `MAYDAY:` or `CLEARED?` with the state.
