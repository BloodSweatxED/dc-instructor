# Phase 16 Medication Policy Boundary

Status: approved for implementation.

## Policy

Static ontology primitives must not contain medication dose, route, frequency, or duration.

The DC Instructor product layer may pass through medication details only when they are explicitly present in the clinician-entered ED note. Passthrough means formatting what the clinician already wrote. It does not mean inference.

If the note says:

```text
amoxicillin-clavulanate 875 mg twice daily for 7 days
```

The product may include that medication instruction.

If the note says:

```text
start antibiotics
```

The product must not choose an antibiotic, dose, schedule, or duration.

## Banner

The medication verification banner is non-negotiable:

```text
Review before giving to patient. Verify medications, doses, and follow-up instructions.
```

It should remain prominent in the UI. It is a checkpoint, not a footer disclaimer.

## Ontology Wording

Use prescription-referential language:

- Take the antibiotic as listed on your prescription.
- Take prescribed pain or nausea medicine only as directed.
- If tamsulosin was prescribed, it relaxes the ureter and may help the stone pass.

Avoid static dosing language.

## Future Product-Layer Flag

Add a future medication provenance indicator:

- clinician-stated medication
- ontology general medication advice
- model-generated medication text requiring extra review

This gives clinicians a faster scan path when reviewing output.
