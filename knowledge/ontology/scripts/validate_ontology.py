#!/usr/bin/env python3
from __future__ import annotations

from ontology_lib import SECTIONS, OntologyError, assemble_discharge, load_phenotypes, load_primitives, load_source_cards, read_json, ROOT


REQUIRED_TEXT_KEYS = {"en_4", "en_6", "en_hl1"}
REQUIRED_SECTIONS = {section_id for section_id, _ in SECTIONS}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OntologyError(message)


def validate() -> list[str]:
    source_cards = load_source_cards()
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    messages = []

    for source_id, source in source_cards.items():
        require(source_id == source["id"], f"Source key mismatch for {source_id}")
        require(source["supports"], f"{source_id} needs at least one support statement")

    for primitive_id, primitive in primitives.items():
        require(primitive_id == primitive["id"], f"Primitive key mismatch for {primitive_id}")
        require(set(primitive["text"]) == REQUIRED_TEXT_KEYS, f"{primitive_id} must have en_4, en_6, and en_hl1 text")
        require(primitive["section"] in REQUIRED_SECTIONS, f"{primitive_id} has invalid section {primitive['section']}")
        for source_id in primitive["source_card_ids"]:
            require(source_id in source_cards, f"{primitive_id} references missing source card {source_id}")

    for phenotype_id, phenotype in phenotypes.items():
        require(phenotype_id == phenotype["id"], f"Phenotype key mismatch for {phenotype_id}")
        require(set(phenotype["required_sections"]) == REQUIRED_SECTIONS, f"{phenotype_id} must require all six output sections")
        for source_id in phenotype["source_card_ids"]:
            require(source_id in source_cards, f"{phenotype_id} references missing source card {source_id}")
        for primitive_id in phenotype["primitive_ids"]:
            require(primitive_id in primitives, f"{phenotype_id} references missing primitive {primitive_id}")
            require(phenotype_id in primitives[primitive_id]["phenotypes"], f"{primitive_id} does not list phenotype {phenotype_id}")
        for section_id in REQUIRED_SECTIONS:
            has_section = any(primitives[primitive_id]["section"] == section_id for primitive_id in phenotype["primitive_ids"])
            require(has_section, f"{phenotype_id} has no primitive for section {section_id}")
        messages.append(f"validated phenotype: {phenotype_id}")

    smoke_cases = read_json(ROOT / "evals" / "ontology_smoke_cases.json")
    for case in smoke_cases:
        output = assemble_discharge(case["phenotype"], case["reading_level"])
        lowered = output.lower()
        for section_header in case["must_include_sections"]:
            require(section_header in output, f"{case['id']} missing section {section_header}")
        for term in case["must_include_terms"]:
            require(term.lower() in lowered, f"{case['id']} missing term {term}")
        messages.append(f"smoke passed: {case['id']}")

    return messages


def main() -> int:
    try:
        for message in validate():
            print(message)
    except OntologyError as exc:
        print(f"ontology validation failed: {exc}")
        return 1
    print("ontology validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
