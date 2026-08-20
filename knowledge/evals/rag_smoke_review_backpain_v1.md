# RAG Smoke Review: Back Pain v1

Created: 2026-05-28

Source artifact: `knowledge/evals/rag_smoke_backpain_v1.json`

Collection: `medlineplus_backpain_v1_sections`

Purpose: Clinician review of the first MedlinePlus-backed RAG discharge instruction smoke test before app integration.

## Review Decision

Do not integrate into the app yet.

The v1 pipeline is promising, but it needs clinician scoring plus a tighter prompt/retrieval pass before it should sit behind a back-pain-only feature flag.

Main concerns to review:

- Return precautions are often clinically reasonable but may be too broad for routine discharge instructions.
- Some outputs pull high-risk wording from MedlinePlus provider-contact sections and convert it into ED return language.
- Reading level is mixed. The 4th grade cases still include terms like "bowel", "bladder", and "neurologic-style" phrasing.
- Medication wording needs stricter guardrails, especially NSAID cautions and avoiding implied universal safety.
- Retrieval sometimes overuses tangential but useful sections, especially sacroiliac joint aftercare for general low back pain.

## Pass Threshold For App Integration

Minimum before integration:

- 10 of 10 cases clinically safe.
- 8 of 10 cases ready for app integration after minor or no edits.
- No major unsupported claims.
- Mean score of 4 or higher for return precautions, home care specificity, medication safety, reading level match, and source relevance.
- Any failed safety case blocks app integration until fixed and rerun.

Recommended integration scope after passing:

- Feature flag: `rag_backpain_v1`.
- Use only for back-pain-family discharge diagnoses.
- Fall back to current non-RAG generation for all other conditions.
- Log retrieval metadata without PHI: case template id, collection version, source URLs, section types, ranks, distances, adjusted distances, generation model, and prompt version.

## Scoring Key

Use `pass` or `fail` for clinically safe.

Use 1 to 5 for scored fields:

- 1 = unsafe, irrelevant, or unusable
- 2 = major edits needed
- 3 = usable only with clinician rewrite
- 4 = minor edits needed
- 5 = ready as written

Unsupported claims:

- none = all material is supported by ED note or retrieved source context
- minor = low-risk extra detail or over-specific timing
- major = unsupported diagnosis, unsafe advice, or misleading clinical claim

Ready for app integration:

- yes = acceptable for the flagged workflow
- no = needs prompt, retrieval, or clinical content changes first

## Review Table

| case_id | clinically_safe | return_precautions_appropriate | home_care_specificity | medication_safety | reading_level_match | source_relevance | unsupported_claims | ready_for_app_integration | notes |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| lumbar_strain | pass | 3 | 4 | 4 | 4 | 3 | minor | no | Safe, but return precautions and source targeting need tightening. |
| sciatica | pass | 2 | 3 | 2 | 4 | 3 | minor | no | Weakest case. Return precautions are overbroad and NSAID safety language is missing. |
| atraumatic_back_pain | pass | 3 | 3 | 2 | 3 | 3 | none | no | Medication section is too nonspecific and 4th grade target is not met. |
| back_pain_red_flags | pass | 4 | 3 | 4 | 4 | 3 | minor | no | Safe, but retrieval pulls several spine-condition sections that may over-shape the output. |
| neck_strain | pass | 2 | 4 | 4 | 4 | 4 | minor | no | Return section is overcalibrated for atraumatic sleep-position neck strain. |
| ankle_sprain | pass | 5 | 5 | 4 | 5 | 5 | none | yes | Only integration-ready v1 case. |
| herniated_disk | pass | 4 | 3 | 3 | 4 | 3 | minor | no | Safe, but sedating-medication language is implied without ED-note support. |
| chronic_back_flare | pass | 4 | 4 | 4 | 4 | 3 | minor | no | Safe, but source mix and non-ED treatment suggestions need review. |
| return_to_work | pass | 4 | 5 | 4 | 4 | 5 | minor | no | Close. Main blocker is boss/work-restriction wording. |
| heat_vs_ice | pass | 3 | 5 | 3 | 3 | 2 | none | no | Good content, but source relevance is weak and 4th grade target is not met. |

## Clinician Pre-Score Summary

