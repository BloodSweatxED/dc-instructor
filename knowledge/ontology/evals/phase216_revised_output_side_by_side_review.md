# Phase 216 Revised Output Side-By-Side Review

Date: 2026-06-03

Purpose: promotion-readiness review for the four active revised drafts after Phase 215.

Default decision:

- Do not promote any phenotype without explicit clinician approval.
- Treat this packet as review evidence, not approval.
- Keep `sprain_strain_non_ankle_xray_negative` draft-only until site-specific stress is clean enough for promotion.

## Promotion Readiness Snapshot

| Phenotype | Current recommendation | Main reason |
| --- | --- | --- |
| `skin_avulsion_or_abrasion_simple` | Best first promotion candidate after clinician approval | Narrow output, clear repair/deep-structure blockers, no tetanus or static antibiotic advice. |
| `acute_otitis_media_uncomplicated` | Second promotion candidate after clinician approval | Adult-only, clinician-plan dependent, follow-up and timeline now concrete. |
| `suture_removal_or_wound_check_no_infection` | Conditional promotion only after clinician approval | Depends on clinician-entered wound readiness and wound follow-up plan. |
| `sprain_strain_non_ankle_xray_negative` | Keep draft-only | Needs more site-specific confidence work before promotion. |

## 1. Simple Skin Avulsion Or Abrasion

Phenotype ID: `skin_avulsion_or_abrasion_simple`

Review focus:

- Acceptability of combining simple abrasion, skin tear, and small skin avulsion.
- Whether 2 to 3 day fallback follow-up is acceptable when no clinician schedule is given.
- Whether the output is appropriately silent on tetanus and topical antibiotics unless clinician-entered.

```text
DIAGNOSIS:
Your clinician diagnosed a simple skin abrasion, skin tear, or skin avulsion.

WHAT WE FOUND:
Your clinician documented a superficial skin wound without a repair need, retained foreign body concern, deep structure injury, infection concern, or other wound red flag.

WHAT TO DO AT HOME:
- Keep the wound clean and follow the dressing plan your clinician gave you.
- Do not scrub, pick, or peel the injured skin.
- Protect the area from friction, soaking, or another injury while the skin is closing.
- Many abrasions heal new surface skin within 7 to 14 days. Skin tears and avulsions, especially in older adults, can take longer.

MEDICATIONS:
- Use only the dressing supplies, ointment, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- Bleeding that will not stop with firm pressure or the wound starts opening wider.
- New numbness, weakness, color change, trouble moving the area, or concern that something is stuck in the wound.

FOLLOW UP:
Follow up with primary care, urgent care, wound clinic, or the ED in 2 to 3 days if the wound is not improving, or sooner if your clinician gave a specific schedule.
```

Reviewer decision:

```yaml
skin_avulsion_or_abrasion_simple:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## 2. Acute Otitis Media

Phenotype ID: `acute_otitis_media_uncomplicated`

Review focus:

- Adult-only scope.
- 7 to 14 day fallback follow-up wording.
- Recovery timeline wording for antibiotic and watchful-waiting plans.
- Return precautions including neck stiffness and serious intracranial/infectious concern.

```text
DIAGNOSIS:
Your clinician diagnosed a middle ear infection called acute otitis media.

WHAT WE FOUND:
Your clinician documented no mastoiditis concern, no ear tubes or perforated eardrum concern, no ear canal infection pathway, and no other ear red flags in this discharge plan.

WHAT TO DO AT HOME:
- Rest as needed and drink fluids if you are allowed to.
- Keep cotton swabs, earbuds, and other objects out of the ear unless your clinician told you otherwise.
- Use warm compresses only if they feel comfortable and your clinician said they are safe.
- Most adults start to improve within 2 to 3 days when antibiotics are prescribed, or within about 5 to 7 days with a watchful-waiting plan.

MEDICATIONS:
- Use only the pain medicine, ear drops, or antibiotics your clinician prescribed or said are safe for you.
- If your clinician gave you a delayed-antibiotic or watchful-waiting plan, follow those exact instructions instead of starting antibiotics on your own.

RETURN TO ED IF:
- Fever that is high or not improving, unable to keep fluids down, shaking chills, neck stiffness, confusion, severe headache, or looking seriously ill.
- Redness, swelling, or pain behind the ear, or the ear starts sticking out.
- New hearing loss, dizziness, facial weakness, fluid or blood draining from the ear, or symptoms that get worse after discharge.

