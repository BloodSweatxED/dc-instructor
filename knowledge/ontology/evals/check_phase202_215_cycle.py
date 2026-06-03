#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, assemble_discharge, read_json  # noqa: E402


ACTIVE_DRAFTS = {
    "acute_otitis_media_uncomplicated",
    "suture_removal_or_wound_check_no_infection",
    "skin_avulsion_or_abrasion_simple",
    "sprain_strain_non_ankle_xray_negative",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_case(case: dict) -> None:
    result = classify(case["condition"], case.get("ed_note", ""))
    require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
    for expected in case.get("expected_missing_required_context", []):
        require(expected in result.get("missing_required_context", []), f"{case['id']} missing context {expected}: {result}")


def main() -> int:
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_items = {item["id"]: item for item in manifest["phenotypes"]}
    payload = gate_payload()

    for phenotype_id in ACTIVE_DRAFTS:
        phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
        manifest_item = manifest_items[phenotype_id]
        output = assemble_discharge(phenotype_id, "6")
        require(phenotype["status"] == "needs_review", f"{phenotype_id} should be active needs_review")
        require(phenotype["review"]["status"] == "needs_review", f"{phenotype_id} review should be needs_review")
        require(phenotype["runtime"]["mode"] == "draft_only_until_reviewed", f"{phenotype_id} should remain draft-only")
        require(manifest_item["status"] == "needs_review", f"{phenotype_id} manifest status should be needs_review")
        require("today" not in output.lower(), f"{phenotype_id} output should not contain today")

    aom = read_json(ROOT / "phenotypes" / "acute_otitis_media_uncomplicated.json")
    require("elderly_frail" not in aom["runtime"]["unsafe_modifiers"], "AOM frail elderly should not be a hard blocker")
    require("meningitis_or_cns_infection_concern" in aom["runtime"]["unsafe_modifiers"], "AOM should block meningitis signs")
    require("lateral_sinus_thrombosis_concern" in aom["runtime"]["unsafe_modifiers"], "AOM should block venous sinus thrombosis concern")

    suture = read_json(ROOT / "phenotypes" / "suture_removal_or_wound_check_no_infection.json")
    require("high_risk_wound_location" in suture["runtime"]["unsafe_modifiers"], "Suture/wound check should block high-risk wound locations")
    require(
        any(item["id"] == "clinician_entered_wound_follow_up_plan" for item in suture["runtime"]["required_context"]),
        "Suture/wound check should require clinician-entered wound follow-up plan",
    )

    sprain_output = assemble_discharge("sprain_strain_non_ankle_xray_negative", "6").lower()
    require("acetaminophen" not in sprain_output, "Sprain/strain static output should not name acetaminophen")
    require("ibuprofen" not in sprain_output, "Sprain/strain static output should not name ibuprofen")
    require("x-ray was performed" in sprain_output, "Sprain/strain output should require x-ray performed wording")
    require("pain out of proportion" in sprain_output, "Sprain/strain output should include compartment syndrome plain-language signal")

    for case in json.loads((ROOT / "evals" / "phase202_215_reviewed_revision_runtime_cases.json").read_text(encoding="utf-8")):
        assert_case(case)

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 4, f"active drafts should be four: {payload['active_draft_phenotypes']}")
    require(not payload["phenotype_expansion_allowed"], "expansion should remain blocked while active drafts await approval")

    print("phase202-215 cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
