import copy
import datetime
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


evaluator, validator, renderer = load("evaluate"), load("validate"), load("render_catalog")


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.case = {"id": "refund", "expected_route": "billing", "requires_human_approval": True,
                     "required_facts": ["review"], "forbidden_promises": ["refund approved"]}
        self.candidate = {"case_id": "refund", "route": "billing", "requires_human_approval": True,
                          "reply": "This needs review."}

    def test_acceptable_candidate(self):
        self.assertEqual(evaluator.evaluate([self.case], [self.candidate])["passed_cases"], 1)

    def test_unsafe_candidate_fails_several_independent_checks(self):
        self.candidate.update(route="general", requires_human_approval=False, reply="Refund approved.")
        failed = evaluator.evaluate([self.case], [self.candidate])["results"][0]["failed_checks"]
        self.assertEqual(set(failed), {"route", "human_approval", "required: review", "forbidden: refund approved"})

    def test_missing_candidate_is_failure(self):
        self.assertEqual(evaluator.evaluate([self.case], [])["failed_cases"], 1)

    def test_empty_or_nonlist_inputs_are_rejected(self):
        for cases, candidates in (([], []), ({}, []), ([self.case], {}), ([self.case], [None])):
            with self.subTest(cases=cases, candidates=candidates):
                with self.assertRaises(ValueError):
                    evaluator.evaluate(cases, candidates)

    def test_malformed_case_schema_is_rejected(self):
        for field, value in (("id", ""), ("expected_route", 42), ("requires_human_approval", "true"),
                             ("required_facts", "review"), ("forbidden_promises", [None])):
            case = dict(self.case, **{field: value})
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    evaluator.evaluate([case], [self.candidate])

    def test_string_approval_flag_is_not_boolean(self):
        self.candidate["requires_human_approval"] = "true"
        self.assertEqual(evaluator.evaluate([self.case], [self.candidate])["failed_cases"], 1)

    def test_duplicate_and_unknown_candidates_rejected(self):
        with self.assertRaises(ValueError):
            evaluator.evaluate([self.case], [self.candidate, self.candidate])
        self.candidate["case_id"] = "unknown"
        with self.assertRaises(ValueError):
            evaluator.evaluate([self.case], [self.candidate])

    def test_required_phrase_does_not_match_inside_larger_word(self):
        self.candidate["reply"] = "This was reviewed."
        self.assertEqual(evaluator.evaluate([self.case], [self.candidate])["failed_cases"], 1)

    def test_supplied_demonstration_catches_both_unsafe_controls(self):
        folder = ROOT / "examples/support-triage"
        cases = json.loads((folder / "cases.json").read_text())
        candidates = json.loads((folder / "candidates.json").read_text())
        report = evaluator.evaluate(cases, candidates)
        failures = {result["case_id"] for result in report["results"] if not result["passed"]}
        self.assertEqual(failures, {"injection-attempt", "billing-dispute"})
        self.assertEqual(report["passed_cases"], 4)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.entry = {field: "Example" for field in validator.FIELDS}
        self.entry.update(url="https://example.com/tool", source_checked_on="2026-11-04")
        self.today = datetime.date(2026, 11, 4)

    def test_valid_metadata(self):
        self.assertEqual(validator.validate_resources([self.entry], self.today), [])

    def test_duplicates_missing_metadata_and_future_dates(self):
        duplicate = copy.deepcopy(self.entry)
        duplicate["source_checked_on"] = "2026-11-05"
        duplicate.pop("verification_scope")
        errors = validator.validate_resources([self.entry, duplicate], self.today)
        self.assertEqual(len(errors), 4)

    def test_rejects_credentials_and_non_https(self):
        for url in ("http://example.com", "https://user:secret@example.com", "https://exa mple.com"):
            self.entry["url"] = url
            self.assertTrue(validator.validate_resources([self.entry], self.today))

    def test_generated_table_escapes_pipe(self):
        self.entry["business_use"] = "A | B"
        self.assertIn("A \\| B", renderer.render([self.entry]))

    def test_common_scope_is_shown_once_and_distinct_scopes_remain_attributable(self):
        self.entry["verification_scope"] = "Public source review only."
        other = dict(self.entry, id="other", name="Other")
        common = renderer.render([self.entry, other])
        self.assertEqual(common.count("Public source review only."), 1)
        other["verification_scope"] = "Hands-on review of a synthetic task."
        distinct = renderer.render([self.entry, other])
        self.assertIn("Scope 1: Hands-on review of a synthetic task.", distinct)
        self.assertIn("Scope 2: Public source review only.", distinct)
        self.assertIn("2026-11-04 (scope 1)", distinct)
        self.assertIn("2026-11-04 (scope 2)", distinct)


class MarkdownTests(unittest.TestCase):
    def test_headings_repeated_and_fenced(self):
        text = "# Work & Review\n# Work & Review\n```md\n# Hidden\n```\n"
        self.assertEqual(validator.heading_anchors(text), {"work--review", "work--review-1"})

    def test_missing_targets_anchors_and_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Start\n[ok](#start)\n[bad](#missing)\n[absent](absent.md)\n[escape](../x.md)\n```md\n[ignored](ignored.md)\n```\n")
            errors = validator.validate_markdown(root)
            self.assertEqual(len(errors), 3)
            self.assertTrue(any("anchor does not exist" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
