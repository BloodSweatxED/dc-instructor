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


PROMOTED_SPRAIN = "sprain_strain_knee_or_shoulder_xray_negative"
WRIST_DRAFT = "wrist_sprain_xray_negative"
ALLOWED_V1_SITES = {
    "knee sprain xray negative",
    "shoulder sprain xray negative",
}
EXCLUDED_V1_SITES = {
    "elbow sprain xray negative",
    "foot sprain xray negative",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def assert_sprain_v1_boundary(manifest_item: dict) -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{PROMOTED_SPRAIN}.json")
    runtime = phenotype["runtime"]

    require(phenotype["status"] == "reviewed", "sprain/strain should be reviewed")
    require(phenotype["review"]["status"] == "reviewed", "sprain/strain review should be reviewed")
    require(runtime["mode"] == "reviewed_ontology_enabled", "sprain/strain should run ontology mode")
    require(manifest_item["status"] == "reviewed", "manifest should preserve sprain reviewed status")
    require(manifest_item["review_status"] == "reviewed", "manifest should preserve sprain review status")

    high_confidence_terms = set(runtime.get("high_confidence_terms", []))
    required_site_terms = {
        term
        for item in runtime.get("required_context", [])
        if item["id"] == "knee_or_shoulder_site_documented"
        for term in item.get("terms", [])
    }
    unsafe_modifiers = set(runtime.get("unsafe_modifiers", []))

    require(ALLOWED_V1_SITES.issubset(high_confidence_terms), "knee/shoulder should remain high-confidence reviewed sites")
    require(ALLOWED_V1_SITES.issubset(required_site_terms), "knee/shoulder should satisfy site context")
    require("wrist sprain xray negative" not in high_confidence_terms, "wrist should not be in shared reviewed v1")
    require(EXCLUDED_V1_SITES.isdisjoint(high_confidence_terms), "elbow/foot should not be high-confidence v1 sites")
    require(EXCLUDED_V1_SITES.isdisjoint(required_site_terms), "elbow/foot should not satisfy v1 site context")
    require("elbow_or_foot_site_pending_split" in unsafe_modifiers, "elbow/foot pending split blocker missing")


def assert_site_cases() -> None:
    for site in ALLOWED_V1_SITES:
        result = classify(site, f"{site}. X-ray performed and negative. Neurovascular exam intact.")
        require(result["phenotype_id"] == PROMOTED_SPRAIN, f"{site} should match reviewed sprain: {result}")
        require(result["fallback_reason"] is None, f"{site} should run reviewed ontology mode: {result}")
        require(result["confidence"] >= 0.86, f"{site} confidence should remain high: {result}")
        require(not result["exclusions"], f"{site} should not have exclusions: {result}")
        require(not result["missing_required_context"], f"{site} should not miss required context: {result}")

    for site in EXCLUDED_V1_SITES:
        result = classify(site, f"{site}. X-ray performed and negative. Neurovascular exam intact.")
        require(result["phenotype_id"] == PROMOTED_SPRAIN, f"{site} should still route to sprain for auditability: {result}")
        require(result["fallback_reason"] == "unsafe_modifier_present", f"{site} should be explicit site exclusion: {result}")
        require("elbow_or_foot_site_pending_split" in result["exclusions"], f"{site} missing split blocker: {result}")

    wrist_missing = classify(
        "wrist sprain xray negative",
        "Wrist sprain xray negative. X-ray performed and negative. Neurovascular exam intact.",
    )
    require(wrist_missing["phenotype_id"] == WRIST_DRAFT, f"wrist should route to wrist draft: {wrist_missing}")
    require(wrist_missing["fallback_reason"] == "required_runtime_context_missing", f"wrist should require no-scaphoid documentation: {wrist_missing}")
    require("no_scaphoid_tenderness_documented" in wrist_missing["missing_required_context"], f"wrist should miss scaphoid context: {wrist_missing}")


def assert_phase217_fixture() -> None:
    for case in json.loads((ROOT / "evals" / "phase217_sprain_site_stress_runtime_cases.json").read_text(encoding="utf-8")):
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] == case["expected_phenotype_id"], f"{case['id']} phenotype mismatch: {result}")
        require(result["fallback_reason"] == case["expected_fallback_reason"], f"{case['id']} fallback mismatch: {result}")
        for expected in case.get("expected_exclusions", []):
            require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
        for expected in case.get("expected_missing_required_context", []):
            require(
                expected in result["missing_required_context"],
                f"{case['id']} missing required context {expected}: {result}",
            )
        min_confidence = case.get("expected_min_confidence")
        if min_confidence is not None:
            require(result["confidence"] >= min_confidence, f"{case['id']} confidence too low: {result}")


def assert_gate_and_graph() -> None:
    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 0, f"active drafts should be cleared after wrist approval: {payload}")
    require(payload["active_draft_phenotypes"] == [], f"active draft list should be empty after wrist approval: {payload}")
    require(payload["phenotype_expansion_allowed"], "expansion should reopen after wrist approval")

    graph = read_json(ROOT / "graph" / "graph_seed.json")
    require(graph["node_count"] == len(graph["nodes"]), "graph node count drift")
    require(graph["edge_count"] == len(graph["edges"]), "graph edge count drift")
    require(graph["node_count"] == 2170, "unexpected graph node count after wrist revision")
    require(graph["edge_count"] == 3325, "unexpected graph edge count after wrist revision")


def assert_output_modifier_contract() -> None:
    output_panel = Path("src/components/OutputPanel.jsx").read_text(encoding="utf-8")
    generate_js = Path("netlify/functions/generate.js").read_text(encoding="utf-8")
    runtime_js = Path("netlify/functions/ontology-runtime.js").read_text(encoding="utf-8")
    require("generationMeta?.output_modifiers" in output_panel, "OutputPanel should still read output modifiers")
    require("Modifier review:" in output_panel, "OutputPanel should still display modifier review banner")
    require("ontology.output_modifiers || []" in generate_js, "generate.js should still pass output modifiers")
    require("outputModifierHits" in runtime_js, "Netlify runtime should still compute output modifiers")


def main() -> int:
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_by_id = {item["id"]: item for item in manifest["phenotypes"]}
    require(PROMOTED_SPRAIN in manifest_by_id, "sprain/strain missing from manifest")

    assert_sprain_v1_boundary(manifest_by_id[PROMOTED_SPRAIN])
    assert_site_cases()
    assert_phase217_fixture()
    assert_gate_and_graph()
    assert_output_modifier_contract()
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)

    print("phase251-301 sprain promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
