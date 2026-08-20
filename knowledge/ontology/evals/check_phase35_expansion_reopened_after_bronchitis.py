#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_bronchitis_no_pneumonia"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    payload = gate_payload()

    require(phenotype["status"] == "reviewed", "bronchitis must be reviewed before expansion reopens")
    require(phenotype["review"]["status"] == "reviewed", "bronchitis review must be reviewed before expansion reopens")
    require(payload["reviewed_runtime_clean"], "reviewed runtime must stay clean")
    require(payload["phenotype_expansion_allowed"], "phenotype expansion should reopen")
    require(payload["active_draft_phenotype_count"] == 0, "active draft phenotypes should be closed")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should be closed")
    require(payload["reviewed_source_gap_count"] == 0, "reviewed source gaps should be closed")
    require(
        payload["phase20_coverage"]["contradictory_covered"] == payload["phase20_coverage"]["reviewed_count"],
        "every reviewed phenotype needs contradictory-note coverage",
    )

    print("phase35 expansion reopened after bronchitis checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
