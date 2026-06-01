# Viral pharyngitis, strep negative

Phenotype ID: `viral_pharyngitis_strep_negative`

Status: `reviewed`

## Inclusion Criteria

- Sore throat with negative strep testing and no deep neck infection signs.

## Exclusions

- Peritonsillar abscess concern.
- Epiglottitis concern.
- Immunocompromised host.
- Concern for mono complications.

## Must-Not-Miss Diagnoses

- Peritonsillar abscess.
- Epiglottitis.
- Retropharyngeal abscess.
- Airway compromise.

## Primitive List

- `viral_pharyngitis_strep_negative.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: drooling, trismus, voice_change, airway_symptoms, immunocompromised
- `viral_pharyngitis_strep_negative.home_care.home_care_1.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.home_care.home_care_2.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.home_care.home_care_3.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: drooling, trismus, voice_change, airway_symptoms, immunocompromised
- `viral_pharyngitis_strep_negative.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: drooling, trismus, voice_change, airway_symptoms, immunocompromised
- `viral_pharyngitis_strep_negative.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `viral_pharyngitis_strep_negative.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: drooling, trismus, voice_change, airway_symptoms, immunocompromised

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your sore throat is most consistent with a viral infection.

WHAT WE FOUND:
Your strep test was negative. Your exam did not show signs of a dangerous throat or neck infection today.

WHAT TO DO AT HOME:
- Drink fluids.
- Try warm liquids, honey if safe for you, or throat lozenges.
- Avoid sharing cups and wash your hands often.

MEDICATIONS:
- Antibiotics are not needed for a viral sore throat.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Trouble breathing, drooling, muffled voice, stiff neck, or trouble opening your mouth.
- You cannot swallow fluids.
- Fever or throat pain becomes much worse.

FOLLOW UP:
Follow up with primary care if symptoms are not improving or if your clinician instructed you to recheck.
```
