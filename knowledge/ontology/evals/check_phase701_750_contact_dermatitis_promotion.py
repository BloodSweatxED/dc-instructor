#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, assemble_discharge, read_json  # noqa: E402


PHENOTYPE_ID = "contact_dermatitis_uncomplicated"
CASES_PATH = ROOT / "evals" / "phase701_750_contact_dermatitis_promotion_runtime_cases.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def output_modifier_ids(result: dict) -> set[str]:
    return {item["id"] for item in result.get("output_modifiers", [])}


def assert_case(case: dict) -> None:
    result = classify(case["condition"], case.get("ed_note", ""))
    require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
    if case["expected_fallback_reason"] is None:
        require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
    for expected in case.get("expected_missing_required_context", []):
        require(expected in result.get("missing_required_context", []), f"{case['id']} missing context {expected}: {result}")
    for expected in case.get("expected_output_modifiers", []):
        require(expected in output_modifier_ids(result), f"{case['id']} missing output modifier {expected}: {result}")


def assert_reviewed_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_row = next(row for row in manifest["phenotypes"] if row["id"] == PHENOTYPE_ID)
    output = assemble_discharge(PHENOTYPE_ID, "6").lower()
    unsafe_modifiers = set(phenotype["runtime"].get("unsafe_modifiers", []))
    output_modifiers = {item["id"] for item in phenotype["runtime"].get("output_modifiers", [])}
    required_context = {item["id"] for item in phenotype["runtime"].get("required_context", [])}

    require(phenotype["status"] == "reviewed", "contact dermatitis should be reviewed")
    require(phenotype["review"]["status"] == "reviewed", "contact dermatitis review should be reviewed")
    require(phenotype["review"]["last_reviewed"] == "2026-06-05", "contact dermatitis review date should match approval date")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "contact dermatitis runtime should be reviewed ontology")
    require(manifest_row["status"] == "reviewed", "manifest should mark contact dermatitis reviewed")
    require(manifest_row["review_status"] == "reviewed", "manifest should mark contact dermatitis review reviewed")

    require("not an infection, allergic emergency, or serious medication reaction" in output, "plain-language finding should remain")
    require("may take one to three weeks to fully clear" in output, "recovery timeline should remain")
    require("swelling around the eyes or genitals" not in output, "return precautions should not include blocked locations")
    require("hydrocortisone" not in output, "static output should not name hydrocortisone")
    require("prednisone" not in output, "static output should not name prednisone")

    for context_id in {
        "clinician_diagnosis_contact_dermatitis",
        "contact_trigger_or_distribution_documented",
        "dangerous_rash_features_absent",
    }:
        require(context_id in required_context, f"missing required context {context_id}")
    for blocker in {
        "anaphylaxis",
        "airway_symptoms",
        "mucosal_lesions",
        "severe_cutaneous_adverse_reaction",
        "contact_dermatitis_infection_concern",
        "eye_or_genital_rash_location",
        "burn_or_chemical_wound",
        "immunocompromised",
        "pregnancy",
        "pediatric_pathway",
    }:
        require(blocker in unsafe_modifiers, f"missing blocker {blocker}")
    for modifier in {
        "frail_elderly_large_bsa_contact_dermatitis",
        "occupational_recurrent_contact_dermatitis",
    }:
        require(modifier in output_modifiers, f"{modifier} should be an output modifier")


def assert_gate_open() -> None:
    payload = gate_payload()
    active_ids = {
        item["phenotype_id"] if isinstance(item, dict) else item
        for item in payload["active_draft_phenotypes"]
    }
    require(PHENOTYPE_ID not in active_ids, f"contact dermatitis should not be an active draft: {payload}")
    require(payload["reviewed_runtime_clean"], "reviewed runtime should be clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should be zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should be zero")
    require(payload["active_draft_phenotype_count"] == 0, "active draft queue should be empty after promotion")


def main() -> int:
    for case in json.loads(CASES_PATH.read_text(encoding="utf-8")):
        assert_case(case)

    assert_reviewed_contract()
    assert_gate_open()

    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)

    print("phase701-750 contact dermatitis promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
