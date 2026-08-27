#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


PHENOTYPE_ID = "abdominal_pain_nonspecific_reassuring_workup"
REQUIRED_CONTEXT_ID = "clinician_directed_recheck_plan"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next(item for item in manifest["phenotypes"] if item["id"] == PHENOTYPE_ID)

    require(phenotype["status"] == "reviewed", f"{PHENOTYPE_ID} must be reviewed")
    require(phenotype["review"]["status"] == "reviewed", f"{PHENOTYPE_ID} review status must be reviewed")
    require(manifest_item["status"] == "reviewed", f"{PHENOTYPE_ID} manifest status must be reviewed")
    require(manifest_item["review_status"] == "reviewed", f"{PHENOTYPE_ID} manifest review status must be reviewed")
    require("poor_follow_up" in manifest_item["unsafe_modifiers"], "poor_follow_up missing from manifest blockers")
    require(
        any(item.get("id") == REQUIRED_CONTEXT_ID for item in manifest_item.get("required_context", [])),
        "clinician-directed recheck context missing from manifest",
    )

    clean = classify(
        "abdominal pain recheck",
        "Adult with abdominal pain. ED evaluation reassuring. No fever. No vomiting. Discharged with explicit recheck plan.",
    )
    require(clean["phenotype_id"] == PHENOTYPE_ID, f"clean abdominal case did not match: {clean}")
    require(clean["fallback_reason"] is None, f"clean abdominal case should enter ontology mode: {clean}")

    missing_recheck = classify(
        "abdominal pain reassuring evaluation",
        "Adult with abdominal pain. ED evaluation reassuring. No fever. Discharged with return precautions only.",
    )
    require(
        missing_recheck["fallback_reason"] == "required_runtime_context_missing",
        f"missing recheck case should block on required context: {missing_recheck}",
    )

    poor_follow_up = classify(
        "abdominal pain recheck",
        "Adult with abdominal pain. ED evaluation reassuring. Discharged with explicit recheck plan, but patient has poor follow up.",
    )
    require(poor_follow_up["fallback_reason"] == "unsafe_modifier_present", f"poor follow-up case should block: {poor_follow_up}")
    require("poor_follow_up" in poor_follow_up["exclusions"], f"poor_follow_up exclusion missing: {poor_follow_up}")

    print("phase27 abdominal promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
