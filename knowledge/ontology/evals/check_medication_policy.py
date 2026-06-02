#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import load_primitives  # noqa: E402


DOSE_PATTERN = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:mg|mcg|g|grams?|ml|mL|units?)\b|\bq\s?\d+\s?h\b|\b(?:bid|tid|qid|daily|twice daily|three times daily)\b",
    re.IGNORECASE,
)

ALLOWED_GENERAL_TERMS = {"label"}


def main() -> int:
    failures: list[str] = []
    for primitive in load_primitives().values():
        if primitive.get("section") != "medications":
            continue
        for key, text in primitive.get("text", {}).items():
            if DOSE_PATTERN.search(text):
                lowered = text.lower()
                if not any(term in lowered for term in ALLOWED_GENERAL_TERMS):
                    failures.append(f"{primitive['id']} {key} contains static dose-like text: {text}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print("medication policy checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
