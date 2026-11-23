import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "checks"))
import check_report
import usage


class ReportTests(unittest.TestCase):
    def test_good_report(self):
        self.assertEqual(check_report.check("T2 done. 3 files.\nNEXT: T3, features."), [])

    def test_too_long_fails(self):
        text = "\n".join(["line"] * 20) + "\nNEXT: x"
        self.assertTrue(check_report.check(text))

    def test_missing_call_fails(self):
        self.assertTrue(check_report.check("All done, looks great."))

    def test_bold_call_accepted(self):
        self.assertEqual(check_report.check("ok\n**REQUEST:** pick A or B."), [])

    def test_empty_fails(self):
        self.assertTrue(check_report.check("  "))


class UsageTests(unittest.TestCase):
    def test_sums_each_api_message_once(self):
        a = {"message": {"id": "m1", "usage": {"input_tokens": 2, "output_tokens": 10,
                                                 "cache_read_input_tokens": 5, "cache_creation_input_tokens": 100}}}
        dup = json.loads(json.dumps(a))   # same api message repeated per content block
        b = {"message": {"id": "m2", "usage": {"input_tokens": 1, "output_tokens": 4}}}
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            for row in (a, dup, b, {"type": "other"}):
                f.write(json.dumps(row) + "\n")
        tot, n = usage.sum_usage(f.name)
        os.unlink(f.name)
        self.assertEqual((n, tot["in"], tot["out"], tot["cr"], tot["cc"]), (2, 3, 14, 5, 100))


if __name__ == "__main__":
    unittest.main()
