#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_bronchitis_no_pneumonia"
REQUIRED_SOURCE_CARDS = [
    "cdc.acute_bronchitis",
    "medlineplus.acute_bronchitis",
    "cdc.antibiotic_use_adult_outpatient",
]
REQUIRED_PLAN_TEXT = [
    TARGET,
    "Hypoxia.",
    "Respiratory distress.",
    "Pneumonia, infiltrate, consolidation",
    "Do not give medication names, doses, schedules, or durations",
    "vague cough no-match",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    ranking = (ROOT / "evals" / "phase29_candidate_ranking.md").read_text(encoding="utf-8")
    plan = (ROOT / "evals" / "phase30_acute_bronchitis_source_plan.md").read_text(encoding="utf-8")

    require(f"Recommendation: build `{TARGET}` next." in ranking, "phase29 ranking must recommend acute bronchitis")
    for source_id in REQUIRED_SOURCE_CARDS:
        path = ROOT / "source_cards" / f"{source_id}.json"
        require(path.exists(), f"missing source card {source_id}")
        card = read_json(path)
        require(card["id"] == source_id, f"source card ID mismatch for {source_id}")
        require(card.get("url"), f"source card {source_id} missing URL")
        require(source_id in plan, f"phase30 plan missing source {source_id}")
    for text in REQUIRED_PLAN_TEXT:
        require(text in plan, f"phase30 plan missing required text: {text}")

    print("phase29-30 candidate plan checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
