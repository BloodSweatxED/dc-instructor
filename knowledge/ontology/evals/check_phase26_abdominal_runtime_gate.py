#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


PHENOTYPE_ID = "abdominal_pain_nonspecific_reassuring_workup"
PHENOTYPE_PATH = ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json"
MANIFEST_PATH = ROOT / "runtime" / "ontology_manifest.json"
REQUIRED_CONTEXT_ID = "clinician_directed_recheck_plan"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def abdominal_manifest_entry() -> dict[str, Any]:
    manifest = read_json(MANIFEST_PATH)
    for item in manifest.get("phenotypes", []):
        if item["id"] == PHENOTYPE_ID:
            return item
    raise OntologyError(f"{PHENOTYPE_ID} missing from runtime manifest")


def has_required_context(item: dict[str, Any]) -> bool:
    return any(row.get("id") == REQUIRED_CONTEXT_ID for row in item.get("required_context", []))


def main() -> int:
    phenotype = read_json(PHENOTYPE_PATH)
    manifest_item = abdominal_manifest_entry()

    require(has_required_context(phenotype["runtime"]), "phenotype missing clinician-directed recheck gate")
    require(has_required_context(manifest_item), "runtime manifest missing clinician-directed recheck gate")
    require("poor_follow_up" in phenotype["runtime"]["unsafe_modifiers"], "phenotype missing poor_follow_up hard blocker")
    require("poor_follow_up" in manifest_item["unsafe_modifiers"], "runtime manifest missing poor_follow_up hard blocker")

    missing_recheck = classify(
        "abdominal pain reassuring evaluation",
        "Adult with abdominal pain. ED evaluation reassuring. No fever. Discharged with return precautions only.",
    )
    require(missing_recheck["phenotype_id"] == PHENOTYPE_ID, f"missing-recheck case did not match abdominal draft: {missing_recheck}")
    require(
        missing_recheck["fallback_reason"] == "required_runtime_context_missing",
        f"missing-recheck case did not block on required context: {missing_recheck}",
    )
    require(
        REQUIRED_CONTEXT_ID in missing_recheck["missing_required_context"],
        f"missing-recheck case did not report {REQUIRED_CONTEXT_ID}: {missing_recheck}",
    )

    explicit_recheck = classify(
        "abdominal pain recheck",
        "Adult with abdominal pain. ED evaluation reassuring. Discharged with explicit recheck plan.",
    )
    require(explicit_recheck["phenotype_id"] == PHENOTYPE_ID, f"explicit-recheck case did not match abdominal draft: {explicit_recheck}")
    if phenotype["status"] == "reviewed" and phenotype["review"]["status"] == "reviewed":
        require(explicit_recheck["fallback_reason"] is None, f"explicit-recheck case should enter ontology mode: {explicit_recheck}")
    else:
        require(
            explicit_recheck["fallback_reason"] == "phenotype_not_clinician_reviewed",
            f"explicit-recheck case should only be blocked by review status: {explicit_recheck}",
        )

    poor_follow_up = classify(
        "abdominal pain recheck",
        "Adult with abdominal pain. ED evaluation reassuring. Discharged with explicit recheck plan, but patient is unable to follow up.",
    )
    require(poor_follow_up["fallback_reason"] == "unsafe_modifier_present", f"poor-follow-up case did not block: {poor_follow_up}")
    require("poor_follow_up" in poor_follow_up["exclusions"], f"poor-follow-up case missing exclusion: {poor_follow_up}")

    print("phase26 abdominal runtime gate checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
