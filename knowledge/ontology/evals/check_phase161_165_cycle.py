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


AOM = "acute_otitis_media_uncomplicated"


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


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{AOM}.json")
    payload = gate_payload()

    require(phenotype["status"] in {"needs_review", "retired"}, "AOM should remain needs_review or retired")
    require(phenotype["review"]["status"] in {"needs_review", "retired"}, "AOM review should remain needs_review or retired")
    require(phenotype["runtime"]["mode"] in {"draft_only_until_reviewed", "retired_product_layer_fallback_only"}, "AOM should remain out of ontology mode")

    required_context_ids = {item["id"] for item in phenotype["runtime"].get("required_context", [])}
    require(
        {"adult_patient_context", "clinician_diagnosis_acute_otitis_media", "clinician_entered_treatment_plan", "structured_absence_of_ear_red_flags"}.issubset(required_context_ids),
        f"AOM required context incomplete: {required_context_ids}",
    )
    for blocker in ["pediatric_pathway", "specialist_directed_ent_plan", "tympanic_membrane_perforation_or_tube"]:
        require(blocker in phenotype["runtime"]["unsafe_modifiers"], f"AOM missing blocker {blocker}")

    for filename in [
        "phase156_acute_otitis_media_runtime_cases.json",
        "phase157_acute_otitis_media_stress_runtime_cases.json",
        "phase163_acute_otitis_media_second_stress_runtime_cases.json",
    ]:
        for case in json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")):
            assert_case(case)

    required_docs = {
        "phase161_acute_otitis_media_clinician_review_answers.md": "Decision: revise and keep draft. Do not promote.",
        "phase162_acute_otitis_media_revised_draft.md": "Patient-facing output:",
        "phase164_acute_otitis_media_gate_check.md": "Phenotype expansion allowed: false.",
        "phase165_handoff.md": "Completed through Phase 165.",
    }
    for doc_name, required_text in required_docs.items():
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    active_ids = [row["phenotype_id"] for row in payload["active_draft_phenotypes"]]
    require(AOM not in active_ids or active_ids == [AOM], f"AOM should not be mixed with other active drafts: {active_ids}")

    print("phase161-165 cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
