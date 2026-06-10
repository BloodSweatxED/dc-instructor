# RAG Smoke Review: Back Pain v3

Created: 2026-05-28

Source artifact: `knowledge/evals/rag_smoke_backpain_v3.json`

Collection: `medlineplus_backpain_v1_sections`

Prompt version: `backpain_rag_prompt_v3`

Retrieval version: `backpain_retrieval_v3`

Purpose: Focused review after v2 passed broad readiness but left lumbar strain as the only holdout.

## V3 Calibration Targets

- Preserve v2 wins for sciatica and neck strain.
- Move lumbar strain home care back above threshold.
- Prefer acute low back pain and general back-care sources over sacroiliac joint aftercare for routine lumbar strain and atraumatic low back pain.
- Keep uncomplicated lumbar strain home care practical: activity, ice then heat, sleep positioning, sitting support, and brief lifting precautions.
- Avoid chiropractor, massage, acupuncture, injections, or specialist-oriented advice in routine lumbar strain home care.

## Review Table

| case_id | clinically_safe | return_precautions_appropriate | home_care_specificity | medication_safety | reading_level_match | source_relevance | unsupported_claims | ready_for_app_integration | notes |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| lumbar_strain |  |  |  |  |  |  |  |  |  |
| sciatica |  |  |  |  |  |  |  |  |  |
| atraumatic_back_pain |  |  |  |  |  |  |  |  |  |
| back_pain_red_flags |  |  |  |  |  |  |  |  |  |
| neck_strain |  |  |  |  |  |  |  |  |  |
| ankle_sprain |  |  |  |  |  |  |  |  |  |
| herniated_disk |  |  |  |  |  |  |  |  |  |
| chronic_back_flare |  |  |  |  |  |  |  |  |  |
| return_to_work |  |  |  |  |  |  |  |  |  |
| heat_vs_ice |  |  |  |  |  |  |  |  |  |

## Patient-Facing Outputs To Review

### lumbar_strain Output

```text
DIAGNOSIS:

You have a lumbar strain. This is a muscle or ligament injury in your lower back.

WHAT WE FOUND:

Your exam today was reassuring. Your strength and feeling in your legs are normal. You can walk. You have no fever. You have no problems with controlling your bladder or bowels. These findings tell us your back pain is from a muscle strain and not from a serious problem with your nerves or spine.

WHAT TO DO AT HOME:

Stay gently active. Do not stay in bed all day. Resting too much can make back pain last longer. Move around the house and do light activities as you are able.

For the first day or two, avoid lifting heavy objects. Avoid twisting your back. Stop any activity that makes the pain much worse.

Use ice on the painful area for the first 1 to 2 days. Apply it for 15 to 20 minutes at a time. After the first 1 to 2 days, you can try heat instead if it feels better. Use a heating pad or warm towel.

Sleep in a position that feels comfortable. Many people feel better curled on their side with a pillow between their knees. If you sleep on your back, place a pillow under your knees.

When you sit, use good posture. Place a small pillow or rolled towel behind your lower back for support. If you sit for long periods, take breaks to stand and walk around.

As your pain improves over the next few days, you can slowly return to your normal activities.

MEDICATIONS:

You can take ibuprofen or acetaminophen for pain.

Ibuprofen works well for muscle and ligament pain. Take it with food to protect your stomach. Do not use ibuprofen if you have stomach ulcers, kidney problems, or if your doctor has told you not to take it.

You can use acetaminophen instead of ibuprofen or alternate between the two if one medicine alone does not help enough.

RETURN TO ED IF:

Come back to the emergency department right away if you develop any of these problems:

You lose control of your bladder or bowels.

You develop numbness in your groin, buttocks, or inner thighs.

You develop new weakness in your legs or trouble walking.

You develop a fever.

You fall or are injured and the pain suddenly gets much worse.

Your pain becomes so severe that you cannot get comfortable in any position.

FOLLOW UP:

See your regular doctor within 1 to 2 weeks to check on your progress.

If your pain lasts longer than 4 weeks or does not improve with home care, your doctor may refer you to a specialist or recommend physical therapy.
```

### sciatica Output

