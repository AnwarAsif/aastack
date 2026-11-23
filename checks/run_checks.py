"""Run the commands in CONSTRAINTS.md, cheapest tier first. Tiers: fast (every edit, under 5s), task (ticket end), full (verification).
Usage: run_checks.py [fast|task|full] [--hook]   --hook: silent when all pass, exit 2 with the failures on stderr (for PostToolUse)."""
import os
import pathlib
import re
import subprocess
import sys

TIERS = ["fast", "task", "full"]
ROW = re.compile(r"^\|\s*(C\d+)\s*\|")


def parse(text):
    rows = []
    for ln in text.splitlines():
        if ROW.match(ln):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(c) >= 5:
                rows.append({"id": c[0], "what": c[1], "cmd": c[2].strip("`"), "threshold": c[3], "tier": c[4].lower()})
    return rows


def select(rows, tier):
    n = TIERS.index(tier)
    return [r for r in rows if r["tier"] in TIERS and TIERS.index(r["tier"]) <= n and r["cmd"] not in ("", "-") and not r["cmd"].startswith("(")]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    hook = "--hook" in sys.argv
    tier = args[0] if args else "task"
    root = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR") or ".").resolve()
    f = root / "CONSTRAINTS.md"
    if not f.exists():
        if not hook:
            print("no CONSTRAINTS.md, nothing to run")
        return 0
    failed = []
    for r in select(parse(f.read_text()), tier):
        p = subprocess.run(r["cmd"], shell=True, cwd=root, capture_output=True, text=True, timeout=300)
        ok = p.returncode == 0
        if not hook:
            print(("PASS " if ok else "FAIL ") + f"{r['id']} {r['what']}")
        if not ok:
            failed.append(f"{r['id']} {r['what']}: {(p.stdout + p.stderr).strip()[-300:]}")
    if hook and failed:
        print("Constraints failing. Fix the work, not the check.\n" + "\n".join(failed), file=sys.stderr)
        return 2
    if not hook:
        print(f"{len(failed)} failing" if failed else f"all {tier}-tier constraints pass")
    return 1 if failed and not hook else 0


if __name__ == "__main__":
    sys.exit(main())
