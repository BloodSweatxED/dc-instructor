#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError  # noqa: E402


TARGET = "acute_bronchitis_no_pneumonia"
PHASE20_CASES = {
    "phase20_bronchitis_contradictory_note_blocks",
    "phase20_bronchitis_vague_chief_complaint_fallback",
}
PHASE32_CASE_PATH = ROOT / "evals" / "phase32_acute_bronchitis_runtime_cases.json"
PHASE32_DOC_PATH = ROOT / "evals" / "phase32_acute_bronchitis_stress.md"


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
    phase20_cases = json.loads((ROOT / "evals" / "phase20_runtime_cases.json").read_text(encoding="utf-8"))
    phase20_ids = {case["id"] for case in phase20_cases}
    require(PHASE20_CASES <= phase20_ids, "phase20 bronchitis contradictory and vague cases are required")

    phase32_cases = json.loads(PHASE32_CASE_PATH.read_text(encoding="utf-8"))
    require(len(phase32_cases) == 7, "phase32 should keep seven bronchitis stress cases")
    for case in [case for case in phase20_cases if case["id"] in PHASE20_CASES]:
        assert_case(case)
    for case in phase32_cases:
        assert_case(case)

    doc = PHASE32_DOC_PATH.read_text(encoding="utf-8")
    for text in ["Hemoptysis blocker.", "Frail elderly blocker.", "Phase 20 contradictory-note case for bronchitis."]:
        require(text in doc, f"phase32 doc missing {text}")

    print("phase32 acute bronchitis stress checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
