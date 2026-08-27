#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [
    ("diagnosis", "DIAGNOSIS:"),
    ("what_we_found", "WHAT WE FOUND:"),
    ("home_care", "WHAT TO DO AT HOME:"),
    ("medications", "MEDICATIONS:"),
    ("return_precautions", "RETURN TO ED IF:"),
    ("follow_up", "FOLLOW UP:"),
]
OPTIONAL_SECTIONS = [
    ("resources", "RESOURCES:"),
]
READING_LEVEL_KEYS = {
    "4": "en_4",
    "6": "en_6",
    "hl1": "en_hl1",
    "HL1": "en_hl1",
    "en_4": "en_4",
    "en_6": "en_6",
    "en_hl1": "en_hl1",
}


class OntologyError(Exception):
    pass


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_phenotypes() -> dict[str, dict[str, Any]]:
    phenotypes = {}
    for path in sorted((ROOT / "phenotypes").glob("*.json")):
        item = read_json(path)
        phenotypes[item["id"]] = item
    return phenotypes


def load_source_cards() -> dict[str, dict[str, Any]]:
    cards = {}
    for path in sorted((ROOT / "source_cards").glob("*.json")):
        item = read_json(path)
        cards[item["id"]] = item
    return cards


def load_primitives() -> dict[str, dict[str, Any]]:
    primitives = {}
    for path in sorted((ROOT / "primitives").glob("*.json")):
        items = read_json(path)
        if not isinstance(items, list):
            raise OntologyError(f"{path} must contain a list of primitives")
        for item in items:
            primitive_id = item["id"]
            if primitive_id in primitives:
                raise OntologyError(f"Duplicate primitive id: {primitive_id}")
            primitives[primitive_id] = item
    return primitives


def reading_key(reading_level: str) -> str:
    try:
        return READING_LEVEL_KEYS[reading_level]
    except KeyError as exc:
        allowed = ", ".join(sorted(READING_LEVEL_KEYS))
        raise OntologyError(f"Unsupported reading level '{reading_level}'. Use one of: {allowed}") from exc


def priority_rank(primitive: dict[str, Any]) -> tuple[int, str]:
    ranks = {"required": 0, "high": 1, "medium": 2, "low": 3}
    return ranks.get(primitive.get("priority", "low"), 9), primitive["id"]


def assemble_discharge(phenotype_id: str, reading_level: str = "6") -> str:
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    key = reading_key(reading_level)

    if phenotype_id not in phenotypes:
        raise OntologyError(f"Unknown phenotype: {phenotype_id}")

    phenotype = phenotypes[phenotype_id]
    selected = []
    for primitive_id in phenotype["primitive_ids"]:
        try:
            selected.append(primitives[primitive_id])
        except KeyError as exc:
            raise OntologyError(f"{phenotype_id} references missing primitive {primitive_id}") from exc

    lines = []
    for section_id, header in [*SECTIONS, *OPTIONAL_SECTIONS]:
        section_items = [item for item in selected if item["section"] == section_id]
        section_items.sort(key=priority_rank)
        if not section_items:
            if section_id in {item[0] for item in OPTIONAL_SECTIONS}:
                continue
            raise OntologyError(f"{phenotype_id} has no primitives for section {section_id}")

        lines.append(header)
        if section_id in {"home_care", "medications", "return_precautions", "resources"}:
            for item in section_items:
                lines.append(f"- {item['text'][key]}")
        else:
            lines.extend(item["text"][key] for item in section_items)
        lines.append("")

    return "\n".join(lines).strip() + "\n"
