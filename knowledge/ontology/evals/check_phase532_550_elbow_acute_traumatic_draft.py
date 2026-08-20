#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, assemble_discharge, read_json  # noqa: E402


TARGET = "elbow_sprain_acute_traumatic_xray_negative"
OVERUSE = "elbow_sprain_overuse_xray_negative"
FOOT = "foot_sprain_xray_negative"
CASES_PATH = ROOT / "evals" / "phase532_550_elbow_acute_traumatic_runtime_cases.json"
SOURCE_CARDS = {
    "medlineplus.sprains_strains",
    "aaos.distal_biceps_tendon_tear",
    "aaos.olecranon_bursitis",
}
REQUIRED_CONTEXT = {
    "adult_acute_traumatic_elbow_sprain_diagnosis",
    "xray_performed_and_negative",
    "intact_neurovascular_and_hand_motor_exam",
    "acute_traumatic_mechanism_documented",
    "no_elbow_instability_concern_attested",
    "no_distal_tendon_or_ligament_rupture_concern_attested",
}
BLOCKERS = {
    "overuse_or_repetitive_mechanism",
    "fracture_seen",
    "dislocation",
    "open_wound",
    "open_fracture",
    "high_energy_trauma",
    "crush_injury",
    "elbow_instability_or_ucl_lcl_concern",
    "tendon_or_ligament_rupture_concern",
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


def assert_reviewed_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next(item for item in manifest["phenotypes"] if item["id"] == TARGET)

    require(phenotype["status"] == "reviewed", "acute elbow sprain should be promoted to reviewed")
    require(phenotype["review"]["status"] == "reviewed", "acute elbow sprain review should be reviewed")
    require(phenotype["review"]["last_reviewed"] == "2026-06-05", "acute elbow review date should reflect clinician approval")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "acute elbow sprain runtime should be reviewed ontology")
    require(manifest_item["status"] == "reviewed", "manifest should mark acute elbow sprain reviewed")
    require(manifest_item["review_status"] == "reviewed", "manifest should mark acute elbow sprain review reviewed")
    require(set(phenotype["source_card_ids"]) == SOURCE_CARDS, "acute elbow sprain source cards drifted")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == BLOCKERS, "acute elbow sprain blockers drifted")
    require({item["id"] for item in phenotype["runtime"]["required_context"]} == REQUIRED_CONTEXT, "acute elbow sprain required context drifted")
    require("elbow pain" not in set(manifest_item["condition_terms"]), "broad elbow pain must not be a condition term")

    overuse = next(item for item in manifest["phenotypes"] if item["id"] == OVERUSE)
    foot = next(item for item in manifest["phenotypes"] if item["id"] == FOOT)
    require(overuse["status"] == "reviewed", "reviewed elbow overuse should stay reviewed")
    require(foot["status"] == "reviewed", "reviewed foot should stay reviewed")

    text = assemble_discharge(TARGET, "6")
    for required in [
        "Your clinician diagnosed an elbow sprain.",
        "Your x-ray did not show a fracture.",
        "Your clinician did not find signs of elbow instability or tendon rupture.",
        "Rest the elbow for the first 24 to 48 hours.",
        "begin gentle range of motion as pain allows",
        "Do not immobilize the elbow on your own unless instructed.",
        "Most elbow sprains improve over 1 to 3 weeks.",
        "Trouble rotating your forearm, turning your palm up, or turning your palm down.",
        "A pop or sudden worsening after the injury",
        "new swollen bump over the back of the elbow",
        "primary care, sports medicine, or orthopedics within 1 to 2 weeks",
        "forearm rotation is limited",
    ]:
        require(required in text, f"assembled note missing expected phrase: {required}")


def assert_cases() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 15, "Phase 532-550 acute elbow fixture should keep 15 cases")
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        if case["expected_fallback_reason"] in {None, "phenotype_not_clinician_reviewed"}:
            require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
        for expected in case.get("expected_exclusions", []):
            require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
        for expected in case.get("expected_missing_required_context", []):
            require(
                expected in result["missing_required_context"],
                f"{case['id']} missing required context {expected}: {result}",
            )


def assert_gate_state() -> None:
    payload = gate_payload()
    active_ids = {
        item["phenotype_id"] if isinstance(item, dict) else item
        for item in payload["active_draft_phenotypes"]
    }
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(
        "elbow_sprain_acute_traumatic_xray_negative" not in active_ids,
        f"acute elbow should not remain an active draft after promotion: {payload}",
    )


def assert_netlify_parity() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    assert_reviewed_contract()
    assert_cases()
    assert_gate_state()
    assert_netlify_parity()
    print("phase532-550 acute traumatic elbow sprain reviewed checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
