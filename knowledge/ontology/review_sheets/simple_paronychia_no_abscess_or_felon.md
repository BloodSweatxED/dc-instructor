# Simple paronychia without abscess or felon

Phenotype ID: `simple_paronychia_no_abscess_or_felon`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of simple paronychia or nail-fold infection.
- No drainable abscess, felon, flexor tenosynovitis concern, spreading cellulitis, diabetes foot pathway, or immunocompromised-host pathway.

## Exclusions

- Abscess, pus pocket, felon, flexor tenosynovitis, deep-space hand infection, or procedure-level drainage plan.
- Spreading cellulitis, systemic illness, diabetes foot risk, peripheral vascular disease, neuropathy, or immunocompromised host.
- Bite wound, crush injury, open fracture, or specialist-directed hand plan.

## Must-Not-Miss Diagnoses

- Felon.
- Flexor tenosynovitis.
- Cellulitis.
- Deep-space hand infection.

## Primitive List

- `simple_paronychia_no_abscess_or_felon.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, felon_or_tenosynovitis_concern, deep_space_location, secondary_skin_infection_concern, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, bite_wound, crush_injury, open_fracture, specialist_directed_wound_plan
- `simple_paronychia_no_abscess_or_felon.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, felon_or_tenosynovitis_concern, deep_space_location, secondary_skin_infection_concern, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, bite_wound, crush_injury, open_fracture, specialist_directed_wound_plan
- `simple_paronychia_no_abscess_or_felon.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, felon_or_tenosynovitis_concern, deep_space_location, secondary_skin_infection_concern, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, bite_wound, crush_injury, open_fracture, specialist_directed_wound_plan
- `simple_paronychia_no_abscess_or_felon.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `simple_paronychia_no_abscess_or_felon.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, felon_or_tenosynovitis_concern, deep_space_location, secondary_skin_infection_concern, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, systemic_illness, bite_wound, crush_injury, open_fracture, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a mild nail-fold infection called paronychia.

WHAT WE FOUND:
Your exam was reassuring enough for home care today. We did not find an abscess, a deep fingertip infection, or spreading cellulitis.

WHAT TO DO AT HOME:
- Soak the finger or toe in warm water if your clinician said this is safe for you.
- Keep the area clean and dry between soaks.
- Do not bite, cut, or dig at the nail fold.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Take antibiotics only if they were prescribed.

RETURN TO ED IF:
- Pus, worsening swelling, spreading redness, fever, or red streaks.
- Severe fingertip pain, a tense swollen finger pad, numbness, or trouble moving the finger.
- Symptoms worsen despite the plan you were given.

FOLLOW UP:
Follow up with primary care, urgent care, or the ED if symptoms are not improving in 1 to 2 days, or sooner if they worsen.
```
