"""Spec gate: SPEC.md is DRAFT or APPROVED, and never APPROVED with a TBD left."""
import pathlib
import re
import sys


def spec_status(text):
    m = re.search(r"^Status:\s*(\w+)", text, re.M)
    return m.group(1) if m else None


def check(text):
    errors = []
    status = spec_status(text)
    if status not in ("DRAFT", "APPROVED"):
        errors.append("SPEC.md needs a line 'Status: DRAFT' or 'Status: APPROVED'.")
    if status == "APPROVED" and re.search(r"\bTBD\b", text):
        errors.append("SPEC.md is APPROVED but still has TBD. Run the grill-spec skill and fill every TBD.")
    return errors


if __name__ == "__main__":
    path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "SPEC.md")
    errs = check(path.read_text())
    print("\n".join(errs) or "spec ok")
    sys.exit(1 if errs else 0)
