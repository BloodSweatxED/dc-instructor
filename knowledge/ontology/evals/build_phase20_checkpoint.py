#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, load_phenotypes, load_primitives  # noqa: E402
from check_low_confidence_near_misses import ALLOWED_LOW_CONFIDENCE  # noqa: E402


CHECKPOINT_DIR = ROOT / "evals" / "phase20_checkpoint"
RESULTS_PATH = ROOT / "evals" / "runtime_case_results.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def all_runtime_cases() -> dict[str, dict[str, Any]]:
    cases: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "evals").glob("*_runtime_cases.json")):
        for item in read_json(path):
            cases[item["id"]] = {**item, "case_file": path.name}
    return cases


def phase20_results(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in results if row["case_id"].startswith("phase20_")]


def reviewed_phenotypes(phenotypes: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        phenotype_id: phenotype
        for phenotype_id, phenotype in phenotypes.items()
        if phenotype.get("review", {}).get("status") == "reviewed" and phenotype.get("status") == "reviewed"
    }


def source_gap_index(phenotypes: dict[str, dict[str, Any]], primitives: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 20 Source-Gap Index",
        "",
        "| Item | Status | Gap |",
        "| --- | --- | --- |",
    ]
    for phenotype_id, phenotype in sorted(phenotypes.items()):
        audit = phenotype.get("source_audit", {})
        if audit.get("source_needed") or not phenotype.get("source_card_ids"):
            gap = "missing source card" if not phenotype.get("source_card_ids") else "source audit still needed"
            lines.append(f"| phenotype `{phenotype_id}` | {phenotype['review']['status']} | {gap} |")
    for primitive_id, primitive in sorted(primitives.items()):
        audit = primitive.get("source_audit", {})
        if audit.get("source_needed") or not primitive.get("source_card_ids"):
            lines.append(f"| primitive `{primitive_id}` | {primitive['review']['status']} | source audit still needed |")
    if len(lines) == 4:
        lines.append("| none | reviewed library | no current source gaps found |")
    return lines


def review_packet_index(phenotypes: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 20 Review Packet Index",
        "",
        "| Phenotype | Status | Last reviewed | Packet | Source cards |",
        "| --- | --- | --- | --- | --- |",
    ]
    for phenotype_id, phenotype in sorted(phenotypes.items()):
        packet = ROOT / "review_sheets" / f"{phenotype_id}_v1_review_packet.md"
        packet_label = packet.relative_to(ROOT) if packet.exists() else "missing"
        review = phenotype.get("review", {})
        last_reviewed = review.get("last_reviewed") or "unknown"
        source_cards = ", ".join(f"`{row}`" for row in phenotype.get("source_card_ids", [])) or "none"
        lines.append(
            f"| `{phenotype_id}` | {review.get('status', phenotype.get('status', 'unknown'))} | "
            f"{last_reviewed} | `{packet_label}` | {source_cards} |"
        )
    return lines


def false_positive_table(results: list[dict[str, Any]], cases: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 20 False-Positive Pressure Table",
        "",
        "These cases intentionally contain a candidate phenotype signal but must not enter ontology mode.",
        "",
        "| Case | Candidate | Fallback | Exclusions | Case type |",
        "| --- | --- | --- | --- | --- |",
    ]
    for result in results:
        case = cases[result["case_id"]]
        classification = result["result"]
        expected_fallback = case.get("expected_fallback_reason")
        if classification["phenotype_id"] and expected_fallback is not None:
            case_type = "medication-sensitive" if "_med_sensitive_" in result["case_id"] else "contradictory or vague"
            exclusions = ", ".join(f"`{item}`" for item in classification.get("exclusions", [])) or "none"
            lines.append(
                f"| `{result['case_id']}` | `{classification['phenotype_id']}` | "
                f"{classification['fallback_reason']} | {exclusions} | {case_type} |"
            )
    if len(lines) == 6:
        lines.append("| none | none | none | none | no candidate fallbacks found |")
    return lines


def false_negative_table(results: list[dict[str, Any]], cases: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 20 False-Negative Pressure Table",
        "",
        "These vague-chief-complaint cases should fall back unless the classifier has enough reviewed-phenotype signal.",
        "",
        "| Case | Input condition | Candidate | Fallback |",
        "| --- | --- | --- | --- |",
    ]
    for result in results:
        case = cases[result["case_id"]]
        classification = result["result"]
        if "_vague_chief_complaint_" in result["case_id"]:
            candidate = f"`{classification['phenotype_id']}`" if classification["phenotype_id"] else "none"
            lines.append(
                f"| `{result['case_id']}` | {case['condition']} | {candidate} | {classification['fallback_reason']} |"
            )
    return lines


