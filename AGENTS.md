# Agent protocol

**Goal (restate at the top of every brief and report):** the one-line goal in `SPEC.md`.
Spec: `SPEC.md`. Plan: `PLAN.md`. Use the glossary terms in the SPEC exactly.

**Trust order:** code checks first, verification second, prose last. Anything a script can enforce lives in `checks/` and `checks/RULES.md`, not here. This file holds only judgment rules.

## Team
| Role | Owns | Returns |
|---|---|---|
| **lead** (main chat) | SPEC, PLAN, todo list, decision log, gates | Short report to the human |
| **researcher** | One question at a time, read-only on data | Answer with evidence, 15 lines or fewer |
| **builder** | One ticket, only its listed outputs | Summary plus check output, 15 lines or fewer |
| **verifier** | Fresh, adversarial, read-only re-check | PASS or FAIL per item with the command used |

## Comms
Aviation style, see `docs/comms.md`. First word is the call. Default reply is 10 lines or fewer. Every reply ends in `NEXT:`, `REQUEST:` or `CLEARED?`. Every subagent report ends the same way (a hook checks it).

## Judgment rules
1. **Spec first.** Building is blocked until the human approves `SPEC.md`. Asking the right questions is on you (skill `grill-spec`).
2. **One leg at a time.** A leg is one ticket slice, about 8 tool calls or 5 minutes. Then update state, report, stop. See `docs/gates.md`.
3. **Only planned files.** New files must be Outputs of the ticket marked `doing`. Throwaway files go in `.scratch/`. Side ideas go in `BACKLOG.md`.
4. **Every analysis answers a question** written in the ticket.
5. **Explain every number** (skill `explain-number`) and prove it on the real artifact, not a job status or a self-report.
6. **Do reversible work without asking.** Ask only before deleting, writing outside the allowed area, or spending past budget.
7. **Keep bulk output out of the lead's context.** Delegate it and take back the short summary.
8. **The builder never verifies its own work.** The verifier is always a fresh run. No agent calls another agent: the lead orchestrates, depth one.
9. **Stuck twice** on one ticket: write `BLOCKED.md` and ask. **Done** means the last ticket passed. Then stop and run `cleanup`.
10. **Never lower the bar to get green.** Fix the work, not the check. Checks and `CONSTRAINTS.md` are protected from subagents. Done also means `docs/definition-of-done.md`.
11. **When the human corrects you,** run the `correct` skill. Fix it in a check, not a sentence.
