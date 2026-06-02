# Abscess after incision and drainage V1 Review Packet

Phenotype ID: `abscess_after_i_and_d`

Clinical status: reviewed_for_limited_abscess_after_ed_drainage_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

## Inclusion Criteria

- Abscess drained in the ED and patient discharged.
- No deep-space infection or sepsis concern.

## Exclusions

- Deep hand, face, neck, breast, genital, or perirectal abscess pathway.
- Sepsis or immunocompromised host needing separate planning.

## Must-Not-Miss Diagnoses

- Necrotizing infection.
- Deep-space infection.
- Sepsis.
- Retained foreign body.

## Source Audit

- `medlineplus.skin_abscess` supports this phenotype's reviewed concepts.
- MedlinePlus supports skin abscess symptoms, pus drainage, fever or chills, and need to seek care for new symptoms after treatment.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `deep_space_location`
- `immunocompromised`
- `packing_required`
- `recurrent_abscess`
- `sepsis`
- `necrotizing_infection_concern`

## Primitive List

- `abscess_after_i_and_d.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `abscess_after_i_and_d.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `abscess_after_i_and_d.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `abscess_after_i_and_d.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `abscess_after_i_and_d.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `abscess_after_i_and_d.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `abscess_after_i_and_d.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `abscess_after_i_and_d.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `abscess_after_i_and_d.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `abscess_after_i_and_d.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `abscess_after_i_and_d.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `abscess_after_i_and_d.resources.source_link_1.v1` | `resources` | audit: source_supported
- `abscess_after_i_and_d.resources.followup_reminder.v1` | `resources` | audit: source_supported

## Patient-Facing Output

```text
DIAGNOSIS:
You had an abscess, which is a pocket of pus under the skin.

WHAT WE FOUND:
You came to the ED because the area was painful and swollen. We opened and drained the abscess, which is the main treatment. You were safe to go home with wound care instructions.

WHAT TO DO AT HOME:
- Keep the dressing clean and dry today.
- Wash your hands before and after touching the wound.
- Do not squeeze, dig into, or try to drain the wound again at home.

MEDICATIONS:
- Take antibiotics only if they were prescribed.
- Use pain medicine only if it is safe for you and follow the label or your clinician's instructions.

RETURN TO ED IF:
- Come back for fever, spreading redness, red streaks, worsening swelling, or feeling very sick.
- Come back for severe pain, numbness, bleeding that will not stop, or pus building back up.
- Come back if packing falls out early and you were told it needed to stay in.

FOLLOW UP:
Call your primary care doctor's office or clinic. Say, "I was in the emergency department and was diagnosed with an abscess that was drained. I need a follow-up visit as instructed for a wound check."

RESOURCES:
- Bring these instructions to your follow-up visit.
- Learn more: MedlinePlus - Skin abscess (https://medlineplus.gov/ency/article/000863.htm).
```
