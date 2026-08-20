# Foot contusion without fracture or diabetic-foot red flags

Phenotype ID: `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated foot contusion or bruise.
- No fracture/dislocation concern, neurovascular compromise, severe pain, bleeding-risk plan, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture or dislocation concern, major trauma, open wound, neurovascular compromise, severe pain, compartment concern, or inability to use the area.
- Anticoagulation/bleeding disorder requiring a separate plan, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Neurovascular compromise.
- Compartment syndrome.
- Significant bleeding risk.

## Primitive List

- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, anticoagulated, unable_to_bear_weight_lower_extremity, diabetic_foot, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, anticoagulated, unable_to_bear_weight_lower_extremity, diabetic_foot, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, anticoagulated, unable_to_bear_weight_lower_extremity, diabetic_foot, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_contusion_uncomplicated_no_fracture_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, anticoagulated, unable_to_bear_weight_lower_extremity, diabetic_foot, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated foot bruise.

WHAT WE FOUND:
Your clinician diagnosed a foot bruise. We did not find a fracture, circulation problem, nerve problem, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest the sore area as instructed.
- Use ice or elevation if recommended.
- Avoid activity that clearly worsens the pain until you are improving.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid NSAIDs if your clinician told you not to take them.

RETURN TO ED IF:
- Worsening severe pain, rapidly increasing swelling, numbness, weakness, color change, or trouble using the area.
- New deformity, concern for a broken bone, or pain not improving as expected.
- Easy bleeding, a very large bruise, fever, or new symptoms that worry you.

FOLLOW UP:
Follow up with primary care, orthopedics, urgent care, or the ED if pain is not improving or your clinician told you to recheck.
```
