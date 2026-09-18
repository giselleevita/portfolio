#!/usr/bin/env python3
"""Validate local links, assets, and basic accessibility in the static site."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"
SKIPPED_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[tuple[str, int]] = []
        self.references: list[tuple[str, str, int]] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        line, _ = self.getpos()
        element_id = values.get("id")
        if element_id:
            self.ids.append((element_id, line))

        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.references.append((tag, value, line))

        if tag == "img" and not (values.get("alt") or "alt" in values):
            self.errors.append(f"index.html:{line}: image is missing an alt attribute")


def validate() -> list[str]:
    parser = SiteParser()
    parser.feed(HTML_FILE.read_text(encoding="utf-8"))
    errors = parser.errors

    seen_ids: dict[str, int] = {}
    for element_id, line in parser.ids:
        if element_id in seen_ids:
            errors.append(
                f"index.html:{line}: duplicate id {element_id!r} "
                f"(first declared on line {seen_ids[element_id]})"
            )
        else:
            seen_ids[element_id] = line

    for tag, raw_reference, line in parser.references:
        parsed = urlsplit(raw_reference)
        if parsed.scheme.lower() in SKIPPED_SCHEMES or raw_reference.startswith("//"):
            continue

        if parsed.path:
            target = ROOT / unquote(parsed.path.lstrip("/"))
            if not target.exists():
                errors.append(
                    f"index.html:{line}: {tag} references missing local file "
                    f"{parsed.path!r}"
                )

        if parsed.fragment and not parsed.path and parsed.fragment not in seen_ids:
            errors.append(
                f"index.html:{line}: link targets missing fragment #{parsed.fragment}"
            )

    try:
        json.loads((ROOT / "site-config.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"site-config.json: invalid or unreadable JSON: {exc}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Static site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Static site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
