# Uncomplicated cellulitis treated as outpatient V1 Review Packet

Phenotype ID: `cellulitis_uncomplicated_oral_antibiotics`

Clinical status: reviewed_for_limited_uncomplicated_outpatient_cellulitis_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

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

## Source Audit

- `medlineplus.cellulitis` supports this phenotype's reviewed concepts.
- `cdc.group_a_strep_cellulitis` supports this phenotype's reviewed concepts.
- MedlinePlus and CDC support cellulitis treatment framing, antibiotic use when clinically indicated, and escalation for worsening or severe infection.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `immunocompromised`
- `rapid_progression`
- `diabetic_foot`
- `bite_wound`
- `near_eye_or_genitals`
- `sepsis`
- `necrotizing_infection_concern`
- `deep_space_location`

## Primitive List

- `cellulitis_uncomplicated_oral_antibiotics.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `cellulitis_uncomplicated_oral_antibiotics.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `cellulitis_uncomplicated_oral_antibiotics.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `cellulitis_uncomplicated_oral_antibiotics.resources.source_link_1.v1` | `resources` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.resources.source_link_2.v1` | `resources` | audit: source_supported
- `cellulitis_uncomplicated_oral_antibiotics.resources.followup_reminder.v1` | `resources` | audit: source_supported

## Patient-Facing Output

```text
DIAGNOSIS:
You were treated for cellulitis, which is a skin infection.

WHAT WE FOUND:
You came to the ED for redness, pain, or swelling of the skin. Your exam fit cellulitis that can be treated at home. We did not find signs of a deeper emergency infection.

WHAT TO DO AT HOME:
- Keep the area clean and dry.
- Raise the arm or leg above heart level as much as possible, including when sleeping.
- Mark the edge of the redness if your clinician asked you to. Take a phone photo of the marked border so you can tell if it is spreading.

MEDICATIONS:
- Take the antibiotic as prescribed. Do not stop early unless a clinician or pharmacist tells you to.
- Use acetaminophen or ibuprofen only if it is safe for you and follow the label.

RETURN TO ED IF:
- Come back for fever, shaking chills, confusion, or feeling very sick.
- Come back if redness spreads fast, pain becomes severe, you notice numbness, pus, or red streaks.
- Come back if the infection is near the eye, genitals, or a joint and gets worse.

FOLLOW UP:
Call your primary care doctor's office or clinic. Say, "I was in the emergency department and was diagnosed with cellulitis. I need a follow-up visit within 48-72 hours."

RESOURCES:
- Bring these instructions to your follow-up visit.
- Learn more: MedlinePlus - Cellulitis (https://medlineplus.gov/cellulitis.html).
- Learn more: CDC - Clinical Guidance for Group A Streptococcal Cellulitis (https://www.cdc.gov/group-a-strep/hcp/clinical-guidance/cellulitis.html).
```