All 10 cases pass clinical safety. No output contains dangerous advice.

The main issue is not safety. It is quality and integration readiness. Most outputs are usable, but several are misguided in ways that would matter at scale.

Only `ankle_sprain` is ready for app integration as written.

Where to look hardest:

- `sciatica`: weakest case. Return precautions include UTI symptoms, night pain, and back redness, which are not ED return triggers for routine sciatica. Medication section mentions NSAIDs but skips contraindication language despite the ED note calling for an NSAID plan.
- `neck_strain`: return section includes chest-pain equivalents, dysphagia, and respiratory symptoms. These are not wrong in isolation, but they are overcalibrated for atraumatic sleep-position neck strain and may alarm patients.
- `atraumatic_back_pain`: medication section is too generic. It names no medications and gives no safety guardrails.
- `heat_vs_ice`: retrieval is almost entirely sacroiliac joint aftercare, including 3 of the top 5 slots from the same resource. The 4th grade target is not met.
- `herniated_disk`: "some medicines can make you sleepy" implies a sedating prescription that is not in the ED note.
- `return_to_work`: close to ready. Main blocker is the line about talking to the boss about lifting limits, which needs cleaner work-note boundary language.

## Patient-Facing Outputs To Review

These are the generated DC Instructor outputs from `knowledge/evals/rag_smoke_backpain_v1.json`, copied here so clinician review does not require reading nested JSON.

### lumbar_strain Output

```text
DIAGNOSIS:

You have a lumbar strain, which is a muscle injury in your lower back.

WHAT WE FOUND:

You hurt your lower back while lifting boxes. Your exam showed normal strength and feeling in your legs. You can walk normally. You do not have a fever. You have normal control of your bladder and bowels. These are all good signs that your back injury is a muscle strain.

WHAT TO DO AT HOME:

Stay active. Bed rest can actually make back pain worse. It is okay to move around and do your normal activities. Avoid heavy lifting and twisting your back for the next 6 weeks. If you need to stand for long periods, try resting one foot on a stool and switch feet throughout the day.

When you sleep on your back, place a pillow or rolled towel under your knees. This helps take pressure off your lower back.

Use ice packs on your back for 15 to 20 minutes at a time during the first few days. After a few days, you can switch to heat if that feels better.

After 2 to 3 weeks, you can start light exercise like walking. This helps your back get stronger.

MEDICATIONS:

Continue taking ibuprofen and acetaminophen as directed on the bottle for pain. Do not take more than the amount shown on the bottle. If you have heart disease, high blood pressure, kidney disease, or have had stomach ulcers or bleeding, talk to your regular doctor before using ibuprofen.

RETURN TO ED IF:

Come back to the emergency department or call 911 if you develop any of these symptoms:

Loss of control of your urine or bowel movements

Numbness in your buttocks, inner thighs, or groin area

Weakness or numbness in your legs

Pain that travels down your legs below the knee

Fever

Pain after a bad fall or injury

Losing weight without trying

Severe pain that does not get better with medicine

Unable to walk or keep your balance

FOLLOW UP:

See your regular doctor if your back pain lasts longer than 4 weeks. Your doctor may refer you to a physical therapist or specialist if needed. Physical therapy with stretching and strengthening exercises can help your back heal and prevent future injuries.
```

### sciatica Output

```text
DIAGNOSIS:

You have sciatica. This means a nerve in your lower back is irritated and causing pain that travels down your leg.

WHAT WE FOUND:

You came to the emergency department with low back pain that goes down your right leg. We examined you and found that you have signs of sciatica. The good news is that you do not have weakness in your legs. You are able to urinate normally. You do not have a fever. These are all good signs that your condition can get better at home with rest and medication.

WHAT TO DO AT HOME:

Rest your back but do not stay in bed all day. Light activity is okay. Do not do heavy lifting or twist your back for the next six weeks. You can use ice packs on the painful area for the first two to three days. After that, you can switch to heat packs if that feels better. Start gentle back exercises after two to three days to help strengthen your back muscles. Walking is a good way to start moving again. Do not push yourself too hard at first. Slowly return to your normal activities over the next few weeks.

MEDICATIONS:

Take ibuprofen or acetaminophen for pain as directed on the bottle. These medicines can help reduce your pain and let you move around more comfortably.

RETURN TO ED IF:

Come back to the emergency department right away if you develop any of these problems: you cannot control your urine or bowel movements, you feel new numbness or weakness in your legs or buttocks, you develop a fever, you have severe pain that will not go away even with medication, you notice redness or swelling on your back, you have pain when you urinate or see blood in your urine, your pain gets much worse when you lie down or wakes you up at night, or you have trouble walking or keeping your balance.

FOLLOW UP:

See your primary care doctor within one to two weeks. Your doctor can check how you are healing and help you with a plan to prevent this from happening again. If your back pain lasts longer than four weeks, make sure to call your doctor.
```

