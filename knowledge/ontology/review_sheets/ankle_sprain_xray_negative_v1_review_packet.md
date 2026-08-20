# Ankle Sprain With Negative X-Ray V1 Review Packet

Phenotype ID: `ankle_sprain_xray_negative`

Clinical status: reviewed for limited use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-05-29.

## Inclusion Criteria

- Ankle injury consistent with sprain.
- Fracture not seen on x-ray or fracture evaluation not concerning.
- Foot is warm and well perfused.
- Sensation and movement are intact at discharge.
- Patient can use brace, wrap, crutches, or protected weight bearing as instructed.

## Exclusions

- Open fracture or dislocation.
- Neurovascular compromise.
- Concern for septic joint.
- High-risk tendon rupture or unstable injury requiring urgent specialty pathway.
- Child with growth plate concern requiring pediatric-specific instructions.

## Must-Not-Miss Diagnoses

- Occult fracture.
- Lisfranc injury or high ankle sprain when exam suggests it.
- Compartment syndrome in severe trauma.
- Neurovascular compromise.
- Infection if symptoms are not traumatic.

## Source Audit

- `medlineplus.ankle_sprain_aftercare`: supports patient-facing home care, brace or wrap protection, ice, elevation, gradual activity, and return precautions.
- `wikem.ankle_sprain`: supports ED phenotype boundaries and must-not-miss framing only.
- No WikEM patient-facing prose is copied.
- Medication doses remain omitted until a dosing policy is reviewed.
- Negative x-ray language is allowed only through the phenotype gate and blocked when `no_xray_performed` or `fracture_seen` is detected.

## Blocked Modifiers

- `fracture_seen`
- `neurovascular_compromise`
- `no_xray_performed`
- `open_wound`
- `unable_to_bear_weight`

## Runtime Behavior

| Case | Expected behavior |
| --- | --- |
| `ankle_sprain_xray_negative` with negative x-ray and intact neurovascular exam | ontology mode |
| ankle sprain with numb toes | generator fallback |
| ankle sprain with open wound | generator fallback |
| ankle fracture language | generator fallback |
| ankle sprain without x-ray | generator fallback |
| vague ankle pain | generator fallback |

## Patient-Facing Output

```text
DIAGNOSIS:
You have an ankle sprain. Your x-ray did not show a fracture.

WHAT WE FOUND:
Your foot has good blood flow, feeling, and movement. You can go home with a brace, wrap, or crutches as instructed.

WHAT TO DO AT HOME:
- Wear the brace or wrap as instructed. Rest and protect your ankle for the next few days.
- Put ice on your ankle for 15 to 20 minutes at a time. Keep your ankle raised above heart level when you sit or lie down.
- Walk only as much as you were instructed. If walking causes significant pain, use crutches and limit weight on the ankle.

MEDICATIONS:
- You can use acetaminophen for pain. Follow the bottle directions and do not take more than the label says.
- Ibuprofen or naproxen may help pain and swelling. Take them with food. Do not use them if you have kidney disease, stomach ulcers or bleeding, take blood thinners, or were told to avoid them.

RETURN TO ED IF:
- Come back to the emergency department right away if your foot or toes become numb, cold, blue, very pale, or hard to move.
- Come back to the emergency department right away if pain or swelling gets much worse, you cannot walk at all, the skin becomes very red or hot, or you develop a fever.

FOLLOW UP:
See your regular doctor, urgent care, sports medicine, or orthopedics in 5 to 7 days if pain or walking is not improving.
```

## Sign-Off

This phenotype is acceptable as a first deterministic ontology output for a narrow ED ankle sprain discharge case when runtime gates pass.
