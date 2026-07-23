#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_bronchitis_no_pneumonia"
REQUIRED_BLOCKERS = {
    "hypoxia",
    "respiratory_distress",
    "pneumonia",
    "focal_lung_findings_or_infiltrate",
    "copd_or_asthma_exacerbation_pathway",
    "immunocompromised",
    "elderly_frail",
    "hemoptysis",
    "cardiac_or_pe_chest_pain_concern",
    "sepsis",
    "unstable_vitals",
    "antibiotic_prescribed_for_suspected_bacterial_infection",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    manifest = read_json(ROOT / "runtime" / "ontology_manifest.json")
    manifest_item = next((item for item in manifest["phenotypes"] if item["id"] == TARGET), None)
    packet = (ROOT / "review_sheets" / f"{TARGET}_v1_review_packet.md").read_text(encoding="utf-8")

    require(phenotype["status"] == "reviewed", "bronchitis phenotype must be reviewed")
    require(phenotype["review"]["status"] == "reviewed", "bronchitis review status must be reviewed")
    require(phenotype["review"]["production_status"] == "enabled_with_runtime_modifier_gates", "production status missing")
    require(manifest_item is not None, "manifest missing bronchitis")
    require(manifest_item["status"] == "reviewed", "manifest status must be reviewed")
    require(manifest_item["review_status"] == "reviewed", "manifest review status must be reviewed")
    require(set(manifest_item["unsafe_modifiers"]) == REQUIRED_BLOCKERS, "bronchitis blockers changed unexpectedly")
    require("cough" not in set(manifest_item["condition_terms"]), "broad cough must not be standalone runtime term")
    require("Patient-Facing Output" in packet, "review packet must embed full patient-facing output")
    require("Do not use broad cough as a standalone runtime term." in packet, "review packet missing cough guardrail")

    clean = classify(
        "acute bronchitis no pneumonia",
        "Adult with cough and chest cold symptoms. Clinician diagnosis is acute bronchitis. No pneumonia concern, no focal lung findings, oxygenation acceptable, breathing comfortable, discharged home.",
    )
    require(clean["phenotype_id"] == TARGET, f"clean bronchitis should match: {clean}")
    require(clean["fallback_reason"] is None, f"clean bronchitis should enter ontology mode: {clean}")

    vague = classify("cough", "Cough for two days. No final respiratory discharge phenotype documented.")
    require(vague["phenotype_id"] is None, f"vague cough should not match: {vague}")
    require(vague["fallback_reason"] == "no_supported_phenotype_match", f"vague cough fallback mismatch: {vague}")

    blocker = classify(
        "acute bronchitis",
        "Adult diagnosed with acute bronchitis but reports hemoptysis and coughing blood.",
    )
    require(blocker["fallback_reason"] == "unsafe_modifier_present", f"hemoptysis should block: {blocker}")
    require("hemoptysis" in blocker["exclusions"], f"hemoptysis exclusion missing: {blocker}")

    print("phase34 acute bronchitis promotion checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