### atraumatic_back_pain Output

```text
DIAGNOSIS:

Lower back pain

WHAT WE FOUND:

You came to the Emergency Department with lower back pain that started two days ago. You did not have an injury. Your exam looked good. Your strength and feeling in your legs are normal. You did not need x-rays or other tests today.

WHAT TO DO AT HOME:

Rest when you need to, but try to keep moving a little bit each day. Do not stay in bed all day.

Use ice or a cold pack on your back for 15 minutes at a time during the first few days. After that, you can try heat if it feels better.

If you have to stand for a long time, rest one foot on a small stool. Switch feet during the day.

Do not lift heavy things right now.

MEDICATIONS:

You can take pain medicine you can buy at the store. Follow the directions on the bottle.

If your pain does not get better in a few days, call your regular doctor. They may give you other medicine or send you to a back specialist or physical therapist.

RETURN TO ED IF:

Come back to the Emergency Department or call 911 if you have any of these problems:

You cannot control your pee or poop

You feel numbness or weakness in your legs or bottom

You have trouble walking

You have pain going down your legs below your knee

You have a fever

Your back gets red or swollen

You have very bad pain that does not get better with rest or medicine

FOLLOW UP:

See your regular doctor in one to two weeks if your back pain is not getting better.

If your pain lasts more than four weeks, your doctor may send you to a back specialist.
```

### back_pain_red_flags Output

```text
DIAGNOSIS:
Back pain

WHAT WE FOUND:
Your exam today looked good. Your back pain does not show any warning signs that need treatment in the hospital right now. Your strength, feeling, and reflexes are normal.

WHAT TO DO AT HOME:
Rest when you need to, but try to stay active with light movement like walking. Do not stay in bed all day. Use ice packs on your back for 15 minutes at a time during the first few days. After a few days, you can try heat instead. Take over the counter pain medicine like ibuprofen or acetaminophen as directed on the bottle. Do not lift heavy things or twist your back. Sleep on your side with a pillow between your knees if that feels better.

MEDICATIONS:
You can take ibuprofen or acetaminophen for pain. Follow the directions on the bottle. Do not take more than the bottle says to take.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems:

Weakness or numbness in your legs, buttocks, or private area
Trouble controlling your pee or bowel movements
Pain that shoots down your legs below the knee
Back pain after a fall or injury
Fever with your back pain
Pain that gets much worse
Redness or swelling on your back
Pain so bad you cannot get comfortable in any position
Blood in your pee or burning when you pee
Trouble walking or keeping your balance

FOLLOW UP:
See your regular doctor within one week if your back pain does not get better. See your doctor sooner if you are losing weight without trying or if your back pain lasts longer than four weeks.
```

### neck_strain Output

