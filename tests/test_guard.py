"""Each check must pass on good input and FAIL on the mistake it exists to catch."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "checks"))
import check_spec
import guard

PROJECT = {
    "top_files": ["SPEC.md", "PLAN.md", "AGENTS.md"],
    "top_dirs": ["docs", "src", "sql", "tests", "checks", ".scratch"],
    "free_dirs": [".scratch", "tests", "checks", "docs"],
    "manifest_dirs": ["src", "sql"],
    "locked_until_approved": ["src", "sql"],
    "enforce_manifest": True,
    "scratch": ".scratch",
}
DRAFT = "Status: DRAFT  (change to APPROVED later)"
APPROVED = "Status: APPROVED"
PLAN_DOING = (
    "| # | Ticket | Owner | Output | Check | Budget | Status |\n|---|---|---|---|---|---|---|\n"
    "| T2 | label | builder | src/label.py, sql/02_label.sql | x | 50k | doing |\n"
    "| T3 | feats | builder | src/features.py | x | 50k | todo |\n"
)
PLAN_NONE = PLAN_DOING.replace("doing", "todo")


class SpecTests(unittest.TestCase):
    def test_approved_with_tbd_fails(self):
        self.assertTrue(check_spec.check("Status: APPROVED\nx TBD"))

    def test_draft_status_parsed(self):
        self.assertEqual(check_spec.spec_status(DRAFT), "DRAFT")

    def test_missing_status_fails(self):
        self.assertTrue(check_spec.check("no status here"))


class GuardTests(unittest.TestCase):
    def v(self, rel, spec=APPROVED, plan=PLAN_DOING, exists=False):
        return guard.verdict(rel, PROJECT, spec, plan, exists)

    def test_build_blocked_until_approved(self):
        self.assertIsNotNone(self.v("src/label.py", spec=DRAFT))
        self.assertIsNone(self.v("src/label.py"))

    def test_free_dirs_allowed_while_draft(self):
        for rel in ("checks/x.py", "docs/notes.md", "tests/test_a.py", ".scratch/anything.txt"):
            self.assertIsNone(self.v(rel, spec=DRAFT), rel)

    def test_unknown_paths_blocked(self):
        for rel in ("notes.md", "stuff/a.py", "../outside.txt"):
            self.assertIsNotNone(self.v(rel), rel)

    def test_variant_names_blocked(self):
        for rel in ("src/label_final.py", "src/features_v2.py", "docs/report_copy.md"):
            self.assertIsNotNone(self.v(rel), rel)

    def test_scratch_allows_any_name(self):
        self.assertIsNone(self.v(".scratch/model_final_v2.py"))

    def test_new_file_must_be_planned_output(self):
        self.assertIsNone(self.v("src/label.py"))
        self.assertIsNotNone(self.v("src/features.py"))
        self.assertIsNotNone(self.v("src/random_helper.py"))

    def test_no_active_ticket_blocks_new_files(self):
        self.assertIsNotNone(self.v("src/label.py", plan=PLAN_NONE))

    def test_existing_file_can_be_edited(self):
        self.assertIsNone(self.v("src/features.py", exists=True))


if __name__ == "__main__":
    unittest.main()
