---
name: connector-name
type: mcp | cli | api
access: read-only
---

## What it reaches
One line.

## Setup
Install or configure steps, no secrets. Environment variables needed: `EXAMPLE_TOKEN`, `EXAMPLE_HOST`.

## Allowed
- Read queries with a row limit.

## Forbidden
- Deletes, grants, schema changes, writes to source systems.

## Writes
Only to: `<the one place>`.

## Smoke test
`<one cheap read-only command>`. Expected: `<what success looks like>`.
