# RAG Smoke Review: Back Pain v2

Created: 2026-05-28

Source artifact: `knowledge/evals/rag_smoke_backpain_v2.json`

Collection: `medlineplus_backpain_v1_sections`

Prompt version: `backpain_rag_prompt_v2`

Retrieval version: `backpain_retrieval_v2`

Purpose: Clinician review of the second MedlinePlus-backed RAG discharge instruction smoke test after v1 pre-score calibration.

## V2 Calibration Targets

- Tighten sciatica return precautions and add NSAID safety language.
- Tighten atraumatic neck strain return precautions.
- Improve 4th grade medication and reading-level behavior.
- Reduce duplicate and tangential sources.
- Remove implied sedating-medication cautions unless supported by the ED note.
- Replace boss-negotiation language with cleaner work-restriction wording.
- Avoid numeric OTC dosing unless the ED note provides it.
- Keep generic low-back return precautions out of urinary, night-pain, and weight-loss drift unless the ED note supports them.

## Review Table

| case_id | clinically_safe | return_precautions_appropriate | home_care_specificity | medication_safety | reading_level_match | source_relevance | unsupported_claims | ready_for_app_integration | notes |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| lumbar_strain | pass | 5 | 3 | 4 | 4 | 3 | minor | no | Only holdout. Return precautions improved, but home care lost useful ice/heat timing and positioning. |
| sciatica | pass | 5 | 3 | 5 | 4 | 4 | minor | yes | Major improvement. Integration-ready. |
| atraumatic_back_pain | pass | 4 | 3 | 4 | 4 | 3 | minor | yes | Serviceable and ready, though home care could still be more specific. |
| back_pain_red_flags | pass | 4 | 4 | 5 | 4 | 3 | minor | yes | Ready. |
| neck_strain | pass | 4 | 4 | 4 | 4 | 4 | minor | yes | Major improvement. Integration-ready. |
| ankle_sprain | pass | 5 | 4 | 5 | 5 | 5 | none | yes | Ready. |
| herniated_disk | pass | 4 | 4 | 4 | 4 | 4 | minor | yes | Ready. |
| chronic_back_flare | pass | 5 | 4 | 4 | 4 | 3 | none | yes | Ready. |
| return_to_work | pass | 4 | 5 | 4 | 4 | 4 | minor | yes | Ready after work-note wording fix. |
| heat_vs_ice | pass | 4 | 5 | 4 | 4 | 3 | none | yes | Ready despite remaining source relevance drag. |

## Clinician Pre-Score Summary

V2 is a meaningful jump from v1. 9 of 10 cases are ready for app integration and the set passes the 8 of 10 readiness threshold.

The headline wins are `sciatica` and `neck_strain`. Both were v1 weak points and both are now integration-ready.

The remaining holdout is `lumbar_strain`. Return precautions improved from 3 to 5, but home care fell from 4 to 3. V2 removed useful routine lumbar strain advice, including ice/heat timing, pillow positioning, and practical comfort measures. It also added chiropractor/massage language, which is less useful for a routine ED lumbar strain discharge.

Integration hesitation:

- Source relevance mean is about 3.6. Sacroiliac joint aftercare still appears as rank 1 in lumbar strain, atraumatic back pain, chronic back flare, and heat versus ice.
- Home care mean is about 3.9, just below the 4.0 threshold.
- A focused lumbar-source and lumbar-home-care pass could likely move the full set over the sign-off line.

## Patient-Facing Outputs To Review

### lumbar_strain Output

