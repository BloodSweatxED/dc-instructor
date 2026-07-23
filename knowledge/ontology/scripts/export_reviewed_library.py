#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from ontology_lib import SECTIONS, assemble_discharge


ROOT = Path(__file__).resolve().parents[3]
ONTOLOGY_ROOT = ROOT / "knowledge" / "ontology"
LIBRARY_ROOT = ROOT / "library"
MANIFEST_PATH = ONTOLOGY_ROOT / "runtime" / "ontology_manifest.json"

READING_LEVELS = (
    ("4", "en_4th.md"),
    ("6", "en_6th.md"),
    ("HL1", "en_HL1.md"),
)
SECTION_HEADERS = [header for _, header in SECTIONS]


def reviewed_phenotype_ids() -> list[str]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return sorted(
        phenotype["id"]
        for phenotype in manifest["phenotypes"]
        if phenotype.get("status") == "reviewed"
        and phenotype.get("review_status") == "reviewed"
    )


def six_section_only(text: str) -> str:
    lines = text.splitlines()
    kept: list[str] = []

    for line in lines:
        if line.endswith(":") and line not in SECTION_HEADERS:
            break
        kept.append(line)

    return "\n".join(kept).rstrip() + "\n"


def main() -> int:
    LIBRARY_ROOT.mkdir(exist_ok=True)

    for phenotype_id in reviewed_phenotype_ids():
        condition_dir = LIBRARY_ROOT / phenotype_id
        condition_dir.mkdir(exist_ok=True)

        for reading_level, filename in READING_LEVELS:
            output = six_section_only(assemble_discharge(phenotype_id, reading_level))
            (condition_dir / filename).write_text(output, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
