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


TARGET = "conjunctivitis_uncomplicated_no_contact_lens"
SOURCE_CARDS = {"cdc.conjunctivitis", "medlineplus.conjunctivitis"}
BLOCKERS = {
    "contact_lens_use",
    "chemical_eye_exposure",
    "corneal_ulcer_or_keratitis_concern",
    "acute_glaucoma_mimic",
    "eye_trauma_or_foreign_body",
    "severe_eye_pain",
    "photophobia",
    "vision_change",
    "herpes_or_zoster_eye_concern",
    "periorbital_or_orbital_cellulitis_concern",
    "immunocompromised",
    "pregnancy",
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

    require(phenotype["status"] in {"draft", "needs_review", "retired"}, "conjunctivitis must remain unreviewed or retired")
    require(phenotype["review"]["status"] in {"draft", "needs_review", "retired"}, "conjunctivitis review status must not be reviewed")
    require(
        phenotype["runtime"]["mode"] in {"draft_only_until_reviewed", "retired_product_layer_fallback_only"},
        "conjunctivitis runtime must remain out of ontology mode",
    )
    require(set(phenotype["source_card_ids"]) == SOURCE_CARDS, "conjunctivitis source cards changed unexpectedly")
    require(set(phenotype["runtime"]["unsafe_modifiers"]) == BLOCKERS, "conjunctivitis blockers changed unexpectedly")
    require(manifest_item is not None, "manifest missing conjunctivitis")
    for broad in ["red eye", "eye discharge", "itchy eye"]:
        require(broad not in set(manifest_item["condition_terms"]), f"broad term must not be standalone: {broad}")

    cases = []
    for filename in [
        "phase47_conjunctivitis_runtime_cases.json",
        "phase48_conjunctivitis_stress_runtime_cases.json",
        "phase52_conjunctivitis_boundary_runtime_cases.json",
    ]:
        cases.extend(json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")))
    require(len(cases) == 15, "phase47-52 should keep fifteen conjunctivitis cases")
    for case in cases:
        assert_case(case)

    for doc_name, required_text in [
        ("phase46_conjunctivitis_source_plan.md", "Do not use conjunctivitis as a catch-all eye complaint fallback."),
        ("phase49_conjunctivitis_review_packet.md", "Decision: keep as draft. Do not promote yet."),
        ("phase50_conjunctivitis_review_decision.md", "Do not promote until a clinician review packet approves the eye red-flag boundary."),
    ]:
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(TARGET not in {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}, "conjunctivitis should not remain an active draft after Phase 54")
    require(payload["draft_source_gap_count"] == 0, "conjunctivitis draft should not introduce source gaps")

    print("phase46-50 conjunctivitis cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
