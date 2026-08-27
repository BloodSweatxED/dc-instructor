#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


PHENOTYPE_ID = "abdominal_pain_nonspecific_reassuring_workup"
PHENOTYPE_PATH = ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json"
CASES_PATH = ROOT / "evals" / "phase23_runtime_cases.json"

REQUIRED_UNSAFE_MODIFIERS = {
    "pregnancy",
    "elderly",
    "immunocompromised",
    "poor_follow_up",
    "peritoneal_signs",
    "uncontrolled_vomiting",
    "fever",
    "gi_bleeding",
    "sepsis",
    "unstable_vitals",
}
DISALLOWED_STANDALONE_TERMS = {"abdominal pain", "belly pain"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def load_cases() -> list[dict[str, Any]]:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


def main() -> int:
    phenotype = read_json(PHENOTYPE_PATH)
    terms = set(phenotype.get("runtime", {}).get("condition_terms", []))
    unsafe = set(phenotype.get("runtime", {}).get("unsafe_modifiers", []))
    cases = load_cases()

    require(phenotype["status"] in {"draft", "needs_review", "reviewed"}, f"{PHENOTYPE_ID} has unexpected status")
    require(
        phenotype["review"]["status"] in {"draft", "needs_review", "reviewed"},
        f"{PHENOTYPE_ID} has unexpected review status",
    )
    require(DISALLOWED_STANDALONE_TERMS.isdisjoint(terms), "broad standalone abdominal-pain condition terms are not allowed")
    require(REQUIRED_UNSAFE_MODIFIERS.issubset(unsafe), "abdominal draft missing required unsafe modifiers")
    require(
        any(
            item.get("id") == "clinician_directed_recheck_plan"
            for item in phenotype.get("runtime", {}).get("required_context", [])
        ),
        "abdominal phenotype missing clinician-directed recheck runtime context gate",
    )
    require(len(cases) >= 6, "phase23 abdominal stress cases missing")
    require(
        any(
            item["expected_phenotype_id"] == PHENOTYPE_ID and item.get("expected_fallback_reason") is None
            for item in cases
        ),
        "phase27 must include a clean abdominal ontology case",
    )
    require(
        any(item["expected_fallback_reason"] == "unsafe_modifier_present" for item in cases),
        "phase23 must include unsafe modifier cases",
    )
    require(
        any(item["expected_fallback_reason"] == "no_supported_phenotype_match" for item in cases),
        "phase23 must include broad/vague no-match case",
    )
    require(
        any(item["expected_fallback_reason"] == "required_runtime_context_missing" for item in cases),
        "phase26 must include missing clinician-directed recheck blocker case",
    )

    print("phase23 abdominal narrowing checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