```text
DIAGNOSIS:
You have a lumbar strain. This means you pulled or stretched the muscles and soft tissues in your lower back.

WHAT WE FOUND:
You hurt your lower back after lifting boxes. Your exam in the emergency department was reassuring. You have normal strength and feeling in your legs. You can walk normally. You do not have a fever. You are not having problems controlling your bladder or bowels.

WHAT TO DO AT HOME:
You can move around as much as you can tolerate. Resting in bed for long periods can actually slow your recovery. Try to stay as active as possible without making the pain much worse. Gentle walking is usually helpful. You can use ice or heat on your back, whichever feels better to you. A physical therapist can teach you safe stretching and strengthening exercises when you are ready. You may also consider seeing a chiropractor or massage therapist if your pain continues.

MEDICATIONS:
Continue taking ibuprofen and acetaminophen as needed for pain. You can find these at the store without a prescription. Talk with your doctor before using ibuprofen if you have heart disease, high blood pressure, kidney disease, or have had stomach ulcers or bleeding in your stomach in the past. Do not take more than the amount shown on the bottle.

RETURN TO ED IF:
Come back to the emergency department right away if you develop any of these problems: new weakness in your legs, new numbness between your legs or in your buttocks, trouble controlling your pee or poop, a fever, trouble walking or keeping your balance, severe pain that keeps getting worse, or back pain after a hard fall or injury.

FOLLOW UP:
If your back pain lasts longer than four weeks, follow up with your primary care doctor. Your doctor may refer you to a specialist or physical therapist if needed.
```

### sciatica Output

```text
DIAGNOSIS:
Sciatica. This is pain that travels from your lower back down your leg. It happens when the sciatic nerve gets irritated or pressed on.

WHAT WE FOUND:
You have pain in your lower back that goes down your right leg. The exam showed that your sciatic nerve is irritated. You do not have weakness in your legs. You can control your bladder and bowels normally. You do not have a fever. These are good signs.

WHAT TO DO AT HOME:
Do not stay in bed. Resting in bed does not help sciatica get better. Move around as much as you can handle. Start with light activity and slowly do more each day. Do not lift heavy things or twist your back for the next six weeks. Use heat or ice on the painful area. Try ice for the first two to three days, then switch to heat if that feels better. You can start gentle back exercises after two to three weeks. Focus on exercises that make your stomach muscles stronger and help your back move better. Sit up straight when you sit, stand, or drive. Do not slump.

MEDICATIONS:
You can take ibuprofen or naproxen for pain. These medicines help with pain and swelling. Do not take these medicines if you have kidney disease, stomach ulcers, bleeding problems, take blood thinners, or if a doctor told you to avoid them. You can also take acetaminophen for pain. Follow the directions on the bottle.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems. New weakness in your leg or foot. New numbness in your groin, buttocks, or between your legs. Trouble controlling your pee or poop. Fever. You cannot walk or put weight on your leg. Pain that gets much worse even after taking medicine.

FOLLOW UP:
See your primary care doctor in the next one to two weeks. Your doctor can check how you are doing and help you if the pain is not getting better. Most people with sciatica get better in a few weeks with home care. If your pain lasts longer than four weeks, call your doctor.
```

### atraumatic_back_pain Output

```text
DIAGNOSIS:
Low back pain with no injury.

WHAT WE FOUND:
You have low back pain that started two days ago. You did not hurt your back in a fall or accident. Your exam today was normal. Your nerves are working well. You do not need X-rays or other tests today.

WHAT TO DO AT HOME:
Rest your back but do not stay in bed all day. Move around gently. Short walks are good. Try sitting, standing, and lying down in different positions to find what feels best. Use ice packs on your back for 15 minutes at a time during the first few days. After a few days you can try heat if it helps. Do not lift heavy things. Do not twist or bend deeply until your pain gets better. Light stretching may help after a few days. A physical therapist can teach you safe exercises when you are ready.

MEDICATIONS:
You can take pain medicine you buy at the store. Ibuprofen or naproxen can help with pain and swelling. Do not take ibuprofen or naproxen if you have kidney disease, stomach ulcers, stomach bleeding, or take blood thinners. Do not take them if a doctor told you to avoid them. Acetaminophen is another choice for pain. Follow the directions on the bottle. Do not take more than the bottle says.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems. New numbness or tingling in your groin, buttocks, or private area. New weakness in your legs. Trouble controlling your pee or poop. Fever. You fall or get hurt badly. You cannot walk or stand. Your pain gets much worse and does not get better with rest and medicine.

FOLLOW UP:
See your regular doctor in one to two weeks if your pain is not getting better. Your doctor may send you to a back specialist or physical therapist if needed. Most low back pain gets better in a few weeks with rest and pain medicine.
```