```text
DIAGNOSIS:
Sciatica affecting your right leg.

WHAT WE FOUND:
You have pain in your low back that travels down your right leg. This is called sciatica. It happens when a nerve in your lower back gets irritated or squeezed. We checked you carefully. You do not have any signs of nerve damage that would need emergency treatment. You can move your leg normally. You do not have a fever. You can control your bladder and bowels. These findings mean you can safely go home and treat this with rest, medicine, and follow-up care.

WHAT TO DO AT HOME:
Stay as active as you can, but avoid heavy lifting and twisting your back for the next six weeks. Bed rest is not helpful. Gentle movement is better. After two or three days, start walking and doing your normal activities slowly. Do not push through severe pain. Use ice on the painful area for the first two to three days. Put ice in a towel and apply it for 15 to 20 minutes at a time. After that, you can switch to heat if it feels better. Start gentle back exercises after a few days to keep your back and stomach muscles strong. Focus on good posture when you sit, stand, or drive. Sit up straight and do not slump.

MEDICATIONS:
You can take ibuprofen or naproxen for pain. These medicines reduce swelling and pain. Do not use ibuprofen or naproxen if you have kidney disease, stomach ulcers, a history of stomach bleeding, or if you take blood thinners. Do not use them if your doctor has told you to avoid these medicines. You can also use acetaminophen for pain. Acetaminophen does not reduce swelling, but it can help with discomfort. Follow the directions on the bottle. Do not take more than the label says.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems. New weakness in your leg or foot. New numbness in your groin, buttocks, or genital area. Trouble controlling your pee or poop. Fever. You cannot walk or put weight on your leg. Pain becomes much worse even after taking medicine and resting.

FOLLOW UP:
See your primary care doctor within one to two weeks. Your doctor can check your progress and help you with exercises or other treatments if the pain is not improving. If your pain lasts longer than four weeks, call your doctor for another visit.
```

### atraumatic_back_pain Output

```text
DIAGNOSIS:
Low back pain with no serious signs.

WHAT WE FOUND:
You have pain in your lower back. You did not have an injury. We checked you carefully. Your strength is normal. You can feel things normally. You do not have any warning signs of a serious problem. You do not need an x-ray or other scan right now.

WHAT TO DO AT HOME:
Stay active. You do not need bed rest. Move around gently. Short walks help. Stop heavy lifting for a few days. Stop hard exercise for a few days. Use ice on your back for the first two to three days. Put the ice pack on for fifteen to twenty minutes at a time. After two to three days, you can try heat instead. A heating pad or warm towel may help. When you sit, put a small pillow or rolled towel behind your lower back. If you sit for a long time, put a stool under your feet so your knees are higher than your hips. When you sleep, try lying on your side with your knees bent. Put a pillow between your knees. If you sleep on your back, put a pillow under your knees. Do not lift heavy things for a few days. When you feel better, gentle exercises to make your belly muscles stronger can help protect your back.

MEDICATIONS:
You can take ibuprofen or naproxen for pain. These are sold without a prescription. Do not use these medicines if you have kidney disease, stomach ulcers, stomach bleeding, take blood thinners, or were told to avoid these medicines. You can take acetaminophen instead. This is also sold without a prescription. Follow the directions on the bottle.

RETURN TO ED IF:
Come back to the emergency department right away if you have new weakness in your legs, new numbness in your groin or bottom, trouble controlling your pee or poop, fever, trouble walking, or very bad pain that keeps getting worse.

FOLLOW UP:
See your regular doctor in one to two weeks if your pain does not get better. If your pain lasts longer than four weeks, your doctor may send you to a specialist. Physical therapy, stretching, or exercises may help. Some people also get better with massage, acupuncture, or a visit to a chiropractor.
```

### back_pain_red_flags Output

