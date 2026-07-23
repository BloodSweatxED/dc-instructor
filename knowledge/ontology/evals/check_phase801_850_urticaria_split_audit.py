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
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


PHENOTYPE_ID = "allergic_reaction_resolved_no_anaphylaxis"
AUDIT_PATH = ROOT / "evals" / "phase801_850_urticaria_split_audit.md"
CASES_PATH = ROOT / "evals" / "phase801_850_urticaria_split_runtime_cases.json"
SOURCE_ID = "medlineplus.hives"


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


def main() -> int:
    source = read_json(ROOT / "source_cards" / f"{SOURCE_ID}.json")
    require(source["id"] == SOURCE_ID, "hives source card id mismatch")
    require(source["source_type"] == "public_patient_education", "hives source card type drifted")
    require(source["use_policy"] == "evidence_support", "hives source card policy drifted")
    for phrase in {"urticaria", "Airway swelling", "trouble breathing"}:
        require(any(phrase in support for support in source["supports"]), f"hives source missing support phrase {phrase}")

    phenotype = read_json(ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json")
    require(SOURCE_ID in phenotype["source_card_ids"], "allergic reaction phenotype should include hives source support")
    require(phenotype["status"] == "reviewed", "allergic reaction phenotype should stay reviewed")
    require("hives" in phenotype["runtime"]["condition_terms"], "hives condition term should remain")
    require("urticaria" in phenotype["runtime"]["condition_terms"], "urticaria condition term should remain")
    require(not phenotype["runtime"].get("high_confidence_terms"), "bare hives should not be promoted to high confidence")

    audit = AUDIT_PATH.read_text(encoding="utf-8")
    for required in {
        "Do not open a separate `urticaria_uncomplicated` draft",
        "Bare hives and bare urticaria remain low-confidence generator fallback",
        "acute_urticaria_reassuring_ed_assessment_no_anaphylaxis_or_angioedema",
        "medication instructions entered by clinician only",
        "Hold. Do not draft or promote a separate urticaria phenotype yet.",
    }:
        require(required in audit, f"missing audit decision phrase: {required}")

    require(
        not (ROOT / "phenotypes" / "urticaria_uncomplicated.json").exists(),
        "urticaria_uncomplicated should not be opened as a phenotype in phase 801-850",
    )

    for case in json.loads(CASES_PATH.read_text(encoding="utf-8")):
        assert_case(case)

    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["phenotype_expansion_allowed"], "gate should remain open after urticaria source audit")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 0, "active draft queue should remain empty")

    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)

    print("phase801-850 urticaria split audit checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