### back_pain_red_flags Output

```text
DIAGNOSIS:
Back pain

WHAT WE FOUND:
You have back pain. We checked you today and did not find signs of serious problems. Your exam looked good. Your strength and feeling were normal. You did not have fever or signs of infection.

WHAT TO DO AT HOME:
Rest when you need to, but try to stay gently active. Avoid heavy lifting, twisting, and bending for the next few days. Use ice packs for 15 to 20 minutes at a time during the first two days if it helps. After that, you can try heat if you prefer. Walk short distances several times a day to keep your back from getting stiff. Avoid sitting or standing in one position for a long time.

MEDICATIONS:
You can take over-the-counter pain medicine to help with discomfort. Acetaminophen can help with pain. Ibuprofen or naproxen can help with pain and swelling. Follow the directions on the bottle. Do not take ibuprofen or naproxen if you have stomach ulcers, kidney problems, or if your doctor has told you to avoid these medicines. Take pain medicine with food to protect your stomach.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems:

New weakness in your legs or trouble walking
New numbness or tingling in your legs, feet, or private area
Loss of control of your urine or bowel movements
Fever
Pain after a fall or injury
Pain going down your leg below the knee
Pain so severe you cannot get comfortable in any position
New trouble with balance

FOLLOW UP:
See your regular doctor in one to two weeks if your back pain is not getting better. Call your doctor sooner if your pain gets worse or if you lose weight without trying.
```

### neck_strain Output

```text
DIAGNOSIS:
Neck strain from sleeping in an awkward position.

WHAT WE FOUND:
You have strained the muscles in your neck. This happened from sleeping in an awkward position. Your exam today was reassuring. You have no weakness or numbness in your arms. You can move your neck in all directions, even though it is uncomfortable. This type of injury usually gets better with rest and simple home treatments.

WHAT TO DO AT HOME:
Rest your neck for the first few days. Avoid heavy lifting and activities that make the pain worse. After the first two to three days, start gentle neck exercises. Move your head slowly up and down, side to side, and ear to ear. These stretches help your neck muscles loosen up.

Use ice packs on your neck for the first two to three days. Place the ice pack on the sore area for 15 to 20 minutes at a time. After two to three days, switch to heat. Use a heating pad, warm shower, or warm compress. Do not fall asleep with a heating pad or ice pack on your skin.

Sleep on a firm mattress with a pillow that supports your neck. A regular pillow or a special neck pillow can help. Ask someone to gently massage the sore areas if that feels good.

Gentle activities like walking can help your neck heal. They improve blood flow to the injured muscles. As you feel better, you can slowly return to your normal activities.

MEDICATIONS:
You can take over-the-counter pain relievers. Ibuprofen and acetaminophen can help reduce pain and swelling. Do not take ibuprofen if you have kidney problems, stomach ulcers, or are allergic to it. Follow the directions on the bottle.

RETURN TO ED IF:
Come back to the emergency department if you develop any of these symptoms:

New numbness, tingling, or weakness in your arm or hand.

Your neck pain gets much worse or is so bad you cannot get comfortable.

You develop a fever with a very stiff neck.

You have new trouble walking or keeping your balance.

You lose control of urination or bowel movements.

You injure your neck again in a fall or accident.

FOLLOW UP:
If your pain does not improve in one week with home care, call your regular doctor for an appointment. Your doctor may recommend physical therapy if the pain continues. Physical therapy can include massage, stretching, and strengthening exercises to help your neck heal completely.
```

