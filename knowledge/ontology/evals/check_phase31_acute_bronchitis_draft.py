#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_bronchitis_no_pneumonia"
CASE_PATH = ROOT / "evals" / "phase31_acute_bronchitis_runtime_cases.json"
DOC_PATH = ROOT / "evals" / "phase31_acute_bronchitis_draft.md"
REQUIRED_SOURCE_CARDS = {
    "cdc.acute_bronchitis",
    "medlineplus.acute_bronchitis",
    "cdc.antibiotic_use_adult_outpatient",
}
REQUIRED_BLOCKERS = {
    "hypoxia",
    "respiratory_distress",
    "pneumonia",
    "focal_lung_findings_or_infiltrate",
    "copd_or_asthma_exacerbation_pathway",
    "immunocompromised",
    "elderly_frail",
    "hemoptysis",
    "cardiac_or_pe_chest_pain_concern",
    "sepsis",
    "unstable_vitals",
    "antibiotic_prescribed_for_suspected_bacterial_infection",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    gate = read_json(ROOT / "evals" / "phase21_expansion_gate" / "phase21_expansion_gate.json")
    manifest_item = next((item for item in manifest["phenotypes"] if item["id"] == TARGET), None)

    promoted = phenotype["status"] == "reviewed" and phenotype["review"]["status"] == "reviewed"
    if promoted:
        require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "promoted bronchitis must be runtime enabled")
    else:
        require(phenotype["status"] in {"draft", "needs_review"}, "acute bronchitis must remain draft or needs_review before promotion")
        require(phenotype["review"]["status"] in {"draft", "needs_review"}, "acute bronchitis review status must not be reviewed before promotion")
        require(phenotype["runtime"]["mode"] == "draft_only_until_reviewed", "runtime mode must remain draft-only before promotion")
    require(set(phenotype["source_card_ids"]) == REQUIRED_SOURCE_CARDS, "source cards changed unexpectedly")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == REQUIRED_BLOCKERS, "runtime blockers changed unexpectedly")
    require(manifest_item is not None, "manifest missing acute bronchitis")
    if promoted:
        require(manifest_item["status"] == "reviewed", "manifest status must be reviewed after promotion")
        require(manifest_item["review_status"] == "reviewed", "manifest review status must be reviewed after promotion")
    else:
        require(manifest_item["status"] in {"draft", "needs_review"}, "manifest status must not be reviewed before promotion")
        require(manifest_item["review_status"] in {"draft", "needs_review"}, "manifest review status must not be reviewed before promotion")
    require(gate["reviewed_runtime_clean"], "reviewed runtime should remain clean with bronchitis draft present")
    if promoted:
        require(gate["phenotype_expansion_allowed"], "expansion gate should reopen after bronchitis promotion")
        require(gate["active_draft_phenotype_count"] == 0, "active drafts should close after bronchitis promotion")
    else:
        require(not gate["phenotype_expansion_allowed"], "expansion gate should close while bronchitis is an active draft")
        require(gate["active_draft_phenotype_count"] == 1, "bronchitis should be the only active draft phenotype")
        require(
            gate["active_draft_phenotypes"][0]["phenotype_id"] == TARGET,
            "active draft phenotype should be acute bronchitis",
        )
    require(gate["draft_source_gap_count"] == 0, "bronchitis draft should not introduce source gaps")

    terms = set(manifest_item["condition_terms"])
    require("cough" not in terms, "broad cough must not be a standalone runtime term")
    require("acute bronchitis" in terms, "manifest missing acute bronchitis term")
    require("chest cold" in terms, "manifest missing chest cold term")

    doc = DOC_PATH.read_text(encoding="utf-8")
    for phrase in [
        "Do not promote acute bronchitis yet.",
        "Do not add broad `cough` as a standalone term.",
        "Do not infer antibiotic instructions.",
        "Vague cough does not match.",
    ]:
        require(phrase in doc, f"phase31 doc missing guardrail: {phrase}")

    cases = json.loads(CASE_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 7, "phase31 must keep the first seven runtime cases")
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        for exclusion in case.get("expected_exclusions", []):
            require(exclusion in result["exclusions"], f"{case['id']} missing exclusion {exclusion}: {result}")

    print("phase31 acute bronchitis draft checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
