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
CASES_PATH = ROOT / "evals" / "phase651_700_contact_dermatitis_runtime_cases.json"


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


def assert_draft_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json")
    output = assemble_discharge(PHENOTYPE_ID, "6").lower()
    unsafe_modifiers = set(phenotype["runtime"].get("unsafe_modifiers", []))
    required_context = {item["id"] for item in phenotype["runtime"].get("required_context", [])}

    require(phenotype["status"] == "reviewed", "contact dermatitis should be reviewed after clinician approval")
    require(phenotype["review"]["status"] == "reviewed", "contact dermatitis review should be reviewed after clinician approval")
    require(phenotype["review"]["last_reviewed"] == "2026-06-05", "contact dermatitis review date should reflect clinician approval")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "contact dermatitis should be ontology-enabled after promotion")
    require("today" not in output, "contact dermatitis output should not contain today")
    require("hydrocortisone" not in output, "contact dermatitis static output should not name hydrocortisone")
    require("prednisone" not in output, "contact dermatitis static output should not name prednisone")
    require("antibiotic" in output, "contact dermatitis output should explicitly avoid unapproved leftover antibiotic ointment")
    require(
        "not an infection, allergic emergency, or serious medication reaction" in output,
        "contact dermatitis should use clinician-reviewed plain-language what-we-found wording",
    )
    require(
        "may take one to three weeks to fully clear" in output,
        "contact dermatitis should include recovery timeline",
    )
    require(
        "swelling around the eyes or genitals" not in output,
        "contact dermatitis return precautions should not imply eye/genital cases are included",
    )
    require(
        "increasing pain around the rash" in output,
        "contact dermatitis return precautions should include trimmed infection-worsening wording",
    )

    for context_id in {
        "clinician_diagnosis_contact_dermatitis",
        "contact_trigger_or_distribution_documented",
        "dangerous_rash_features_absent",
    }:
        require(context_id in required_context, f"missing required context {context_id}")
    for blocker in {
        "airway_symptoms",
        "mucosal_lesions",
        "severe_cutaneous_adverse_reaction",
        "contact_dermatitis_infection_concern",
        "eye_or_genital_rash_location",
        "immunocompromised",
        "pregnancy",
        "pediatric_pathway",
    }:
        require(blocker in unsafe_modifiers, f"missing blocker {blocker}")


def main() -> int:
    for case in json.loads(CASES_PATH.read_text(encoding="utf-8")):
        assert_case(case)

    assert_draft_contract()

    payload = gate_payload()
    active_ids = {
        item["phenotype_id"] if isinstance(item, dict) else item
        for item in payload["active_draft_phenotypes"]
    }
    require(PHENOTYPE_ID not in active_ids, f"contact dermatitis should not remain an active draft after promotion: {payload}")
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")

    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)

    print("phase651-700 contact dermatitis reviewed checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