### ankle_sprain Output

```text
DIAGNOSIS:

You have an ankle sprain. This means you stretched or tore one of the ligaments in your ankle. The x-ray showed no broken bones.

WHAT WE FOUND:

You hurt your ankle while walking. Your ankle has mild swelling. The blood flow and nerves in your foot and ankle are working normally. The x-ray did not show a fracture.

WHAT TO DO AT HOME:

Rest your ankle. Try not to walk on it too much for the first few days. Use crutches if walking hurts.

Put ice on your ankle for 15 to 20 minutes at a time. Do this several times a day for the first 2 to 3 days. Put a towel between the ice and your skin.

Keep your ankle raised above your heart when you sit or lie down. This helps reduce swelling.

Wear the brace we gave you. This protects your ankle while it heals.

Do not walk or exercise too much too soon. Start slowly when your ankle feels better.

MEDICATIONS:

You can take over-the-counter pain medicine like ibuprofen or naproxen to help with pain and swelling. Follow the directions on the bottle. Take these medicines with food. Do not use them if you have stomach ulcers or kidney problems.

You can also use acetaminophen for pain. Do not take more than the bottle says to take.

RETURN TO ED IF:

You cannot walk at all or walking causes very bad pain.

Your ankle becomes very swollen or the swelling gets much worse.

Your foot or ankle becomes numb, tingly, very cold, or changes color to dark red or black and blue.

You develop a fever.

The pain gets much worse instead of better.

FOLLOW UP:

See your regular doctor in 5 to 7 days to check how your ankle is healing. Your doctor can help you know when it is safe to return to sports or exercise. You may need physical therapy if your ankle is not getting better.
```

### herniated_disk Output

```text
DIAGNOSIS:

Herniated disk with recurrent back pain.

WHAT WE FOUND:

You came to the emergency department today with back pain from your known herniated disk. We checked you carefully and found no new weakness in your legs. You told us you have no trouble controlling your bladder or bowel. The pain got better with medication we gave you.

WHAT TO DO AT HOME:

Rest for the first few days but avoid staying in bed all day. Start moving around gently as you feel able. Do not lift heavy objects or twist your back for the next six weeks. After two to three weeks, you can slowly start light exercise again.

When sitting, place a small pillow or rolled towel behind your lower back for support. Try putting a stool under your feet so your knees are higher than your hips. If you stand at work, rest one foot on a stool and switch feet throughout the day.

Apply ice to your back for 15 to 20 minutes at a time during the first two days. After that, you can use heat if it feels better.

MEDICATIONS:

Take over-the-counter pain medicine as needed. Ibuprofen or naproxen can help with pain and swelling. Acetaminophen is another option for pain relief. If you have stomach problems, kidney disease, or take blood thinners, ask your doctor before using ibuprofen or naproxen.

RETURN TO ED IF:

Come back to the emergency department right away if you develop any of these problems:

You lose control of your bladder or bowel.

You notice new numbness, weakness, or tingling in your legs, feet, buttocks, or pelvis.

Your leg becomes so weak you cannot walk or keep your balance.

Your pain becomes severe and you cannot get comfortable in any position.

You develop a fever with your back pain.

Your pain shoots down your leg below the knee.

FOLLOW UP:

See your regular doctor or spine specialist within one to two weeks. They can help you with a long-term treatment plan. This may include physical therapy to strengthen your back and learn safe ways to move, lift, and exercise. Your doctor can also discuss other treatments if your pain does not improve over time.
```

### chronic_back_flare Output

