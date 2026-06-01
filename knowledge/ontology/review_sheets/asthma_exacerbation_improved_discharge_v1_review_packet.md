# Asthma exacerbation improved for discharge V1 Review Packet

Phenotype ID: `asthma_exacerbation_improved_discharge`

Clinical status: reviewed_for_limited_improved_asthma_exacerbation_discharge_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

## Inclusion Criteria

- Asthma flare improved after ED treatment and safe for outpatient plan.

## Exclusions

- Persistent hypoxia.
- Impending respiratory failure.
- Pneumonia or pulmonary embolism concern.
- No access to rescue medication.

## Must-Not-Miss Diagnoses

- Respiratory failure.
- Pneumonia.
- Pneumothorax.
- Pulmonary embolism mimic.

## Source Audit

- `medlineplus.asthma` supports this phenotype's reviewed concepts.
- MedlinePlus supports asthma symptoms, flare-up framing, trigger avoidance, prescribed inhaler use, and escalation for severe or life-threatening attacks.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `hypoxia`
- `poor_inhaler_access`
- `pregnancy`
- `chest_pain`
- `frequent_relapse`
- `respiratory_distress`

## Primitive List

- `asthma_exacerbation_improved_discharge.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `asthma_exacerbation_improved_discharge.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `asthma_exacerbation_improved_discharge.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `asthma_exacerbation_improved_discharge.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `asthma_exacerbation_improved_discharge.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `asthma_exacerbation_improved_discharge.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `asthma_exacerbation_improved_discharge.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `asthma_exacerbation_improved_discharge.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `asthma_exacerbation_improved_discharge.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `asthma_exacerbation_improved_discharge.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `asthma_exacerbation_improved_discharge.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier

## Patient-Facing Output

```text
DIAGNOSIS:
You were treated for an asthma flare.

WHAT WE FOUND:
Your breathing improved enough for discharge today. Asthma can worsen again, so use the plan you were given closely.

WHAT TO DO AT HOME:
- Avoid smoke, fumes, and known triggers.
- Use your spacer if one was prescribed.
- Rest and avoid heavy exertion until breathing is back to baseline.

MEDICATIONS:
- Use your rescue inhaler exactly as prescribed.
- Take steroids or controller medicines exactly as prescribed.

RETURN TO ED IF:
- Shortness of breath at rest, blue lips, severe wheezing, or trouble speaking full sentences.
- Rescue inhaler is not helping or you need it much more often than instructed.
- Chest pain, fainting, confusion, or worsening symptoms.

FOLLOW UP:
Follow up with primary care, pulmonology, or asthma clinic as instructed.
```
