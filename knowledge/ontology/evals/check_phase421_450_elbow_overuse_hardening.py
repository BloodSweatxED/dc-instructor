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
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "elbow_sprain_overuse_xray_negative"
CASES_PATH = ROOT / "evals" / "phase421_450_elbow_overuse_hardening_runtime_cases.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_runtime_cases() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 10, "Phase 421-450 elbow hardening fixture should keep 10 cases")
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        if case["expected_fallback_reason"] in {None, "phenotype_not_clinician_reviewed"}:
            require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
            require(result["exclusions"] == [], f"{case['id']} should not have exclusions: {result}")
            require(result["missing_required_context"] == [], f"{case['id']} should not miss required context: {result}")
        for expected in case.get("expected_exclusions", []):
            require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
        output_modifier_ids = [item["id"] for item in result.get("output_modifiers", [])]
        for expected in case.get("expected_output_modifiers", []):
            require(expected in output_modifier_ids, f"{case['id']} missing output modifier {expected}: {result}")


def assert_manifest_hardening_terms() -> None:
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    item = next(row for row in manifest["phenotypes"] if row["id"] == TARGET)
    require(item["status"] == "reviewed", "elbow overuse should be reviewed after clinician approval")
    require(item["review_status"] == "reviewed", "elbow overuse should be reviewed after clinician approval")
    output_modifier_ids = {row["id"] for row in item.get("output_modifiers", [])}
    require("anticoagulated" in output_modifier_ids, "anticoagulated output modifier missing")
    require("immunocompromised" in output_modifier_ids, "immunocompromised output modifier missing")

    context_by_id = {row["id"]: set(row["terms"]) for row in item["required_context"]}
    require("xray shows no acute fracture" in context_by_id["xray_performed_and_negative"], "xray no acute fracture term missing")
    require("no fracture seen on xray" in context_by_id["xray_performed_and_negative"], "no fracture seen xray term missing")
    require("motor in the hand is normal" in context_by_id["intact_neurovascular_and_hand_motor_exam"], "hand motor normal term missing")


def assert_gate_state() -> None:
    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    active_ids = {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}
    require(TARGET not in active_ids, f"elbow overuse should not remain an active draft after approval: {payload}")
    if not active_ids:
        require(payload["phenotype_expansion_allowed"], "expansion gate should reopen when no active drafts remain")


def assert_netlify_parity() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    assert_manifest_hardening_terms()
    assert_runtime_cases()
    assert_gate_state()
    assert_netlify_parity()
    print("phase421-450 elbow overuse hardening checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