def medication_provenance_decision() -> list[str]:
    return [
        "# Phase 20 Medication Provenance UI Decision",
        "",
        "Decision: keep medication provenance section-level for now.",
        "",
        "Rationale: the current product metadata is a review aid, not medication reconciliation. Section-level provenance keeps the clinician's scan path visible without implying the system validated dose, schedule, route, indication, renal adjustment, pregnancy status, allergy status, or drug interactions.",
        "",
        "Line-level markers should wait until the product has structured medication spans from the clinician-entered note, a line-to-source mapping contract, and a UI pattern that can mark uncertainty without making unvalidated medication text look safer than it is.",
        "",
        "Phase 20 keeps medication-sensitive runtime cases focused on fallback behavior. They verify that medication context can block ontology mode when it changes discharge risk, while leaving prescribing logic out of scope.",
    ]


def low_confidence_audit(results: list[dict[str, Any]]) -> list[str]:
    low_confidence = [row for row in results if row["result"]["fallback_reason"] == "low_confidence"]
    lines = [
        "# Phase 20 Low-Confidence Near-Miss Audit",
        "",
        "Low-confidence fallback is allowed only when the candidate match is intentional symptom-only or chief-complaint-only behavior. Ruled-out diagnoses and absent final diagnoses should become `no_supported_phenotype_match` instead.",
        "",
        "| Case | Candidate | Confidence | Rationale |",
        "| --- | --- | --- | --- |",
    ]
    for result in sorted(low_confidence, key=lambda row: row["case_id"]):
        case_id = result["case_id"]
        rationale = ALLOWED_LOW_CONFIDENCE.get(case_id, "unexpected low-confidence case")
        candidate = result["result"]["phenotype_id"]
        confidence = result["result"]["confidence"]
        lines.append(f"| `{case_id}` | `{candidate}` | {confidence} | {rationale} |")
    if not low_confidence:
        lines.append("| none | none | none | no low-confidence near misses found |")
    return lines


def summary(results: list[dict[str, Any]], phenotypes: dict[str, dict[str, Any]]) -> list[str]:
    reviewed = reviewed_phenotypes(phenotypes)
    contradictory = [row for row in results if "_contradictory_note_" in row["case_id"]]
    vague = [row for row in results if "_vague_chief_complaint_" in row["case_id"]]
    med_sensitive = [row for row in results if "_med_sensitive_" in row["case_id"]]
    ontology = [row for row in results if row["result"]["fallback_reason"] is None]
    unsafe = [row for row in results if row["result"]["fallback_reason"] == "unsafe_modifier_present"]
    low_conf = [row for row in results if row["result"]["fallback_reason"] == "low_confidence"]
    no_match = [row for row in results if row["result"]["fallback_reason"] == "no_supported_phenotype_match"]
    return [
        "# Phase 20 Runtime Depth Checkpoint",
        "",
        f"Reviewed runtime-enabled phenotypes: {len(reviewed)}.",
        f"Phase 20 runtime cases: {len(results)}.",
        f"Contradictory-note cases: {len(contradictory)}.",
        f"Vague-chief-complaint cases: {len(vague)}.",
        f"Medication-sensitive cases: {len(med_sensitive)}.",
        f"Ontology-mode clean passes in Phase 20: {len(ontology)}.",
        f"Unsafe-modifier fallbacks in Phase 20: {len(unsafe)}.",
        f"Low-confidence fallbacks in Phase 20: {len(low_conf)}.",
        f"No-match fallbacks in Phase 20: {len(no_match)}.",
        "",
        "Checkpoint read: Phase 20 is a depth gate, not a phenotype-expansion phase. The classifier should keep ambiguous or contradictory notes out of ontology mode even when a reviewed phenotype is nearby.",
        "",
        "Low-confidence behavior is now allowlisted. New low-confidence candidates should fail `check_low_confidence_near_misses.py` until reviewed.",
        "",
        "Next recommended move: use this checkpoint as the gate before adding new phenotypes or expanding patient-facing content.",
    ]


def main() -> int:
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    results = phase20_results(read_json(RESULTS_PATH))
    cases = all_runtime_cases()
    write(CHECKPOINT_DIR / "summary.md", summary(results, phenotypes))
    write(CHECKPOINT_DIR / "false_positive_table.md", false_positive_table(results, cases))
    write(CHECKPOINT_DIR / "false_negative_table.md", false_negative_table(results, cases))
    write(CHECKPOINT_DIR / "source_gap_index.md", source_gap_index(phenotypes, primitives))
    write(CHECKPOINT_DIR / "review_packet_index.md", review_packet_index(phenotypes))
    write(CHECKPOINT_DIR / "medication_provenance_decision.md", medication_provenance_decision())
    write(CHECKPOINT_DIR / "low_confidence_near_miss_audit.md", low_confidence_audit(read_json(RESULTS_PATH)))
    print(f"wrote checkpoint docs to {CHECKPOINT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
