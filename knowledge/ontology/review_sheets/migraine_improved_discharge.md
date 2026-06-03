# Migraine improved after ED treatment

Phenotype ID: `migraine_improved_discharge`

Status: `retired`

Review status: revise. Not ready for promotion.

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of migraine that improved after ED treatment.
- Structured confirmation of clinical improvement after ED treatment is present.
- Structured confirmation that headache red flags are absent is present. Do not infer this from lack of documentation.

## Exclusions

- Sudden, severe headache that reaches its worst point within seconds, worst headache of life, subarachnoid hemorrhage concern, stroke/TIA concern, unresolved neurologic deficit, seizure, or altered mental status not fully resolved at discharge.
- Fever with headache, neck stiffness, meningitis/encephalitis concern, pregnancy, immunocompromise, head trauma within 7 days, age over 50 with new headache pattern, or unstable vital signs.
- Uncontrolled vomiting at discharge, specialist-directed neurology plan, headache not improved enough for discharge, first-lifetime headache of this severity, or CT not performed when documented concern exists.

## Must-Not-Miss Diagnoses

- Subarachnoid hemorrhage.
- Stroke or TIA.
- Meningitis or encephalitis.
- Intracranial mass or elevated intracranial pressure.
- Cerebral venous thrombosis.
- Pre-eclampsia in pregnancy.

## Runtime Requirements

- Requires structured clinical improvement.
- Requires structured red-flag absence.
- Does not use broad headache or severe headache as standalone terms.
- Soft blockers remain blockers until an explicit clinician-override pathway exists.

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician diagnosed your headache as a migraine. Your symptoms improved with treatment.

WHAT WE FOUND:
Your ED team treated your migraine and confirmed that you were improved enough to go home with this plan.

WHAT TO DO AT HOME:
- Rest in a quiet, dark place if symptoms return.
- Drink more fluids if you can and avoid triggers you already know affect you.
- Limit screen time, bright light, noise, and heavy mental stimulation while you are recovering.
- Use stress reduction techniques that work for you, such as slow breathing, quiet rest, or gentle stretching.
- Avoid driving or operating heavy machinery until you feel fully alert and your thinking is clear.
- Most people feel better within one to two days. Fatigue and trouble concentrating can last up to 48 hours after a migraine resolves.
- Keep a headache log. Write down or record on your phone when headaches start, how long they last, how severe they are, and any symptoms that come with them. Bring this log to your follow-up visit.

MEDICATIONS:
- Use only the headache medicines your clinician prescribed or said are safe for you.
- Do not take extra doses or mix medicines unless your clinician told you to.

RETURN TO ED IF:
- A sudden, severe headache that reaches its worst point within seconds, or feels like the worst headache of your life; headache after injury; fainting; confusion; seizure; or trouble staying awake.
- New weakness, numbness, trouble speaking, vision loss, trouble walking, fever, or stiff neck.
- Vomiting that will not stop, headache that is much worse or different than usual, or symptoms that do not improve as expected.

FOLLOW UP:
Follow up with primary care or a headache clinician as instructed, especially if headaches are new, changing, or frequent.
```
