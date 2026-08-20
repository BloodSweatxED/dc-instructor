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


OTITIS = "otitis_externa_no_mastoiditis"
EPISTAXIS = "epistaxis_resolved_no_posterior_bleed"
MIGRAINE = "migraine_improved_discharge"


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
    otitis = read_json(ROOT / "phenotypes" / f"{OTITIS}.json")
    epistaxis = read_json(ROOT / "phenotypes" / f"{EPISTAXIS}.json")
    migraine = read_json(ROOT / "phenotypes" / f"{MIGRAINE}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_items = {item["id"]: item for item in manifest["phenotypes"]}
    payload = gate_payload()

    require(otitis["status"] == "retired", "otitis should be retired by Phase 64")
    require(otitis["runtime"]["mode"] == "retired_product_layer_fallback_only", "otitis should be product-layer fallback only")
    require(epistaxis["status"] == "retired", "epistaxis should be retired by Phase 70")
    require(epistaxis["runtime"]["mode"] == "retired_product_layer_fallback_only", "epistaxis should be product-layer fallback only")
    require(migraine["status"] in {"needs_review", "retired"}, "migraine should remain unreviewed or retired")
    require(migraine["review"]["status"] in {"needs_review", "retired"}, "migraine review should remain unreviewed or retired")
    require(
        migraine["runtime"]["mode"] in {"draft_only_until_reviewed", "retired_product_layer_fallback_only"},
        "migraine should remain out of ontology mode",
    )

    for phenotype_id, broad_terms in {
        OTITIS: ["ear pain", "ear drainage"],
        EPISTAXIS: ["bleeding", "nasal bleeding"],
        MIGRAINE: ["headache", "severe headache"],
    }.items():
        terms = set(manifest_items[phenotype_id]["condition_terms"])
        for broad in broad_terms:
            require(broad not in terms, f"{phenotype_id} broad term must not be standalone: {broad}")

    for filename in [
        "phase58_otitis_externa_runtime_cases.json",
        "phase59_otitis_externa_stress_runtime_cases.json",
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
        "phase61_otitis_externa_review_packet.md": "Patient-facing output:",
        "phase64_otitis_externa_retirement.md": "retired_product_layer_fallback_only",
        "phase67_epistaxis_source_plan.md": "Source limitations:",
        "phase70_epistaxis_review_decision.md": "Decision: keep retired/product-layer fallback.",
        "phase73_migraine_source_plan.md": "Source limitations:",
        "phase74_migraine_draft.md": "Patient-facing output:",
        "phase78_migraine_review_decision.md": "Decision: keep draft. Do not promote.",
        "phase80_handoff.md": "Completed through Phase 80.",
    }
    for doc_name, required_text in required_docs.items():
        text = (ROOT / "evals" / doc_name).read_text(encoding="utf-8")
        require(required_text in text, f"{doc_name} missing required text")

    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    active_ids = [row["phenotype_id"] for row in payload["active_draft_phenotypes"]]
    require(MIGRAINE not in active_ids, f"migraine should not remain active after Phase 82: {active_ids}")
    if active_ids:
        require(not payload["phenotype_expansion_allowed"], f"expansion should close while active drafts exist: {active_ids}")
    else:
        require(payload["phenotype_expansion_allowed"], "expansion should reopen after all active drafts are retired or reviewed")
    require(payload["draft_source_gap_count"] == 0, "migraine draft should not introduce source gaps")

    print("phase61-80 cycle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
