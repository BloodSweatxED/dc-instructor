#!/usr/bin/env python3
from __future__ import annotations

import argparse

from ontology_lib import OntologyError, assemble_discharge


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble discharge instructions from ontology primitives.")
    parser.add_argument("--phenotype", required=True, help="Phenotype id, such as lumbar_strain_no_red_flags")
    parser.add_argument("--reading-level", default="6", help="One of 4, 6, hl1")
    args = parser.parse_args()

    try:
        print(assemble_discharge(args.phenotype, args.reading_level), end="")
    except OntologyError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