```text
DIAGNOSIS:
Back pain

WHAT WE FOUND:
Your exam today showed that your back pain is not caused by a serious problem right now. Your nerves, strength, and reflexes look good. You do not have signs of infection or nerve damage at this time.

WHAT TO DO AT HOME:
Rest your back for the first day or two, but try to return to light activities as soon as you can. Staying in bed too long can make back pain worse. Move slowly and avoid heavy lifting, bending, or twisting. Use ice packs on your back for 15 to 20 minutes at a time during the first two days. After that, you can try heat packs or warm baths if they feel better. Do gentle stretches when you feel ready. Walk short distances several times a day to keep your back from getting stiff.

MEDICATIONS:
You can take over the counter pain medicines like ibuprofen or naproxen to help with pain and swelling. Take these with food to protect your stomach. You can also use acetaminophen if you prefer. Follow the directions on the bottle and do not take more than recommended. If you have kidney problems, stomach ulcers, or take blood thinners, ask your regular doctor before using ibuprofen or naproxen.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems:

Weakness or numbness in your legs or feet
Loss of control of your urine or bowel movements
Numbness in your buttocks, groin, or inner thighs
Fever with your back pain
Pain that shoots down your leg below your knee
Pain that gets much worse instead of better
Back pain after a fall or injury
Trouble walking or keeping your balance

FOLLOW UP:
See your regular doctor in one to two weeks if your pain is not getting better. Also see your doctor if this back pain feels different or worse than back pain you have had before. Make an appointment sooner if you are losing weight without trying or if your pain lasts longer than four weeks.
```

### neck_strain Output

```text
DIAGNOSIS:
Neck strain from sleeping in an awkward position.

WHAT WE FOUND:
Your exam today showed neck muscle strain. You have no weakness or numbness in your arms. Your neck moves in all directions even though it is uncomfortable. This type of neck pain usually gets better with rest and simple home care.

WHAT TO DO AT HOME:
Apply ice to your neck for the first two to three days. Put the ice in a towel or use an ice pack for 15 to 20 minutes at a time. After two to three days, switch to heat. Use warm showers, a heating pad, or warm compresses. Do not fall asleep with a heating pad or ice on your neck.

Rest from your normal activities for the first few days to let the swelling go down. After that, slowly move your neck up and down, side to side, and ear to ear. These gentle movements stretch the muscles.

Ask someone to gently rub the sore areas. Sleep on a firm mattress with a pillow that supports your neck. A regular pillow or a special neck pillow can work.

You can use a soft neck collar for short times if it helps, but do not wear it all day long. Your neck muscles need to stay strong.

Start light activities like walking or gentle stretching when you feel ready. Do not start exercises too soon or your pain may get worse.

MEDICATIONS:
You can take over-the-counter pain relievers like ibuprofen or acetaminophen. Follow the directions on the bottle. If you have stomach problems, kidney problems, or take blood thinners, ask your doctor before using ibuprofen.

RETURN TO ED IF:
You develop numbness, tingling, or weakness in your arm or hand.

You have a fever and your neck becomes very stiff.

You injure your neck in a fall or accident.

Your pain gets much worse.

You have trouble walking or keeping your balance.

You lose control of your bladder or bowels.

FOLLOW UP:
See your regular doctor if your neck pain does not improve in one week with home care.
```

### ankle_sprain Output

```text
DIAGNOSIS:
Ankle sprain

WHAT WE FOUND:
You twisted your ankle while walking. Your x-ray showed no broken bones. You have some swelling but your nerves and blood flow are working well.

WHAT TO DO AT HOME:
Rest your ankle as much as you can for the next few days. Put ice on your ankle for 15 to 20 minutes at a time, several times each day. Keep your ankle elevated above your heart when you sit or lie down. This helps reduce swelling. Wear the brace we gave you to protect your ankle. You may need to keep some or all of your weight off your injured ankle for a few days. Walk carefully and avoid activities that cause pain.

MEDICATIONS:
You can take over-the-counter pain medicine such as ibuprofen or naproxen to help with pain and swelling. If you have kidney problems, stomach ulcers, or take blood thinners, talk to your regular doctor before taking these medicines. You can also take acetaminophen for pain.

RETURN TO ED IF:
You cannot walk or walking causes severe pain. Your pain gets worse instead of better. Your ankle becomes more swollen or the swelling does not go down. Your ankle becomes red, black and blue, or very discolored. Your foot or toes become numb, tingly, cold, or change color. You develop a fever.

FOLLOW UP:
See your regular doctor in 5 to 7 days to check how your ankle is healing. If your ankle still feels weak or gives out easily after a few weeks, you may need more treatment or physical therapy. Talk to your doctor before you go back to sports or high impact activities.
```

