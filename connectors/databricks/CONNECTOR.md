---
name: databricks
type: cli
access: read-only
---

## What it reaches
Databricks workspace tables through the Databricks CLI, a connector or Databricks Connect.

## Setup
Install the Databricks CLI and create a profile (`databricks auth login`). Environment variables if not using a profile: `DATABRICKS_HOST`, `DATABRICKS_TOKEN`. Never commit them.
Ask the workspace admin for a read-only grant on source schemas and write rights on one scratch schema only.

## Allowed
- `SELECT` with `LIMIT` or a partition filter. Aggregates over full tables are fine.
- Creating and overwriting tables in the scratch schema.

## Forbidden
- Any write to source schemas. `DROP`, `DELETE`, `TRUNCATE`, `GRANT`, `ALTER` outside scratch.
- Full-table `SELECT *` exports of large tables.

## Writes
Only to the scratch schema named in SPEC.md. Make writes idempotent: overwrite the table or MERGE, never blind append.

## Smoke test
`databricks current-user me` then `SELECT 1` on the SQL warehouse. Expected: your user name, then one row.
