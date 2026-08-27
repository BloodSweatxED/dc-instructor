# Uncomplicated body ringworm without cellulitis

Phenotype ID: `tinea_corporis_uncomplicated_no_cellulitis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized tinea corporis or body ringworm.
- No cellulitis, abscess, scalp/nail/beard involvement, extensive disease, or immunocompromised-host pathway.

## Exclusions

- Cellulitis, abscess, or secondary infection concern.
- Scalp, nail, beard, groin, or foot fungal pathway requiring different instructions.
- Extensive, recurrent, treatment-failure, or immunocompromised-host disease.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Abscess.
- Tinea capitis requiring oral treatment.
- Immunocompromised-host fungal infection.

## Primitive List

- `tinea_corporis_uncomplicated_no_cellulitis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, scalp_or_nail_or_beard_fungal_infection, groin_or_foot_fungal_pathway, extensive_or_recurrent_fungal_rash, immunocompromised, systemic_illness
- `tinea_corporis_uncomplicated_no_cellulitis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, scalp_or_nail_or_beard_fungal_infection, groin_or_foot_fungal_pathway, extensive_or_recurrent_fungal_rash, immunocompromised, systemic_illness
- `tinea_corporis_uncomplicated_no_cellulitis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, scalp_or_nail_or_beard_fungal_infection, groin_or_foot_fungal_pathway, extensive_or_recurrent_fungal_rash, immunocompromised, systemic_illness
- `tinea_corporis_uncomplicated_no_cellulitis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_corporis_uncomplicated_no_cellulitis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, scalp_or_nail_or_beard_fungal_infection, groin_or_foot_fungal_pathway, extensive_or_recurrent_fungal_rash, immunocompromised, systemic_illness

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit ringworm of the skin, also called tinea corporis.

WHAT WE FOUND:
Your exam was reassuring for a localized fungal skin infection. We did not find signs of cellulitis, an abscess, or a deeper emergency infection today.

WHAT TO DO AT HOME:
- Keep the area clean and dry.
- Avoid sharing towels, clothing, or sports gear until the rash is improving.
- Wash your hands after touching the rash.

MEDICATIONS:
- Use the antifungal cream, spray, or powder exactly as directed on the label or by your clinician.
- Do not use steroid cream on the rash unless your clinician specifically told you to.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, or severe pain.
- The rash spreads quickly, involves the scalp or nails, or keeps coming back.
- You feel very ill or your immune system is weakened.

FOLLOW UP:
Follow up with primary care or dermatology if the rash is not improving with treatment or if it returns.
```
