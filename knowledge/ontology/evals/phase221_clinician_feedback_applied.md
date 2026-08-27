# Phase 221 Clinician Feedback Applied

Date: 2026-06-03

Source: structured clinician feedback on the three Phase 216 review-ready drafts.

Decision after Phase 222:

- All three were promoted after final cleanup.
- Modifier disposition is documented in `phase222_promotion_decision.md`.
- Revisions were encoded for language specificity, follow-up timing, and high-risk runtime modifiers.

## 1. Simple Skin Avulsion Or Abrasion

Phenotype ID: `skin_avulsion_or_abrasion_simple`

Feedback status: promoted after modifier disposition was confirmed.

Encoded changes:

- Replaced vague wound red flag wording.
- Replaced "while the skin is closing" with "while the skin heals."
- Sharpened ischemic color-change language.
- Rewrote retained-foreign-body return precaution as active patient concern.
- Anchored follow-up to lack of improvement after 2 to 3 days.
- Added runtime modifiers for diabetes, peripheral vascular disease, anticoagulation, and delayed wound presentation.

```text
DIAGNOSIS:
Your clinician diagnosed a simple skin abrasion, skin tear, or skin avulsion.

WHAT WE FOUND:
Your clinician documented a superficial skin wound without a repair need, retained foreign body concern, deep structure injury, infection concern, or other wound concern.

WHAT TO DO AT HOME:
- Keep the wound clean and follow the dressing plan your clinician gave you.
- Do not scrub, pick, or peel the injured skin.
- Protect the area from friction, soaking, or another injury while the skin heals.
- Many abrasions heal new surface skin within 7 to 14 days. Skin tears and avulsions, especially in older adults, can take longer.

MEDICATIONS:
- Use only the dressing supplies, ointment, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- Bleeding that will not stop with firm pressure or the wound starts opening wider.
- New numbness, weakness, skin turning pale, blue, or very dark, trouble moving the area, or if you think something may still be inside the wound.

FOLLOW UP:
Follow up with primary care, urgent care, wound clinic, or the ED if the wound is not improving after 2 to 3 days, or sooner if your clinician gave a specific schedule.
```

Disposition:

- Immunocompromised remains a true v1 blocker.
- Diabetes, PVD, anticoagulation, and clean delayed presentation are output modifiers.

## 2. Acute Otitis Media

Phenotype ID: `acute_otitis_media_uncomplicated`

Feedback status: promoted after final language fix and modifier-scope confirmation.

Encoded changes:

- Rewrote internal "ear canal infection pathway" language.
- Rewrote fluid advice in plainer language.
- Split recovery timeline for antibiotics vs watchful waiting.
- Replaced "often" with "typically."
- Added mild ear fullness or muffled hearing duration.
- Replaced "high fever" and "looking seriously ill."
- Sharpened dizziness language.
- Split follow-up timing by antibiotic vs watchful-waiting pathway.
- Restored frail elderly as runtime modifier.
- Added diabetes and unreliable watchful-waiting follow-up modifiers.

```text
DIAGNOSIS:
Your clinician diagnosed a middle ear infection called acute otitis media.

WHAT WE FOUND:
Your clinician documented no mastoiditis concern, no ear tubes or perforated eardrum, no ear canal infection, and no other serious ear concern in this discharge plan.

WHAT TO DO AT HOME:
- Rest as needed and drink fluids unless your clinician told you to limit them.
- Keep cotton swabs, earbuds, and other objects out of the ear unless your clinician told you otherwise.
- Use warm compresses only if they feel comfortable and your clinician said they are safe.
- Most adults start to improve within 2 to 3 days with antibiotics. With a watchful-waiting plan, improvement often begins within 5 to 7 days.
- Mild ear fullness or muffled hearing can last 2 to 4 weeks even as you recover.

MEDICATIONS:
- Use only the pain medicine, ear drops, or antibiotics your clinician prescribed or said are safe for you.
- If your clinician gave you a delayed-antibiotic or watchful-waiting plan, follow those exact instructions instead of starting antibiotics on your own.

RETURN TO ED IF:
- Fever that is not improving, unable to keep fluids down, shaking chills, neck stiffness, confusion, severe headache, or feeling much worse overall.
- Redness, swelling, or pain behind the ear, or the ear starts sticking out.
- New hearing loss, new or severe dizziness or spinning sensation, facial weakness, fluid or blood draining from the ear, or symptoms that get worse after discharge.

FOLLOW UP:
If your clinician prescribed antibiotics, follow up in 7 to 10 days or sooner if symptoms are not improving. If your clinician gave a watchful-waiting plan, follow up in 2 to 3 days if symptoms are not improving. Follow any different schedule your clinician gave you.
```

Disposition:

- `elderly_frail` and `diabetes_general_risk` are output modifiers.
- `watchful_waiting_follow_up_unreliable` remains a pathway-specific runtime blocker.

## 3. Suture Removal Or Wound Check Without Infection

Phenotype ID: `suture_removal_or_wound_check_no_infection`

Feedback status: promoted after return-precaution and runtime-gate cleanup.

Encoded changes:

- Rewrote diagnosis to avoid presupposing healing.
- Rewrote What We Found to document absence of infection/opening/concern rather than positive healing progress.
- Removed antibiotics-continuation bullet.
- Made runtime gate dependency explicit in review notes and inclusion language.
- Added diabetes, peripheral vascular disease, and anticoagulation runtime modifiers.
- Converted diabetes, peripheral vascular disease, and anticoagulation to output modifiers.
- Sharpened color-change language.
- Tightened the runtime gate so wound readiness alone is not sufficient.

```text
DIAGNOSIS:
Your clinician examined your wound.

WHAT WE FOUND:
Your clinician documented no signs of infection, wound opening, or other wound concern at this visit.

WHAT TO DO AT HOME:
- Keep the area clean and follow the wound care instructions your clinician gave you.
- Do not pick at scabs, glue, strips, stitches, or staples.
- Protect the area from friction, soaking, or injury until your clinician says normal activity is safe.
- Most clean wounds continue to heal over 1 to 2 weeks. Scarring can take several months to fade.

MEDICATIONS:
- Use only the ointment, dressing supplies, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- The wound opens, bleeds and will not stop, or stitches or staples come out too early.
- New numbness, weakness, color change, or trouble moving the injured area.

FOLLOW UP:
Follow up on the wound schedule your clinician gave you. If no schedule was given and symptoms worsen or you are worried, arrange a recheck within 2 to 3 days.
```

Disposition:

- Runtime requires documented expected healing or explicit wound clearance plus a clinician-entered wound follow-up plan.
