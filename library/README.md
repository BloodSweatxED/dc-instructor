# DC Instructor discharge instruction library

This directory contains exported patient-facing discharge instructions from
reviewed ontology phenotypes.

Files are organized as:

```text
library/<phenotype_id>/en_4th.md
library/<phenotype_id>/en_6th.md
library/<phenotype_id>/en_HL1.md
```

Only phenotypes marked `reviewed` in
`knowledge/ontology/runtime/ontology_manifest.json` are exported. Retired and
draft phenotypes are intentionally excluded.

Regenerate with:

```bash
knowledge/.venv/bin/python knowledge/ontology/scripts/export_reviewed_library.py
```

Validate that `library/` still matches reviewed ontology assembly with:

```bash
knowledge/.venv/bin/python knowledge/ontology/scripts/validate_reviewed_library.py
```
