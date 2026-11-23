import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "checks"))
import check_skills
import check_weakened
import guard
import run_checks

DIRS = {"src", "sql", "tests"}
CFG = {
    "top_files": ["PLAN.md", "SPEC.md", "CONSTRAINTS.md"],
    "top_dirs": ["src", "tests", "checks", ".claude", ".scratch"],
    "free_dirs": [".scratch", "tests", "checks"],
    "manifest_dirs": [], "locked_until_approved": [], "enforce_manifest": False, "scratch": ".scratch",
    "protected_dirs": ["checks", ".claude"], "protected_files": ["CONSTRAINTS.md"], "protected_if_existing": ["tests"],
}


class ProtectionTests(unittest.TestCase):
    def v(self, rel, agent, exists=True):
        return guard.verdict(rel, CFG, "Status: APPROVED", "", exists, agent)

    def test_subagents_cannot_edit_checks_or_constraints(self):
        for agent in ("builder", "researcher", "verifier"):
            for rel in ("checks/check_spec.py", "CONSTRAINTS.md", ".claude/settings.json"):
                self.assertIsNotNone(self.v(rel, agent), (agent, rel))

    def test_lead_and_main_can_edit(self):
        for agent in (None, "lead", "main"):
            self.assertIsNone(self.v("checks/check_spec.py", agent))

    def test_builder_can_add_new_test_but_not_edit_existing(self):
        self.assertIsNone(self.v("tests/test_new.py", "builder", exists=False))
        self.assertIsNotNone(self.v("tests/test_old.py", "builder", exists=True))


class WeakenedTests(unittest.TestCase):
    def test_added_suppression_flagged(self):
        diff = "+++ b/src/a.py\n+x = f()  # noqa\n+y = 1\n"
        self.assertEqual(len(check_weakened.scan_diff(diff, DIRS)), 1)

    def test_skip_marker_in_tests_flagged(self):
        diff = "+++ b/tests/test_a.py\n+@unittest.skip('flaky')\n"
        self.assertTrue(check_weakened.scan_diff(diff, DIRS))

    def test_clean_diff_and_unwatched_paths_pass(self):
        self.assertEqual(check_weakened.scan_diff("+++ b/src/a.py\n+y = 1\n", DIRS), [])
        self.assertEqual(check_weakened.scan_diff("+++ b/docs/a.md\n+use # noqa here\n", DIRS), [])

    def test_removed_lines_are_not_flagged(self):
        self.assertEqual(check_weakened.scan_diff("+++ b/src/a.py\n-x = 1  # noqa\n", DIRS), [])

    def test_constraint_row_changed_or_removed(self):
        old = "| C1 | a | cmd | exit 0 | fast |\n| C2 | b | cmd2 | 0.8 | task |\n"
        self.assertEqual(check_weakened.constraint_changes(old, old), [])
        new = "| C1 | a | cmd | exit 0 | fast |\n| C2 | b | cmd2 | 0.5 | task |\n"
        self.assertEqual(check_weakened.constraint_changes(old, new), ["CONSTRAINTS.md: C2 changed"])
        self.assertEqual(check_weakened.constraint_changes(old, "| C1 | a | cmd | exit 0 | fast |\n"),
                         ["CONSTRAINTS.md: C2 removed"])


class RunnerTests(unittest.TestCase):
    TEXT = ("| ID | Constraint | Command | Threshold | Tier |\n|---|---|---|---|---|\n"
            "| C1 | a | true | exit 0 | fast |\n| C2 | b | `true` | exit 0 | task |\n"
            "| C3 | c | - | - | full |\n| C4 | d | true | x | full |\n")

    def test_tier_selection_is_cumulative_and_skips_placeholders(self):
        rows = run_checks.parse(self.TEXT)
        self.assertEqual([r["id"] for r in run_checks.select(rows, "fast")], ["C1"])
        self.assertEqual([r["id"] for r in run_checks.select(rows, "task")], ["C1", "C2"])
        self.assertEqual([r["id"] for r in run_checks.select(rows, "full")], ["C1", "C2", "C4"])


class SkillRuleTests(unittest.TestCase):
    GOOD = "---\nname: demo\ndescription: Use when testing. Does one thing.\n---\nbody\n"

    def test_good(self):
        self.assertEqual(check_skills.check_skill("demo", self.GOOD), [])

    def test_name_must_match_folder(self):
        self.assertTrue(check_skills.check_skill("other", self.GOOD))

    def test_description_must_lead_with_use(self):
        self.assertTrue(check_skills.check_skill("demo", self.GOOD.replace("Use when testing", "Tests things")))

    def test_description_too_long_or_wordy(self):
        long = self.GOOD.replace("Does one thing.", "x" * 1100)
        self.assertTrue(check_skills.check_skill("demo", long))
        wordy = self.GOOD.replace("Does one thing.", "One. Two. Three. Four.")
        self.assertTrue(check_skills.check_skill("demo", wordy))

    def test_all_real_skills_pass(self):
        import pathlib
        root = pathlib.Path(__file__).resolve().parents[1] / "skills"
        errs = []
        for d in root.iterdir():
            if d.is_dir():
                errs += check_skills.check_skill(d.name, (d / "SKILL.md").read_text())
        self.assertEqual(errs, [])


if __name__ == "__main__":
    unittest.main()
