# Phase 37 Acute Sinusitis Source Plan

Target phenotype: `acute_sinusitis_supportive_care`.

Clinical label: Acute sinusitis supportive care without antibiotic plan.

Source cards:

- `cdc.sinus_infection`
- `medlineplus.sinusitis`
- `cdc.antibiotic_use_adult_outpatient`

Proposed inclusion boundary:

- Adult with clinician diagnosis or discharge impression of acute sinusitis, sinus infection, or acute rhinosinusitis.
- Discharge plan is supportive care without clinician-entered antibiotic instructions.
- No orbital, intracranial, dental, facial trauma, sepsis, airway, or admission concern.
- No chronic or recurrent sinusitis pathway.

Proposed hard blockers:

- `antibiotic_prescribed_for_sinusitis`
- `severe_bacterial_sinusitis_features`
- `orbital_or_intracranial_sinusitis_concern`
- `dental_or_facial_trauma_source`
- `immunocompromised`
- `elderly_frail`
- `pregnancy`
- `sepsis`
- `unstable_vitals`
- `chronic_or_recurrent_sinusitis`

Harvest risks to avoid:

- Do not say antibiotics are never needed.
- Do not give medication names, doses, schedules, or durations unless clinician-entered medication details exist.
- Do not promise a fixed symptom duration.
- Do not use broad congestion, facial pain, or cold symptoms as standalone runtime terms.
- Do not use sinusitis as a fallback for unmatched URI complaints.