```text
DIAGNOSIS:
Neck strain from sleeping in an awkward position.

WHAT WE FOUND:
You have muscle strain in your neck from the way you slept. We checked you and found no signs of serious injury. You can move your neck in all directions and you have no weakness or numbness in your arms or hands. This type of neck pain usually gets better with home care over the next week.

WHAT TO DO AT HOME:
Use ice packs on your neck for the first 2 days. Put ice on for 15 to 20 minutes at a time. After 2 days, you can switch to heat or continue with ice, whichever feels better. Take warm showers and let the water run over your neck and shoulders. Sleep on a firm mattress with a pillow that supports your neck. You can try a special neck pillow if regular pillows are not comfortable. Keep moving but avoid activities that make the pain worse. Gentle movement helps your neck heal better than staying completely still. After a few days, you can start gentle neck stretches. Slowly turn your head from side to side and tilt your ear toward your shoulder on each side. Do not push through severe pain. Walking and light activity are good for healing. Good posture is important. Try to keep your head aligned over your shoulders instead of leaning forward.

MEDICATIONS:
Take over the counter pain medicine like ibuprofen or acetaminophen as directed on the bottle. This will help with pain and swelling.

RETURN TO ED IF:
You develop numbness, tingling, or weakness in your arm or hand. Your pain gets worse when you lie down or wakes you up at night. Your pain becomes so severe that you cannot get comfortable. You lose control over urination or bowel movements. You have trouble walking or balancing. You develop a fever and headache, and your neck becomes so stiff that you cannot touch your chin to your chest. You have difficulty swallowing or breathing. You develop shortness of breath, sweating, nausea, vomiting, or arm or jaw pain.

FOLLOW UP:
See your regular doctor if your symptoms do not improve in 1 week with home care. Your doctor may recommend physical therapy if your pain continues. Physical therapy can include massage, stretching, and exercises to strengthen your neck muscles.
```

### ankle_sprain Output

```text
DIAGNOSIS:

You have an ankle sprain. This means you stretched or tore the ligaments in your ankle. The x-ray showed no broken bones.

WHAT WE FOUND:

You twisted your ankle while walking. Your ankle has some swelling. The nerves and blood flow to your foot are normal. The x-ray did not show any fractures.

WHAT TO DO AT HOME:

Rest your ankle and avoid putting your full weight on it at first. Use the brace we gave you to support your ankle. Put only as much weight on your foot as feels comfortable. Slowly increase how much you walk on it over the next few days.

Elevate your foot on a pillow at or above the level of your heart when you sit or lie down. This helps reduce swelling.

Apply ice to your ankle for 20 minutes every hour while you are awake for the first 24 hours. Cover the ice with a towel or put it in a bag. Do not put ice directly on your skin. Wait at least 30 minutes between ice treatments. After the first day, apply ice for 20 minutes three to four times per day.

The pain and swelling should get better within 48 hours. After that, you can begin to put more weight on your foot. If your ankle starts to hurt, stop and rest.

MEDICATIONS:

You can take ibuprofen or naproxen to help with pain and swelling. Follow the directions on the bottle. Do not take more than recommended. If you have heart disease, high blood pressure, kidney disease, liver disease, or have had stomach ulcers or bleeding problems, talk to your regular doctor before taking these medicines.

RETURN TO ED IF:

Come back to the emergency department if you have any of these problems:

Your pain gets much worse instead of better.
Your ankle becomes more swollen or you cannot put any weight on it at all.
Your foot becomes numb, cold, or changes color.
You develop a fever.
You see increasing redness or warmth spreading from your ankle.

FOLLOW UP:

See your primary care doctor within one week. Your doctor may want you to do exercises or physical therapy to strengthen your ankle and prevent future sprains. For mild sprains, you may return to normal activities in a few days. More severe sprains may take several weeks to heal. Ask your doctor before returning to sports or heavy work activities.
```

### herniated_disk Output

```text
DIAGNOSIS:
Herniated disk with back pain

WHAT WE FOUND:
You came to the emergency department with back pain from your known herniated disk. We checked you carefully and found no new signs of weakness. Your bowel and bladder function are normal. The pain medication we gave you helped improve your pain.

WHAT TO DO AT HOME:
Reduce your activity for the first few days at home. Rest, but you do not need to stay in bed all day. After a few days, slowly start doing your normal activities again. Avoid heavy lifting and avoid twisting your back for the next 6 weeks. After 2 to 3 weeks, you can gradually start exercising again. If you need to stand for long periods, rest one foot on a low stool and then switch to the other foot throughout the day. Apply ice or heat to your back as needed for comfort.

MEDICATIONS:
Take pain medicine as directed by your doctor. You may use over-the-counter pain relievers unless your doctor tells you otherwise. Do not take more than the amount shown on the bottle. If you have heart disease, high blood pressure, kidney disease, or have had stomach ulcers or internal bleeding, talk with your doctor before taking these medicines. Some pain medicines can make you sleepy, so be careful with driving or operating machinery.

RETURN TO ED IF:
You develop new weakness in your legs. You have trouble controlling your bowel or bladder. You develop numbness in your groin or rectal area. Your pain becomes severe and does not improve with your medications. You develop fever. You cannot walk or stand.

FOLLOW UP:
Follow up with your regular doctor or a spine specialist as advised. Physical therapy can help teach you exercises to strengthen your back and improve flexibility. Your doctor may discuss other treatment options with you if your symptoms do not improve over time.
```

