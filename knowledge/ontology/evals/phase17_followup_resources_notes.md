# Phase 17 Follow-Up and Resources Notes

Status: implemented as optional ontology resources.

## Follow-Up Direction

Use follow-up instructions that are generalizable but actionable.

Pattern:

```text
Call your primary care doctor's office. Say, "I was in the emergency department and was diagnosed with [condition]. I need a follow-up visit within [timeframe]."
```

This lets the library stay broadly reusable while giving the patient a concrete script.

## Resources Section

The original product goal includes:

- Findings
- Medications
- Home Care
- Follow-Up
- Return Precautions
- Resources for additional learning

The current ontology renderer has six sections and does not yet render a Resources section. Adding it should be a deliberate renderer/schema/eval change, not a one-off packet edit.

Phase 17 should decide:

- Whether `RESOURCES:` becomes a seventh ontology section.
- Whether resources are generated from source cards.
- Whether resources appear only in the product layer.
- How to avoid overwhelming the patient with article-style links.

## Implementation

Resources are optional `resources` primitives. The six clinical sections remain required.

Resource primitives are generated from reviewed phenotype source cards by:

```text
knowledge/ontology/style/add_followup_resources.py
```

Current pattern:

```text
RESOURCES:
- Learn more: [source] - [title] ([url]).
- Bring these instructions to your follow-up visit.
```

Resources are deliberately short. They are not disease articles copied into the discharge instructions.