### herniated_disk Output

```text
DIAGNOSIS:
Herniated disk with recurrent back pain

WHAT WE FOUND:
You came to the emergency department with back pain from your known herniated disk. We checked you and found no signs of new nerve problems. You do not have weakness in your legs. Your bladder and bowel control are normal. The medication we gave you helped your pain improve.

WHAT TO DO AT HOME:
Rest for the first few days but avoid staying in bed all day. Start moving around as you feel able. Avoid heavy lifting and twisting your back for the next six weeks. After two to three weeks, you can slowly start exercising again.

When you sit, use a small pillow or rolled towel behind your lower back for support. Put a stool under your feet so your knees are higher than your hips. If you stand at work for long periods, rest one foot on a stool and switch feet throughout the day.

Apply ice or heat to your back for comfort. Do whichever feels better to you.

Start gentle exercises to strengthen your stomach muscles when your pain improves. This helps protect your back. Stretching exercises for your spine and legs also help. Consider yoga, tai chi, or physical therapy.

MEDICATIONS:
Continue taking the pain medication as directed by your doctor. You can use over-the-counter pain relievers like ibuprofen or naproxen if you do not have kidney problems, stomach ulcers, or bleeding problems. You can also use acetaminophen. Follow the directions on the bottle.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these problems:

Severe back pain that does not improve with medication
New numbness or tingling in your legs, feet, or private area
New weakness in your legs or trouble walking
Loss of control of your bladder or bowels
Pain that shoots down your leg below your knee
Fever with your back pain
Pain after a fall or injury

FOLLOW UP:
See your regular doctor or spine specialist within one to two weeks. They can help you with long-term treatment for your herniated disk. You may need physical therapy or other treatments. Call to schedule your appointment in the next few days.
```

### chronic_back_flare Output

```text
DIAGNOSIS:

Flare of chronic low back pain

WHAT WE FOUND:

Your back pain has gotten worse, but we did not find signs of nerve damage, infection, or injury that needs emergency treatment. This is a flare of your long-term back pain.

WHAT TO DO AT HOME:

You can move around and do your normal activities as much as you can handle. You do not need to stay in bed. Moving helps your back heal better than resting for a long time.

Use heat on your back to help with pain and stiffness. You can use a heating pad or warm towel for 15 to 20 minutes at a time.

If you usually sleep on your back, put a pillow under your knees. If you sleep on your side, put a pillow between your knees.

Gentle stretching may help when you feel ready. Do not push through sharp pain.

MEDICATIONS:

You can take over-the-counter pain medicines like ibuprofen or naproxen if they are safe for you. Do not take these medicines if you have kidney disease, heart disease, high blood pressure, or have had stomach ulcers or bleeding in your stomach before. Follow the directions on the bottle. Do not take more than the bottle says.

You can also take acetaminophen for pain. Follow the directions on the bottle.

RETURN TO ED IF:

Come back to the emergency department if you have any of these problems:

You lose control of your bladder or bowel.

You have numbness or weakness in your legs or feet.

You cannot stand or walk when you could before.

You have a fever.

Your pain becomes much worse and does not get better with medicine.

FOLLOW UP:

See your regular doctor or a back specialist in the next one to two weeks. They can help you manage your chronic back pain with physical therapy, exercises, or other treatments. If your pain does not get better with home care and medicine, they may talk to you about other options like injections or referral to a specialist.
```

### return_to_work Output

