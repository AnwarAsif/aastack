# Connectors

A connector says how agents reach one outside system (database, API, service) safely. One folder per connector with a `CONNECTOR.md`.

Rules for every connector:
- **Read-only by default.** Name the single place writes are allowed (for example one scratch schema).
- **No secrets in the repo.** `CONNECTOR.md` lists the environment variable names; values live in your shell or secret store. `.mcp.json` is gitignored; commit only `.mcp.json.example`.
- **Smoke test.** Every connector has one cheap read-only command that proves access works.
- **List forbidden actions** explicitly (deletes, grants, writes to source).
- Builders and researchers read the connector file before first use.

Add one with the `add-connector` steps: copy `_template/CONNECTOR.md`, fill it in, run the smoke test, record the result in docs/decisions.tsv.
