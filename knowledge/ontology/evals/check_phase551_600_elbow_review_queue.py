#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "elbow_sprain_acute_traumatic_xray_negative"
REVIEWED_OVERUSE = "elbow_sprain_overuse_xray_negative"
CASES_PATH = ROOT / "evals" / "phase551_600_elbow_review_queue_runtime_cases.json"
REVIEW_PACKET_PATH = ROOT / "review_sheets" / f"{TARGET}_v1_review_packet.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_cases() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    require(len(cases) == 10, "Phase 551-600 elbow review-queue fixture should keep 10 cases")
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        if case["expected_fallback_reason"] in {None, "phenotype_not_clinician_reviewed"}:
            require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
        for expected in case.get("expected_exclusions", []):
            require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
        for expected in case.get("expected_missing_required_context", []):
            require(
                expected in result["missing_required_context"],
                f"{case['id']} missing required context {expected}: {result}",
            )


def assert_reviewed_gate() -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    active_manifest = next(row for row in manifest["phenotypes"] if row["id"] == TARGET)
    overuse_manifest = next(row for row in manifest["phenotypes"] if row["id"] == REVIEWED_OVERUSE)
    payload = gate_payload()
    active_ids = {
        item["phenotype_id"] if isinstance(item, dict) else item
        for item in payload["active_draft_phenotypes"]
    }

    require(phenotype["status"] == "reviewed", "acute elbow should be reviewed after clinician approval")
    require(phenotype["review"]["status"] == "reviewed", "acute elbow review should be reviewed after clinician approval")
    require(phenotype["review"]["last_reviewed"] == "2026-06-05", "acute elbow review date should reflect clinician approval")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "acute elbow runtime should be reviewed ontology")
    require(active_manifest["status"] == "reviewed", "manifest should mark acute elbow reviewed")
    require(active_manifest["review_status"] == "reviewed", "manifest should mark acute elbow review reviewed")
    require(overuse_manifest["status"] == "reviewed", "reviewed elbow overuse route should stay reviewed")
    require(overuse_manifest["review_status"] == "reviewed", "reviewed elbow overuse review status should stay reviewed")

    require(
        TARGET not in active_ids,
        f"acute elbow should not remain an active draft after promotion: {payload}",
    )
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")

    packet = REVIEW_PACKET_PATH.read_text(encoding="utf-8")
    require("Production status: enabled with runtime modifier gates." in packet, "acute elbow review packet should mark production enabled")
    require("forearm rotation is limited" in packet, "acute elbow review packet should include rotation follow-up trigger")


def assert_netlify_parity() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    assert_cases()
    assert_reviewed_gate()
    assert_netlify_parity()
    print("phase551-600 elbow reviewed promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
