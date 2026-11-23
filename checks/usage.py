"""SubagentStop hook: append token usage to docs/usage.tsv. Never blocks (always exit 0).
Reads message.usage from the transcript JSONL (input_tokens, output_tokens, cache_read_input_tokens,
cache_creation_input_tokens), counting each API message once. Field names checked against a real transcript."""
import datetime
import json
import os
import pathlib
import sys

HEADER = "ts\tagent\tsource\tapi_messages\tinput\toutput\tcache_read\tcache_create\n"


def sum_usage(path):
    seen = {}
    for line in open(path, errors="ignore"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        m = d.get("message") if isinstance(d, dict) else None
        u = m.get("usage") if isinstance(m, dict) else None
        if isinstance(u, dict):
            seen[m.get("id") or d.get("uuid") or len(seen)] = u
    tot = {"in": 0, "out": 0, "cr": 0, "cc": 0}
    for u in seen.values():
        tot["in"] += u.get("input_tokens", 0) or 0
        tot["out"] += u.get("output_tokens", 0) or 0
        tot["cr"] += u.get("cache_read_input_tokens", 0) or 0
        tot["cc"] += u.get("cache_creation_input_tokens", 0) or 0
    return tot, len(seen)


def main():
    try:
        data = json.load(sys.stdin)
        path = data.get("agent_transcript_path") or data.get("transcript_path")
        if not path or not os.path.exists(path):
            return 0
        tot, n = sum_usage(path)
        root = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or ".")
        out = root / "docs" / "usage.tsv"
        out.parent.mkdir(exist_ok=True)
        new = not out.exists()
        with open(out, "a") as f:
            if new:
                f.write(HEADER)
            src = "agent" if data.get("agent_transcript_path") else "session"
            f.write("\t".join(map(str, [datetime.datetime.now().isoformat(timespec="seconds"),
                                        data.get("agent_type", "main"), src, n,
                                        tot["in"], tot["out"], tot["cr"], tot["cc"]])) + "\n")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
