# Uncomplicated cellulitis treated as outpatient

Phenotype ID: `cellulitis_uncomplicated_oral_antibiotics`

Status: `draft`

## Inclusion Criteria

- Localized cellulitis judged safe for outpatient therapy.
- No shock, necrotizing infection concern, or deep-space infection concern.

## Exclusions

- Sepsis or unstable vital signs.
- Necrotizing soft tissue infection concern.
- Diabetic foot infection, bite wound, or immunocompromised host requiring a separate pathway.

## Must-Not-Miss Diagnoses

- Necrotizing soft tissue infection.
- Abscess needing drainage.
- Sepsis.
- Septic joint when over a joint.

## Primitive List

- `cellulitis_uncomplicated_oral_antibiotics.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: immunocompromised, rapid_progression, diabetic_foot, bite_wound, near_eye_or_genitals
- `cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_1.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_2.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_3.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.medications.medication_guidance_1.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: immunocompromised, rapid_progression, diabetic_foot, bite_wound, near_eye_or_genitals
- `cellulitis_uncomplicated_oral_antibiotics.medications.medication_guidance_2.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: immunocompromised, rapid_progression, diabetic_foot, bite_wound, near_eye_or_genitals
- `cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `cellulitis_uncomplicated_oral_antibiotics.follow_up.default_follow_up.v1` | `follow_up` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: immunocompromised, rapid_progression, diabetic_foot, bite_wound, near_eye_or_genitals

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for a skin infection called cellulitis.

WHAT WE FOUND:
Your exam fits a skin infection that is safe to treat at home today. We did not find signs of a deeper emergency infection.

WHAT TO DO AT HOME:
- Keep the area clean and dry.
- Raise the arm or leg when you can.
- Mark the edge of redness if your clinician asks you to.

MEDICATIONS:
- Take the antibiotic exactly as prescribed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, shaking chills, confusion, or feeling very ill.
- Redness spreading fast, severe pain, numbness, pus, or red streaks.
- The infection is near the eye, genitals, or a joint and gets worse.

FOLLOW UP:
Arrange recheck with primary care, urgent care, or the ED as instructed, especially if not improving.
```
