#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_low_confidence_near_misses import ALLOWED_LOW_CONFIDENCE  # noqa: E402
from ontology_lib import ROOT, load_phenotypes, load_primitives  # noqa: E402


GATE_DIR = ROOT / "evals" / "phase21_expansion_gate"
RESULTS_PATH = ROOT / "evals" / "runtime_case_results.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def reviewed(item: dict[str, Any]) -> bool:
    return item.get("status") == "reviewed" and item.get("review", {}).get("status") == "reviewed"


def retired(item: dict[str, Any]) -> bool:
    return item.get("status") == "retired" or item.get("review", {}).get("status") == "retired"


def active_draft(item: dict[str, Any]) -> bool:
    return not reviewed(item) and not retired(item)


def source_gap(item: dict[str, Any]) -> str | None:
    if retired(item):
        return None
    audit = item.get("source_audit", {})
    if not item.get("source_card_ids"):
        return "missing source card"
    if audit.get("source_needed"):
        return "source audit still needed"
    return None


def reviewed_source_gaps(phenotypes: dict[str, dict[str, Any]], primitives: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    gaps: list[dict[str, str]] = []
    for phenotype_id, phenotype in sorted(phenotypes.items()):
        gap = source_gap(phenotype)
        if gap and reviewed(phenotype):
            gaps.append({"item": f"phenotype `{phenotype_id}`", "status": "reviewed", "gap": gap})
    for primitive_id, primitive in sorted(primitives.items()):
        gap = source_gap(primitive)
        if gap and primitive.get("review", {}).get("status") == "reviewed":
            gaps.append({"item": f"primitive `{primitive_id}`", "status": "reviewed", "gap": gap})
    return gaps


def draft_source_gaps(phenotypes: dict[str, dict[str, Any]], primitives: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    gaps: list[dict[str, str]] = []
    for phenotype_id, phenotype in sorted(phenotypes.items()):
        gap = source_gap(phenotype)
        if gap and active_draft(phenotype):
            gaps.append({"item": f"phenotype `{phenotype_id}`", "status": phenotype["review"]["status"], "gap": gap})
    for primitive_id, primitive in sorted(primitives.items()):
        gap = source_gap(primitive)
        if gap and active_draft(primitive):
            gaps.append({"item": f"primitive `{primitive_id}`", "status": primitive["review"]["status"], "gap": gap})
    return gaps


def active_draft_phenotypes(phenotypes: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for phenotype_id, phenotype in sorted(phenotypes.items()):
        if active_draft(phenotype):
            rows.append(
                {
                    "phenotype_id": phenotype_id,
                    "status": phenotype.get("status", "unknown"),
                    "review_status": phenotype.get("review", {}).get("status", "unknown"),
                    "reason": "not clinician-reviewed",
                }
            )
    return rows


def phase20_coverage(results: list[dict[str, Any]], phenotypes: dict[str, dict[str, Any]]) -> dict[str, Any]:
    reviewed_ids = sorted(phenotype_id for phenotype_id, phenotype in phenotypes.items() if reviewed(phenotype))
    phase20 = [row for row in results if row["case_id"].startswith("phase20_")]
    contradictory = {row["result"]["phenotype_id"] for row in phase20 if "_contradictory_note_" in row["case_id"]}
    vague = {
        row["case_id"].replace("phase20_", "").replace("_vague_chief_complaint_fallback", "")
        for row in phase20
        if "_vague_chief_complaint_" in row["case_id"]
    }
    return {
        "reviewed_count": len(reviewed_ids),
        "phase20_count": len(phase20),
        "contradictory_covered": len([phenotype_id for phenotype_id in reviewed_ids if phenotype_id in contradictory]),
        "vague_cases": len(vague),
    }


def low_confidence_status(results: list[dict[str, Any]]) -> dict[str, Any]:
    low_confidence = [
        row["case_id"]
        for row in results
        if row.get("result", {}).get("fallback_reason") == "low_confidence"
    ]
    unexpected = sorted(set(low_confidence) - set(ALLOWED_LOW_CONFIDENCE))
    missing = sorted(set(ALLOWED_LOW_CONFIDENCE) - set(low_confidence))
    return {
        "allowed": len(low_confidence),
        "unexpected": unexpected,
        "missing_allowed": missing,
    }


def gate_payload() -> dict[str, Any]:
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    results = read_json(RESULTS_PATH)
    reviewed_gaps = reviewed_source_gaps(phenotypes, primitives)
    draft_gaps = draft_source_gaps(phenotypes, primitives)
    active_drafts = active_draft_phenotypes(phenotypes)
    low_confidence = low_confidence_status(results)
    coverage = phase20_coverage(results, phenotypes)
    reviewed_runtime_clean = not reviewed_gaps and not low_confidence["unexpected"] and not low_confidence["missing_allowed"]
    expansion_allowed = reviewed_runtime_clean and not draft_gaps and not active_drafts
    return {
        "phase": 21,
        "gate": "expansion_readiness",
        "reviewed_runtime_clean": reviewed_runtime_clean,
        "phenotype_expansion_allowed": expansion_allowed,
        "reviewed_source_gap_count": len(reviewed_gaps),
        "draft_source_gap_count": len(draft_gaps),
        "active_draft_phenotype_count": len(active_drafts),
        "low_confidence": low_confidence,
        "phase20_coverage": coverage,
        "reviewed_source_gaps": reviewed_gaps,
        "draft_source_gaps": draft_gaps,
        "active_draft_phenotypes": active_drafts,
        "decision": "reviewed runtime may continue; phenotype expansion remains blocked" if not expansion_allowed else "phenotype expansion allowed",
    }


def summary(payload: dict[str, Any]) -> list[str]:
    return [
        "# Phase 21 Expansion Gate",
        "",
        f"Reviewed runtime clean: {str(payload['reviewed_runtime_clean']).lower()}.",
        f"Phenotype expansion allowed: {str(payload['phenotype_expansion_allowed']).lower()}.",
        f"Reviewed source gaps: {payload['reviewed_source_gap_count']}.",
        f"Draft source gaps: {payload['draft_source_gap_count']}.",
        f"Active draft phenotypes: {payload['active_draft_phenotype_count']}.",
        f"Approved low-confidence near misses: {payload['low_confidence']['allowed']}.",
        f"Phase 20 runtime cases: {payload['phase20_coverage']['phase20_count']}.",
        "",
        f"Decision: {payload['decision']}.",
        "",
        "Interpretation: the reviewed ontology path can keep running behind the current gates. Do not add new phenotypes or expand patient-facing content until active drafts are narrowed, reviewed, promoted, or explicitly retired.",
    ]


def blockers(payload: dict[str, Any]) -> list[str]:
    lines = [
        "# Phase 21 Expansion Blockers",
        "",
        "| Item | Status | Gap | Action |",
        "| --- | --- | --- | --- |",
    ]
    for row in payload["reviewed_source_gaps"]:
        lines.append(f"| {row['item']} | {row['status']} | {row['gap']} | fix before runtime use |")
    for row in payload["draft_source_gaps"]:
        action = "source-card remediation or retire draft"
        lines.append(f"| {row['item']} | {row['status']} | {row['gap']} | {action} |")
    for row in payload["active_draft_phenotypes"]:
        lines.append(
            f"| phenotype `{row['phenotype_id']}` | {row['review_status']} | {row['reason']} | narrow and review, or retire draft |"
        )
    if len(lines) == 4:
        lines.append("| none | reviewed library | no blocker | expansion allowed |")
    return lines


def phase22_plan(payload: dict[str, Any]) -> list[str]:
    draft_phenotype_gaps = [row for row in payload["draft_source_gaps"] if row["item"].startswith("phenotype")]
    active_drafts = [f"phenotype `{row['phenotype_id']}`" for row in payload["active_draft_phenotypes"]]
    targets = ", ".join([*(row["item"] for row in draft_phenotype_gaps), *active_drafts]) or "none"
    return [
        "# Phase 22 Source Remediation Plan",
        "",
        "Goal: close or retire draft source gaps and active draft phenotypes before any phenotype expansion.",
        "",
        f"Current active draft targets: {targets}.",
        "",
        "Recommended sequence:",
        "",
        "1. `chest_pain_low_risk_negative_ed_workup` is retired as static ontology content. Keep chest pain in product-layer fallback unless it is rebuilt later as a much narrower reviewed phenotype.",
        "2. Decide whether `abdominal_pain_nonspecific_reassuring_workup` is worth preserving as a narrow reviewed phenotype, or should stay product-only/LLM fallback because it is too broad for static ontology mode.",
        "3. If abdominal pain is preserved, narrow boundaries before editing patient-facing primitives.",
        "4. Generate a clinician review packet only after source cards exist and the phenotype boundaries are narrowed.",
        "5. Keep active phenotypes draft until source audit, runtime contradiction cases, medication policy, and clinician review pass.",
        "",
        "Recommendation: abdominal pain can be considered only if narrowed to a very explicit recheck/return-precaution phenotype.",
    ]


def main() -> int:
    GATE_DIR.mkdir(parents=True, exist_ok=True)
    payload = gate_payload()
    (GATE_DIR / "phase21_expansion_gate.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    write(GATE_DIR / "summary.md", summary(payload))
    write(GATE_DIR / "expansion_blockers.md", blockers(payload))
    write(GATE_DIR / "phase22_source_remediation_plan.md", phase22_plan(payload))
    print(f"wrote expansion gate docs to {GATE_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
