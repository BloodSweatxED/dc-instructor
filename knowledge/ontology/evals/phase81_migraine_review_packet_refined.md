# Phase 81 Migraine Review Packet Refinement

Target phenotype: `migraine_improved_discharge`.

Decision: revise. Do not promote.

Reason:

- The prior patient-facing text required revision after clinician review.
- Secondary-headache exclusion is too high-stakes for ontology-mode use without explicit clinician approval.
- Public sources support migraine education and general headache warning signs, but they do not by themselves validate ED discharge risk stratification.
- Broad headache and severe headache terms must not become standalone runtime matches.

Patient-facing output:

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

Required clinician review questions before any later promotion:

1. Are the secondary-headache blockers sufficient for this product surface?
2. Should pregnancy, age over 50 with new headache, immunocompromise, trauma, fever with headache, neurologic deficit, thunderclap onset, uncontrolled vomiting, and unstable vitals remain absolute runtime blockers?
3. Is the phrase "fits a migraine pattern" acceptable when the product is assembling discharge instructions from a clinician diagnosis?
4. Should this phenotype require explicit ED-note context that symptoms improved and no red flags were documented?

Clinician review answers incorporated:

- Secondary-headache blockers are not sufficient without runtime structured input confirmation.
- The absolute blockers are non-negotiable and should not be modifier-toggled or clinician-overrideable.
- First-lifetime headache of this severity and CT not performed with documented concern are soft blockers requiring an explicit clinician-override pathway before promotion.
- "Fits a migraine pattern" is not acceptable because it implies product inference.
- Negative-documentation language is not acceptable and was removed.
- Base home care should not reference vision returning to normal. Aura-specific language belongs in a conditional branch.
