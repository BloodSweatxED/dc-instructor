# Resolved anterior nosebleed without packing or anticoagulation red flags

Phenotype ID: `anterior_epistaxis_resolved_no_packing_or_anticoagulation`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated resolved anterior nosebleed.
- No emergency red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Red flags requiring a separate ED pathway, unstable vital signs, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Posterior or severe bleeding.
- Deep infection.
- Foreign body or trauma.
- High-risk host complication.

## Primitive List

- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, posterior_epistaxis_or_uncontrolled_bleeding, unstable_vitals
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, posterior_epistaxis_or_uncontrolled_bleeding, unstable_vitals
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, posterior_epistaxis_or_uncontrolled_bleeding, unstable_vitals
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `anterior_epistaxis_resolved_no_packing_or_anticoagulation.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: posterior_epistaxis_or_uncontrolled_bleeding, anticoagulated, bleeding_disorder, facial_or_nasal_trauma, posterior_epistaxis_or_uncontrolled_bleeding, unstable_vitals

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated resolved anterior nosebleed.

WHAT WE FOUND:
Your clinician diagnosed resolved anterior nosebleed. We did not find red flags requiring a separate emergency pathway today.

WHAT TO DO AT HOME:
- Avoid picking, probing, or putting objects into the affected area.
- Use the care plan your clinician recommended.
- Keep follow-up if your clinician asked for recheck.

MEDICATIONS:
- Use medicines only if prescribed or recommended.
- Do not add leftover antibiotics, drops, sprays, or packing care unless your clinician told you to.

RETURN TO ED IF:
- Bleeding that will not stop, worsening pain, fever, swelling, or feeling very ill.
- Dizziness, fainting, severe headache, trouble breathing, or new neurologic symptoms.
- Symptoms that recur, worsen, or do not improve as expected.

FOLLOW UP:
Follow up with primary care, ENT, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
