# Principles

One line each. If a principle can be a check, it becomes a check (checks/RULES.md) and leaves this file.

- **Prove it works.** Verify against the real artifact, not a proxy or a self-report. If a check fails, suspect the way you observed first.
- **Explain the number.** Spread, limiter, and what else it could measure, before trusting it.
- **Fix root causes.** Reproduce, ask why until you reach the first wrong decision, fix it there and everywhere it repeats.
- **Attack the premise.** After two failed fixes that share an assumption, test the assumption.
- **Build the lever.** Repeated manual work becomes a script.
- **Sequence verifiable units.** Each step ends in a checked state.
- **Subtract before you add.** Remove dead things first. Smallest change that solves it.
- **One source of truth** per decision. Do not restate what a file already says.
- **Model the domain.** Name the data shape and the glossary first.
- **Parse at the boundary.** Validate external data once where it enters.
- **Make operations idempotent.** Rerunning converges to the same result.
- **Separate before serializing.** Parallel runs write separate outputs.
- **Test behavior, not internals.** A wrong value fails; a refactor does not.
- **Guard the context window.** Bulk output goes to subagents; take back summaries.
- **Never block on the human** for reversible work. Ask before irreversible actions.
- **Encode lessons in structure.** A correction becomes a check, not a sentence.
