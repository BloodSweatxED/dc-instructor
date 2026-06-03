#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_sinusitis_supportive_care"
SOURCE_CARDS = {
    "cdc.sinus_infection",
    "medlineplus.sinusitis",
    "cdc.antibiotic_use_adult_outpatient",
}
BLOCKERS = {
    "antibiotic_prescribed_for_sinusitis",
    "severe_bacterial_sinusitis_features",
    "orbital_or_intracranial_sinusitis_concern",
    "dental_or_facial_trauma_source",
    "immunocompromised",
    "elderly_frail",
    "pregnancy",
    "sepsis",
    "unstable_vitals",
    "chronic_or_recurrent_sinusitis",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_case(case: dict) -> None:
    result = classify(case["condition"], case.get("ed_note", ""))
    require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next((item for item in manifest["phenotypes"] if item["id"] == TARGET), None)
    payload = gate_payload()

    promoted = phenotype["status"] == "reviewed" and phenotype["review"]["status"] == "reviewed"
    if promoted:
        require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "promoted sinusitis must be runtime enabled")
    else:
        require(phenotype["status"] in {"draft", "needs_review"}, "sinusitis must remain draft or needs_review before promotion")
        require(phenotype["review"]["status"] in {"draft", "needs_review"}, "sinusitis review status must not be reviewed before promotion")
        require(phenotype["runtime"]["mode"] == "draft_only_until_reviewed", "sinusitis runtime must remain draft-only before promotion")
    require(set(phenotype["source_card_ids"]) == SOURCE_CARDS, "sinusitis source cards changed unexpectedly")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == BLOCKERS, "sinusitis blockers changed unexpectedly")
    require(manifest_item is not None, "manifest missing sinusitis")
    require("congestion" not in set(manifest_item["condition_terms"]), "broad congestion must not be standalone term")
    require("facial pain" not in set(manifest_item["condition_terms"]), "broad facial pain must not be standalone term")
    require("cold symptoms" not in set(manifest_item["condition_terms"]), "broad cold symptoms must not be standalone term")

    for source_id in SOURCE_CARDS:
        require((ROOT / "source_cards" / f"{source_id}.json").exists(), f"missing source card {source_id}")

    for doc_name, required_text in [
        ("phase36_candidate_ranking_after_bronchitis.md", "Recommendation: build `acute_sinusitis_supportive_care` next as a draft only."),
        ("phase37_acute_sinusitis_source_plan.md", "Do not use sinusitis as a fallback for unmatched URI complaints."),
        ("phase38_acute_sinusitis_draft.md", "Do not promote sinusitis yet."),
        ("phase39_acute_sinusitis_stress.md", "Dental source or facial trauma blocker."),
        ("phase40_acute_sinusitis_review_decision.md", "Decision: do not promote `acute_sinusitis_supportive_care` yet."),
    ]:
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    cases = []
    for filename in ["phase38_acute_sinusitis_runtime_cases.json", "phase39_acute_sinusitis_stress_runtime_cases.json"]:
        cases.extend(json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")))
    require(len(cases) == 10, "phase38-39 should keep ten sinusitis runtime cases")
    for case in cases:
        assert_case(case)

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    if promoted:
        active_ids = {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}
        require(TARGET not in active_ids, "sinusitis should no longer be an active draft after promotion")
    else:
        require(not payload["phenotype_expansion_allowed"], "expansion gate should close while sinusitis is active draft")
        require(payload["active_draft_phenotype_count"] == 1, "sinusitis should be the only active draft")
        require(payload["active_draft_phenotypes"][0]["phenotype_id"] == TARGET, "active draft should be sinusitis")
    require(payload["draft_source_gap_count"] == 0, "sinusitis draft should not introduce source gaps")

    print("phase36-40 acute sinusitis cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