```text
DIAGNOSIS:

Flare of chronic low back pain.

WHAT WE FOUND:

You came to the emergency department with a flare of your long-term back pain. We checked you and did not find any signs of nerve damage, infection, or injury. Your exam was reassuring.

WHAT TO DO AT HOME:

You can slowly return to your normal activities as you feel able. Staying in bed for a long time can make back pain worse. Start with gentle movement and add more activity each day as your pain allows.

Use heat on your lower back to help with pain and stiffness. You can use a heating pad or warm towel for 15 to 20 minutes at a time. Some people find cold packs helpful in the first few days. Try both and use what works best for you.

If you usually sleep on your back, put a pillow under your knees. If you sleep on your side, try curling up with a pillow between your legs.

MEDICATIONS:

You can take over-the-counter pain medicine like ibuprofen or naproxen if it is safe for you. Do not take ibuprofen or naproxen if you have kidney disease, heart disease, high blood pressure, or have had stomach ulcers or bleeding in your stomach. Follow the directions on the bottle. Do not take more than the amount listed.

You can also use acetaminophen for pain.

RETURN TO ED IF:

Come back to the emergency department right away if you have:

Loss of control of your bladder or bowels.
New numbness or weakness in your legs or feet.
Severe pain that gets much worse even with medicine.
Fever with your back pain.
Pain that spreads down your leg with numbness or tingling.

FOLLOW UP:

See your regular doctor within the next one to two weeks. Your doctor can help you manage your long-term back pain. They may suggest physical therapy, stretching exercises, or other treatments. If your pain does not get better with home care and medicine, your doctor can discuss other options with you.
```

### return_to_work Output

```text
DIAGNOSIS:
Back pain improving after injury

WHAT WE FOUND:
Your exam today looked good. Your back pain is getting better. You are ready to start returning to work, but you need to protect your back while it finishes healing.

WHAT TO DO AT HOME:
Start moving more each day but avoid sudden increases in activity. Walking and gentle movement help your back heal. If you drive to work, bring your car seat forward so you do not bend when driving. Stop every hour on long drives to walk around. Do not lift heavy items right after a long car ride.

When you stand for long periods, rest one foot on a low stool or step. Switch feet every few minutes throughout the day. Take breaks to sit down when you can.

Return to work gradually. Start with light duty if possible. Avoid heavy lifting for the first few days. When you do lift, keep items close to your body. Bend your knees instead of your back. Ask for help with heavy or awkward items.

Ice your back for 15 to 20 minutes if pain increases after activity.

MEDICATIONS:
You can take ibuprofen or naproxen to help with pain and swelling. Take these medicines with food to protect your stomach. Do not use them if you have stomach ulcers or kidney problems.

You can also take acetaminophen for pain.

RETURN TO ED IF:
You lose control of your bowel or bladder.

You develop numbness or weakness in your legs.

You have severe pain that does not improve with rest and medicine.

You develop a fever.

Your pain suddenly gets much worse.

FOLLOW UP:
Follow the work restrictions on your note. If your job requires heavy lifting and your pain is not better in one to two weeks, see your regular doctor to discuss your return to work plan. Your doctor may refer you to physical therapy to help strengthen your back and teach you safe lifting techniques.
```

### heat_vs_ice Output

```text
DIAGNOSIS:
Low back pain

WHAT WE FOUND:
Your back hurts but we did not find anything serious. Your strength is normal. You can move your legs. You do not have signs that you need more tests right now.

WHAT TO DO AT HOME:
You can use ice or heat. Both can help. Use ice for the first two or three days. Put ice on your back for about 20 minutes at a time. Do this two or three times a day. Do not put ice right on your skin. Use a towel or cloth. After two or three days you can switch to heat. Use a heating pad on low. Heat helps your muscles relax.

Rest for the first few days but do not stay in bed all day. Move around a little bit each day. Start slow. Do not do hard work or heavy lifting right away. Stop if something makes the pain worse.

When you sleep, try lying on your side with your knees pulled up. Put a pillow between your knees. If you sleep on your back, put a pillow under your knees.

MEDICATIONS:
You can take pain medicine you buy at the store.

Ibuprofen or naproxen can help with pain and swelling. Do not use ibuprofen or naproxen if you have kidney problems, if you have had stomach ulcers or bleeding, if you take blood thinners, or if your doctor told you to avoid them.

You can also use acetaminophen for pain.

Follow the directions on the bottle. Do not take more than the bottle says.

RETURN TO ED IF:
Come back to the emergency room right away if you have any of these problems:

Your legs become weak or you cannot walk.

You feel numbness in your groin, buttocks, or private area.

You cannot control your pee or poop.

You have a fever.

You fall or get hurt badly.

Your pain gets much worse even after rest and medicine.

FOLLOW UP:
See your regular doctor in one to two weeks if your pain is not better. Your doctor may send you to physical therapy or another specialist if you need more help.
```

