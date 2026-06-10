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


WRIST_PHENOTYPE = "wrist_sprain_xray_negative"
PROMOTED_SPRAIN = "sprain_strain_knee_or_shoulder_xray_negative"
RETIRED_BROAD = "sprain_strain_non_ankle_xray_negative"
ALLOWED_LATER_DRAFTS = {"elbow_sprain_overuse_xray_negative"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_wrist_reviewed_contract(manifest_by_id: dict[str, dict]) -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{WRIST_PHENOTYPE}.json")
    manifest_item = manifest_by_id[WRIST_PHENOTYPE]
    runtime = phenotype["runtime"]

    require(phenotype["status"] == "reviewed", "wrist should be reviewed after clinician approval")
    require(phenotype["review"]["status"] == "reviewed", "wrist review should be reviewed after approval")
    require(runtime["mode"] == "reviewed_ontology_enabled", "wrist runtime mode should be reviewed ontology enabled")
    require(manifest_item["status"] == "reviewed", "manifest should keep wrist reviewed status")
    require(manifest_item["review_status"] == "reviewed", "manifest should keep wrist review status")

    required_ids = {item["id"] for item in runtime.get("required_context", [])}
    require("wrist_site_documented" in required_ids, "wrist site context missing")
    require("xray_performed_and_negative" in required_ids, "wrist negative x-ray context missing")
    require("intact_neurovascular_exam" in required_ids, "wrist neurovascular context missing")
    require("no_scaphoid_tenderness_documented" in required_ids, "wrist scaphoid absence context missing")

    blockers = set(runtime.get("unsafe_modifiers", []))
    for blocker in {
        "foosh_scaphoid_risk",
        "scaphoid_tenderness_pattern",
        "hand_tendon_risk",
        "pediatric_growth_plate_pathway",
        "elderly_osteoporotic_high_risk_msk",
        "specialist_directed_orthopedic_plan",
    }:
        require(blocker in blockers, f"wrist blocker missing: {blocker}")


def assert_broad_sprain_retired(manifest_by_id: dict[str, dict]) -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{RETIRED_BROAD}.json")
    require(phenotype["status"] == "retired", "broad non-ankle sprain draft should stay retired")
    require(phenotype["review"]["status"] == "retired", "broad non-ankle sprain review should stay retired")
    require(manifest_by_id[RETIRED_BROAD]["status"] == "retired", "manifest should keep broad sprain retired")
    require(manifest_by_id[RETIRED_BROAD]["review_status"] == "retired", "manifest should keep broad sprain review retired")
    require(
        phenotype["runtime"]["mode"] == "retired_product_layer_fallback_only",
        "broad sprain should stay retired to product-layer fallback only",
    )


def assert_wrist_runtime_cases() -> None:
    cases = json.loads((ROOT / "evals" / "phase302_350_wrist_sprain_runtime_cases.json").read_text(encoding="utf-8"))
    require(len(cases) == 23, "Phase 302-350 wrist fixture should keep 23 runtime cases")
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
        if case["expected_fallback_reason"] is None:
            require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")


def assert_patient_text_and_gate() -> None:
    wrist_text = assemble_discharge(WRIST_PHENOTYPE, "6")
    require("signs of a deeper injury" in wrist_text.lower(), "wrist draft should explain scaphoid screen in patient language")
    require("base of your thumb" in wrist_text.lower(), "wrist draft should include lay thumb-side return language")
    require("does not show up on the first x-ray" in wrist_text.lower(), "wrist follow-up should explain occult fracture risk")

    knee_shoulder_text = assemble_discharge(PROMOTED_SPRAIN, "6")
    require("new inability to bear weight" in knee_shoulder_text.lower(), "knee/shoulder reviewed text should keep knee-specific return precaution")

    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    active_ids = {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}
    require(WRIST_PHENOTYPE not in active_ids, f"wrist should not remain active draft after approval: {payload}")
    unexpected = sorted(active_ids - ALLOWED_LATER_DRAFTS)
    require(unexpected == [], f"unexpected active drafts after wrist approval: {payload}")
    if not active_ids:
        require(payload["phenotype_expansion_allowed"], "expansion should reopen after wrist approval when no later draft is active")


def assert_netlify_wrist_parity() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_by_id = {item["id"]: item for item in manifest["phenotypes"]}
    require(WRIST_PHENOTYPE in manifest_by_id, "wrist phenotype missing from manifest")
    require(PROMOTED_SPRAIN in manifest_by_id, "promoted knee/shoulder sprain missing from manifest")

    assert_wrist_reviewed_contract(manifest_by_id)
    assert_broad_sprain_retired(manifest_by_id)
    assert_wrist_runtime_cases()
    assert_patient_text_and_gate()
    assert_netlify_wrist_parity()

    print("phase302-351 wrist sprain reviewed gate checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
