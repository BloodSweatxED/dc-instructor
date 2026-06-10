# Phase 19 Medication Provenance

Status: implemented as first-pass product metadata.

## Goal

Give the reviewing clinician a faster scan path for medication risk without letting the static ontology generate doses or letting the LLM infer missing prescriptions.

## Provenance Modes

- `ontology_general`: reviewed ontology output with general medication guidance only.
- `clinician_stated_present`: generator output where the ED note contains a known medication name with nearby dose, schedule, or duration text.
- `general_medication_mention_only`: generator output where the ED note mentions medication in broad terms, such as antibiotics or pain medicine, without explicit details.
- `no_clinician_med_details`: generator output where no medication detail is detected in the ED note.

All modes remain passthrough-only and review-required. Medication inference is never allowed.

## Current UI

`src/components/OutputPanel.jsx` displays the provenance label beside the generation mode. This keeps the medication check inside the clinician's copy/edit workflow.

## Limitations

This is a conservative metadata indicator, not a medication reconciliation engine. It does not validate the dose, schedule, indication, allergy status, renal adjustment, pregnancy status, or drug-drug interactions.

Phase 20 should decide whether to add line-level medication markers or keep the current section-level review metadata.
