#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_sinusitis_supportive_care"


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
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next((item for item in manifest["phenotypes"] if item["id"] == TARGET), None)
    packet = (ROOT / "review_sheets" / f"{TARGET}_v1_review_packet.md").read_text(encoding="utf-8")
    payload = gate_payload()

    require(phenotype["status"] == "reviewed", "sinusitis must be reviewed")
    require(phenotype["review"]["status"] == "reviewed", "sinusitis review status must be reviewed")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "sinusitis must be runtime enabled")
    require(manifest_item is not None, "manifest missing sinusitis")
    require(manifest_item["status"] == "reviewed", "manifest sinusitis status must be reviewed")
    for broad in ["congestion", "facial pain", "cold symptoms"]:
        require(broad not in set(manifest_item["condition_terms"]), f"broad term must not be standalone: {broad}")
    for text in [
        "Do not say antibiotics are never needed.",
        "Do not use broad congestion, facial pain, or cold symptoms as standalone runtime terms.",
        "Patient-Facing Output",
    ]:
        require(text in packet, f"sinusitis review packet missing: {text}")

    cases = []
    for filename in [
        "phase38_acute_sinusitis_runtime_cases.json",
        "phase39_acute_sinusitis_stress_runtime_cases.json",
        "phase43_acute_sinusitis_post_promotion_runtime_cases.json",
    ]:
        cases.extend(json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")))
    for case in cases:
        assert_case(case)

    require(payload["reviewed_runtime_clean"], "reviewed runtime must remain clean")
    active_ids = {row["phenotype_id"] for row in payload["active_draft_phenotypes"]}
    require(TARGET not in active_ids, "sinusitis should not remain an active draft after promotion")

    print("phase41-45 acute sinusitis promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
