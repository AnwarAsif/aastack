"""List stray files: not in the file tree, or in a manifest folder but not an Output of any PLAN.md ticket.
Usage: tree_audit.py [--root DIR] [--clean-scratch]   Exit 1 when strays exist."""
import argparse
import json
import os
import pathlib
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from guard import load_cfg  # noqa: E402
from plan import matches, output_globs  # noqa: E402

SKIP = {".git", "__pycache__", "node_modules", ".venv"}
IGNORE_NAMES = {".DS_Store", ".gitkeep"}


def audit(root, cfg, plan_text):
    globs = output_globs(plan_text)
    strays, scratch = [], []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name in IGNORE_NAMES:
            continue
        rel = p.relative_to(root)
        if SKIP & set(rel.parts):
            continue
        parts = rel.parts
        if parts[0] == cfg["scratch"]:
            scratch.append(str(rel))
        elif len(parts) == 1:
            if parts[0] not in cfg["top_files"]:
                strays.append(str(rel))
        elif parts[0] not in cfg["top_dirs"]:
            strays.append(str(rel))
        elif cfg["enforce_manifest"] and parts[0] in cfg["manifest_dirs"] and not matches(str(rel), globs):
            strays.append(str(rel))
    return strays, scratch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--clean-scratch", action="store_true")
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()
    cfg = load_cfg(root)
    plan = (root / "PLAN.md").read_text() if (root / "PLAN.md").exists() else ""
    strays, scratch = audit(root, cfg, plan)
    if a.clean_scratch:
        sd = root / cfg["scratch"]
        for child in sd.iterdir() if sd.exists() else []:
            if child.name != ".gitkeep":
                shutil.rmtree(child) if child.is_dir() else child.unlink()
        print(f"scratch emptied ({len(scratch)} files)")
    for s in strays:
        print(f"STRAY {s}")
    print(f"{len(strays)} stray, {len(scratch)} in scratch" if strays or scratch else "tree clean")
    return 1 if strays else 0


if __name__ == "__main__":
    sys.exit(main())
