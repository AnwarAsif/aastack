import os
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "checks"))
import tree_audit

CFG = {"top_files": ["PLAN.md", "SPEC.md"], "top_dirs": ["src", "docs", ".scratch"], "manifest_dirs": ["src"],
       "enforce_manifest": True, "scratch": ".scratch"}
PLAN = "| # | Output | Status |\n|---|---|---|\n| T1 | src/a.py | doing |\n"


def make(root, *files):
    for f in files:
        p = pathlib.Path(root, f)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("x")


class AuditTests(unittest.TestCase):
    def run_audit(self, *files):
        with tempfile.TemporaryDirectory() as d:
            make(d, *files)
            return tree_audit.audit(pathlib.Path(d), CFG, PLAN)

    def test_clean(self):
        strays, _ = self.run_audit("PLAN.md", "src/a.py", "docs/n.md")
        self.assertEqual(strays, [])

    def test_unplanned_file_is_stray(self):
        strays, _ = self.run_audit("src/a.py", "src/b.py")
        self.assertEqual(strays, ["src/b.py"])

    def test_top_level_and_unknown_dir_strays(self):
        strays, _ = self.run_audit("notes.md", "misc/x.py")
        self.assertEqual(sorted(strays), ["misc/x.py", "notes.md"])

    def test_scratch_reported_not_stray(self):
        strays, scratch = self.run_audit(".scratch/t.txt")
        self.assertEqual((strays, scratch), ([], [".scratch/t.txt"]))


if __name__ == "__main__":
    unittest.main()
