#!/usr/bin/env bash
# Makes the adapter links so each tool sees the same agents/ and skills/ folders. Safe to rerun.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .claude .github
link() { [ -e "$2" ] || [ -L "$2" ] || ln -s "$1" "$2"; }
link ../agents .claude/agents
link ../skills .claude/skills
link ../skills .github/skills
echo "links ready: .claude/agents .claude/skills .github/skills"
