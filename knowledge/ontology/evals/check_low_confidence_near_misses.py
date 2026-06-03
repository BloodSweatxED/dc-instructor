#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, OntologyError  # noqa: E402


RESULTS_PATH = ROOT / "evals" / "runtime_case_results.json"

ALLOWED_LOW_CONFIDENCE = {
    "phase14_asthma_vague_wheeze_fallback": "symptom-only wheezing remains near asthma but below ontology threshold",
    "phase14_asthma_near_miss_copd_fallback": "COPD wheezing may share asthma terms but must not enter ontology mode",
    "phase14_vague_rash_fallback": "rash with allergy language remains near allergy but below ontology threshold",
    "phase14_low_confidence_lung_infection": "possible lung infection remains near pneumonia but lacks discharge phenotype",
    "phase14_low_confidence_hit_head": "hit-head triage language remains near minor head injury but lacks final diagnosis",
    "phase14_low_confidence_kidney_stone": "possible stone language remains near renal colic but lacks final diagnosis",
    "phase20_asthma_vague_chief_complaint_fallback": "symptom-only wheezing remains near asthma but below ontology threshold",
    "phase20_concussion_vague_chief_complaint_fallback": "chief complaint names concussion but lacks red-flag and imaging review",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    results = read_json(RESULTS_PATH)
    low_confidence = {
        item["case_id"]: item
        for item in results
        if item.get("result", {}).get("fallback_reason") == "low_confidence"
    }
    unexpected = sorted(set(low_confidence) - set(ALLOWED_LOW_CONFIDENCE))
    missing = sorted(set(ALLOWED_LOW_CONFIDENCE) - set(low_confidence))

    if unexpected:
        rows = ", ".join(unexpected)
        raise OntologyError(f"unexpected low-confidence near-miss cases: {rows}")
    if missing:
        rows = ", ".join(missing)
        raise OntologyError(f"approved low-confidence cases no longer present: {rows}")

    print(f"low-confidence near-miss checks passed: {len(low_confidence)} approved cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
