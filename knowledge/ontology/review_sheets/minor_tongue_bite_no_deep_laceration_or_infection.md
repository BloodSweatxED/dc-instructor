# Minor tongue bite without deep laceration or infection red flags

Phenotype ID: `minor_tongue_bite_no_deep_laceration_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of minor tongue bite injury.
- No deep laceration requiring repair, uncontrolled bleeding, dental/facial trauma pathway, infection, airway symptoms, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Deep laceration or repair needed, uncontrolled bleeding, dental/facial trauma source, airway symptoms, deep-space swelling, infection concern, severe pain, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed wound/oral surgery plan.

## Must-Not-Miss Diagnoses

- Airway swelling.
- Deep laceration requiring repair.
- Dental or facial trauma.
- Wound infection.

## Primitive List

- `minor_tongue_bite_no_deep_laceration_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, laceration_repair_needed, dental_or_facial_trauma_source, wound_infection_concern, severe_pain, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_tongue_bite_no_deep_laceration_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, laceration_repair_needed, dental_or_facial_trauma_source, wound_infection_concern, severe_pain, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_tongue_bite_no_deep_laceration_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, laceration_repair_needed, dental_or_facial_trauma_source, wound_infection_concern, severe_pain, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_tongue_bite_no_deep_laceration_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_tongue_bite_no_deep_laceration_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, laceration_repair_needed, dental_or_facial_trauma_source, wound_infection_concern, severe_pain, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a minor tongue bite injury.

WHAT WE FOUND:
Your clinician diagnosed a minor tongue bite injury. We did not find a deep laceration, uncontrolled bleeding, dental or facial trauma emergency, infection, or airway concern today.

WHAT TO DO AT HOME:
- Use gentle mouth care as your clinician instructed.
- Avoid irritating foods or activities until it feels better.
- Do not use leftover antibiotic, steroid, or numbing medicine unless your clinician told you to.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Use rinses, ointments, or other treatment only if your clinician recommended it.

RETURN TO ED IF:
- Trouble breathing, trouble swallowing, drooling, throat swelling, or tongue swelling.
- Bleeding that will not stop, rapidly worsening swelling, pus, fever, or severe pain.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, dental/oral surgery if instructed, or the ED if symptoms are not improving or your clinician told you to recheck.
```
