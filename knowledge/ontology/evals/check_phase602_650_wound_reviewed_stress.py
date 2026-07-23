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


CASES_PATH = ROOT / "evals" / "phase602_650_wound_reviewed_stress_runtime_cases.json"
PHENOTYPE_ID = "skin_avulsion_or_abrasion_simple"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def output_modifier_ids(result: dict) -> set[str]:
    return {item["id"] for item in result.get("output_modifiers", [])}


def assert_case(case: dict) -> None:
    result = classify(case["condition"], case.get("ed_note", ""))
    require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
    for expected in case.get("expected_missing_required_context", []):
        require(expected in result.get("missing_required_context", []), f"{case['id']} missing context {expected}: {result}")
    for expected in case.get("expected_output_modifiers", []):
        require(expected in output_modifier_ids(result), f"{case['id']} missing output modifier {expected}: {result}")


def assert_reviewed_wound_contract() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json")
    output = assemble_discharge(PHENOTYPE_ID, "6").lower()
    output_modifiers = {item["id"] for item in phenotype["runtime"].get("output_modifiers", [])}
    unsafe_modifiers = set(phenotype["runtime"].get("unsafe_modifiers", []))

    require(phenotype["status"] == "reviewed", "skin avulsion/abrasion should remain reviewed")
    require(phenotype["review"]["status"] == "reviewed", "skin avulsion/abrasion review should remain reviewed")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "skin avulsion/abrasion should remain ontology enabled")
    require("today" not in output, "skin avulsion/abrasion output should not contain today")
    require("tetanus" not in output, "skin avulsion/abrasion static output should not include tetanus advice")
    require("topical antibiotic" not in output, "skin avulsion/abrasion static output should not include topical antibiotic advice")

    for modifier in {"diabetes_general_risk", "peripheral_vascular_disease", "anticoagulated", "delayed_wound_presentation"}:
        require(modifier in output_modifiers, f"{modifier} should remain an output modifier")
    for blocker in {"immunocompromised", "diabetic_foot", "bite_wound", "dirty_wound", "wound_infection_concern", "retained_foreign_body"}:
        require(blocker in unsafe_modifiers, f"{blocker} should remain a true blocker")


def main() -> int:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    for case in cases:
        assert_case(case)

    assert_reviewed_wound_contract()

    payload = gate_payload()
    active_ids = {
        item["phenotype_id"] if isinstance(item, dict) else item
        for item in payload["active_draft_phenotypes"]
    }
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(PHENOTYPE_ID not in active_ids, f"skin avulsion/abrasion should not be an active draft: {payload}")

    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)

    print("phase602-650 wound reviewed stress checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
