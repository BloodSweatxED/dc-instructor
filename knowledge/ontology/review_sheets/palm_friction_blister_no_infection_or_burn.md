# Palm friction blister without infection or burn red flags

Phenotype ID: `palm_friction_blister_no_infection_or_burn`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated palm friction blister.
- No burn, chemical exposure, infection, diabetic-foot risk when relevant, neurovascular compromise, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Burn or chemical wound, cellulitis or infection concern, open deep wound, diabetic foot when relevant, poor circulation, neuropathy, neurovascular compromise, severe pain, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed wound/podiatry plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Burn or chemical wound.
- Diabetic foot infection when foot-related.
- Neurovascular compromise.

## Primitive List

- `palm_friction_blister_no_infection_or_burn.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_or_chemical_wound, flexor_tenosynovitis_concern, hand_tendon_risk, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_pain, specialist_directed_wound_plan, wound_infection_concern
- `palm_friction_blister_no_infection_or_burn.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_or_chemical_wound, flexor_tenosynovitis_concern, hand_tendon_risk, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_pain, specialist_directed_wound_plan, wound_infection_concern
- `palm_friction_blister_no_infection_or_burn.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_or_chemical_wound, flexor_tenosynovitis_concern, hand_tendon_risk, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_pain, specialist_directed_wound_plan, wound_infection_concern
- `palm_friction_blister_no_infection_or_burn.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_friction_blister_no_infection_or_burn.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_or_chemical_wound, flexor_tenosynovitis_concern, hand_tendon_risk, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_pain, specialist_directed_wound_plan, wound_infection_concern

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated friction blister on the palm.

WHAT WE FOUND:
Your clinician diagnosed a friction blister on the palm. We did not find burn, infection, poor blood flow, deep wound, or another skin emergency today.

WHAT TO DO AT HOME:
- Protect the blister from rubbing or pressure.
- Keep the area clean and dry as your clinician instructed.
- Do not cut or dig into the blister unless your clinician specifically instructed you.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Use creams, ointments, dressings, or padding only as your clinician recommended.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, or worsening swelling.
- New numbness, blue or pale skin, severe pain, black skin, or rapidly worsening symptoms.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, wound care, podiatry if foot-related, or the ED if symptoms are not improving or your clinician told you to recheck.
```
