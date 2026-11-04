#!/usr/bin/env python3
"""Validate resource metadata and local Markdown targets without network access."""
import argparse
import datetime
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("id", "name", "url", "category", "kind", "business_use", "review_question",
          "source_checked_on", "verification_scope")


def validate_resources(document, today=None):
    today = today or datetime.date.today()
    entries = document.get("resources") if isinstance(document, dict) else document
    if not isinstance(entries, list) or not entries:
        return ["resources must be a nonempty list"]
    errors, seen_ids, seen_urls = [], set(), set()
    for index, item in enumerate(entries):
        prefix = f"resources[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for field in FIELDS:
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}.{field} must be a nonempty string")
        for field, seen in (("id", seen_ids), ("url", seen_urls)):
            value = item.get(field)
            if isinstance(value, str):
                canonical = value.rstrip("/").casefold() if field == "url" else value
                if canonical in seen:
                    errors.append(f"{prefix} duplicate {field}: {value}")
                seen.add(canonical)
        url = item.get("url")
        if isinstance(url, str):
            try:
                parsed = urlsplit(url)
                if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or any(c.isspace() for c in url):
                    errors.append(f"{prefix}.url must be an HTTPS URL without credentials or whitespace")
            except ValueError:
                errors.append(f"{prefix}.url is malformed")
        value = item.get("source_checked_on")
        if isinstance(value, str):
            try:
                checked = datetime.date.fromisoformat(value)
                if checked.isoformat() != value or checked > today:
                    errors.append(f"{prefix}.source_checked_on must be ISO date no later than {today}")
            except ValueError:
                errors.append(f"{prefix}.source_checked_on must be an ISO date")
    return errors


def without_fences(text):
    output, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            token = match.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output)


def heading_anchors(text):
    anchors, counts = set(), {}
    for line in without_fences(text).splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", match.group(1))
        title = re.sub(r"<[^>]+>", "", title).lower()
        title = "".join(c for c in title if c in " -_" or unicodedata.category(c)[0] in "LN")
        slug = title.replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug + (f"-{count}" if count else ""))
    anchors.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return anchors


def validate_markdown(root):
    root = Path(root).resolve()
    errors = []
    for source in sorted(root.rglob("*.md")):
        if ".git" in source.parts:
            continue
        text = without_fences(source.read_text(encoding="utf-8"))
        # Inline links and images, including optional quoted titles and <wrapped paths>.
        targets = re.findall(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', text)
        targets += re.findall(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', text, flags=re.M)
        for raw in targets:
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            path = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            label = f"{source.relative_to(root)}: {target}"
            if not path.is_relative_to(root):
                errors.append(label + " escapes repository")
            elif not path.exists():
                errors.append(label + " target does not exist")
            elif parsed.fragment and path.suffix.lower() == ".md":
                if unquote(parsed.fragment) not in heading_anchors(path.read_text(encoding="utf-8")):
                    errors.append(label + " anchor does not exist")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        document = json.loads((args.root / "data/resources.json").read_text())
        errors = validate_resources(document) + validate_markdown(args.root)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    for error in errors:
        print("ERROR:", error)
    if not errors:
        entries = document["resources"] if isinstance(document, dict) else document
        print(f"Validated {len(entries)} resources and all local Markdown targets. External URLs were not fetched.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
