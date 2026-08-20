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


PHENOTYPE_ID = "adult_constipation_reassuring_ed_assessment_no_obstruction_or_bleeding"
CASES_PATH = ROOT / "evals" / "phase851_constipation_promotion_runtime_cases.json"
SOURCE_IDS = {
    "medlineplus.constipation_self_care",
    "niddk.constipation_adults",
    "medlineplus.intestinal_obstruction",
}
REQUIRED_CONTEXT = {
    "clinician_diagnosis_constipation",
    "reassuring_ed_assessment_or_benign_abdominal_exam",
    "no_obstruction_concern_documented",
    "no_gi_bleeding_documented",
}
BLOCKERS = {
    "bowel_obstruction_or_ileus_concern",
    "no_flatus",
    "abdominal_distention",
    "severe_or_focal_abdominal_pain",
    "peritoneal_signs",
    "surgical_abdomen",
    "persistent_vomiting",
    "unable_to_tolerate_oral_fluids",
    "severe_dehydration",
    "gi_bleeding",
    "fecal_impaction_procedure_plan",
    "opioid_induced_constipation",
    "elderly_frail",
    "nursing_home_patient",
    "pregnancy",
    "pediatric_pathway",
    "immunocompromised",
    "cancer_red_flag",
    "cauda_equina_concern",
    "urinary_retention",
    "poor_follow_up",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_case(case: dict) -> None:
    result = classify(case["condition"], case.get("ed_note", ""))
    require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
    if case["expected_fallback_reason"] is None:
        require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
    for expected in case.get("expected_missing_required_context", []):
        require(
            expected in result["missing_required_context"],
            f"{case['id']} missing required context {expected}: {result}",
        )


def assert_reviewed_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_row = next(row for row in manifest["phenotypes"] if row["id"] == PHENOTYPE_ID)
    output = assemble_discharge(PHENOTYPE_ID, "6")
    output_lower = output.lower()

    require(phenotype["status"] == "reviewed", "constipation should be reviewed")
    require(phenotype["review"]["status"] == "reviewed", "constipation review should be reviewed")
    require(phenotype["review"]["last_reviewed"] == "2026-06-06", "constipation review date should reflect clinician approval")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "constipation runtime should be reviewed ontology")
    require(manifest_row["status"] == "reviewed", "manifest should mark constipation reviewed")
    require(manifest_row["review_status"] == "reviewed", "manifest should mark constipation review reviewed")
    require(set(phenotype["source_card_ids"]) == SOURCE_IDS, "constipation source cards drifted")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == BLOCKERS, "constipation blockers drifted")
    require({item["id"] for item in phenotype["runtime"]["required_context"]} == REQUIRED_CONTEXT, "constipation required context drifted")

    for forbidden in {
        "polyethylene glycol",
        "miralax",
        "docusate",
        "colace",
        "senna",
        "ibuprofen",
        "no signs of blockage",
        "no signs of bowel blockage",
        "imaging showed",
        "ct showed",
    }:
        require(forbidden not in output_lower, f"static output should not include: {forbidden}")

    for required in {
        "Your clinician examined you and your symptoms were consistent with constipation. No signs of an emergency cause were found on exam.",
        "Most people see improvement within one to three days of starting treatment.",
        "New back pain, leg weakness, or trouble urinating.",
        "Follow up with your primary care provider or urgent care within two to three days if your symptoms are not improving.",
        "Do not use laxatives if you develop severe abdominal pain, repeated vomiting, or a swollen belly.",
    }:
        require(required in output, f"assembled note missing expected phrase: {required}")


def assert_gate_open() -> None:
    payload = gate_payload()
    active_ids = {
        item["phenotype_id"] if isinstance(item, dict) else item
        for item in payload["active_draft_phenotypes"]
    }
    require(PHENOTYPE_ID not in active_ids, f"constipation should not be an active draft: {payload}")
    require(payload["reviewed_runtime_clean"], "reviewed runtime should be clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should be zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should be zero")
    require(payload["active_draft_phenotype_count"] == 0, "active draft queue should be empty after promotion")


def main() -> int:
    assert_reviewed_contract()

    for case in json.loads(CASES_PATH.read_text(encoding="utf-8")):
        assert_case(case)

    assert_gate_open()
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)

    print("phase851 constipation promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
