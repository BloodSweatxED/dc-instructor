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


RETIRED = {
    "conjunctivitis_uncomplicated_no_contact_lens": ["eye redness", "red eye"],
    "otitis_externa_no_mastoiditis": ["ear pain", "ear drainage"],
    "epistaxis_resolved_no_posterior_bleed": ["bleeding", "nasal bleeding"],
    "migraine_improved_discharge": ["headache", "severe headache"],
}


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
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_items = {item["id"]: item for item in manifest["phenotypes"]}
    payload = gate_payload()

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    for phenotype_id, broad_terms in RETIRED.items():
        phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
        manifest_item = manifest_items[phenotype_id]
        require(phenotype["status"] == "retired", f"{phenotype_id} should be retired")
        require(phenotype["review"]["status"] == "retired", f"{phenotype_id} review status should be retired")
        require(
            phenotype["runtime"]["mode"] == "retired_product_layer_fallback_only",
            f"{phenotype_id} should be product-layer fallback only",
        )
        require(manifest_item["status"] == "retired", f"{phenotype_id} manifest status should be retired")
        require(manifest_item["review_status"] == "retired", f"{phenotype_id} manifest review status should be retired")
        terms = set(manifest_item["condition_terms"])
        for broad in broad_terms:
            require(broad not in terms, f"{phenotype_id} broad term must not be standalone: {broad}")

    for filename in [
        "phase47_conjunctivitis_runtime_cases.json",
        "phase52_conjunctivitis_boundary_runtime_cases.json",
        "phase62_otitis_externa_boundary_runtime_cases.json",
        "phase68_epistaxis_runtime_cases.json",
        "phase69_epistaxis_stress_runtime_cases.json",
        "phase74_migraine_runtime_cases.json",
        "phase75_migraine_stress_runtime_cases.json",
        "phase77_migraine_boundary_runtime_cases.json",
    ]:
        for case in json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")):
            assert_case(case)

    required_docs = {
        "phase81_migraine_review_packet_refined.md": "Patient-facing output:",
        "phase82_migraine_retirement.md": "retired_product_layer_fallback_only",
        "phase83_expansion_gate_after_migraine_retirement.md": "Phenotype expansion allowed: true.",
        "phase81_150_stabilization_run.md": "Phase ledger:",
        "phase150_handoff.md": "Completed through Phase 150.",
    }
    for doc_name, required_text in required_docs.items():
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    active_ids = [row["phenotype_id"] for row in payload["active_draft_phenotypes"]]
    require(
        all(phenotype_id not in RETIRED for phenotype_id in active_ids),
        f"retired Phase 81-150 phenotypes should not remain active drafts: {active_ids}",
    )
    if active_ids:
        require(not payload["phenotype_expansion_allowed"], f"later active drafts should close expansion: {active_ids}")
    else:
        require(payload["phenotype_expansion_allowed"], "expansion should be allowed when no active drafts remain")

    print("phase81-150 stabilization checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