## Case Review Blocks

### lumbar_strain

Condition: lumbar strain

Requested reading level: 6th Grade

ED note: Adult with atraumatic low back pain after lifting boxes. Normal lower-extremity strength and sensation. No fever. No bowel or bladder symptoms. No saddle anesthesia. Able to walk. Treated with ibuprofen and acetaminophen.

Retrieval query: lumbar strain low back pain home care activity medicine return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 2 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 3 | Back Pain | treatment | Low back pain - acute | treatment |
| 4 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |
| 5 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### sciatica

Condition: sciatica

Requested reading level: 6th Grade

ED note: Adult with low back pain radiating down the right leg. Positive straight leg raise. No weakness. No urinary retention. No fever. Discharged with NSAID plan and PCP follow-up.

Retrieval query: sciatica discharge instructions numbness weakness home care return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Sciatica | when_to_seek_care | Sciatica | when_to_contact_a_medical_professional |
| 2 | Sciatica | treatment | Sciatica | treatment |
| 3 | Sciatica | when_to_seek_care | Piriformis syndrome | when_to_call_the_doctor |
| 4 | Sciatica | treatment | Piriformis syndrome | treatment |
| 5 | Sciatica | overview | Sciatica | full_summary |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### atraumatic_back_pain

Condition: atraumatic low back pain

Requested reading level: 4th Grade

ED note: Adult with two days of lower back pain. No trauma. No neurologic deficits. No red flags. Vitals normal. No imaging indicated today.

Retrieval query: atraumatic acute low back pain discharge instructions home care return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | self_care | Sacroiliac joint pain - aftercare | follow_up |
| 2 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 3 | Back Pain | treatment | Low back pain - acute | treatment |
| 4 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |
| 5 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### back_pain_red_flags

Condition: back pain with return precautions

Requested reading level: 6th Grade

ED note: Adult evaluated for back pain. Exam reassuring today. Needs clear return precautions for weakness, numbness, fever, trauma, bowel or bladder changes, and worsening pain.

Retrieval query: back pain red flags bowel bladder weakness fever trauma return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 2 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |
| 3 | Back Pain | when_to_seek_care | Sacroiliac joint pain - aftercare | when_to_call_the_doctor |
| 4 | Back Pain | symptoms | Low back pain - acute | symptoms |
| 5 | Sciatica | when_to_seek_care | Sciatica | when_to_contact_a_medical_professional |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### neck_strain

Condition: neck strain

Requested reading level: 6th Grade

ED note: Adult with neck pain after sleeping awkwardly. No trauma. No arm weakness or numbness. Full range of motion with discomfort. Discharged with conservative care.

Retrieval query: neck strain neck spasm home care conservative treatment return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Neck Injuries and Disorders | self_care | Neck pain | home_care |
| 2 | Neck Injuries and Disorders | when_to_seek_care | Neck pain or spasms - self care | when_to_call_the_doctor |
| 3 | Neck Injuries and Disorders | treatment | Neck pain or spasms - self care | stretches_and_exercises |
| 4 | Neck Injuries and Disorders | self_care | Neck pain | home_care |
| 5 | Neck Injuries and Disorders | when_to_seek_care | Torticollis | when_to_contact_a_medical_professional |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### ankle_sprain

Condition: ankle sprain

Requested reading level: 6th Grade

