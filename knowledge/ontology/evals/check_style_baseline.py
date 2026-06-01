#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import assemble_discharge  # noqa: E402


STYLE_CHECKS = {
    "asthma_exacerbation_improved_discharge": {
        "required": [
            "You had an asthma flare-up",
            "You came to the ED",
            "breathing treatments",
            "steroids",
            "breathing comfortably",
            "Rest for the next 1-2 days",
            "trigger your asthma",
            "rescue inhaler is not helping",
            "within 3-5 days",
        ],
        "forbidden": [
            "Your breathing improved enough for discharge today.",
            "use the plan you were given closely",
        ],
    }
}


def main() -> int:
    failures: list[str] = []
    for phenotype_id, checks in STYLE_CHECKS.items():
        output = assemble_discharge(phenotype_id, "6")
        for phrase in checks["required"]:
            if phrase not in output:
                failures.append(f"{phenotype_id} missing style phrase: {phrase}")
        for phrase in checks["forbidden"]:
            if phrase in output:
                failures.append(f"{phenotype_id} still has stale phrase: {phrase}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print("style baseline checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
