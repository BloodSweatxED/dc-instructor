# Cervical strain without neurologic deficit

Phenotype ID: `cervical_strain_no_neuro_deficit`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of cervical strain, neck strain, or musculoskeletal neck pain.
- Reassuring neurologic assessment documented.
- No trauma imaging concern, infection, meningitis, vascular emergency, cardiac concern, or specialist-directed spine plan.

## Exclusions

- Fall, crash, high-energy trauma, midline cervical spine tenderness, fracture concern, or intoxication limiting exam.
- New neurologic deficit, weakness, numbness, gait problem, bowel or bladder dysfunction, or spinal cord concern.
- Fever, meningitis concern, epidural abscess or spinal infection concern, chest pain/ACS concern, carotid or vertebral artery dissection concern, or specialist-directed spine plan.

## Must-Not-Miss Diagnoses

- Cervical spine fracture or instability.
- Spinal cord compression.
- Meningitis.
- Spinal epidural abscess.
- Cervical artery dissection.
- Acute coronary syndrome referred pain.

## Primitive List

- `cervical_strain_no_neuro_deficit.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, high_energy_trauma, midline_cervical_tenderness, neurologic_deficit, new_neurologic_deficit, meningitis_or_cns_infection_concern, spinal_infection_concern, chest_pain, cervical_artery_dissection_concern, specialist_directed_spine_plan, unstable_vitals
- `cervical_strain_no_neuro_deficit.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, high_energy_trauma, midline_cervical_tenderness, neurologic_deficit, new_neurologic_deficit, meningitis_or_cns_infection_concern, spinal_infection_concern, chest_pain, cervical_artery_dissection_concern, specialist_directed_spine_plan, unstable_vitals
- `cervical_strain_no_neuro_deficit.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, high_energy_trauma, midline_cervical_tenderness, neurologic_deficit, new_neurologic_deficit, meningitis_or_cns_infection_concern, spinal_infection_concern, chest_pain, cervical_artery_dissection_concern, specialist_directed_spine_plan, unstable_vitals
- `cervical_strain_no_neuro_deficit.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `cervical_strain_no_neuro_deficit.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, high_energy_trauma, midline_cervical_tenderness, neurologic_deficit, new_neurologic_deficit, meningitis_or_cns_infection_concern, spinal_infection_concern, chest_pain, cervical_artery_dissection_concern, specialist_directed_spine_plan, unstable_vitals

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician diagnosed a neck muscle strain.

WHAT WE FOUND:
Your exam was reassuring today. We did not find signs of a nerve injury, spine emergency, infection, or other dangerous cause that needs a different plan.

WHAT TO DO AT HOME:
- Stay gently active as tolerated. Avoid heavy lifting or sudden twisting until you are improving.
- Use heat or ice if it helps your pain.
- Return to normal activity gradually as your neck movement improves.

MEDICATIONS:
- Use only the pain medicine your clinician prescribed or said is safe for you.
- Do not take extra doses or mix sedating medicines unless your clinician told you to.

RETURN TO ED IF:
- New weakness, numbness, trouble walking, loss of bladder or bowel control, or pain shooting down both arms or legs.
- Fever, severe headache, stiff neck with illness, confusion, fainting, chest pain, or trouble breathing.
- Pain after a fall, crash, or other trauma, or pain that is much worse despite the plan.

FOLLOW UP:
Follow up with primary care, occupational medicine, or a spine clinician as instructed if not improving.
```
