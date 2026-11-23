"""Read the ticket table in PLAN.md. Columns used: Output and Status (case-insensitive)."""
import fnmatch
import re


def tickets(text):
    rows = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    if len(rows) < 3:
        return []
    head = [c.strip().lower() for c in rows[0].strip().strip("|").split("|")]
    out = []
    for ln in rows[2:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) == len(head):
            out.append(dict(zip(head, cells)))
    return out


def output_globs(text, statuses=None):
    globs = []
    for t in tickets(text):
        if statuses and t.get("status", "").lower() not in statuses:
            continue
        for g in re.split(r"[,\s]+", t.get("output", "")):
            g = g.strip("`").strip()
            if g and g not in ("-", "none"):
                globs.append(g)
    return globs


def matches(rel, globs):
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*") for g in globs)
