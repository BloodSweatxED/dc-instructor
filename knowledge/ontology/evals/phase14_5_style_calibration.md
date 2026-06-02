# Phase 14.5 Style Calibration

Status: started.

The Phase 13 ontology promotion preserved safety gates, but the asthma comparison showed a voice regression. The ontology output was safe and readable, but too thin compared with the live DC Instructor tool.

## Decision

Use the live DC Instructor tool as the style baseline.

Use MedlinePlus, CDC, and other source cards as evidence guardrails only. They should not make the output sound like public-health library prose.

## First Calibrated Phenotype

`asthma_exacerbation_improved_discharge`

Changes:

- Restored ED-course narrative in `WHAT WE FOUND`.
- Changed diagnosis to patient-language flare-up wording.
- Added concrete home-care actions from the live output while avoiding unsupported medication dosing.
- Kept medication dosing out of static ontology primitives.
- Made return precautions closer to the live ED-output cadence.
- Added a local-policy-sensitive follow-up interval for review.

## Remaining Work

Before adding new phenotypes, collect or author golden outputs for the other reviewed phenotypes and run the same calibration:

- `community_acquired_pneumonia_outpatient`
- `minor_head_injury_no_red_flags`
- `concussion_discharge_no_imaging_red_flags`
- `renal_colic_stable_no_infection`
- the 11 earlier reviewed phenotypes

Medication policy remains separate. The style layer should not invent doses.

## Phase 15 Update

Phase 15 adds a reproducible style overlay for the expanded reviewed packs in `knowledge/ontology/style/apply_style_calibration.py`.

The overlay is intentionally separate from source-card generation:

- Source cards answer: "Is this concept supported?"
- Style calibration answers: "Does this sound like DC Instructor?"
- Product tailoring answers: "What did this specific patient need, receive, and get prescribed?"
