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


TARGET = "elbow_sprain_overuse_xray_negative"
CASES_PATH = ROOT / "evals" / "phase391_420_elbow_overuse_review_runtime_cases.json"
REVIEW_PATH = ROOT / "evals" / "phase391_420_elbow_overuse_review_packet.md"
ALLOWED_ACTIVE_DRAFTS = {TARGET}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_runtime_cases() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 16, "Phase 391-420 elbow review fixture should keep 16 cases")
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


def assert_draft_hold_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next(item for item in manifest["phenotypes"] if item["id"] == TARGET)

    require(phenotype["status"] == "reviewed", "elbow overuse should be reviewed after clinician approval")
    require(phenotype["review"]["status"] == "reviewed", "elbow overuse review should be reviewed")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "elbow overuse runtime should be reviewed-enabled")
    require(manifest_item["status"] == "reviewed", "manifest should keep elbow overuse reviewed")
    require(manifest_item["review_status"] == "reviewed", "manifest should keep elbow overuse reviewed")
    require("elbow pain" not in set(manifest_item["condition_terms"]), "broad elbow pain must not become a condition term")
    require("elbow sprain xray negative" not in set(manifest_item["condition_terms"]), "acute elbow sprain must not match the overuse draft")


def assert_patient_note_and_review_packet() -> None:
    text = assemble_discharge(TARGET, "6")
    for required in [
        "Your clinician diagnosed an elbow overuse injury",
        "not caused by a sudden injury",
        "no signs of instability",
        "Do not immobilize it unless your clinician gave you a brace or splint plan.",
        "elbow tendon overuse can take weeks to months to fully settle down",
        "primary care, occupational medicine, sports medicine, or orthopedics in 1 to 2 weeks",
        "swollen painful bump over the back of the elbow",
    ]:
        require(required in text, f"assembled note missing expected phrase: {required}")

    review_text = REVIEW_PATH.read_text(encoding="utf-8")
    require("## Full Assembled Patient-Facing Note" in review_text, "review packet should include full assembled note section")
    require(text in review_text, "review packet should inline the exact assembled patient-facing note")
    require("Decision: revise then promote." in review_text, "review packet should state revise-then-promote decision")


def assert_gate_state() -> None:
    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "elbow overuse draft should not introduce source gaps")
    active_ids = {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}
    require(TARGET not in active_ids, f"elbow overuse should not remain an active draft after approval: {payload}")
    if not active_ids:
        require(payload["phenotype_expansion_allowed"], "expansion gate should reopen when no active drafts remain")


def assert_netlify_parity() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    assert_draft_hold_contract()
    assert_runtime_cases()
    assert_patient_note_and_review_packet()
    assert_gate_state()
    assert_netlify_parity()
    print("phase391-420 elbow overuse reviewed checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
