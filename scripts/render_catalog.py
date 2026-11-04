#!/usr/bin/env python3
"""Generate the readable catalog from data/resources.json (no network or packages)."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def escape(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(document):
    entries = document["resources"] if isinstance(document, dict) else document
    scopes = sorted({entry["verification_scope"] for entry in entries})
    lines = ["# Business AI resource guide", "",
             "Generated from [data/resources.json](../data/resources.json). Edit the JSON and run `python3 scripts/render_catalog.py`.", "",
             "Source review means the linked official page was reviewed for relevance. It is not hands-on testing, procurement approval, a price guarantee, or a comparative endorsement. See [review methodology](methodology.md).", "",
             f"This catalog contains {len(entries)} resources. Check current terms, plan requirements, regional availability, and data handling before use."]
    if len(scopes) == 1:
        lines += ["", "Review scope for every entry: " + scopes[0]]
    else:
        lines += ["", "Review scopes (referenced in the Source checked column):", ""]
        lines += [f"- Scope {index + 1}: {scope}" for index, scope in enumerate(scopes)]
    for category in sorted({entry["category"] for entry in entries}):
        lines += ["", "## " + category, "",
                  "| Resource | Type | Business use | Pilot review question | Source checked |",
                  "| --- | --- | --- | --- | --- |"]
        for entry in sorted((item for item in entries if item["category"] == category), key=lambda item: item["name"].casefold()):
            checked = entry["source_checked_on"]
            if len(scopes) > 1:
                checked += f" (scope {scopes.index(entry['verification_scope']) + 1})"
            cells = [f"[{escape(entry['name'])}]({entry['url']})", escape(entry["kind"]),
                     escape(entry["business_use"]), escape(entry["review_question"]),
                     escape(checked)]
            lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the checked-in guide needs regeneration.")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    output = render(json.loads((args.root / "data/resources.json").read_text()))
    target = args.root / "docs/resource-guide.md"
    if args.check:
        if not target.exists() or target.read_text() != output:
            print("Catalog guide is stale. Run python3 scripts/render_catalog.py")
            return 1
        print("Catalog guide matches the source JSON.")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output)
        print("Generated docs/resource-guide.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
