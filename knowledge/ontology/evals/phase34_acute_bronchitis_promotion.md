# Phase 34 Acute Bronchitis Promotion

`acute_bronchitis_no_pneumonia` is promoted to reviewed runtime content after Phase 32 stress coverage and Phase 33 clinician review.

Runtime mode: `reviewed_ontology_enabled`.

Promotion constraints preserved:

- No broad `cough` standalone term.
- No acute bronchitis catch-all fallback.
- No medication names, doses, schedules, or durations.
- Antibiotic guidance remains stewardship-only unless clinician-entered medication details exist elsewhere.
- Pneumonia concern, hypoxia, respiratory distress, COPD or asthma pathway, immunocompromise, frail elderly status, hemoptysis, PE or cardiac chest-pain concern, sepsis, unstable vitals, and antibiotics prescribed for suspected bacterial infection all block ontology mode.
