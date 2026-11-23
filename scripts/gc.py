#!/usr/bin/env python3
"""Safe cleanup report. Stdlib only, no tokens used.
  gc.py [--dir D]               report junk files and merged local branches
  gc.py [--dir D] --apply --yes delete the safe items (untracked junk files, merged local branches)
Never touches tracked files and never pushes."""
import argparse
import fnmatch
import pathlib
import subprocess

JUNK_FILES = [".DS_Store", "*.orig", "*.rej", "*.bak", "*.swp", "*~", "*.tmp", "Thumbs.db"]
JUNK_DIRS = ["__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".ipynb_checkpoints"]
SKIP = {".git", "node_modules", ".venv"}


def git(root, *args):
    try:
        return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, timeout=30).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def find(root):
    files, dirs = [], []
    tracked = set(git(root, "ls-files").splitlines())
    for p in root.rglob("*"):
        rel = p.relative_to(root)
        if SKIP & set(rel.parts):
            continue
        if p.is_dir() and p.name in JUNK_DIRS:
            dirs.append(p)
        elif p.is_file() and str(rel) not in tracked and any(fnmatch.fnmatch(p.name, g) for g in JUNK_FILES):
            files.append(p)
    merged = [b.strip().lstrip("* ") for b in git(root, "branch", "--merged").splitlines()]
    branches = [b for b in merged if b and b not in ("main", "master") and not b.startswith("(")]
    return files, dirs, branches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()
    root = pathlib.Path(a.dir).resolve()
    files, dirs, branches = find(root)
    print(f"junk files {len(files)} | junk dirs {len(dirs)} | merged branches {len(branches)}")
    for p in files + dirs:
        print("  ", p.relative_to(root))
    for b in branches:
        print("   branch", b)
    if a.apply and a.yes:
        import shutil
        for p in files:
            p.unlink()
        for d in dirs:
            shutil.rmtree(d, ignore_errors=True)
        for b in branches:
            git(root, "branch", "-d", b)
        print("deleted the safe items above")
    elif a.apply:
        print("add --yes to confirm")


if __name__ == "__main__":
    main()
