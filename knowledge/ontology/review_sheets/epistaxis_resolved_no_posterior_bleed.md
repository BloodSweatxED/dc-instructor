# Resolved nosebleed without posterior bleed concern

Phenotype ID: `epistaxis_resolved_no_posterior_bleed`

Status: `retired`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of epistaxis or nosebleed that resolved before discharge.
- No posterior bleed concern, active bleeding, facial trauma, anticoagulation complication, bleeding disorder, airway issue, or unstable vital signs documented.

## Exclusions

- Posterior epistaxis, ongoing bleeding, packing requiring specific plan, or recurrent severe bleed.
- Anticoagulation complication, bleeding disorder, anemia/syncope concern, unstable vital signs, or airway symptoms.
- Facial or nasal trauma, suspected fracture, or specialist-directed ENT plan.

## Must-Not-Miss Diagnoses

- Posterior epistaxis.
- Hemorrhagic shock.
- Facial fracture.
- Airway compromise.
- Coagulopathy or anticoagulation complication.

## Primitive List

- `epistaxis_resolved_no_posterior_bleed.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, airway_symptoms, unstable_vitals, syncope
- `epistaxis_resolved_no_posterior_bleed.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, airway_symptoms, unstable_vitals, syncope
- `epistaxis_resolved_no_posterior_bleed.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, airway_symptoms, unstable_vitals, syncope
- `epistaxis_resolved_no_posterior_bleed.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `epistaxis_resolved_no_posterior_bleed.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, airway_symptoms, unstable_vitals, syncope

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for a nosebleed that stopped.

WHAT WE FOUND:
Your clinician did not document ongoing bleeding, posterior nosebleed concern, major trauma, or another emergency bleeding problem in these discharge instructions.

WHAT TO DO AT HOME:
- Do not blow or pick your nose today.
- Keep your head above your heart when resting.
- Use the nasal moisture plan your clinician recommended if one was given.

MEDICATIONS:
- Use only nasal sprays or medicines your clinician prescribed or said are safe.
- Do not stop blood thinners unless the clinician who prescribes them tells you to.

RETURN TO ED IF:
- Bleeding starts again and will not stop with firm pressure.
- Blood runs down your throat, you vomit blood, or you have trouble breathing.
- You feel faint, weak, confused, have chest pain, or bleeding follows an injury.

FOLLOW UP:
Follow up with primary care or ENT as instructed, especially if nosebleeds keep happening.
```
