#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, OntologyError, read_json  # noqa: E402


TARGET = "acute_bronchitis_no_pneumonia"
DOC_PATH = ROOT / "evals" / "phase33_acute_bronchitis_review_packet.md"
SHEET_PATH = ROOT / "review_sheets" / f"{TARGET}.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def main() -> int:
    phenotype = read_json(ROOT / "phenotypes" / f"{TARGET}.json")
    doc = DOC_PATH.read_text(encoding="utf-8")
    sheet = SHEET_PATH.read_text(encoding="utf-8")

    require(phenotype["source_audit"]["source_supported"], "bronchitis source audit must be supported before review")
    require("Assembled Six-Section Output" in sheet, "draft review sheet must embed patient-facing output")
    for text in [
        "Decision: approve for narrow reviewed runtime use after Phase 32 stress coverage passes.",
        "Do not promise exact symptom duration.",
        "Do not add broad `cough` as a runtime term.",
        "Do not use this as a fallback for unmatched respiratory complaints.",
    ]:
        require(text in doc, f"phase33 review doc missing: {text}")

    print("phase33 acute bronchitis review packet checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
