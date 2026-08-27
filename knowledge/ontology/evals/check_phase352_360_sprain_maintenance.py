#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, assemble_discharge, read_json  # noqa: E402


PROMOTED_SPRAIN = "sprain_strain_knee_or_shoulder_xray_negative"
WRIST_PHENOTYPE = "wrist_sprain_xray_negative"
RETIRED_BROAD = "sprain_strain_non_ankle_xray_negative"
FOOT_PHENOTYPE = "foot_sprain_xray_negative"
ACUTE_ELBOW_PHENOTYPE = "elbow_sprain_acute_traumatic_xray_negative"
ALLOWED_LATER_DRAFTS = {"elbow_sprain_overuse_xray_negative"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_knee_shoulder_text() -> None:
    assembled = assemble_discharge(PROMOTED_SPRAIN, "6")
    review_sheet = (ROOT / "review_sheets" / f"{PROMOTED_SPRAIN}.md").read_text(encoding="utf-8")

    for text in (assembled, review_sheet):
        lowered = text.lower()
        require(
            "symptoms that get worse instead of better" not in lowered,
            "knee/shoulder return precaution should not keep weak worsening tail",
        )
        require(
            "fever, spreading redness or warmth, pus, or severe pain with movement" in lowered,
            "knee/shoulder return precaution should use concrete infection language",
        )


def assert_elbow_routes_to_active_draft_and_foot_reviewed() -> None:
    elbow = classify(
        "elbow sprain xray negative",
        "Elbow sprain xray negative. X-ray performed and negative. Neurovascular exam intact.",
    )
    require(
        elbow["phenotype_id"] == ACUTE_ELBOW_PHENOTYPE,
        f"acute traumatic elbow should route to acute elbow phenotype: {elbow}",
    )
    require(
        elbow["fallback_reason"] == "required_runtime_context_missing",
        f"incomplete acute traumatic elbow should not produce reviewed ontology output: {elbow}",
    )
    require(
        "adult_acute_traumatic_elbow_sprain_diagnosis" in elbow["missing_required_context"],
        f"incomplete acute traumatic elbow should require runtime context: {elbow}",
    )

    foot = classify(
        "foot sprain xray negative",
        "Foot sprain xray negative. X-ray performed and negative. Neurovascular exam intact.",
    )
    require(foot["phenotype_id"] == FOOT_PHENOTYPE, f"foot should route to reviewed foot phenotype: {foot}")
    require(foot["fallback_reason"] is None, f"foot should produce reviewed ontology output: {foot}")


def assert_gate_open() -> None:
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    by_id = {item["id"]: item for item in manifest["phenotypes"]}
    require(by_id[PROMOTED_SPRAIN]["status"] == "reviewed", "knee/shoulder sprain should stay reviewed")
    require(by_id[WRIST_PHENOTYPE]["status"] == "reviewed", "wrist sprain should stay reviewed")
    require(by_id[FOOT_PHENOTYPE]["status"] == "reviewed", "foot sprain should stay reviewed")
    require(by_id[ACUTE_ELBOW_PHENOTYPE]["status"] == "reviewed", "acute elbow sprain should stay reviewed")
    require(by_id[RETIRED_BROAD]["status"] == "retired", "broad sprain should stay retired")

    active_drafts = [
        item["id"]
        for item in manifest["phenotypes"]
        if item["status"] == "draft" and item["review_status"] not in {"retired", "reviewed"}
    ]
    unexpected = sorted(set(active_drafts) - ALLOWED_LATER_DRAFTS)
    require(unexpected == [], f"unexpected active drafts after sprain maintenance: {active_drafts}")


def main() -> int:
    assert_knee_shoulder_text()
    assert_elbow_routes_to_active_draft_and_foot_reviewed()
    assert_gate_open()
    print("phase352-360 sprain maintenance checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
