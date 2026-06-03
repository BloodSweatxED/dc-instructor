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


AOM = "acute_otitis_media_uncomplicated"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_case(case: dict) -> None:
    result = classify(case["condition"], case.get("ed_note", ""))
    require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
    for expected in case.get("expected_missing_required_context", []):
        require(expected in result.get("missing_required_context", []), f"{case['id']} missing context {expected}: {result}")


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{AOM}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = {item["id"]: item for item in manifest["phenotypes"]}[AOM]
    payload = gate_payload()

    require(phenotype["status"] == "needs_review", "AOM should remain draft/needs_review")
    require(phenotype["review"]["status"] == "needs_review", "AOM review should remain needs_review")
    require(phenotype["runtime"]["mode"] == "draft_only_until_reviewed", "AOM should not be ontology-enabled")
    require(phenotype["source_audit"]["source_supported"], "AOM should have source support")
    require(not phenotype["source_audit"]["source_needed"], "AOM should not have a draft source gap")
    require(set(phenotype["source_card_ids"]) == {"cdc.ear_infection", "medlineplus.ear_infections"}, "AOM source cards mismatch")

    for broad in ["ear pain", "ear infection"]:
        require(broad not in set(manifest_item["condition_terms"]), f"AOM broad term must not be standalone: {broad}")

    for filename in [
        "phase156_acute_otitis_media_runtime_cases.json",
        "phase157_acute_otitis_media_stress_runtime_cases.json",
    ]:
        for case in json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")):
            assert_case(case)

    required_docs = {
        "phase152_candidate_ranking_after_phase151.md": "Recommendation: build `acute_otitis_media_uncomplicated` next as draft only.",
        "phase153_acute_otitis_media_source_plan.md": "Source limitations:",
        "phase155_acute_otitis_media_draft.md": "Patient-facing output:",
        "phase158_acute_otitis_media_review_packet.md": "Should this be promoted as a narrow reviewed ontology phenotype, revised, or retired",
        "phase159_acute_otitis_media_review_decision.md": "Decision: keep draft. Do not promote.",
        "phase160_handoff.md": "Completed through Phase 160.",
    }
    for doc_name, required_text in required_docs.items():
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    active_ids = [row["phenotype_id"] for row in payload["active_draft_phenotypes"]]
    require(active_ids == [AOM], f"AOM should be the only active draft: {active_ids}")
    require(not payload["phenotype_expansion_allowed"], "expansion should close while AOM is active draft")

    print("phase152-160 cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
