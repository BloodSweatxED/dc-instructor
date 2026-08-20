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


CONJUNCTIVITIS = "conjunctivitis_uncomplicated_no_contact_lens"
OTITIS = "otitis_externa_no_mastoiditis"


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
    conjunctivitis = read_json(ROOT / "phenotypes" / f"{CONJUNCTIVITIS}.json")
    otitis = read_json(ROOT / "phenotypes" / f"{OTITIS}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_items = {item["id"]: item for item in manifest["phenotypes"]}
    payload = gate_payload()

    require(conjunctivitis["status"] == "retired", "conjunctivitis should be retired")
    require(conjunctivitis["review"]["status"] == "retired", "conjunctivitis review status should be retired")
    require(conjunctivitis["runtime"]["mode"] == "retired_product_layer_fallback_only", "conjunctivitis should be product-layer fallback only")
    for blocker in [
        "chemical_eye_exposure",
        "corneal_ulcer_or_keratitis_concern",
        "acute_glaucoma_mimic",
    ]:
        require(blocker in conjunctivitis["runtime"]["unsafe_modifiers"], f"conjunctivitis missing blocker {blocker}")

    require(otitis["status"] in {"needs_review", "retired"}, "otitis externa should remain unreviewed or retired")
    require(otitis["review"]["status"] in {"needs_review", "retired"}, "otitis externa review status should remain unreviewed or retired")
    require(
        otitis["runtime"]["mode"] in {"draft_only_until_reviewed", "retired_product_layer_fallback_only"},
        "otitis externa should remain out of ontology mode",
    )
    require(set(otitis["source_card_ids"]) == {"cdc.swimmers_ear", "medlineplus.swimmers_ear"}, "otitis source cards changed")
    for broad in ["ear pain", "ear drainage"]:
        require(broad not in set(manifest_items[OTITIS]["condition_terms"]), f"broad otitis term must not be standalone: {broad}")

    for filename in [
        "phase47_conjunctivitis_runtime_cases.json",
        "phase48_conjunctivitis_stress_runtime_cases.json",
        "phase52_conjunctivitis_boundary_runtime_cases.json",
        "phase58_otitis_externa_runtime_cases.json",
        "phase59_otitis_externa_stress_runtime_cases.json",
    ]:
        for case in json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8")):
            assert_case(case)

    required_docs = {
        "phase51_conjunctivitis_review_packet.md": "Patient-facing output:",
        "phase54_conjunctivitis_retirement.md": "retired_product_layer_fallback_only",
        "phase57_otitis_externa_source_plan.md": "Source limitations:",
        "phase58_otitis_externa_draft.md": "Patient-facing output:",
        "phase60_review_decision.md": "Otitis externa decision: keep draft.",
        "phase60_handoff.md": "Completed through Phase 60.",
    }
    for doc_name, required_text in required_docs.items():
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    active_ids = [row["phenotype_id"] for row in payload["active_draft_phenotypes"]]
    require(OTITIS not in active_ids, f"otitis should not remain active after Phase 64: {active_ids}")
    if active_ids:
        require(not payload["phenotype_expansion_allowed"], f"expansion should close while active drafts exist: {active_ids}")
    else:
        require(payload["phenotype_expansion_allowed"], "expansion should reopen after all active drafts are retired or reviewed")
    require(payload["draft_source_gap_count"] == 0, "otitis draft should not introduce source gaps")

    print("phase51-60 cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
