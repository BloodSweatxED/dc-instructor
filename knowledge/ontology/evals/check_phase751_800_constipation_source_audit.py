#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


AUDIT_PATH = ROOT / "evals" / "phase751_800_constipation_source_boundary_audit.md"
SOURCE_IDS = {
    "medlineplus.constipation_self_care",
    "niddk.constipation_adults",
    "medlineplus.intestinal_obstruction",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    for source_id in SOURCE_IDS:
        card = read_json(ROOT / "source_cards" / f"{source_id}.json")
        require(card["id"] == source_id, f"{source_id} source card id mismatch")
        require(card["source_type"] == "public_patient_education", f"{source_id} source type drifted")
        require(card["use_policy"] == "evidence_support", f"{source_id} use policy drifted")
        require(card.get("supports"), f"{source_id} should include support statements")

    audit = AUDIT_PATH.read_text(encoding="utf-8")
    for required in {
        "Do not open `constipation_uncomplicated` as a draft",
        "Hold. Do not draft or promote constipation yet.",
        "adult_constipation_reassuring_ed_assessment_no_obstruction_or_bleeding",
        "medication instructions entered by clinician only",
        "bowel obstruction",
        "blood in stool",
        "persistent vomiting",
    }:
        require(required in audit, f"missing audit decision phrase: {required}")

    require(
        not (ROOT / "phenotypes" / "constipation_uncomplicated.json").exists(),
        "constipation_uncomplicated should not be opened as a phenotype in phase 751-800",
    )

    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["phenotype_expansion_allowed"], "gate should remain open after source-only audit")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 0, "active draft queue should remain empty")

    print("phase751-800 constipation source audit checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
