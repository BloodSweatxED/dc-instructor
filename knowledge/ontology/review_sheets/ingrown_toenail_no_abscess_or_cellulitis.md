# Ingrown toenail without abscess or cellulitis

Phenotype ID: `ingrown_toenail_no_abscess_or_cellulitis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of ingrown toenail.
- No abscess, cellulitis, diabetic foot concern, poor circulation concern, nail procedure aftercare pathway, or systemic illness.

## Exclusions

- Abscess, cellulitis, pus, fever, or systemic illness.
- Diabetes, poor circulation, immunocompromised host, neuropathy, or diabetic foot pathway.
- Recent nail procedure or specialist-directed podiatry plan.

## Must-Not-Miss Diagnoses

- Toe cellulitis.
- Paronychia or abscess requiring drainage.
- Diabetic foot infection.
- Ischemic toe.

## Primitive List

- `ingrown_toenail_no_abscess_or_cellulitis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, toe_cellulitis_or_pus, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, specialist_directed_podiatry_plan
- `ingrown_toenail_no_abscess_or_cellulitis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, toe_cellulitis_or_pus, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, specialist_directed_podiatry_plan
- `ingrown_toenail_no_abscess_or_cellulitis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, toe_cellulitis_or_pus, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, specialist_directed_podiatry_plan
- `ingrown_toenail_no_abscess_or_cellulitis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ingrown_toenail_no_abscess_or_cellulitis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, toe_cellulitis_or_pus, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an ingrown toenail.

WHAT WE FOUND:
Your exam was reassuring enough for home care today. We did not find an abscess, spreading cellulitis, or another emergency foot problem.

WHAT TO DO AT HOME:
- Soak the foot in warm salty water if your clinician said this is safe for you.
- Keep the foot dry the rest of the day.
- Wear wide, comfortable shoes or sandals.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Take antibiotics only if they were prescribed.

RETURN TO ED IF:
- Pus, spreading redness, fever, chills, or worsening swelling.
- Severe pain, numbness, black or blue skin, or you cannot walk normally.
- You have diabetes, poor circulation, or a weakened immune system and symptoms worsen.

FOLLOW UP:
Follow up with primary care or podiatry if home care is not helping or if this keeps coming back.
```
