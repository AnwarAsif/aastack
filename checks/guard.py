"""PreToolUse hook for Write, Edit and NotebookEdit. Exit 2 blocks the write; the message goes to the agent.

Rules, all read from checks/tree.json:
  1. Writes stay inside the project and inside the allowed file tree.
  2. No 'final', 'v2', 'copy', 'old', 'tmp' variants outside the scratch folder.
  3. Locked folders stay locked until SPEC.md says Status: APPROVED.
  4. New files in manifest folders must be listed in the Output column of a PLAN.md ticket whose Status is 'doing'.
  5. Subagents (builder, researcher, verifier) cannot edit protected files: checks, CONSTRAINTS.md, hook settings and
     existing tests. A failing check is fixed in the work, never by weakening the check. Only the lead or the human edits them.
The scratch folder is the one place agents may drop throwaway files.
"""
import json
import os
import pathlib
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from check_spec import spec_status  # noqa: E402
from plan import matches, output_globs  # noqa: E402

BAD_NAME = re.compile(r"(^|[_\-.])(final|v\d+|copy|old|tmp|backup|draft\d*)([_\-.]|$)", re.I)
DEFAULT = {"top_files": [], "top_dirs": [], "free_dirs": [], "manifest_dirs": [],
           "locked_until_approved": [], "enforce_manifest": False, "scratch": ".scratch",
           "protected_dirs": [], "protected_files": [], "protected_if_existing": []}
EXEMPT_AGENTS = {None, "", "lead", "main"}


def load_cfg(root):
    p = root / "checks" / "tree.json"
    cfg = dict(DEFAULT)
    if p.exists():
        cfg.update(json.loads(p.read_text()))
    return cfg


def verdict(rel, cfg, spec_text="", plan_text="", exists=False, agent=None):
    parts = pathlib.PurePosixPath(rel).parts
    if not parts or parts[0] == "..":
        return "Write is outside the project. Write inside the project tree, or use the scratch folder."
    top = parts[0]
    if len(parts) == 1:
        if top not in cfg["top_files"]:
            return f"'{rel}' is not in the file tree. Put it under {sorted(cfg['top_dirs'])} or note the idea in BACKLOG.md."
    elif top not in cfg["top_dirs"]:
        return f"Folder '{top}' is not in the file tree. Use one of {sorted(cfg['top_dirs'])}."
    if agent not in EXEMPT_AGENTS and (top in cfg["protected_dirs"] or rel in cfg["protected_files"]
                                       or (exists and top in cfg["protected_if_existing"])):
        return (f"'{rel}' is protected. Subagents may not edit checks, CONSTRAINTS.md or existing tests: "
                "fix the work, not the check. If the check is wrong, end your report with REQUEST: for the lead.")
    if top == cfg["scratch"]:
        return None
    if BAD_NAME.search(parts[-1]):
        return f"'{parts[-1]}' looks like a copy or a 'final' version. Edit the real file in place instead of making a variant."
    if top in cfg["locked_until_approved"] and spec_status(spec_text) != "APPROVED":
        return "SPEC.md is not APPROVED. Run the grill-spec skill first. Building is blocked until the human approves."
    if cfg["enforce_manifest"] and top in cfg["manifest_dirs"] and not exists:
        doing = output_globs(plan_text, {"doing"})
        if not doing:
            return "No ticket is 'doing' in PLAN.md. Set the ticket you are working on to 'doing' before creating files."
        if not matches(rel, doing):
            return (f"'{rel}' is not an Output of the active ticket. Add it to that ticket's Output column in PLAN.md "
                    f"if it is really needed, or use {cfg['scratch']}/ for throwaway files.")
    return None


def main():
    data = json.load(sys.stdin)
    inp = data.get("tool_input", {})
    path = inp.get("file_path") or inp.get("notebook_path")
    if not path:
        return 0
    root = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or ".").resolve()
    target = pathlib.Path(path).resolve()
    try:
        rel = str(target.relative_to(root))
    except ValueError:
        rel = "../" + target.name
    read = lambda n: (root / n).read_text() if (root / n).exists() else ""  # noqa: E731
    msg = verdict(rel, load_cfg(root), read("SPEC.md"), read("PLAN.md"), target.exists(), data.get("agent_type"))
    if msg:
        print(msg, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
