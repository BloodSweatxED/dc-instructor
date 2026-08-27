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


PROMOTED_AFTER_PHASE_222 = {
    "acute_otitis_media_uncomplicated",
    "sprain_strain_knee_or_shoulder_xray_negative",
    "suture_removal_or_wound_check_no_infection",
    "skin_avulsion_or_abrasion_simple",
    "wrist_sprain_xray_negative",
}

ACTIVE_DRAFTS: set[str] = set()


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
    output_modifier_ids = [item["id"] for item in result.get("output_modifiers", [])]
    for expected in case.get("expected_output_modifiers", []):
        require(expected in output_modifier_ids, f"{case['id']} missing output modifier {expected}: {result}")


def main() -> int:
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_items = {item["id"]: item for item in manifest["phenotypes"]}
    payload = gate_payload()

    for phenotype_id in PROMOTED_AFTER_PHASE_222:
        phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
        manifest_item = manifest_items[phenotype_id]
        output = assemble_discharge(phenotype_id, "6")
        require(phenotype["status"] == "reviewed", f"{phenotype_id} should be reviewed after Phase 222")
        require(phenotype["review"]["status"] == "reviewed", f"{phenotype_id} review should be reviewed after Phase 222")
        require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", f"{phenotype_id} should be ontology enabled")
        require(manifest_item["status"] == "reviewed", f"{phenotype_id} manifest status should be reviewed")
        require("today" not in output.lower(), f"{phenotype_id} output should not contain today")

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
    aom_output_modifier_ids = [item["id"] for item in aom["runtime"].get("output_modifiers", [])]
    require("elderly_frail" in aom_output_modifier_ids, "AOM frail elderly should be an output modifier after Phase 222 feedback")
    require("diabetes_general_risk" in aom_output_modifier_ids, "AOM diabetes should be an output modifier after Phase 222 feedback")
    require("watchful_waiting_follow_up_unreliable" in aom["runtime"]["unsafe_modifiers"], "AOM unreliable watchful-waiting follow-up should remain a pathway-specific blocker")
    require("meningitis_or_cns_infection_concern" in aom["runtime"]["unsafe_modifiers"], "AOM should block meningitis signs")
    require("lateral_sinus_thrombosis_concern" in aom["runtime"]["unsafe_modifiers"], "AOM should block venous sinus thrombosis concern")

    suture = read_json(ROOT / "phenotypes" / "suture_removal_or_wound_check_no_infection.json")
    suture_output_modifier_ids = [item["id"] for item in suture["runtime"].get("output_modifiers", [])]
    require("high_risk_wound_location" in suture["runtime"]["unsafe_modifiers"], "Suture/wound check should block high-risk wound locations")
    require("diabetes_general_risk" in suture_output_modifier_ids, "Suture/wound check diabetes should be an output modifier")
    require("peripheral_vascular_disease" in suture_output_modifier_ids, "Suture/wound check PVD should be an output modifier")
    require("anticoagulated" in suture_output_modifier_ids, "Suture/wound check anticoagulation should be an output modifier")
    require(
        any(item["id"] == "clinician_documented_expected_healing_or_clearance" for item in suture["runtime"]["required_context"]),
        "Suture/wound check should require expected healing or explicit wound clearance",
    )
    require(
        any(item["id"] == "clinician_entered_wound_follow_up_plan" for item in suture["runtime"]["required_context"]),
        "Suture/wound check should require clinician-entered wound follow-up plan",
    )

    deprecated_sprain = read_json(ROOT / "phenotypes" / "sprain_strain_non_ankle_xray_negative.json")
    require(deprecated_sprain["status"] == "retired", "broad non-ankle sprain should be retired")

    sprain_output = assemble_discharge("sprain_strain_knee_or_shoulder_xray_negative", "6").lower()
    require("acetaminophen" not in sprain_output, "Sprain/strain static output should not name acetaminophen")
    require("ibuprofen" not in sprain_output, "Sprain/strain static output should not name ibuprofen")
    require("x-ray was performed" in sprain_output, "Sprain/strain output should require x-ray performed wording")
    require("pain out of proportion" in sprain_output, "Sprain/strain output should include compartment syndrome plain-language signal")
    require("new inability to bear weight" in sprain_output, "Knee/shoulder sprain output should include knee weight-bearing return precaution")

    for case in json.loads((ROOT / "evals" / "phase202_215_reviewed_revision_runtime_cases.json").read_text(encoding="utf-8")):
        assert_case(case)

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 0, f"active drafts should be cleared after wrist approval: {payload['active_draft_phenotypes']}")
    require(payload["active_draft_phenotypes"] == [], f"active draft list should be empty after wrist approval: {payload['active_draft_phenotypes']}")
    require(payload["phenotype_expansion_allowed"], "expansion should reopen after wrist approval")

    print("phase202-215 cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
