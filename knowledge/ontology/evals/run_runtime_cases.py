#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from classify_phenotype import classify  # noqa: E402
from ontology_lib import ROOT, OntologyError  # noqa: E402


OUTPUT_PATH = ROOT / "evals" / "runtime_case_results.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def run_case(case: dict[str, Any]) -> dict[str, Any]:
    result = classify(case["condition"], case.get("ed_note", ""))
    expected_phenotype = case.get("expected_phenotype_id")
    expected_fallback = case.get("expected_fallback_reason")
    require(result["phenotype_id"] == expected_phenotype, f"{case['id']} phenotype mismatch: {result}")
    require(result["fallback_reason"] == expected_fallback, f"{case['id']} fallback mismatch: {result}")
    if expected_fallback is None:
        require(result["confidence"] >= case.get("minimum_confidence", 0.86), f"{case['id']} confidence too low: {result}")
    for expected in case.get("expected_exclusions", []):
        require(expected in result["exclusions"], f"{case['id']} missing exclusion {expected}: {result}")
    for expected in case.get("expected_missing_required_context", []):
        require(
            expected in result.get("missing_required_context", []),
            f"{case['id']} missing required context {expected}: {result}",
        )
    return {"case_id": case["id"], "passed": True, "result": result}


def main() -> int:
    cases = []
    for path in sorted((ROOT / "evals").glob("*_runtime_cases.json")):
        cases.extend(json.loads(path.read_text(encoding="utf-8")))
    results = []
    try:
        for case in cases:
            results.append(run_case(case))
    except OntologyError as exc:
        OUTPUT_PATH.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        print(f"runtime case validation failed: {exc}")
        return 1
    OUTPUT_PATH.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    for result in results:
        print(f"runtime case passed: {result['case_id']}")
    print("runtime case validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
