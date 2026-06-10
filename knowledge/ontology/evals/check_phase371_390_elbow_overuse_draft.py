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


TARGET = "elbow_sprain_overuse_xray_negative"
CASES_PATH = ROOT / "evals" / "phase371_390_elbow_overuse_runtime_cases.json"
SOURCE_CARDS = {
    "aaos.tennis_elbow_lateral_epicondylitis",
    "aaos.medial_epicondylitis_golfers_elbow",
    "aaos.distal_biceps_tendon_tear",
    "aaos.olecranon_bursitis",
}
REQUIRED_CONTEXT = {
    "adult_elbow_overuse_diagnosis",
    "xray_performed_and_negative",
    "intact_neurovascular_and_hand_motor_exam",
    "no_acute_traumatic_mechanism_attested",
    "no_elbow_instability_concern_attested",
}
BLOCKERS = {
    "acute_traumatic_elbow_mechanism",
    "fracture_seen",
    "dislocation",
    "open_wound",
    "open_fracture",
    "high_energy_trauma",
    "crush_injury",
    "elbow_instability_or_ucl_lcl_concern",
    "distal_biceps_or_triceps_concern",
    "ulnar_nerve_pattern",
    "olecranon_bursitis_pathway",
    "neurovascular_compromise",
    "hand_motor_deficit",
    "compartment_syndrome_concern",
    "septic_joint_or_infection_concern",
    "pediatric_growth_plate_pathway",
    "elderly_osteoporotic_high_risk_msk",
    "specialist_directed_orthopedic_plan",
    "no_xray_performed",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_cases() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 14, "Phase 371-390 elbow overuse fixture should keep 14 cases")
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        for expected in case.get("expected_exclusions", []):
            require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
        for expected in case.get("expected_missing_required_context", []):
            require(
                expected in result["missing_required_context"],
                f"{case['id']} missing required context {expected}: {result}",
            )


def assert_draft_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next(item for item in manifest["phenotypes"] if item["id"] == TARGET)

    require(phenotype["status"] == "reviewed", "elbow overuse should be reviewed after clinician approval")
    require(phenotype["review"]["status"] == "reviewed", "elbow overuse review status should be reviewed")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "elbow overuse runtime should be reviewed-enabled")
    require(set(phenotype["source_card_ids"]) == SOURCE_CARDS, "elbow overuse source cards drifted")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == BLOCKERS, "elbow overuse blockers drifted")
    require({item["id"] for item in phenotype["runtime"]["required_context"]} == REQUIRED_CONTEXT, "required context drifted")
    require(manifest_item["status"] == "reviewed", "manifest should keep elbow overuse reviewed")
    require(manifest_item["review_status"] == "reviewed", "manifest should keep elbow overuse reviewed")
    require("elbow pain" not in set(manifest_item["condition_terms"]), "broad elbow pain must not be a condition term")

    text = assemble_discharge(TARGET, "6")
    for required in [
        "not caused by a sudden injury",
        "no signs of instability",
        "Do not immobilize it unless your clinician gave you a brace or splint plan.",
        "elbow tendon overuse can take weeks to months to fully settle down",
        "primary care, occupational medicine, sports medicine, or orthopedics in 1 to 2 weeks",
        "rehab and return-to-activity plan",
    ]:
        require(required in text, f"assembled note missing expected phrase: {required}")


def assert_gate_state() -> None:
    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    active_ids = {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}
    require(TARGET not in active_ids, f"elbow overuse should not remain an active draft after approval: {payload}")
    if not active_ids:
        require(payload["phenotype_expansion_allowed"], "expansion gate should reopen when no active drafts remain")


def main() -> int:
    assert_draft_contract()
    assert_cases()
    assert_gate_state()
    print("phase371-390 elbow overuse reviewed checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
