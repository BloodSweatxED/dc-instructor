# Viral pharyngitis, strep negative V1 Review Packet

Phenotype ID: `viral_pharyngitis_strep_negative`

Clinical status: reviewed_for_limited_strep_negative_viral_pharyngitis_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

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

## Source Audit

- `cdc.sore_throat_basics` supports this phenotype's reviewed concepts.
- `cdc.group_a_strep_pharyngitis` supports this phenotype's reviewed concepts.
- CDC supports viral sore throat antibiotic stewardship and group A strep testing distinctions, including not treating viral pharyngitis with antibiotics.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `drooling`
- `trismus`
- `voice_change`
- `airway_symptoms`
- `immunocompromised`
- `peritonsillar_abscess_concern`
- `epiglottitis_concern`
- `mono_complication_concern`
- `positive_strep_test`
- `antibiotic_prescribed`

## Primitive List

- `viral_pharyngitis_strep_negative.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `viral_pharyngitis_strep_negative.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `viral_pharyngitis_strep_negative.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `viral_pharyngitis_strep_negative.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `viral_pharyngitis_strep_negative.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `viral_pharyngitis_strep_negative.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `viral_pharyngitis_strep_negative.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `viral_pharyngitis_strep_negative.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `viral_pharyngitis_strep_negative.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `viral_pharyngitis_strep_negative.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `viral_pharyngitis_strep_negative.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `viral_pharyngitis_strep_negative.resources.source_link_1.v1` | `resources` | audit: source_supported
- `viral_pharyngitis_strep_negative.resources.source_link_2.v1` | `resources` | audit: source_supported
- `viral_pharyngitis_strep_negative.resources.followup_reminder.v1` | `resources` | audit: source_supported

## Patient-Facing Output

```text
DIAGNOSIS:
Your sore throat is most consistent with a viral infection.

WHAT WE FOUND:
You came to the ED for a sore throat. Your strep test was negative, and your exam did not show signs of a dangerous throat or neck infection today.

WHAT TO DO AT HOME:
- Drink fluids.
- Try warm liquids, honey if safe for you, or throat lozenges.
- Avoid sharing cups and wash your hands often.

MEDICATIONS:
- Antibiotics are not needed for a viral sore throat.
- Use acetaminophen or ibuprofen only if it is safe for you and follow the label.

RETURN TO ED IF:
- Come back right away for trouble breathing, drooling, muffled voice, stiff neck, or trouble opening your mouth.
- Come back if you cannot swallow fluids.
- Come back if fever or throat pain becomes much worse.

FOLLOW UP:
Call your primary care doctor's office or clinic. Say, "I was in the emergency department and was diagnosed with a viral sore throat. I need a follow-up visit within 1 week if symptoms are not improving."

RESOURCES:
- Bring these instructions to your follow-up visit.
- Learn more: CDC - Sore Throat Basics (https://www.cdc.gov/sore-throat/about/index.html).
- Learn more: CDC - Clinical Guidance for Group A Streptococcal Pharyngitis (https://www.cdc.gov/group-a-strep/hcp/clinical-guidance/strep-throat.html).
```
