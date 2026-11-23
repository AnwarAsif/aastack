"""Skill rules, enforced: name matches the folder, description starts with 'Use', at most 1024 chars and 3 sentences
(so it points to when to use the skill and does not summarise its steps), SKILL.md under 500 lines.
Usage: check_skills.py [skills_dir]   Exit 1 on problems."""
import pathlib
import re
import sys


def check_skill(dirname, text):
    errs = []
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return [f"{dirname}: missing frontmatter"]
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if dirname != "_template" and (not name or name.group(1).strip() != dirname):
        errs.append(f"{dirname}: name must equal the folder name")
    if not desc:
        return errs + [f"{dirname}: missing description"]
    d = desc.group(1).strip().strip('"')
    if len(d) > 1024:
        errs.append(f"{dirname}: description is {len(d)} chars, max 1024")
    if not d.startswith("Use "):
        errs.append(f"{dirname}: description must start with 'Use when ...' so the trigger comes first")
    if len(re.findall(r"[.!?](\s|$)", d)) > 3:
        errs.append(f"{dirname}: description has more than 3 sentences; keep the trigger, drop the steps")
    if len(text.splitlines()) > 500:
        errs.append(f"{dirname}: SKILL.md is over 500 lines; move detail to a referenced file")
    return errs


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "skills")
    errs = []
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        f = d / "SKILL.md"
        errs += check_skill(d.name, f.read_text()) if f.exists() else [f"{d.name}: SKILL.md missing"]
    print("\n".join(errs) or "skills ok")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
