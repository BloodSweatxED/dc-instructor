#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


PHENOTYPE_ID = "abdominal_pain_nonspecific_reassuring_workup"
PACKET_PATH = ROOT / "review_sheets" / f"{PHENOTYPE_ID}_v1_review_packet.md"
PHENOTYPE_PATH = ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json"

REQUIRED_TEXT = [
    "Clinical status: needs_clinician_review_for_limited_abdominal_pain_recheck_use.",
    "Production status: blocked until clinician review.",
    "Approve as a narrow review candidate.",
    "Patient-Facing Output",
    "Clinician Review Answers",
    "phase23_abdominal_recheck_draft_fallback",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    require(PACKET_PATH.exists(), f"missing review packet: {PACKET_PATH}")
    packet = PACKET_PATH.read_text(encoding="utf-8")
    phenotype = read_json(PHENOTYPE_PATH)

    require(phenotype["status"] in {"draft", "needs_review"}, f"{PHENOTYPE_ID} must not be reviewed yet")
    require(phenotype["review"]["status"] in {"draft", "needs_review"}, f"{PHENOTYPE_ID} review must not be reviewed yet")
    for text in REQUIRED_TEXT:
        require(text in packet, f"review packet missing required text: {text}")

    print("phase24 abdominal review packet checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
