#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


PHENOTYPE_ID = "abdominal_pain_nonspecific_reassuring_workup"
PHENOTYPE_PATH = ROOT / "phenotypes" / f"{PHENOTYPE_ID}.json"
PACKET_PATH = ROOT / "review_sheets" / f"{PHENOTYPE_ID}_v1_review_packet.md"

REQUIRED_PACKET_TEXT = [
    "Approve as a narrow review candidate.",
    "We did not find an emergency cause that needed surgery or admission",
    "Return for recheck as your clinician instructed.",
    "pain going to the shoulder or back",
    "Medication lines are acceptable as passthrough-only",
    "Do not use it as a catch-all fallback for unmatched abdominal pain.",
]
DISALLOWED_PACKET_TEXT = [
    "Your ED evaluation was reassuring today",
    "new chest pain, trouble breathing",
    "primary care",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    phenotype = read_json(PHENOTYPE_PATH)
    packet = PACKET_PATH.read_text(encoding="utf-8")

    status = phenotype["status"]
    review_status = phenotype["review"]["status"]
    require(status in {"needs_review", "reviewed"}, f"{PHENOTYPE_ID} has unexpected status {status}")
    require(review_status in {"needs_review", "reviewed"}, f"{PHENOTYPE_ID} has unexpected review status {review_status}")
    if status == "reviewed" or review_status == "reviewed":
        required_context = phenotype.get("runtime", {}).get("required_context", [])
        require(
            any(item.get("id") == "clinician_directed_recheck_plan" for item in required_context),
            f"{PHENOTYPE_ID} must not be promoted without clinician-directed recheck runtime gate",
        )
    for text in REQUIRED_PACKET_TEXT:
        require(text in packet, f"phase25 packet missing required text: {text}")
    for text in DISALLOWED_PACKET_TEXT:
        require(text not in packet, f"phase25 packet still contains disallowed text: {text}")

    print("phase25 abdominal feedback checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
