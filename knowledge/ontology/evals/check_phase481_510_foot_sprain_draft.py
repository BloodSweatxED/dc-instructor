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


TARGET = "foot_sprain_xray_negative"
CASES_PATH = ROOT / "evals" / "phase481_510_foot_sprain_runtime_cases.json"
SOURCE_CARDS = {
    "medlineplus.sprains_strains",
    "medlineplus.foot_sprain_aftercare",
}
REQUIRED_CONTEXT = {
    "foot_site_documented",
    "xray_performed_and_negative",
    "intact_neurovascular_exam",
}
BLOCKERS = {
    "ankle_sprain_pathway",
    "no_xray_performed",
    "fracture_seen",
    "dislocation",
    "open_wound",
    "open_fracture",
    "high_energy_trauma",
    "crush_injury",
    "lisfranc_or_midfoot_concern",
    "unable_to_bear_weight_lower_extremity",
    "cannot_ambulate_at_discharge",
    "neurovascular_compromise",
    "tendon_or_ligament_rupture_concern",
    "compartment_syndrome_concern",
    "septic_joint_or_infection_concern",
    "pediatric_growth_plate_pathway",
    "elderly_osteoporotic_high_risk_msk",
    "diabetic_foot",
    "peripheral_vascular_disease",
    "specialist_directed_orthopedic_plan",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_reviewed_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next(item for item in manifest["phenotypes"] if item["id"] == TARGET)

    require(phenotype["status"] == "reviewed", "foot sprain should be promoted to reviewed")
    require(phenotype["review"]["status"] == "reviewed", "foot sprain review should be reviewed")
    require(phenotype["review"]["last_reviewed"] == "2026-06-05", "foot sprain review date should reflect clinician approval")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "foot sprain runtime should be reviewed ontology")
    require(manifest_item["status"] == "reviewed", "manifest should mark foot sprain reviewed")
    require(manifest_item["review_status"] == "reviewed", "manifest should mark foot sprain review as reviewed")
    require(set(phenotype["source_card_ids"]) == SOURCE_CARDS, "foot source cards drifted")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == BLOCKERS, "foot blockers drifted")
    require({item["id"] for item in phenotype["runtime"]["required_context"]} == REQUIRED_CONTEXT, "foot required context drifted")
    require("foot pain" not in set(manifest_item["condition_terms"]), "broad foot pain must not be a condition term")

    text = assemble_discharge(TARGET, "6")
    for required in [
        "Your clinician diagnosed a foot sprain.",
        "Your x-ray did not show a fracture.",
        "you may need a repeat exam or more imaging",
        "Some foot fractures are not visible on the first x-ray.",
        "Circulation, feeling, and movement in your foot and toes were normal.",
        "Protect your foot with the hard-soled shoe, boot, wrap, crutches",
        "If weight-bearing gets significantly worse instead of better, stop and return to the ED.",
        "Minor foot sprains often improve in several days.",
        "You lose the ability to bear weight after going home, or walking becomes significantly worse.",
        "Worsening midfoot pain, bruising on the bottom of the foot",
        "pain that seems out of proportion to the injury",
        "Go sooner if pain or swelling is worse after 2 to 3 days.",
    ]:
        require(required in text, f"assembled note missing expected phrase: {required}")


def assert_cases() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 15, "Phase 481-510 foot fixture should keep 15 cases")
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        if case["expected_fallback_reason"] is None:
            require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
        for expected in case.get("expected_exclusions", []):
            require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")


def assert_gate_state() -> None:
    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotypes"] == [], f"no active drafts should remain after foot promotion: {payload}")
    require(payload["phenotype_expansion_allowed"], "expansion should reopen after foot promotion")


def assert_netlify_parity() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    assert_reviewed_contract()
    assert_cases()
    assert_gate_state()
    assert_netlify_parity()
    print("phase481-510 foot sprain reviewed checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
