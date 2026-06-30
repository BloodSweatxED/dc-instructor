# Acute sinusitis supportive care without antibiotic plan

Phenotype ID: `acute_sinusitis_supportive_care`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of acute sinusitis, sinus infection, or acute rhinosinusitis.
- Supportive-care discharge plan without clinician-entered antibiotic instructions.
- No orbital, intracranial, dental, facial trauma, sepsis, or airway emergency concern.
- No chronic or recurrent sinusitis pathway.

## Exclusions

- Antibiotics prescribed for sinusitis or suspected bacterial sinus infection.
- Severe bacterial sinusitis features requiring clinician-specific antibiotic or watchful-waiting decision.
- Orbital or intracranial complication concern, including eye swelling, vision change, severe headache with neurologic symptoms, meningitis concern, or altered mental status.
- Dental source, facial trauma, immunocompromise, sepsis, unstable vital signs, pregnancy, or frail elderly patient requiring individualized planning.
- Chronic, recurrent, fungal, post-surgical, or ENT-directed sinusitis pathway.

## Must-Not-Miss Diagnoses

- Orbital cellulitis.
- Intracranial infection.
- Meningitis.
- Dental abscess.
- Sepsis.
- Facial trauma.

## Primitive List

- `acute_sinusitis_supportive_care.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: antibiotic_prescribed_for_sinusitis, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, dental_or_facial_trauma_source, immunocompromised, elderly_frail, pregnancy, sepsis, unstable_vitals, chronic_or_recurrent_sinusitis
- `acute_sinusitis_supportive_care.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: antibiotic_prescribed_for_sinusitis, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, dental_or_facial_trauma_source, immunocompromised, elderly_frail, pregnancy, sepsis, unstable_vitals, chronic_or_recurrent_sinusitis
- `acute_sinusitis_supportive_care.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: antibiotic_prescribed_for_sinusitis, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, dental_or_facial_trauma_source, immunocompromised, elderly_frail, pregnancy, sepsis, unstable_vitals, chronic_or_recurrent_sinusitis
- `acute_sinusitis_supportive_care.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_sinusitis_supportive_care.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: antibiotic_prescribed_for_sinusitis, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, dental_or_facial_trauma_source, immunocompromised, elderly_frail, pregnancy, sepsis, unstable_vitals, chronic_or_recurrent_sinusitis

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit acute sinusitis, also called a sinus infection.

WHAT WE FOUND:
Your clinician did not document an emergency sinus complication or a need for an antibiotic plan in these discharge instructions.

WHAT TO DO AT HOME:
- Drink fluids if you are allowed to and rest as needed.
- Use saline spray or humidified air if it helps congestion.
- A warm compress over the sore sinus area may help pressure.

MEDICATIONS:
- Use only the medicines your clinician prescribed or said are safe for you.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Trouble breathing, confusion, fainting, stiff neck, severe headache, or feeling very ill.
- Swelling around the eye, vision changes, double vision, or pain with eye movement.
- Fever, worsening facial pain, or symptoms that get much worse after initially improving.

FOLLOW UP:
Follow up with primary care or ENT as instructed, especially if symptoms are not improving or keep coming back.
```