FOLLOW UP:
Follow up with primary care, urgent care, or an ear clinician in 7 to 14 days, or sooner if symptoms are not improving, unless your clinician gave a different schedule.
```

Reviewer decision:

```yaml
acute_otitis_media_uncomplicated:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## 3. Suture Removal Or Wound Check Without Infection

Phenotype ID: `suture_removal_or_wound_check_no_infection`

Review focus:

- Whether clinician-documented wound readiness is enough for ontology mode.
- Whether the fallback "recheck within 2 to 3 days if worse or worried" is acceptable when no schedule was given.
- Whether high-risk wound locations remain hard blockers.

```text
DIAGNOSIS:
Your clinician checked your healing wound.

WHAT WE FOUND:
Your clinician documented the wound is healing as expected and did not document infection, wound opening, or another wound red flag.

WHAT TO DO AT HOME:
- Keep the area clean and follow the wound care instructions your clinician gave you.
- Do not pick at scabs, glue, strips, stitches, or staples.
- Protect the area from friction, soaking, or injury until your clinician says normal activity is safe.
- Most clean wounds continue to heal over 1 to 2 weeks. Scarring can take several months to fade.

MEDICATIONS:
- Use only the ointment, dressing supplies, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.
- If you were prescribed antibiotics, do not stop them early unless your clinician tells you.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- The wound opens, bleeds and will not stop, or stitches or staples come out too early.
- New numbness, weakness, color change, or trouble moving the injured area.

FOLLOW UP:
Follow up on the wound schedule your clinician gave you. If no schedule was given and symptoms worsen or you are worried, arrange a recheck within 2 to 3 days.
```

Reviewer decision:

```yaml
suture_removal_or_wound_check_no_infection:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## 4. Non-Ankle Sprain Or Strain With Negative X-Ray

Phenotype ID: `sprain_strain_non_ankle_xray_negative`

Review focus:

- Do not promote yet.
- Knee, wrist, and shoulder need clean pass criteria.
- Elbow and foot need either higher-confidence matching or separate handling before promotion.
- Lower-extremity inability to bear weight, scaphoid tenderness, suspected rupture, septic joint, compartment syndrome, and elderly/osteoporotic high-risk patterns remain hard blockers.

```text
DIAGNOSIS:
Your clinician diagnosed a sprain or strain. Your x-ray did not show a fracture.

WHAT WE FOUND:
Your clinician documented that an x-ray was performed and did not show a fracture, and that blood flow, feeling, and movement were intact.

WHAT TO DO AT HOME:
- Protect the injured area with the brace, wrap, sling, splint, crutches, or activity limits your clinician gave you.
- Rest from painful activity at first, then slowly return to normal movement as symptoms allow.
- Raise the injured area when you can, especially while swelling is present.
- Minor sprains and strains may improve over several days. Moderate injuries often take several weeks, and high-grade injuries need follow-up.

MEDICATIONS:
- Use only the medicines your clinician prescribed or said are safe for you.
- Do not take extra doses or combine medicines unless your clinician told you to.

RETURN TO ED IF:
- New numbness, weakness, color change, coldness, or trouble moving the injured area.
- Worsening pain out of proportion, tight or hard swelling, or pain that does not improve with rest and elevation.
- Fever, redness, warmth, pus, severe pain with movement, or symptoms that get worse instead of better.

FOLLOW UP:
Follow up with primary care, urgent care, sports medicine, or orthopedics in 5 to 7 days if pain, swelling, movement, or walking is not improving, or sooner if your clinician gave a specific plan.
```

Reviewer decision:

```yaml
sprain_strain_non_ankle_xray_negative:
  decision: "keep_draft"
  approve_for_ontology_mode: false
  required_revisions:
    - "Resolve elbow and foot low-confidence matching before promotion, or split by site."
  reviewer: ""
  review_date: ""
```

## Reviewer Summary

```yaml
review_summary:
  reviewer: ""
  review_date: ""
  skin_avulsion_or_abrasion_simple:
    decision: ""
    promote: false
    notes: []
  acute_otitis_media_uncomplicated:
    decision: ""
    promote: false
    notes: []
  suture_removal_or_wound_check_no_infection:
    decision: ""
    promote: false
    notes: []
  sprain_strain_non_ankle_xray_negative:
    decision: "keep_draft_until_site_stress_resolved"
    promote: false
    notes:
      - "Elbow and foot site terms currently match below promotion confidence threshold."
  global_required_revisions: []
```
