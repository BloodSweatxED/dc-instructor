#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from ontology_lib import OntologyError  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    payload = gate_payload()
    require(payload["reviewed_runtime_clean"], "reviewed runtime must be clean")
    require(payload["phenotype_expansion_allowed"], "phenotype expansion should be allowed")
    require(payload["active_draft_phenotype_count"] == 0, "active draft phenotypes should be closed")
    require(payload["draft_source_gap_count"] == 0, "draft source gaps should be closed")
    require(
        payload["phase20_coverage"]["contradictory_covered"] == payload["phase20_coverage"]["reviewed_count"],
        "every reviewed phenotype needs contradictory-note coverage",
    )
    print("phase28 expansion reopened checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
