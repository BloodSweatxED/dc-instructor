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
    output_modifier_ids = [item["id"] for item in result.get("output_modifiers", [])]
    for expected in case.get("expected_output_modifiers", []):
        require(expected in output_modifier_ids, f"{case['id']} missing output modifier {expected}: {result}")
    min_confidence = case.get("expected_min_confidence")
    if min_confidence is not None:
        require(result["confidence"] >= min_confidence, f"{case['id']} confidence too low: {result}")
    max_confidence = case.get("expected_max_confidence")
    if max_confidence is not None:
        require(result["confidence"] <= max_confidence, f"{case['id']} confidence unexpectedly high: {result}")


def main() -> int:
    packet = ROOT / "evals" / "phase216_revised_output_side_by_side_review.md"
    require(packet.exists(), "Phase 216 side-by-side review packet is missing")
    packet_text = packet.read_text(encoding="utf-8").lower()
    require("today" not in packet_text, "Phase 216 packet should not reintroduce today")
    feedback_packet = ROOT / "evals" / "phase221_clinician_feedback_applied.md"
    require(feedback_packet.exists(), "Phase 221 clinician feedback packet is missing")
    feedback_text = feedback_packet.read_text(encoding="utf-8").lower()
    require("today" not in feedback_text, "Phase 221 packet should not reintroduce today")

    for phenotype_id in PROMOTED_AFTER_PHASE_222:
        phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
        output = assemble_discharge(phenotype_id, "6")
        require(phenotype["status"] == "reviewed", f"{phenotype_id} should be reviewed")
        require(phenotype["review"]["status"] == "reviewed", f"{phenotype_id} review should be reviewed")
        require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", f"{phenotype_id} should be ontology enabled")
        require("today" not in output.lower(), f"{phenotype_id} output should not contain today")

    for phenotype_id in ACTIVE_DRAFTS:
        phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
        output = assemble_discharge(phenotype_id, "6")
        require(phenotype["status"] == "needs_review", f"{phenotype_id} should remain needs_review")
        require(phenotype["review"]["status"] == "needs_review", f"{phenotype_id} review should remain needs_review")
        require(phenotype["runtime"]["mode"] == "draft_only_until_reviewed", f"{phenotype_id} should remain draft-only")
        require("today" not in output.lower(), f"{phenotype_id} output should not contain today")

    skin = read_json(ROOT / "phenotypes" / "skin_avulsion_or_abrasion_simple.json")
    skin_output = assemble_discharge("skin_avulsion_or_abrasion_simple", "6").lower()
    skin_output_modifier_ids = [item["id"] for item in skin["runtime"].get("output_modifiers", [])]
    for modifier in ["diabetes_general_risk", "peripheral_vascular_disease", "anticoagulated", "delayed_wound_presentation"]:
        require(modifier in skin_output_modifier_ids, f"skin avulsion should include output modifier {modifier}")
    require("immunocompromised" in skin["runtime"]["unsafe_modifiers"], "skin avulsion immunocompromised should remain a v1 blocker")
    require("skin turning pale, blue, or very dark" in skin_output, "skin avulsion should sharpen color-change language")
    require("not improving after 2 to 3 days" in skin_output, "skin avulsion should anchor follow-up timing")

    aom = read_json(ROOT / "phenotypes" / "acute_otitis_media_uncomplicated.json")
    aom_output = assemble_discharge("acute_otitis_media_uncomplicated", "6").lower()
    aom_output_modifier_ids = [item["id"] for item in aom["runtime"].get("output_modifiers", [])]
    for modifier in ["elderly_frail", "diabetes_general_risk"]:
        require(modifier in aom_output_modifier_ids, f"AOM should include output modifier {modifier}")
    require("watchful_waiting_follow_up_unreliable" in aom["runtime"]["unsafe_modifiers"], "AOM should block unreliable watchful-waiting follow-up")
    require("7 to 10 days" in aom_output and "2 to 3 days" in aom_output, "AOM should split antibiotic and watchful-waiting follow-up")
    require("muffled hearing can last 2 to 4 weeks" in aom_output, "AOM should include muffled-hearing recovery timeline")
    require("typically begins within 5 to 7 days" in aom_output, "AOM should cut often from watchful-waiting timeline")

    suture = read_json(ROOT / "phenotypes" / "suture_removal_or_wound_check_no_infection.json")
    suture_output = assemble_discharge("suture_removal_or_wound_check_no_infection", "6").lower()
    suture_output_modifier_ids = [item["id"] for item in suture["runtime"].get("output_modifiers", [])]
    for modifier in ["diabetes_general_risk", "peripheral_vascular_disease", "anticoagulated"]:
        require(modifier in suture_output_modifier_ids, f"suture/wound check should include output modifier {modifier}")
    require("your clinician examined your wound" in suture_output, "suture/wound check should not presuppose healing in diagnosis")
    require("do not stop them early" not in suture_output, "suture/wound check should remove antibiotic-continuation scope conflict")
    require("skin turning pale, blue, or very dark" in suture_output, "suture/wound check should sharpen color-change language")
    require(
        any(item["id"] == "clinician_documented_expected_healing_or_clearance" for item in suture["runtime"]["required_context"]),
        "suture/wound check should require expected healing or explicit wound clearance",
    )

    for case in json.loads((ROOT / "evals" / "phase217_sprain_site_stress_runtime_cases.json").read_text(encoding="utf-8")):
        assert_case(case)

    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 0, f"active drafts should be cleared after wrist approval: {payload['active_draft_phenotypes']}")
    require(payload["active_draft_phenotypes"] == [], f"active draft list should be empty after wrist approval: {payload['active_draft_phenotypes']}")
    require(payload["phenotype_expansion_allowed"], "expansion should reopen after wrist approval")

    print("phase216-220 promotion-readiness checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