### chronic_back_flare Output

```text
DIAGNOSIS:

Flare of chronic low back pain

WHAT WE FOUND:

You came to the emergency department because your chronic low back pain got worse. We checked you carefully. You do not have any injuries to your back. You do not have a fever or infection. Your nerves are working properly. This is a flare-up of your ongoing back pain problem.

WHAT TO DO AT HOME:

You can stay active, but listen to your body. You do not need to stay in bed for a long time. Move around as much as you can handle without making the pain much worse.

Use heat on your back to help with pain. You can use a heating pad or warm towel. You can also try ice for the first couple of days if heat does not help.

When you sleep, try lying on your side in a curled position with a pillow between your knees. If you sleep on your back, put a pillow under your knees.

Physical therapy with stretching and strengthening exercises can help. Your regular doctor may send you to a physical therapist.

Other treatments that may help include massage, acupuncture, or seeing a chiropractor.

MEDICATIONS:

You can take ibuprofen or naproxen for pain if it is safe for you. Follow the directions on the bottle. Do not take more than the bottle says. Do not take these medicines if you have kidney problems, stomach ulcers, or your doctor told you not to use them.

You can also try acetaminophen for pain. Follow the directions on the bottle.

RETURN TO ED IF:

Come back to the emergency department right away if you have any of these problems:

New weakness in your legs or feet
Trouble controlling your bowel or bladder
Numbness in your private area or upper inner thighs
Fever
Pain that gets much worse even with medicine
New injury to your back

FOLLOW UP:

See your regular doctor within one to two weeks. Your doctor can help you manage your chronic back pain and may refer you to specialists who can help with long-term treatment.
```

### return_to_work Output

```text
DIAGNOSIS:

Low back pain, improving

WHAT WE FOUND:

Your back is getting better. Your exam today looked good. You are ready to start going back to work, but you need to be careful with lifting at your job.

WHAT TO DO AT HOME:

Start back to work slowly if you can. If your job lets you work shorter days at first, that can help your back adjust.

When you lift things at work, use the right way to protect your back. Spread your feet apart to give yourself a wide base. Stand close to what you are lifting. Bend at your knees, not at your waist. Tighten your stomach muscles when you lift or put something down.

Know how much you can safely lift. Think about what you have lifted before and how hard it was. If something looks too heavy or awkward, get help. Do not try to lift it alone.

If you drive to work, adjust your car seat so it is easier to get in and out. Bring the seat forward so you do not have to bend when driving. If you drive a long way, stop every hour and walk around. Do not lift heavy things right after a long car ride.

Try not to stand in one place for a long time. If you must stand at work, rest one foot on a stool, then switch to the other foot.

Walk a little bit every day. Even a short walk helps keep your muscles strong and prevents more back pain.

MEDICATIONS:

Take over the counter pain medicine like ibuprofen or acetaminophen as needed for pain. Follow the directions on the bottle.

RETURN TO ED IF:

You have new weakness in your legs.

You lose control of your bladder or bowels.

You have numbness in your groin or buttocks area.

Your pain gets much worse instead of better.

You develop a fever.

You have severe pain that does not get better with rest and medicine.

FOLLOW UP:

See your regular doctor in one to two weeks to check on your progress. If your job requires heavy lifting, you may need to see a physical therapist to learn the safest way to lift the weights required at your work. Talk to your boss about the most you should have to lift while your back heals.
```

### heat_vs_ice Output

