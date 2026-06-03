# Phase 201 Multi-Phenotype Clinician Review Packet

Date: 2026-06-03

Purpose: clinician review for four candidate ontology phenotypes before any promotion.

Default rule:

No phenotype is promoted unless the reviewer explicitly approves it. If approval is incomplete, keep draft or product-layer fallback.

Review choices for each phenotype:

- Approve for narrow ontology mode.
- Revise and keep draft.
- Retire to product-layer fallback.

Required reviewer:

- Emergency Medicine clinician-owner.

## 1. Acute Otitis Media

Phenotype ID:

`acute_otitis_media_uncomplicated`

Current status:

Retired/product-layer fallback only.

Proposed decision:

Approve for narrow ontology mode only if all questions below are answered yes.

### Proposed Scope

Include:

- Adult patient.
- Clinician diagnosis or discharge impression of acute otitis media, otitis media, or middle ear infection.
- Clinician-entered treatment plan is present.
- No mastoiditis, deep ear infection, perforation, tube complication, trauma, foreign body, otitis externa pathway, acute hearing loss, facial weakness, vertigo, severe systemic illness, unstable vitals, recurrent/chronic disease, pediatric pathway, immunocompromise, or ENT-directed plan.

Exclude:

- Pediatric patients.
- Recurrent or chronic otitis media.
- Tympanostomy tube or perforated TM.
- Otitis externa or ear canal infection.
- Mastoiditis or deep ear infection concern.
- Acute hearing loss, vertigo, facial weakness, or neurologic ear sign.
- Immunocompromised or frail elderly patients.
- ENT-directed plan.
- Any case where antibiotic/watchful-waiting instructions are not clinician-entered.

### Patient-Facing Output

```text
DIAGNOSIS:
Your clinician diagnosed a middle ear infection called acute otitis media.

WHAT WE FOUND:
Your discharge plan did not document mastoiditis, eardrum rupture, ear tube complication, ear canal infection, or another ear emergency today.

WHAT TO DO AT HOME:
- Rest as needed and drink fluids if you are allowed to.
- Keep cotton swabs, earbuds, and other objects out of the ear unless your clinician told you otherwise.
- Use warm compresses only if they feel comfortable and your clinician said they are safe.

MEDICATIONS:
- Use only the pain medicine, ear drops, or antibiotics your clinician prescribed or said are safe for you.
- If your clinician gave you a delayed-antibiotic or watchful-waiting plan, follow those exact instructions instead of starting antibiotics on your own.

RETURN TO ED IF:
- Fever that is high or not improving, worsening ear pain, confusion, severe headache, or feeling very ill.
- Redness, swelling, or pain behind the ear, or the ear starts sticking out.
- New hearing loss, dizziness, facial weakness, fluid or blood draining from the ear, or symptoms that get worse after discharge.

FOLLOW UP:
Follow up on the schedule your clinician gave you, especially if symptoms are not improving.
```

### Runtime Requirements

Required context:

- Adult patient context.
- Clinician diagnosis of AOM.
- Clinician-entered treatment plan.
- Structured absence of ear red flags.

Blocked modifiers:

- Mastoiditis or deep ear infection concern.
- Severe systemic ear infection.
- Tympanic membrane perforation or tube.
- Ear trauma or foreign body.
- Otitis externa or ear canal pathway.
- Acute hearing loss.
- Facial weakness or neurologic ear sign.
- Immunocompromised.
- Frail elderly.
- Recurrent or chronic ear infection.
- Pediatric pathway.
- Specialist-directed ENT plan.
- Unstable vitals.

### Review Questions

1. Is adult-only scope correct for v1?
2. Is it acceptable to include delayed-antibiotic and watchful-waiting wording if it only refers to clinician-entered instructions?
3. Should the phrase "ear tube complication" be kept, or should it say "ear tubes or perforated eardrum"?
4. Are vertigo, facial weakness, and acute hearing loss appropriate hard blockers?
5. Should frail elderly be blocked, or only immunocompromised/systemically ill?
6. Should follow-up remain "on the schedule your clinician gave you" with no default interval?
7. Are there any red flags missing from the return precautions?
8. Can this be promoted to reviewed ontology mode?

