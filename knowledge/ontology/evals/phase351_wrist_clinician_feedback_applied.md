# Phase 351 Wrist Clinician Feedback Applied

Date: 2026-06-04

Status: revise applied; wrist remains draft-only pending re-review.

## Clinician Verdict

`wrist_sprain_xray_negative` was judged architecturally sound but not ready for promotion until patient-facing text and runtime clarifications were revised.

## Applied Text Changes

`WHAT WE FOUND` now uses patient-facing language:

> Your x-ray did not show a broken bone. Your clinician checked the blood flow, feeling, and movement in your hand and fingers and they were normal. Your clinician also checked specific areas of your wrist for signs of a deeper injury and did not find any.

`WHAT TO DO AT HOME` now adds a 3 to 5 day check-in signal:

> If your pain and swelling are not improving within 3 to 5 days, do not wait for your scheduled follow-up. Go sooner.

The second return precaution now uses lay symptom language:

> Pain at the base of your thumb or along the thumb side of your wrist that is getting worse, not better.

The infection return precaution now removes the vague tail:

> Fever, redness, warmth, pus, or severe pain with movement.

Follow-up is now non-contingent:

> See your doctor, urgent care, sports medicine, or orthopedics in 5 to 7 days. Wrist injuries can sometimes hide a small fracture that does not show up on the first x-ray. A follow-up visit confirms your wrist is healing the way it should. Go sooner if your clinician gave you a specific plan or if your pain is getting worse.

## Applied Runtime Clarifications

`foosh_scaphoid_risk` now requires FOOSH mechanism plus at least one scaphoid-risk signal:

- snuffbox tenderness
- scaphoid tenderness
- radial-sided wrist pain
- thumb-side wrist pain
- pain at the base of the thumb
- inability to grip

FOOSH alone with a clean scaphoid exam no longer blocks.

`elderly_osteoporotic_high_risk_msk` no longer fires on age-language alone. It now requires documented osteoporosis, osteoporotic language, fragility-fracture history, or low bone density.

`hand_tendon_risk` now explicitly covers:

- inability to extend a finger
- inability to flex the fingertip
- finger droop
- mallet finger
- distal extensor avulsion
- jersey finger
- flexor digitorum profundus avulsion
- FDP avulsion

## Re-Review Status

Do not promote yet. The requested revision has been applied and needs clinician-owner re-review for final promote versus revise versus retire.
