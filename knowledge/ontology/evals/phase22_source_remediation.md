# Phase 22 Source Remediation

Status: complete for source-gap cleanup; promotion still blocked.

## Decisions

- `chest_pain_low_risk_negative_ed_workup` is retired as static ontology content.
- Chest pain should stay product-layer fallback unless rebuilt as a much narrower reviewed phenotype.
- `abdominal_pain_nonspecific_reassuring_workup` received source-card support but remains draft.
- Abdominal pain should not enter reviewed ontology mode until narrowed, stress-tested, and clinician-reviewed.

## Source Cards Added

- `medlineplus.abdominal_pain`
- `medlineplus.abdominal_pain_ency`
- `aha.chest_pain_warning_signs`

## Gate Result

- Reviewed runtime clean: true.
- Draft source gaps: 0.
- Active draft phenotypes: 1.
- Phenotype expansion allowed: false.

## Next Phase

Phase 23 should decide the abdominal-pain path:

1. Retire it as product-layer fallback, or
2. Narrow it into a reviewable recheck/return-precaution phenotype.
