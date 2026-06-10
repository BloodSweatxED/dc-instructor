#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_phase21_expansion_gate import gate_payload  # noqa: E402
from ontology_lib import OntologyError  # noqa: E402


def main() -> int:
    payload = gate_payload()
    if payload["reviewed_source_gap_count"]:
        raise OntologyError("reviewed ontology has source gaps")
    if payload["low_confidence"]["unexpected"]:
        raise OntologyError(f"unexpected low-confidence cases: {payload['low_confidence']['unexpected']}")
    if payload["low_confidence"]["missing_allowed"]:
        raise OntologyError(f"approved low-confidence cases missing: {payload['low_confidence']['missing_allowed']}")
    if payload["phase20_coverage"]["contradictory_covered"] != payload["phase20_coverage"]["reviewed_count"]:
        raise OntologyError("not every reviewed phenotype has Phase 20 contradictory-note coverage")
    print(
        "phase21 expansion gate passed: reviewed runtime may continue; "
        f"phenotype expansion allowed={payload['phenotype_expansion_allowed']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