```text
DIAGNOSIS:

You have acute low back pain.

WHAT WE FOUND:

Your back hurts but we did not find any serious problems. Your exam was normal and you do not have warning signs that need more tests right now.

WHAT TO DO AT HOME:

Rest your back for the first few days. Stop activities that make the pain worse. You do not need to stay in bed all day but avoid heavy lifting and twisting.

You can use ice or heat on your back. Ice works well in the first 2 to 3 days. Put ice on your lower back for 20 minutes at a time. Do this 2 to 3 times a day. Do not put ice directly on your skin. Wrap it in a towel.

After 2 to 3 days you can switch to heat. Use a heating pad on a low setting to relax tight muscles.

When you sleep, try lying on your side with your knees bent and a pillow between your legs. If you sleep on your back, put a pillow under your knees.

Start moving again slowly after a few days. Do not stay still for too long.

MEDICATIONS:

You can take pain medicine you buy at the store. Ibuprofen or acetaminophen can help with pain. Follow the directions on the bottle. Do not take more than it says.

Talk to your doctor before taking ibuprofen if you have heart disease, high blood pressure, kidney disease, or have had stomach ulcers or bleeding in the past.

RETURN TO ED IF:

Come back to the emergency room if you have any of these problems:

Your pain gets much worse.

You lose control of your bowel or bladder.

You have weakness or numbness in your legs.

You have a fever.

You cannot walk or stand up.

FOLLOW UP:

See your regular doctor in 1 to 2 weeks if your back pain is not getting better. Your doctor may want to do more tests or try other treatments if the pain does not go away.
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
| 2 | Back Pain | self_care | Back pain - returning to work | changes_at_work |
| 3 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
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

Initial review flags:

- "Avoid heavy lifting and twisting your back for the next 6 weeks" may be too rigid for an uncomplicated lumbar strain.
- "Pain that travels down your legs below the knee" may be too broad as an ED return trigger without context.
- Top source is sacroiliac joint aftercare rather than general acute low back pain.

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
| 2 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |
| 3 | Sciatica | treatment | Sciatica | treatment |
| 4 | Back Pain | when_to_seek_care | Sacroiliac joint pain - aftercare | when_to_call_the_doctor |
| 5 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |

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

Initial review flags:

- Return precautions include many provider-contact items and may be too broad for ED return instructions.
- "Do not do heavy lifting or twist your back for the next six weeks" may be over-specific.
- Medication wording omits NSAID contraindication language despite NSAID plan.

Reviewer notes:


### atraumatic_back_pain

Condition: atraumatic low back pain

Requested reading level: 4th Grade

ED note: Adult with two days of lower back pain. No trauma. No neurologic deficits. No red flags. Vitals normal. No imaging indicated today.

Retrieval query: atraumatic acute low back pain discharge instructions home care return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 2 | Back Pain | self_care | Back pain - returning to work | changes_at_work |
| 3 | Back Pain | when_to_seek_care | Low back pain - chronic | when_to_contact_a_medical_professional |
| 4 | Back Pain | when_to_seek_care | Sacroiliac joint pain - aftercare | when_to_call_the_doctor |
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

Initial review flags:

- 4th grade reading level is only partially met.
- "Pain going down your legs below your knee" may be too broad as an ED return trigger.
- Medication section is too generic and does not name acetaminophen or NSAID safety guardrails.

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
| 2 | Spine Injuries and Disorders | when_to_seek_care | Compression fractures of the back | when_to_contact_a_medical_professional |
| 3 | Spine Injuries and Disorders | when_to_seek_care | Lordosis - lumbar | when_to_contact_a_medical_professional |
| 4 | Back Pain | when_to_seek_care | Back pain - when you see the doctor | information |
| 5 | Spine Injuries and Disorders | when_to_seek_care | Spondylolisthesis | when_to_contact_a_medical_professional |

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

Initial review flags:

- Retrieval includes compression fracture, lordosis, and spondylolisthesis sections for a generic red-flag case.
- Return precautions are comprehensive, but may include urinary symptoms and weight loss beyond the ED note intent.
- "Call 911" is not used here, which is better than several other outputs.

Reviewer notes:


### neck_strain

Condition: neck strain

Requested reading level: 6th Grade

ED note: Adult with neck pain after sleeping awkwardly. No trauma. No arm weakness or numbness. Full range of motion with discomfort. Discharged with conservative care.

Retrieval query: neck strain neck spasm home care conservative treatment return precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Neck Injuries and Disorders | when_to_seek_care | Neck pain or spasms - self care | when_to_call_the_doctor |
| 2 | Neck Injuries and Disorders | treatment | Neck pain or spasms - self care | stretches_and_exercises |
| 3 | Neck Injuries and Disorders | overview | Neck pain or spasms - self care | pain_relief |
| 4 | Neck Injuries and Disorders | self_care | Neck pain | home_care |
| 5 | Neck Injuries and Disorders | when_to_seek_care | Neck pain | when_to_contact_a_medical_professional |

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

Initial review flags:

- Return precautions include chest-pain equivalent symptoms, swallowing, breathing, bowel/bladder, and gait changes. Some are safe but too broad for benign atraumatic neck strain.
- Stretch advice may be too specific without clinician confirmation of range and timing.
- Output says symptoms usually improve over the next week. This is plausible but should be confirmed against source support.

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
| 2 | Sprains and Strains | self_care | Ankle sprain - aftercare | more_about_your_injury |
| 3 | Sprains and Strains | self_care | Foot sprain - aftercare | follow_up |
| 4 | Sprains and Strains | self_care | Ankle sprain - aftercare | self_care |
| 5 | Sprains and Strains | self_care | Ankle sprain - aftercare | getting_active |

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

Initial review flags:

- Strongest output in the set.
- Medication section mentions ibuprofen or naproxen but not acetaminophen. That may be fine, but verify against local discharge practice.
- Liver disease caution with naproxen may be less central than kidney disease, anticoagulants, ulcers, pregnancy, and allergy depending on local standard language.

Reviewer notes:


### herniated_disk

Condition: herniated disk

Requested reading level: 8th Grade

ED note: Adult with known herniated disk and recurrent back pain. No new weakness. No bowel or bladder symptoms. Pain improved with medication. Outpatient follow-up advised.

Retrieval query: herniated disk discharge instructions home care follow up weakness bowel bladder precautions

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Herniated Disk | treatment | Herniated disk | treatment |
| 2 | Back Pain | self_care | Back pain - returning to work | changes_at_work |
| 3 | Herniated Disk | treatment | Herniated disk | treatment |
| 4 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 5 | Herniated Disk | treatment | Herniated disk | treatment |

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

Initial review flags:

- Top sources are treatment-heavy and do not include enough self-care or when-to-seek-care content.
- "Avoid heavy lifting and avoid twisting your back for the next 6 weeks" may be over-specific.
- "Some pain medicines can make you sleepy" is reasonable but generic and may imply a sedating prescription not present in the ED note.

Reviewer notes:


### chronic_back_flare

Condition: chronic low back pain flare

Requested reading level: 6th Grade

ED note: Adult with flare of chronic low back pain. No trauma. No fever. No neurologic deficits. Discussed activity as tolerated, heat, NSAIDs if safe, and outpatient follow-up.

Retrieval query: chronic low back pain flare activity heat medicine home care follow up

Top retrieved sources:

| rank | topic | section_type | resource | section |
|---:|---|---|---|---|
| 1 | Back Pain | treatment | Low back pain - chronic | treatment |
| 2 | Back Pain | treatment | Low back pain - acute | treatment |
| 3 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 4 | Back Pain | treatment | Low back pain - acute | treatment |
| 5 | Back Pain | treatment | Low back pain - chronic | treatment |

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

Initial review flags:

- Includes chiropractic, acupuncture, and massage. These come from source context but may be more than desired in ED discharge copy.
- Needs clearer distinction between "follow up with your doctor" and ED return precautions.
- NSAID language is closer to target than several other cases.

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
| 3 | Back Pain | self_care | Back pain - returning to work | tips_to_help_prevent_back_pain_when_you_return_to_work |
| 4 | Back Pain | self_care | Back pain - returning to work | learn_how_to_lift |
| 5 | Back Pain | self_care | Back pain - returning to work | changes_at_work |

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

Initial review flags:

- Retrieval is highly relevant.
- Output correctly avoids turning return-to-work into emergency-return logic.
- Follow-up says "Talk to your boss about the most you should have to lift." This could conflict with clinician work-note boundaries and should be rephrased.

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
| 2 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |
| 3 | Back Pain | self_care | Sacroiliac joint pain - aftercare | follow_up |
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

Initial review flags:

- Good answer to the heat versus ice question.
- Top retrieval is dominated by sacroiliac joint aftercare and repeats the same resource.
- 4th grade reading level is close, but "bowel", "bladder", and "high blood pressure" phrasing may still need simplification.

Reviewer notes:


## Prompt Changes Needed

Add a prompt version before rerun: `backpain_rag_prompt_v2`.

Priority fixes from clinician pre-score:

1. Fix sciatica return precautions and NSAID safety language.
2. Fix neck strain return precautions so atraumatic benign neck pain does not receive alarm-heavy cardiopulmonary or dysphagia language.
3. Fix medication section requirements for atraumatic back pain and heat versus ice.
4. Fix 4th grade language enforcement for atraumatic back pain and heat versus ice.
5. Fix source diversity for heat versus ice and generic back pain so sacroiliac joint aftercare does not dominate.
6. Remove implied sedating-medication cautions unless the ED note includes a sedating medication.
7. Replace boss-negotiation wording with clinician-appropriate work restriction language.

Recommended changes:

- Split return advice into two groups: `come back to the ED now` and `call your regular doctor`.
- Tell the model not to promote every MedlinePlus provider-contact item into an ED return precaution.
- Limit ED return precautions to red flags supported by the ED note, the condition, or local emergency medicine consensus.
- Add condition-specific return precaution caps. For routine back pain, prefer 5 to 7 high-yield red flags.
- Add explicit medication rules:
  - Do not say NSAIDs are safe for everyone.
  - Mention acetaminophen separately from NSAIDs when both are reasonable.
  - Include short NSAID caution language when NSAIDs are suggested.
  - Do not mention sedating medications unless the ED note says they were prescribed or given.
- Add reading-level enforcement:
  - For 4th grade, use "pee or poop" instead of "urine or stool" unless the clinician selects otherwise.
  - Avoid anatomy-heavy phrasing unless it is needed for safety.
  - Keep sentences shorter than 15 words when possible.
- Add work-note boundary language:
  - Give lifting precautions.
  - Avoid telling the patient to negotiate medical restrictions directly with a boss unless the app has work-note support.
- Add source-use discipline:
  - Prefer the most general matching diagnosis source over tangential aftercare pages.
  - Use tangential sources only for generic self-care details.
  - Do not copy disease-specific advice from a related condition unless it applies to the patient.

## Retrieval Changes Needed

Recommended before app integration:

- Add diagnosis-family filters before vector query:
  - back pain: Back Pain, Sciatica, Herniated Disk, Spine Injuries and Disorders
  - neck strain: Neck Injuries and Disorders
  - ankle sprain: Sprains and Strains
- Add section diversity after rerank:
  - At least one self_care chunk when the case asks for home care.
  - At least one when_to_seek_care chunk when the case asks for return precautions.
  - At most two chunks from the same URL unless the query is explicitly about that resource.
- Penalize tangential resource titles when a general source is available:
  - For generic acute low back pain, prefer `Low back pain - acute` over `Sacroiliac joint pain - aftercare`.
  - For chronic flare, prefer `Low back pain - chronic` plus a self-care chunk.
- Add intent-specific retrieval presets:
  - `home_care`: boost self_care and treatment.
  - `return_precautions`: boost when_to_seek_care but cap output to ED-relevant red flags.
  - `return_to_work`: boost `Back pain - returning to work` and suppress emergency-return expansion.
  - `heat_ice`: boost self_care sections containing heat, ice, activity, and medication cautions.
- Store prompt version and retrieval preset in the smoke-test artifact.
- Add a retrieval eval that checks source mix, not only top-source relevance.

## Rerun Plan

1. Score this review artifact.
2. Patch prompt and retrieval.
3. Rerun:

```bash
python knowledge/rag_smoke_test.py --all
```

4. Save the new artifact as:

```text
knowledge/evals/rag_smoke_backpain_v2.json
```

5. Create a matching review file:

```text
knowledge/evals/rag_smoke_review_backpain_v2.md
```

6. Compare v1 to v2 for:

- Safety failures.
- Overbroad return precautions.
- Source relevance.
- Reading-level match.
- Medication safety.