Reviewer decision:

```yaml
acute_otitis_media_uncomplicated:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## 2. Suture Removal Or Wound Check Without Infection

Phenotype ID:

`suture_removal_or_wound_check_no_infection`

Current status:

Retired/product-layer fallback only.

Proposed decision:

Consider promotion only if clinician agrees the readiness context is strong enough.

### Proposed Scope

Include:

- Adult patient.
- Clinician-documented wound check, suture removal, or staple removal plan.
- Clinician documents wound is healing as expected or ready for removal.
- No infection, dehiscence, retained foreign body, tendon/nerve/vascular concern, bite wound, open fracture, dirty wound, poor follow-up, pediatric pathway, diabetic foot wound, immunocompromise, or specialist-directed wound plan.

Exclude:

- Wound infection concern.
- Wound dehiscence or wound not ready for removal.
- Early suture or staple loss.
- Retained foreign body.
- Tendon, nerve, vascular, joint, or open fracture concern.
- Bite wound or dirty wound.
- Diabetic foot wound.
- Pediatric patient.
- Immunocompromised patient.
- Specialist-directed wound plan.

### Patient-Facing Output

```text
DIAGNOSIS:
Your clinician checked your healing wound today.

WHAT WE FOUND:
Your discharge plan did not document wound infection, the wound opening, or another wound emergency today.

WHAT TO DO AT HOME:
- Keep the area clean and follow the wound care instructions your clinician gave you.
- Do not pick at scabs, glue, strips, stitches, or staples.
- Protect the area from friction, soaking, or injury until your clinician says normal activity is safe.

MEDICATIONS:
- Use only the ointment, dressing supplies, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- The wound opens, bleeds and will not stop, or stitches or staples come out too early.
- New numbness, weakness, color change, or trouble moving the injured area.

FOLLOW UP:
Follow up on the wound schedule your clinician gave you.
```

### Runtime Requirements

Required context:

- Clinician-documented wound readiness.
- Structured absence of wound red flags.

Blocked modifiers:

- Wound infection concern.
- Wound dehiscence.
- Wound not ready for suture removal.
- Retained foreign body.
- Hand tendon risk.
- Joint violation.
- Open fracture.
- Bite wound.
- Dirty wound.
- Poor follow-up.
- Immunocompromised.
- Diabetic foot.
- Pediatric pathway.
- Specialist-directed wound plan.

### Review Questions

1. Is "clinician documents wound is healing as expected or ready for removal" enough to support ontology mode?
2. Should this include both suture removal and staple removal?
3. Should simple wound check without removal be included, or should it be a separate phenotype?
4. Should face, hand, joint, genital, or high-tension wounds be hard blocked?
5. Should pediatric wounds be excluded for v1?
6. Should diabetic foot wounds and immunocompromised patients be hard blocked?
7. Does the patient-facing output overstate readiness or safety?
8. Can this be promoted to reviewed ontology mode?

Reviewer decision:

```yaml
suture_removal_or_wound_check_no_infection:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## 3. Simple Skin Avulsion Or Abrasion

Phenotype ID:

`skin_avulsion_or_abrasion_simple`

Current status:

Proposed new draft.

Proposed decision:

Draft first. Promote only if the reviewer agrees that the boundary is narrow enough.

### Proposed Scope

Include:

- Adult patient.
- Clinician diagnosis or discharge impression of simple abrasion, skin avulsion, skin tear, or superficial wound.
- Wound cleaned and dressed.
- No deep structure injury.
- No open fracture, joint violation, tendon/nerve/vascular concern, retained foreign body, bite wound, gross contamination, burn pathway, diabetic foot wound, immunocompromise, active infection, uncontrolled bleeding, or specialist-directed plan.
- Tetanus plan handled by clinician or already documented separately.

Exclude:

