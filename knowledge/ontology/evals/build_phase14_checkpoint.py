#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, load_phenotypes, load_primitives  # noqa: E402


CHECKPOINT_DIR = ROOT / "evals" / "phase14_checkpoint"
RESULTS_PATH = ROOT / "evals" / "runtime_case_results.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def runtime_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for path in sorted((ROOT / "evals").glob("*_runtime_cases.json")):
        cases.extend(read_json(path))
    return cases


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def case_index() -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in runtime_cases()}


def review_packet_index(phenotypes: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 14 Review Packet Index",
        "",
        "| Phenotype | Status | Packet | Source cards |",
        "| --- | --- | --- | --- |",
    ]
    for phenotype_id, phenotype in sorted(phenotypes.items()):
        packet = ROOT / "review_sheets" / f"{phenotype_id}_v1_review_packet.md"
        packet_label = packet.relative_to(ROOT) if packet.exists() else "missing"
        source_cards = ", ".join(f"`{row}`" for row in phenotype.get("source_card_ids", [])) or "none"
        lines.append(f"| `{phenotype_id}` | {phenotype['review']['status']} | `{packet_label}` | {source_cards} |")
    return lines


def source_gap_index(phenotypes: dict[str, dict[str, Any]], primitives: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 14 Source-Gap Index",
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
        lines.append("| none | reviewed library | no current reviewed source gaps found |")
    return lines


def false_positive_table(results: list[dict[str, Any]], cases: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 14 False-Positive Table",
        "",
        "These are candidate matches that correctly fell back instead of using ontology mode.",
        "",
        "| Case | Candidate | Fallback | Why it matters |",
        "| --- | --- | --- | --- |",
    ]
    for result in results:
        case = cases[result["case_id"]]
        classification = result["result"]
        if classification["phenotype_id"] and classification["fallback_reason"] in {"low_confidence", "unsafe_modifier_present"}:
            note = "near miss or vague input" if classification["fallback_reason"] == "low_confidence" else "unsafe modifier blocked ontology mode"
            lines.append(
                f"| `{result['case_id']}` | `{classification['phenotype_id']}` | {classification['fallback_reason']} | {note} |"
            )
    if len(lines) == 6:
        lines.append("| none | none | none | no candidate fallbacks found |")
    return lines


def false_negative_table(results: list[dict[str, Any]], cases: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        "# Phase 14 False-Negative Table",
        "",
        "These are no-match fallbacks. In the current policy, false negatives are acceptable if they avoid unsafe ontology mode.",
        "",
        "| Case | Input condition | Expected behavior |",
        "| --- | --- | --- |",
    ]
    for result in results:
        case = cases[result["case_id"]]
        classification = result["result"]
        if classification["phenotype_id"] is None:
            lines.append(f"| `{result['case_id']}` | {case['condition']} | generator fallback |")
    if len(lines) == 6:
        lines.append("| none | none | no no-match fallbacks found |")
    return lines


def medication_policy_gap_list(primitives: dict[str, dict[str, Any]]) -> list[str]:
    reviewed_med_primitives = [
        item for item in primitives.values() if item.get("section") == "medications" and item.get("review", {}).get("status") == "reviewed"
    ]
    lines = [
        "# Phase 14 Medication-Policy Gap List",
        "",
        "Medication dosing, duration, route, contraindication handling, renal adjustment, pregnancy adjustment, pediatric adjustment, and allergy substitution remain out of scope for V1 reviewed ontology output.",
        "",
        "| Area | Current ontology behavior | Needed before dosing-ready output |",
        "| --- | --- | --- |",
        "| Antibiotics | Says to take antibiotics only when prescribed, or exactly as prescribed. | Medication policy with indication-specific regimen, dose, duration, allergy, pregnancy, renal, and local-resistance logic. |",
        "| Asthma medications | Mentions rescue inhaler, steroids, and controller medicines only as prescribed. | Asthma medication policy with inhaler access, steroid plan, controller plan, and return thresholds. |",
        "| Analgesics and antipyretics | Uses label-following language for acetaminophen or ibuprofen if safe. | Contraindication and dosing policy for renal disease, anticoagulation, pregnancy, liver disease, age, and weight. |",
        "| Antiemetics and pain prescriptions | Refers to prescribed pain or nausea medicine without naming dose. | Condition-specific prescription policy and safety rules. |",
        "",
        f"Reviewed medication primitives currently covered by non-dosing policy language: {len(reviewed_med_primitives)}.",
    ]
    return lines


def summary(results: list[dict[str, Any]], phenotypes: dict[str, dict[str, Any]]) -> list[str]:
    reviewed = [item for item in phenotypes.values() if item["review"]["status"] == "reviewed"]
    unsafe = [row for row in results if row["result"]["fallback_reason"] == "unsafe_modifier_present"]
    low_conf = [row for row in results if row["result"]["fallback_reason"] == "low_confidence"]
    no_match = [row for row in results if row["result"]["fallback_reason"] == "no_supported_phenotype_match"]
    ontology = [row for row in results if row["result"]["fallback_reason"] is None]
    return [
        "# Phase 14 Structure and Safety Checkpoint",
        "",
        f"Reviewed phenotypes: {len(reviewed)} of {len(phenotypes)}.",
        f"Runtime cases: {len(results)}.",
        f"Ontology-mode clean passes: {len(ontology)}.",
        f"Unsafe-modifier fallbacks: {len(unsafe)}.",
        f"Low-confidence fallbacks: {len(low_conf)}.",
        f"No-match fallbacks: {len(no_match)}.",
        "",
        "Checkpoint read: structure is holding for iteration. The current deterministic classifier is conservative enough for false negatives, but term-level candidate matches still appear in vague or negated near-miss notes and should remain blocked by low confidence until a better classifier exists.",
        "",
        "Do not expand phenotype count again until review-packet usability, local follow-up interval policy, and medication-policy boundaries are clinician-reviewed.",
    ]


def main() -> int:
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    results = read_json(RESULTS_PATH)
    cases = case_index()
    write(CHECKPOINT_DIR / "summary.md", summary(results, phenotypes))
    write(CHECKPOINT_DIR / "review_packet_index.md", review_packet_index(phenotypes))
    write(CHECKPOINT_DIR / "source_gap_index.md", source_gap_index(phenotypes, primitives))
    write(CHECKPOINT_DIR / "false_positive_table.md", false_positive_table(results, cases))
    write(CHECKPOINT_DIR / "false_negative_table.md", false_negative_table(results, cases))
    write(CHECKPOINT_DIR / "medication_policy_gap_list.md", medication_policy_gap_list(primitives))
    print(f"wrote checkpoint docs to {CHECKPOINT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
