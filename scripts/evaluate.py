#!/usr/bin/env python3
"""Offline checks of hand-authored synthetic support replies; not an AI benchmark."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def contains_phrase(text, phrase):
    return re.search(r"(?<!\w)" + re.escape(phrase.casefold()) + r"(?!\w)", text.casefold()) is not None


def evaluate(cases, candidates):
    """Fail closed for malformed/missing candidates and unsafe literal promises."""
    if not isinstance(cases, list) or not cases:
        raise ValueError("Cases must be a nonempty list")
    if not isinstance(candidates, list):
        raise ValueError("Candidates must be a list")
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise ValueError(f"Case {index} must be an object")
        for field in ("id", "expected_route"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                raise ValueError(f"Case {index}.{field} must be a nonempty string")
        if type(case.get("requires_human_approval")) is not bool:
            raise ValueError(f"Case {index}.requires_human_approval must be a Boolean")
        for field in ("required_facts", "forbidden_promises"):
            values = case.get(field, [])
            if not isinstance(values, list) or any(not isinstance(value, str) or not value.strip() for value in values):
                raise ValueError(f"Case {index}.{field} must be a list of nonempty strings")
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict) or not isinstance(candidate.get("case_id"), str) or not candidate["case_id"].strip():
            raise ValueError(f"Candidate {index} must have a nonempty string case_id")
    case_ids = [case["id"] for case in cases]
    if len(set(case_ids)) != len(case_ids):
        raise ValueError("Duplicate case IDs")
    candidate_ids = [candidate["case_id"] for candidate in candidates]
    if len(set(candidate_ids)) != len(candidate_ids):
        raise ValueError("Duplicate candidate case IDs")
    unknown = set(candidate_ids) - set(case_ids)
    if unknown:
        raise ValueError("Unknown candidate case IDs: " + ", ".join(sorted(unknown)))
    by_id = {candidate["case_id"]: candidate for candidate in candidates}
    results = []
    for case in cases:
        candidate = by_id.get(case["id"])
        checks = {}
        if candidate is None:
            checks["candidate_present"] = False
        else:
            reply = candidate.get("reply", "")
            checks["reply_present"] = isinstance(reply, str) and bool(reply.strip())
            checks["route"] = candidate.get("route") == case["expected_route"]
            checks["human_approval"] = (type(candidate.get("requires_human_approval")) is bool
                                         and candidate["requires_human_approval"] == case["requires_human_approval"])
            for fact in case.get("required_facts", []):
                checks["required: " + fact] = isinstance(reply, str) and contains_phrase(reply, fact)
            for promise in case.get("forbidden_promises", []):
                checks["forbidden: " + promise] = isinstance(reply, str) and not contains_phrase(reply, promise)
        results.append({"case_id": case["id"], "passed": all(checks.values()),
                        "checks": checks, "failed_checks": [name for name, ok in checks.items() if not ok]})
    passed = sum(result["passed"] for result in results)
    return {"scope": "Synthetic, manually authored replies; deterministic rule checks only.",
            "total_cases": len(results), "passed_cases": passed,
            "failed_cases": len(results) - passed, "results": results}


def markdown(report):
    lines = ["# Synthetic support triage check results", "", report["scope"], "",
             f"{report['passed_cases']} of {report['total_cases']} cases passed; {report['failed_cases']} failed.", "",
             "These counts describe the supplied examples. They do not measure an AI model, customer outcomes, or ROI.", "",
             "| Case | Result | Failed checks |", "| --- | --- | --- |"]
    for result in report["results"]:
        failures = "; ".join(result["failed_checks"]) or "None"
        lines.append(f"| {result['case_id']} | {'PASS' if result['passed'] else 'FAIL'} | {failures} |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "examples/support-triage/cases.json")
    parser.add_argument("--candidates", type=Path, default=ROOT / "examples/support-triage/candidates.json")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "examples/support-triage")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if any candidate fails (default includes intentional failures).")
    args = parser.parse_args()
    try:
        report = evaluate(json.loads(args.cases.read_text()), json.loads(args.candidates.read_text()))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    (args.output_dir / "results.md").write_text(markdown(report))
    print(f"{report['passed_cases']}/{report['total_cases']} synthetic cases passed; {report['failed_cases']} failed.")
    return int(args.strict and report["failed_cases"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
