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


PROMOTED = {
    "skin_avulsion_or_abrasion_simple": {
        "output_modifiers": {
            "diabetes_general_risk",
            "peripheral_vascular_disease",
            "anticoagulated",
            "delayed_wound_presentation",
        },
        "true_blockers": {
            "immunocompromised",
            "bite_wound",
            "dirty_wound",
            "wound_infection_concern",
            "laceration_repair_needed",
            "retained_foreign_body",
            "diabetic_foot",
        },
    },
    "acute_otitis_media_uncomplicated": {
        "output_modifiers": {
            "elderly_frail",
            "diabetes_general_risk",
        },
        "true_blockers": {
            "watchful_waiting_follow_up_unreliable",
            "immunocompromised",
            "mastoiditis_or_deep_ear_infection_concern",
            "meningitis_or_cns_infection_concern",
            "lateral_sinus_thrombosis_concern",
            "tympanic_membrane_perforation_or_tube",
            "acute_hearing_loss",
            "facial_weakness_or_neurologic_ear_sign",
            "pediatric_pathway",
            "recurrent_or_chronic_ear_infection",
            "unstable_vitals",
            "specialist_directed_ent_plan",
        },
    },
    "suture_removal_or_wound_check_no_infection": {
        "output_modifiers": {
            "diabetes_general_risk",
            "peripheral_vascular_disease",
            "anticoagulated",
        },
        "true_blockers": {
            "immunocompromised",
            "diabetic_foot",
            "wound_infection_concern",
            "wound_dehiscence",
            "high_risk_wound_location",
            "retained_foreign_body",
            "dirty_wound",
            "bite_wound",
            "poor_follow_up",
            "pediatric_pathway",
            "specialist_directed_wound_plan",
        },
    },
    "sprain_strain_knee_or_shoulder_xray_negative": {
        "output_modifiers": set(),
        "true_blockers": {
            "ankle_sprain_pathway",
            "wrist_site_pending_split",
            "no_xray_performed",
            "fracture_seen",
            "dislocation",
            "open_wound",
            "open_fracture",
            "high_energy_trauma",
            "crush_injury",
            "neurovascular_compromise",
            "tendon_or_ligament_rupture_concern",
            "acute_hemarthrosis_or_large_effusion",
            "compartment_syndrome_concern",
            "septic_joint_or_infection_concern",
            "unable_to_bear_weight_lower_extremity",
            "elbow_or_foot_site_pending_split",
            "pediatric_growth_plate_pathway",
            "elderly_osteoporotic_high_risk_msk",
            "specialist_directed_orthopedic_plan",
        },
    },
}

PROMOTED_SPRAIN = "sprain_strain_knee_or_shoulder_xray_negative"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def modifier_ids(items: list[dict]) -> set[str]:
    return {item["id"] for item in items}


def assert_manifest_parity(phenotype_id: str, phenotype: dict, manifest_item: dict) -> None:
    require(manifest_item["status"] == phenotype["status"], f"{phenotype_id} manifest status drift")
    require(manifest_item["review_status"] == phenotype["review"]["status"], f"{phenotype_id} manifest review drift")
    require(
        modifier_ids(manifest_item.get("output_modifiers", [])) == modifier_ids(phenotype["runtime"].get("output_modifiers", [])),
        f"{phenotype_id} manifest output modifier drift",
    )
    require(
        set(manifest_item.get("unsafe_modifiers", [])) == set(phenotype["runtime"].get("unsafe_modifiers", [])),
        f"{phenotype_id} manifest blocker drift",
    )


def assert_promoted_phenotypes(manifest_by_id: dict[str, dict]) -> None:
    for phenotype_id, expected in PROMOTED.items():
        phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
        require(phenotype["status"] == "reviewed", f"{phenotype_id} should be reviewed")
        require(phenotype["review"]["status"] == "reviewed", f"{phenotype_id} review should be reviewed")
        require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", f"{phenotype_id} runtime should be enabled")
        require(
            modifier_ids(phenotype["runtime"].get("output_modifiers", [])) == expected["output_modifiers"],
            f"{phenotype_id} output modifier disposition drift",
        )
        require(
            expected["true_blockers"].issubset(set(phenotype["runtime"].get("unsafe_modifiers", []))),
            f"{phenotype_id} missing true blockers",
        )
        assert_manifest_parity(phenotype_id, phenotype, manifest_by_id[phenotype_id])


