#!/usr/bin/env bash
# Copy the starter into a new, empty project folder: scripts/new-project.sh ~/Dev/my-job
set -euo pipefail
src="$(cd "$(dirname "$0")/.." && pwd)"
dest="${1:?usage: new-project.sh <target-dir>}"
if [ -e "$dest" ] && [ -n "$(ls -A "$dest" 2>/dev/null)" ]; then echo "target is not empty: $dest" >&2; exit 1; fi
mkdir -p "$dest"
for d in agents skills playbooks connectors checks themes scripts tests docs .claude .github; do cp -R "$src/$d" "$dest/$d"; done
cp "$src/AGENTS.md" "$src/CLAUDE.md" "$src/.gitignore" "$dest/"
cp "$src/templates/SPEC.md" "$src/templates/PLAN.md" "$src/templates/BACKLOG.md" "$src/templates/CONSTRAINTS.md" "$dest/"
cp "$src/templates/tree.project.json" "$dest/checks/tree.json"
cp "$src/templates/decisions.tsv" "$dest/docs/decisions.tsv"
rm -f "$dest/docs/usage.tsv" "$dest/docs/handoff.md"
mkdir -p "$dest/.scratch" "$dest/sql" "$dest/src" "$dest/notebooks" "$dest/outputs"
touch "$dest/.scratch/.gitkeep"
( cd "$dest" && git init -q && git add -A >/dev/null 2>&1 \
  && git -c user.name="${GIT_AUTHOR_NAME:-aastack}" -c user.email="${GIT_AUTHOR_EMAIL:-aastack@localhost}" commit -qm "Start from aastack" >/dev/null 2>&1 || true )
echo "created $dest. Open it in your tool, then ask the lead to run grill-spec."
