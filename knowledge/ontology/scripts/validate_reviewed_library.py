#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from export_reviewed_library import READING_LEVELS, six_section_only
from ontology_lib import SECTIONS, OntologyError, assemble_discharge


ROOT = Path(__file__).resolve().parents[3]
ONTOLOGY_ROOT = ROOT / "knowledge" / "ontology"
LIBRARY_ROOT = ROOT / "library"
MANIFEST_PATH = ONTOLOGY_ROOT / "runtime" / "ontology_manifest.json"
SECTION_HEADERS = [header for _, header in SECTIONS]


def manifest_statuses() -> dict[str, tuple[str | None, str | None]]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {
        phenotype["id"]: (phenotype.get("status"), phenotype.get("review_status"))
        for phenotype in manifest["phenotypes"]
    }


def reviewed_ids(statuses: dict[str, tuple[str | None, str | None]]) -> set[str]:
    return {
        phenotype_id
        for phenotype_id, (status, review_status) in statuses.items()
        if status == "reviewed" and review_status == "reviewed"
    }


def validate_headers(path: Path, text: str) -> None:
    found = [line for line in text.splitlines() if line.endswith(":")]
    if found != SECTION_HEADERS:
        raise OntologyError(f"{path} must contain exactly the six required library sections")


def main() -> int:
    statuses = manifest_statuses()
    expected_ids = reviewed_ids(statuses)
    actual_dirs = {
        path.name
        for path in LIBRARY_ROOT.iterdir()
        if path.is_dir()
    }

    missing = sorted(expected_ids - actual_dirs)
    extra = sorted(actual_dirs - expected_ids)
    if missing:
        raise OntologyError(f"reviewed phenotypes missing from library: {', '.join(missing)}")
    if extra:
        raise OntologyError(f"non-reviewed phenotypes present in library: {', '.join(extra)}")

    checked = 0
    for phenotype_id in sorted(expected_ids):
        condition_dir = LIBRARY_ROOT / phenotype_id
        expected_filenames = {filename for _, filename in READING_LEVELS}
        actual_filenames = {path.name for path in condition_dir.glob("*.md")}
        if actual_filenames != expected_filenames:
            raise OntologyError(
                f"{condition_dir} must contain exactly {', '.join(sorted(expected_filenames))}"
            )

        for reading_level, filename in READING_LEVELS:
            path = condition_dir / filename
            actual = path.read_text(encoding="utf-8")
            expected = six_section_only(assemble_discharge(phenotype_id, reading_level))
            if actual != expected:
                raise OntologyError(f"{path} does not match reviewed ontology assembly")
            validate_headers(path, actual)
            checked += 1

    print(f"reviewed library validation passed: {checked} files across {len(expected_ids)} conditions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