def assert_suture_runtime_gate() -> None:
    phenotype = read_json(ROOT / "phenotypes" / "suture_removal_or_wound_check_no_infection.json")
    required_ids = {item["id"] for item in phenotype["runtime"].get("required_context", [])}
    require(
        "clinician_documented_expected_healing_or_clearance" in required_ids,
        "suture wound check should require expected healing or explicit clearance",
    )
    require(
        "clinician_entered_wound_follow_up_plan" in required_ids,
        "suture wound check should require clinician-entered wound follow-up plan",
    )
    result = classify(
        "suture removal wound check",
        "ready for suture removal. no wound infection concern.",
    )
    require(
        result["fallback_reason"] == "required_runtime_context_missing",
        f"wound readiness alone should not pass runtime: {result}",
    )


def assert_sprain_promotion(manifest_by_id: dict[str, dict]) -> None:
    phenotype = read_json(ROOT / "phenotypes" / f"{PROMOTED_SPRAIN}.json")
    require(phenotype["status"] == "reviewed", "sprain/strain should be reviewed")
    require(phenotype["review"]["status"] == "reviewed", "sprain/strain review should be reviewed")
    require(phenotype["runtime"]["mode"] == "reviewed_ontology_enabled", "sprain/strain should be ontology enabled")
    assert_manifest_parity(PROMOTED_SPRAIN, phenotype, manifest_by_id[PROMOTED_SPRAIN])

    stress_cases = read_json(ROOT / "evals" / "phase217_sprain_site_stress_runtime_cases.json")
    excluded_site_ids = {
        "phase217_elbow_clean_v1_site_exclusion",
        "phase217_foot_clean_v1_site_exclusion",
    }
    for case in stress_cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        if case["id"] in excluded_site_ids:
            require(result["phenotype_id"] == PROMOTED_SPRAIN, f"{case['id']} should still route to reviewed sprain for auditability")
            require(result["fallback_reason"] == "unsafe_modifier_present", f"{case['id']} hold reason drift: {result}")
            require(
                "elbow_or_foot_site_pending_split" in result["exclusions"],
                f"{case['id']} should be explicitly excluded pending site split: {result}",
            )
        elif case["id"] in {
            "phase217_knee_clean_reviewed_ontology",
            "phase217_shoulder_clean_reviewed_ontology",
        }:
            require(result["phenotype_id"] == PROMOTED_SPRAIN, f"{case['id']} should match reviewed sprain")
            require(result["fallback_reason"] is None, f"{case['id']} should run ontology mode: {result}")


def assert_output_modifier_delivery() -> None:
    output_panel = Path("src/components/OutputPanel.jsx").read_text(encoding="utf-8")
    generate_js = Path("netlify/functions/generate.js").read_text(encoding="utf-8")
    runtime_js = Path("netlify/functions/ontology-runtime.js").read_text(encoding="utf-8")
    require("generationMeta?.output_modifiers" in output_panel, "OutputPanel should read output modifiers")
    require("Modifier review:" in output_panel, "OutputPanel should display modifier review banner")
    require("ontology.output_modifiers || []" in generate_js, "generate.js should pass output modifiers in metadata")
    require("outputModifierHits" in runtime_js, "Netlify runtime should compute output modifiers")


def assert_graph_and_gate() -> None:
    graph = read_json(ROOT / "graph" / "graph_seed.json")
    require(graph["node_count"] == len(graph["nodes"]), "graph node count drift")
    require(graph["edge_count"] == len(graph["edges"]), "graph edge count drift")
    require(graph["node_count"] >= 2133, "graph should include Phase 222 promoted phenotype content")
    require(graph["edge_count"] >= 3212, "graph should include Phase 222 promoted phenotype edges")

    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime should remain clean")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should remain zero")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should remain zero")
    require(payload["active_draft_phenotype_count"] == 0, f"active draft count drift after wrist approval: {payload}")
    require(payload["active_draft_phenotypes"] == [], f"active draft list should be empty after wrist approval: {payload}")
    require(payload["phenotype_expansion_allowed"], "expansion should reopen after wrist approval")


def assert_netlify_runtime_smoke() -> None:
    subprocess.run(["node", "knowledge/ontology/evals/run_netlify_runtime_smoke.mjs"], check=True)


def main() -> int:
    decision = ROOT / "evals" / "phase222_promotion_decision.md"
    require(decision.exists(), "Phase 222 promotion decision is missing")
    require("Output modifiers are returned in ontology metadata" in decision.read_text(encoding="utf-8"), "modifier delivery decision missing")

    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_by_id = {item["id"]: item for item in manifest["phenotypes"]}

    assert_promoted_phenotypes(manifest_by_id)
    assert_suture_runtime_gate()
    assert_sprain_promotion(manifest_by_id)
    assert_output_modifier_delivery()
    assert_graph_and_gate()
    assert_netlify_runtime_smoke()

    print("phase222-250 promotion release checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
