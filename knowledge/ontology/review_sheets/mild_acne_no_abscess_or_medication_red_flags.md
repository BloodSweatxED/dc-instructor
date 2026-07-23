# Mild acne without abscess or medication red flags

Phenotype ID: `mild_acne_no_abscess_or_medication_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of mild acne.
- No abscess, cellulitis, severe cystic/nodular disease, severe cutaneous adverse reaction, pregnancy medication issue, systemic illness, or specialist-directed medication plan.

## Exclusions

- Abscess, cellulitis, severe cystic/nodular acne, rapidly worsening swelling, systemic illness, or severe cutaneous adverse reaction.
- Pregnancy medication decision, isotretinoin/teratogenic medication issue, immunocompromised host, pediatric pathway, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Abscess.
- Cellulitis.
- Severe cutaneous adverse reaction.
- Pregnancy medication risk.

## Primitive List

- `mild_acne_no_abscess_or_medication_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, acne_severe_or_medication_sensitive, rapid_progression, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `mild_acne_no_abscess_or_medication_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, acne_severe_or_medication_sensitive, rapid_progression, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `mild_acne_no_abscess_or_medication_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, acne_severe_or_medication_sensitive, rapid_progression, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `mild_acne_no_abscess_or_medication_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_acne_no_abscess_or_medication_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, acne_severe_or_medication_sensitive, rapid_progression, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit mild acne.

WHAT WE FOUND:
Your clinician diagnosed mild acne. We did not find abscess, cellulitis, severe cystic disease, medication emergency, or systemic illness today.

WHAT TO DO AT HOME:
- Wash skin gently and avoid scrubbing.
- Do not pick, squeeze, or pop pimples.
- Use non-comedogenic skin products when possible.

MEDICATIONS:
- Use acne medicine only if prescribed or recommended, and follow the label.
- Stop a product and seek care if you develop severe irritation, swelling, blistering, or peeling.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus pocket, severe pain, or rapidly worsening swelling.
- Skin peeling, mouth sores, target-like rash, facial swelling, or trouble breathing after a medicine.
- Severe cysts, scarring, pregnancy medication concerns, or symptoms not improving with the plan.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms are severe, scarring, worsening, or not improving.
```
