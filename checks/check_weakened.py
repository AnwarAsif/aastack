"""Catch agents that get 'green' by weakening the bar instead of fixing the work.
Flags, compared with a base commit (default HEAD):
  - new suppressions in added lines (noqa, type: ignore, skip markers, eslint-disable, nosec, ...)
  - deleted test files
  - changed or removed rows in CONSTRAINTS.md (a human must approve those)
Without a base commit (new repo) every line in the watched folders counts as added.
Usage: check_weakened.py [--base HEAD] [--root DIR]   Exit 1 when findings exist."""
import argparse
import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from guard import load_cfg  # noqa: E402

SUPPRESS = re.compile(
    r"(#\s*noqa|#\s*type:\s*ignore|#\s*pylint:\s*disable|pragma:\s*no cover|#\s*nosec|nosemgrep|eslint-disable|"
    r"@ts-ignore|@pytest\.mark\.skip|@unittest\.skip|\bunittest\.skip|\bpytest\.skip|\.skip\(|\bxit\(|\bxdescribe\(|"
    r"gitleaks:allow|except\s*(Exception)?\s*:\s*pass|raise NotImplementedError)", re.I)
EXTS = {".py", ".sql", ".js", ".ts", ".tsx", ".sh", ".r", ".ipynb"}
ROW = re.compile(r"^\|\s*(C\d+)\s*\|")


def watched(rel, dirs):
    p = pathlib.PurePosixPath(rel)
    return p.suffix.lower() in EXTS and p.parts and p.parts[0] in dirs


def scan_text(rel, text):
    return [f"{rel}: {ln.strip()[:90]}" for ln in text.splitlines() if SUPPRESS.search(ln)]


def scan_diff(diff_text, dirs):
    out, cur = [], None
    for ln in diff_text.splitlines():
        if ln.startswith("+++ "):
            cur = ln[6:] if ln.startswith("+++ b/") else None
        elif ln.startswith("+") and cur and watched(cur, dirs) and SUPPRESS.search(ln):
            out.append(f"{cur}: {ln[1:].strip()[:90]}")
    return out


def constraint_changes(old, new):
    def rows(t):
        return {m.group(1): ln.strip() for ln in t.splitlines() if (m := ROW.match(ln))}
    a, b = rows(old), rows(new)
    out = [f"CONSTRAINTS.md: {k} removed" for k in a if k not in b]
    out += [f"CONSTRAINTS.md: {k} changed" for k in a if k in b and a[k] != b[k]]
    return out


def git(root, *args):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD")
    ap.add_argument("--root", default=".")
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()
    cfg = load_cfg(root)
    dirs = set(cfg.get("manifest_dirs", [])) | {"tests"}
    findings = []
    has_base = git(root, "rev-parse", "--verify", a.base)[0] == 0
    if has_base:
        findings += scan_diff(git(root, "diff", "--unified=0", a.base)[1], dirs)
        for ln in git(root, "diff", "--name-status", a.base)[1].splitlines():
            if ln.startswith("D\t") and ln[2:].startswith("tests/"):
                findings.append(f"{ln[2:]}: test file deleted")
        c = root / "CONSTRAINTS.md"
        old = git(root, "show", f"{a.base}:CONSTRAINTS.md")
        if c.exists() and old[0] == 0:
            findings += constraint_changes(old[1], c.read_text())
        untracked = git(root, "ls-files", "-o", "--exclude-standard")[1].splitlines()
    else:
        untracked = [str(p.relative_to(root)) for d in dirs if (root / d).exists() for p in (root / d).rglob("*") if p.is_file()]
    for rel in untracked:
        if watched(rel, dirs):
            findings += scan_text(rel, (root / rel).read_text(errors="ignore"))
    for f in findings:
        print("WEAKENED", f)
    print(f"{len(findings)} finding(s). Fix the work, not the check. A human must approve any CONSTRAINTS.md change."
          if findings else "no weakened checks")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
