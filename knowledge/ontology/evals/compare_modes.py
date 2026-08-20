#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from assemble_discharge import assemble_discharge  # noqa: E402
from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, SECTIONS, load_phenotypes, load_primitives, read_json  # noqa: E402


OUTPUT_JSON = ROOT / "evals" / "phase10_mode_comparison.json"
OUTPUT_MD = ROOT / "evals" / "phase10_mode_comparison.md"
BATCH_OUTPUTS = [
    ROOT / "evals" / "generator_batch_01_outputs.json",
    ROOT / "evals" / "generator_batch_02_outputs.json",
]

RED_FLAG_TERMS = [
    "trouble breathing",
    "shortness of breath",
    "chest pain",
    "confusion",
    "faint",
    "weakness",
    "numb",
    "fever",
    "worse",
    "blood",
    "vomiting",
]
UNSAFE_MED_PATTERNS = [
    r"\b\d+\s?(mg|mcg|g|ml|units?)\b",
    r"\bmore than\s+\d+",
    r"\bevery\s+\d+\s*(hours?|hrs?)\b",
]
UNSUPPORTED_CERTAINTY = [
    r"\byour .* (was|were) normal\b",
    r"\bno (heart attack|blood clot|fracture|pneumonia|bleeding)\b",
    r"\btests showed\b",
]


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text)


def reading_proxy(text: str) -> dict[str, Any]:
    terms = words(text)
    sentences = [part.strip() for part in re.split(r"[.!?]\s+", text) if part.strip()]
    avg_sentence = round(len(terms) / max(len(sentences), 1), 1)
    long_words = sum(1 for term in terms if len(term) >= 8)
    return {
        "word_count": len(terms),
        "avg_sentence_words": avg_sentence,
        "long_word_ratio": round(long_words / max(len(terms), 1), 3),
    }


def section_completeness(text: str) -> dict[str, bool]:
    upper = text.upper()
    return {section: header in upper for section, header in SECTIONS}


def count_matches(text: str, patterns: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for pattern in patterns if re.search(pattern, lowered))


def source_support(phenotype_id: str) -> dict[str, Any]:
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    phenotype = phenotypes.get(phenotype_id)
    if not phenotype:
        return {"source_supported": False, "source_needed": True, "review_status": None}
    primitive_rows = [primitives[pid] for pid in phenotype["primitive_ids"] if pid in primitives]
    source_needed = bool(phenotype.get("source_audit", {}).get("source_needed")) or any(
        row.get("source_audit", {}).get("source_needed") for row in primitive_rows
    )
    return {
        "source_supported": not source_needed,
        "source_needed": source_needed,
        "review_status": phenotype["review"]["status"],
    }


def load_generator_cases() -> dict[str, dict[str, Any]]:
    cases = {}
    for path in BATCH_OUTPUTS:
        data = read_json(path)
        for item in data.get("cases", []):
            cases[item["id"]] = item
    return cases


def metrics(text: str, phenotype_id: str | None = None) -> dict[str, Any]:
    lowered = text.lower()
    return {
        "missing_red_flags": not any(term in lowered for term in RED_FLAG_TERMS),
        "unsafe_med_advice": count_matches(text, UNSAFE_MED_PATTERNS),
        "unsupported_certainty": count_matches(text, UNSUPPORTED_CERTAINTY),
        "reading_level_proxy": reading_proxy(text),
        "section_completeness": section_completeness(text),
        "source_support": source_support(phenotype_id) if phenotype_id else {"source_supported": False, "source_needed": True},
    }


def compare() -> list[dict[str, Any]]:
    cases = load_generator_cases()
    phenotypes = load_phenotypes()
    rows: list[dict[str, Any]] = []
    for phenotype_id in sorted(phenotypes):
        if phenotype_id not in cases:
            continue
        generator_text = cases[phenotype_id].get("output") or ""
        ontology_text = assemble_discharge(phenotype_id, "6")
        classifier = classify(cases[phenotype_id]["condition"])
        rows.append(
            {
                "phenotype_id": phenotype_id,
                "classifier": classifier,
                "generator": metrics(generator_text, phenotype_id),
                "ontology": metrics(ontology_text, phenotype_id),
                "clinician_review_target": {
                    "status": phenotypes[phenotype_id]["review"]["status"],
                    "note": "Current target is the phenotype review sheet assembled output; clinician sign-off is still pending.",
                },
                "modifier_handling": {
                    "unsafe_modifiers": phenotypes[phenotype_id].get("runtime", {}).get("unsafe_modifiers", []),
                    "fallback_reason": classifier.get("fallback_reason"),
                },
            }
        )
    return rows


def markdown(rows: list[dict[str, Any]]) -> str:
    lines = [
        "# Phase 10 Mode Comparison",
        "",
        "Compares current generator output, ontology assembly, and the current clinician-review target state.",
        "",
        "| Phenotype | Classifier | Generator risks | Ontology risks | Source support | Review |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        gen = row["generator"]
        ont = row["ontology"]
        support = ont["source_support"]
        generator_risks = f"red_flags_missing={gen['missing_red_flags']}; med={gen['unsafe_med_advice']}; certainty={gen['unsupported_certainty']}"
        ontology_risks = f"red_flags_missing={ont['missing_red_flags']}; med={ont['unsafe_med_advice']}; certainty={ont['unsupported_certainty']}"
        classifier = row["classifier"]
        lines.append(
            f"| `{row['phenotype_id']}` | {classifier['confidence']} / {classifier['fallback_reason'] or 'ontology'} | {generator_risks} | {ontology_risks} | needed={support['source_needed']} | {support['review_status']} |"
        )
    lines.extend(
        [
            "",
            "## Production Gates",
            "",
            "- Source audit must pass before ontology mode can be used.",
            "- Clinician review status must be `reviewed` for phenotype and primitives.",
            "- Unsafe modifier matches force generator fallback.",
            "- The classifier accepts scrubbed ED-note context only and writes no note text.",
            "- Runtime emits `ontology_mode`, `phenotype_id`, `ontology_confidence`, and `fallback_reason` metadata.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    rows = compare()
    OUTPUT_JSON.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(markdown(rows), encoding="utf-8")
    print(f"wrote {OUTPUT_JSON}")
    print(f"wrote {OUTPUT_MD}")
    print(f"rows: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
