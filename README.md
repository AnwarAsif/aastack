# aastack

A starter for agentic jobs. A small team of agents (lead, researcher, builder, verifier), skills that load only when needed, connectors to outside systems, and code checks that keep agents on goal and stop them littering the repo with files.

Works with Claude Code, GitHub Copilot, Cursor and Codex. `AGENTS.md` is the one rulebook; Claude Code also gets hooks that enforce the checks.

## Start a project
```bash
scripts/new-project.sh ~/Dev/my-job     # copies the starter, turns enforcement on, git init
cd ~/Dev/my-job
claude --agent lead                       # then: "run grill-spec"
```
The spec must be approved before anything gets built. Tickets live in `PLAN.md`; only the ticket marked `doing` may create files, and only the ones it lists.

## What is in it
| Folder | Purpose |
|---|---|
| `agents/` | lead, researcher, builder, verifier, and a template for new roles |
| `skills/` | 12 skills that fire on their own trigger, 23 slash-only skills (`/swarm`, `/arena`, `/hillclimb` ...) |
| `playbooks/` | task type to steps: investigate, build-ticket, fix-bug, improve-metric, compare-options, resume |
| `connectors/` | how to reach outside systems safely: read-only, secrets in env vars, a smoke test |
| `checks/` | `guard.py` (write guard, protects checks from subagents), `check_weakened.py`, `run_checks.py` (tiered), `tree_audit.py`, `check_spec.py`, `check_skills.py`, `check_report.py`, `usage.py` |
| `themes/` | neutral theme for notebooks and UI; keep brand themes in your own project |
| `docs/` | `comms.md` (aviation-style calls), `gates.md` (legs, autopilot), `definition-of-done.md`, `principles.md`, `harnesses.md` |
| `templates/` | SPEC, PLAN, BACKLOG, CONSTRAINTS (the quality bar), decision log, report formats |
| `.scratch/` | the one place agents may drop throwaway files; emptied at ticket close |

## Ideas behind it
Deterministic checks first, verification second, prose last; every correction becomes a check. Short aviation-style comms. Skills are small, composable and on demand.

Inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack) (MIT), [Matt Pocock's skills](https://github.com/mattpocock/skills), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT), and the talk "All Code Is Slop (Except Mine)". The text here is written fresh.

## Test
```bash
python3 -m unittest discover -s tests
```

MIT licensed.