- Laceration requiring repair.
- Open fracture.
- Joint violation.
- Tendon, nerve, vascular, or crush injury.
- Retained foreign body.
- Bite wound.
- Dirty or contaminated wound.
- Burn, chemical exposure, or high-pressure injection.
- Diabetic foot wound.
- Immunocompromised patient.
- Pediatric pathway.
- Active infection.
- Uncontrolled bleeding.
- Specialist-directed wound plan.

### Proposed Patient-Facing Output

```text
DIAGNOSIS:
Your clinician treated a superficial skin wound, such as an abrasion, skin tear, or small skin avulsion.

WHAT WE FOUND:
Your discharge plan did not document a deep injury, broken bone, tendon injury, nerve injury, joint injury, retained foreign body, or wound infection today.

WHAT TO DO AT HOME:
- Keep the wound clean and covered as instructed.
- Change the dressing on the schedule your clinician gave you.
- Do not scrub, pick, or pull at healing skin.
- Avoid soaking the wound until your clinician says it is safe.

MEDICATIONS:
- Use only the ointment, dressing supplies, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Redness spreads, pus appears, red streaks develop, fever starts, or swelling or pain gets worse.
- Bleeding will not stop with firm pressure.
- New numbness, weakness, color change, trouble moving the area, or the wound opens or gets deeper.

FOLLOW UP:
Follow up on the wound schedule your clinician gave you.
```

### Proposed Runtime Requirements

Required context:

- Clinician diagnosis of simple abrasion, skin avulsion, or superficial skin tear.
- Wound cleaned and dressed.
- Structured absence of wound red flags.

Blocked modifiers:

- Open fracture.
- Joint violation.
- Hand tendon risk.
- Neurovascular compromise.
- Retained foreign body.
- Bite wound.
- Dirty wound.
- Wound infection concern.
- Wound dehiscence.
- Diabetic foot.
- Immunocompromised.
- Pediatric pathway.
- Specialist-directed wound plan.
- Unstable vitals.

### Review Questions

1. Should skin avulsion, skin tear, and abrasion be one phenotype or separate phenotypes?
2. Should this be adult-only for v1?
3. Should wounds needing sutures, staples, glue, or Steri-Strips be excluded and routed to `laceration_repaired_simple`?
4. Should tetanus be mentioned, or should tetanus remain completely clinician-entered and outside ontology text?
5. Should topical antibiotic ointment be mentioned, or only "ointment if prescribed or instructed"?
6. Are burn, chemical exposure, and high-pressure injection appropriate hard blockers?
7. Are diabetic foot wounds and immunocompromised patients appropriate hard blockers?
8. Can this be promoted after runtime stress testing, or should it remain draft/product-layer fallback?

Reviewer decision:

```yaml
skin_avulsion_or_abrasion_simple:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## 4. Non-Ankle Sprain Or Strain With Negative X-Ray

Phenotype ID:

`sprain_strain_non_ankle_xray_negative`

Current status:

Proposed new draft.

Proposed decision:

Draft first. This should not be a generic "joint pain" phenotype.

### Proposed Scope

Include:

- Adult patient.
- Clinician diagnosis or discharge impression of sprain or strain outside the ankle pathway.
- X-ray or fracture evaluation negative.
- Distal perfusion, sensation, and movement intact.
- Patient can use wrap, brace, sling, crutches, or protected activity as instructed.
- No dislocation, open wound, fracture, neurovascular compromise, tendon rupture concern, septic joint concern, compartment syndrome concern, high-energy trauma, pediatric growth plate concern, or specialist-directed orthopedic plan.

Exclude:

- Ankle sprain, which already has its own phenotype.
- Fracture seen or suspected.
- No x-ray or no documented negative fracture evaluation.
- Dislocation.
- Open wound or open fracture.
- Neurovascular compromise.
- Tendon rupture concern.
- Septic joint or infection concern.
- Severe swelling after high-energy trauma.
- Unable to bear weight or use the limb when this suggests unsafe discharge.
- Pediatric growth plate concern.
- Specialist-directed orthopedic plan.

### Proposed Patient-Facing Output

```text
DIAGNOSIS:
Your clinician diagnosed a sprain or strain. No fracture was seen on today's fracture evaluation.

