"""SubagentStop hook: a subagent report must be 15 lines or fewer and end with a call.
Exit 2 sends the subagent back to fix its report. Allowed last-line calls: NEXT:, REQUEST:, CLEARED?, MAYDAY:, UNABLE:"""
import json
import sys

CALLS = ("NEXT:", "REQUEST:", "CLEARED?", "MAYDAY:", "UNABLE:")
MAX_LINES = 15


def check(text):
    lines = text.strip().splitlines()
    if not lines:
        return ["Report is empty. Say what was done, then end with NEXT: or REQUEST:."]
    errs = []
    if len(lines) > MAX_LINES:
        errs.append(f"Report is {len(lines)} lines, the limit is {MAX_LINES}. Put detail in a file and point to it.")
    if not lines[-1].strip().lstrip("*`>- ").startswith(CALLS):
        errs.append("The last line must start with NEXT:, REQUEST:, CLEARED?, MAYDAY: or UNABLE:.")
    return errs


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active"):
        return 0
    errs = check(data.get("last_assistant_message", ""))
    if errs:
        print(" ".join(errs), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