ED note: Adult twisted ankle while walking. X-ray negative for fracture. Mild swelling. Neurovascularly intact. Discharged with brace, rest, ice, elevation, and PCP follow-up.

Retrieval query: ankle sprain aftercare RICE rest ice elevation follow up return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Sprains and Strains | self_care | Ankle sprain - aftercare | what_to_expect |
| 2 | Sprains and Strains | when_to_seek_care | Ankle sprain - aftercare | when_to_call_the_doctor |
| 3 | Sprains and Strains | self_care | Foot sprain - aftercare | follow_up |
| 4 | Sprains and Strains | self_care | Foot sprain - aftercare | activity |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### herniated_disk

Condition: herniated disk

Requested reading level: 8th Grade

ED note: Adult with known herniated disk and recurrent back pain. No new weakness. No bowel or bladder symptoms. Pain improved with medication. Outpatient follow-up advised.

Retrieval query: herniated disk discharge instructions home care follow up weakness bowel bladder precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | self_care | Back pain - returning to work | changes_at_work |
| 2 | Herniated Disk | when_to_seek_care | Herniated disk | when_to_contact_a_medical_professional |
| 3 | Herniated Disk | treatment | Herniated disk | treatment |
| 4 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 5 | Back Pain | overview | Taking care of your back at home | information |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### chronic_back_flare

Condition: chronic low back pain flare

Requested reading level: 6th Grade

ED note: Adult with flare of chronic low back pain. No trauma. No fever. No neurologic deficits. Discussed activity as tolerated, heat, NSAIDs if safe, and outpatient follow-up.

Retrieval query: chronic low back pain flare activity heat medicine home care follow up

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 2 | Back Pain | treatment | Low back pain - chronic | treatment |
| 3 | Back Pain | treatment | Low back pain - chronic | treatment |
| 4 | Back Pain | treatment | Low back pain - acute | treatment |
| 5 | Back Pain | treatment | Low back pain - acute | treatment |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### return_to_work

Condition: return to work after back pain

Requested reading level: 6th Grade

ED note: Adult with improving back pain asking when to return to work. Job involves lifting. Exam reassuring. Needs lifting precautions and gradual return guidance.

Retrieval query: return to work after back pain lifting precautions gradual activity home care

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | self_care | Back pain - returning to work | tips_to_help_prevent_back_pain_when_you_return_to_work |
| 2 | Back Pain | self_care | Back pain - returning to work | changes_at_work |
| 3 | Back Pain | treatment | Low back pain - acute | treatment |
| 4 | Back Pain | treatment | Low back pain - acute | treatment |
| 5 | Back Pain | self_care | Sacroiliac joint pain - aftercare | activity |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


### heat_vs_ice

Condition: heat versus ice for back pain

Requested reading level: 4th Grade

ED note: Adult with acute low back pain and no red flags. Asked whether to use ice or heat at home.

Retrieval query: acute low back pain ice heat home care instructions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 2 | Back Pain | treatment | Low back pain - acute | treatment |
| 3 | Back Pain | treatment | Low back pain - acute | treatment |
| 4 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 5 | Back Pain | overview | Taking care of your back at home | information |

Reviewer scores:

| field | score |
|---|---|
| clinically_safe |  |
| return_precautions_appropriate |  |
| home_care_specificity |  |
| medication_safety |  |
| reading_level_match |  |
| source_relevance |  |
| unsupported_claims |  |
| ready_for_app_integration |  |

Reviewer notes:


## Compare Against V1

Questions for review:

- Did sciatica improve from return precautions 2 and medication safety 2?
- Did neck strain improve from return precautions 2?
- Did atraumatic back pain and heat versus ice improve on medication safety and reading level?
- Is heat versus ice source relevance now acceptable despite continued SI aftercare use?
- Is return-to-work wording acceptable for app integration?
- Are at least 8 of 10 cases now ready for the back-pain-only feature flag?
