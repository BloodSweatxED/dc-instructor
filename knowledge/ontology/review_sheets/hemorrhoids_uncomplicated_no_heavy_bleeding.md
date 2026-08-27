# Uncomplicated hemorrhoids without heavy bleeding or infection concern

Phenotype ID: `hemorrhoids_uncomplicated_no_heavy_bleeding`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of hemorrhoids.
- No heavy bleeding, unstable vital signs, infection concern, severe abdominal pain, or alternate GI bleeding pathway.
- Medication and procedural instructions are clinician-entered.

## Exclusions

- Heavy bleeding, anticoagulation with bleeding, syncope, unstable vital signs, anemia concern, or bleeding disorder.
- Severe anal pain with fever, abdominal pain, diarrhea, spreading perianal redness, or abscess concern.
- Thrombosed hemorrhoid, irreducible prolapse, rectal mass, malignancy concern, inflammatory bowel disease concern, or new rectal bleeding requiring separate workup.
- Pregnancy, immunocompromise, or poor follow-up.

## Must-Not-Miss Diagnoses

- Lower GI bleeding.
- Perianal or perirectal abscess.
- Fournier gangrene.
- Thrombosed or strangulated hemorrhoid.
- Colorectal malignancy.
- Inflammatory bowel disease.

## Primitive List

- `hemorrhoids_uncomplicated_no_heavy_bleeding.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hemorrhoid_heavy_bleeding, anticoagulated, bleeding_disorder, anemia_concern, syncope, unstable_vitals, gi_bleeding, severe_or_focal_abdominal_pain, fever, perianal_sepsis_or_abscess_concern, hemorrhoid_thrombosis_or_irreducible_prolapse, cancer_red_flag, inflammatory_bowel_disease_concern, pregnancy, immunocompromised, poor_follow_up
- `hemorrhoids_uncomplicated_no_heavy_bleeding.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hemorrhoid_heavy_bleeding, anticoagulated, bleeding_disorder, anemia_concern, syncope, unstable_vitals, gi_bleeding, severe_or_focal_abdominal_pain, fever, perianal_sepsis_or_abscess_concern, hemorrhoid_thrombosis_or_irreducible_prolapse, cancer_red_flag, inflammatory_bowel_disease_concern, pregnancy, immunocompromised, poor_follow_up
- `hemorrhoids_uncomplicated_no_heavy_bleeding.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hemorrhoid_heavy_bleeding, anticoagulated, bleeding_disorder, anemia_concern, syncope, unstable_vitals, gi_bleeding, severe_or_focal_abdominal_pain, fever, perianal_sepsis_or_abscess_concern, hemorrhoid_thrombosis_or_irreducible_prolapse, cancer_red_flag, inflammatory_bowel_disease_concern, pregnancy, immunocompromised, poor_follow_up
- `hemorrhoids_uncomplicated_no_heavy_bleeding.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hemorrhoids_uncomplicated_no_heavy_bleeding.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hemorrhoid_heavy_bleeding, anticoagulated, bleeding_disorder, anemia_concern, syncope, unstable_vitals, gi_bleeding, severe_or_focal_abdominal_pain, fever, perianal_sepsis_or_abscess_concern, hemorrhoid_thrombosis_or_irreducible_prolapse, cancer_red_flag, inflammatory_bowel_disease_concern, pregnancy, immunocompromised, poor_follow_up

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for hemorrhoids.

WHAT WE FOUND:
Your clinician found hemorrhoids and did not find signs of heavy bleeding, infection, or another emergency cause today.

WHAT TO DO AT HOME:
- Avoid straining on the toilet.
- Drink fluids and add fiber as tolerated to keep stool soft.
- Warm sitz baths may help discomfort.

MEDICATIONS:
- Use hemorrhoid creams, suppositories, stool softeners, or pain medicine only as prescribed or recommended by your clinician.
- Do not use extra laxatives or rectal medicines unless your clinician told you to.

RETURN TO ED IF:
- Heavy rectal bleeding, dizziness, fainting, or weakness.
- Severe or worsening anal pain, fever, spreading redness, pus, or foul odor.
- Belly pain with rectal bleeding, black stool, or blood mixed throughout the stool.

FOLLOW UP:
Follow up with primary care, gastroenterology, or surgery as instructed, especially if symptoms do not improve.
```