```text
DIAGNOSIS:
Back pain that is getting better

WHAT WE FOUND:
Your exam today looked good. Your back pain is improving. You want to know when you can go back to your job that involves lifting.

WHAT TO DO AT HOME:
You can start going back to work, but take it slow. Start with light duty if you can. Avoid heavy lifting for the first few days. When you do lift, bend your knees and keep the object close to your body. Do not twist while lifting.

If you drive to work, adjust your car seat so it is easier to get in and out. Move the seat forward so you do not have to lean forward while driving. If you drive a long distance, stop every hour and walk around. Do not lift heavy objects right after a long car ride.

Avoid standing in one place for long periods. If you must stand at work, put one foot on a low stool or box and switch feet throughout the day.

Keep moving at home. Walking and gentle activity help your back heal. After a few weeks, you can slowly add more exercise like swimming or riding a bike. Do not start hard exercise too soon.

Use ice or heat on your back for comfort. Ice works well in the first few days. Heat can help after that. Use for 15 to 20 minutes at a time.

MEDICATIONS:
You can take over the counter pain medicine like ibuprofen or acetaminophen as directed on the package. Take ibuprofen with food. Do not take ibuprofen if you have stomach ulcers or kidney problems.

RETURN TO ED IF:
Come back to the emergency department if you have any of these problems:

New numbness or weakness in your legs or feet
Trouble controlling your bowel or bladder
Pain that gets much worse instead of better
Fever or chills
New shooting pain down your leg

FOLLOW UP:
Follow any work note instructions you were given. If you need changes to your work duties, talk to your regular doctor. Your doctor can write a note with lifting limits or other restrictions.

If your pain lasts more than one month, your doctor may send you to a back specialist or physical therapist. Physical therapy can teach you exercises to strengthen your back and prevent future injuries.
```

### heat_vs_ice Output

```text
DIAGNOSIS:
Acute low back pain

WHAT WE FOUND:
Your back exam today looks good. We do not see any red flags or signs of a serious problem. This is a common injury and most people get better over a few weeks.

WHAT TO DO AT HOME:
You can use ice or heat at home. Both can help. Try ice first. Use ice for the first two to three days. Put the ice pack on your lower back for about 20 minutes at a time. Do it two or three times a day. Do not put ice right on your skin. After two or three days you can switch to heat. Use a heating pad on a low setting to help loosen tight muscles and ease soreness.

Stay as active as you can. Do not stay in bed all day. Stop or slow down your normal activities for just the first few days. This helps calm the pain and reduce swelling. Then slowly go back to what you usually do.

Try lying in a curled up position when you sleep. Put a pillow between your legs. If you sleep on your back put a pillow or rolled towel under your knees.

MEDICATIONS:
You can take over the counter pain medicine.

Ibuprofen or Motrin can help. Naproxen or Aleve can help. Do not take these medicines if you have kidney disease, have had stomach ulcers or bleeding, take blood thinners, or have been told by a doctor to avoid them. Follow the directions on the bottle. Do not take more than the bottle says.

Acetaminophen or Tylenol is another choice for pain. Follow the directions on the bottle. Do not take more than the bottle says.

RETURN TO ED IF:
Come back to the emergency department right away if you have any of these:

New weakness in your legs or trouble walking.

Numbness or loss of feeling in your groin, bottom, or private area.

Trouble controlling your pee or poop or cannot pee.

Fever.

Pain gets much worse or does not start to get better after a few weeks.

Fall or major injury to your back.

FOLLOW UP:
Follow up with your regular doctor in one to two weeks if your pain is not getting better. Your doctor may send you to physical therapy or a specialist if needed.
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
| 1 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 2 | Back Pain | treatment | Low back pain - acute | treatment |
| 3 | Back Pain | overview | Taking care of your back at home | information |
| 4 | Back Pain | overview | Taking care of your back at home | information |
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
| 1 | Back Pain | when_to_seek_care | Low back pain - acute | when_to_contact_a_medical_professional |
| 2 | Back Pain | treatment | Low back pain - acute | treatment |
| 3 | Back Pain | overview | Taking care of your back at home | information |
| 4 | Back Pain | overview | Taking care of your back at home | information |
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
| 4 | Back Pain | overview | Taking care of your back at home | information |
| 5 | Back Pain | self_care | Sacroiliac joint pain - aftercare | symptom_relief |

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


## Compare Against V2

Questions for review:

- Did lumbar strain home care improve from 3 to at least 4?
- Did lumbar strain remain clinically safe after source changes?
- Did source relevance improve for lumbar strain and atraumatic back pain?
- Did sciatica and neck strain remain integration-ready?
- Is the full set now ready for back-pain-only feature-flag integration?

