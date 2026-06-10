#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError  # noqa: E402


CASES_PATH = ROOT / "evals" / "phase151_broad_chief_complaint_stress_runtime_cases.json"
SUMMARY_PATH = ROOT / "evals" / "phase151_broad_chief_complaint_stress.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        result = classify(case["condition"], case.get("ed_note", ""))
        require(result["phenotype_id"] is None, f"{case['id']} should not match a phenotype: {result}")
        require(
            result["fallback_reason"] == "no_supported_phenotype_match",
            f"{case['id']} should fall back as no supported match: {result}",
        )
        results.append((case, result))

    lines = [
        "# Phase 151 Broad Chief Complaint Stress",
        "",
        "Decision: pass. Broad chief complaints do not trigger ontology phenotypes.",
        "",
        "| Case | Condition | Result |",
        "| --- | --- | --- |",
    ]
    for case, result in results:
        lines.append(f"| `{case['id']}` | `{case['condition']}` | `{result['fallback_reason']}` |")
    lines.extend(
        [
            "",
            "Interpretation: headache, ear pain, bleeding, red eye, abdominal pain, chest pain, cough, and dizziness remain generator/product-layer inputs unless a narrow reviewed phenotype and required runtime context are present.",
        ]
    )
    SUMMARY_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("phase151 broad chief complaint stress checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