WHAT WE FOUND:
Your discharge plan did not document a broken bone, dislocation, open wound, poor blood flow, nerve problem, tendon rupture, or joint infection today.

WHAT TO DO AT HOME:
- Rest and protect the injured area as instructed.
- Use the brace, wrap, sling, crutches, or activity limits your clinician gave you.
- Ice and elevate the area if your clinician said it is safe.
- Start gentle movement only when your clinician says it is safe.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use any prescribed medicine exactly as instructed.

RETURN TO ED IF:
- Pain or swelling gets much worse, or you cannot use the limb as instructed.
- New numbness, weakness, color change, coldness, or loss of pulse develops.
- Fever, redness, warmth, pus, or severe pain with movement develops.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED as instructed, especially if pain or function is not improving.
```

### Proposed Runtime Requirements

Required context:

- Clinician diagnosis of sprain or strain.
- Negative x-ray or negative fracture evaluation.
- Structured intact neurovascular status.
- Structured safe discharge support plan.

Blocked modifiers:

- Ankle sprain pathway.
- Fracture seen.
- No x-ray performed or no negative fracture evaluation documented.
- Dislocation.
- Open wound or open fracture.
- Neurovascular compromise.
- Tendon rupture concern.
- Septic joint or infection concern.
- High-energy trauma.
- Unable to bear weight or unable to use limb as instructed.
- Pediatric pathway.
- Specialist-directed orthopedic plan.

### Review Questions

1. Should this include both sprains and strains, or should muscle strain be separate from joint sprain?
2. Should this exclude ankle entirely because `ankle_sprain_xray_negative` already exists?
3. Should wrist, knee, shoulder, finger, elbow, and foot sprains all be allowed under one phenotype?
4. Is "negative x-ray or negative fracture evaluation" enough, or must it require x-ray performed?
5. Should suspected ligament rupture, tendon rupture, or high-grade instability be a hard blocker?
6. Should inability to bear weight be a hard blocker for all body sites, or only lower extremity injuries?
7. Should pediatric growth plate concern be a hard blocker for v1?
8. Can this be promoted after runtime stress testing, or should it remain draft/product-layer fallback?

Reviewer decision:

```yaml
sprain_strain_non_ankle_xray_negative:
  decision: ""
  approve_for_ontology_mode: false
  required_revisions: []
  reviewer: ""
  review_date: ""
```

## Cross-Phenotype Questions

1. Are the adult-only restrictions appropriate for all four phenotypes?
2. Should any of these be split into smaller phenotypes before promotion?
3. Are any return precautions too broad, too narrow, or too alarming?
4. Should any medication language be removed entirely and left only to clinician-entered instructions?
5. Which phenotypes can be promoted now?
6. Which should stay product-layer fallback?
7. Which need another stress-test round before a decision?

## Reviewer Summary

Fill this section before implementation.

```yaml
review_summary:
  reviewer: ""
  review_date: ""
  acute_otitis_media_uncomplicated:
    decision: ""
    promote: false
    notes: []
  suture_removal_or_wound_check_no_infection:
    decision: ""
    promote: false
    notes: []
  skin_avulsion_or_abrasion_simple:
    decision: ""
    promote: false
    notes: []
  sprain_strain_non_ankle_xray_negative:
    decision: ""
    promote: false
    notes: []
  global_required_revisions: []
```

## Implementation Plan After Review

If approved:

1. Encode reviewer decisions in phenotype JSON and generator source.
2. Add or revise source cards.
3. Add runtime required context.
4. Add stress cases for broad complaints and unsafe modifiers.
5. Keep Python and Netlify runtime blockers in sync.
6. Rebuild manifest, primitives, review sheets, graph, and gate.
7. Verify with Python runtime, Netlify smoke, graph rebuild, product tailoring contract, and build.

If not approved:

Retire to product-layer fallback and keep broad complaint inputs out of ontology mode.
