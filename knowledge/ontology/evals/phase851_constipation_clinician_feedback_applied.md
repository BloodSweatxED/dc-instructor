# Phase 851 Constipation Clinician Feedback Applied

Status: complete.

Clinician-owner decision:

```text
Revise, then promote as a narrow v1.
```

Promoted phenotype:

```text
adult_constipation_reassuring_ed_assessment_no_obstruction_or_bleeding
```

Patient-facing revisions applied:

- Rewrote `WHAT WE FOUND` to avoid implying imaging or definitive bowel-blockage exclusion.
- Added a one-to-three-day recovery timeline to `WHAT TO DO AT HOME`.
- Added cauda equina symptom language to `RETURN TO ED IF`.
- Tightened follow-up to primary care or urgent care within two to three days if not improving.

Clinical boundaries preserved:

- Adult only.
- Requires clinician diagnosis or discharge impression of constipation.
- Requires reassuring ED assessment or benign abdominal exam.
- Requires documented no-obstruction and no-GI-bleeding context.
- Keeps all laxative, stool-softener, enema, supplement, and fiber medicine instructions clinician-entered.
- Blocks frail or nursing-home patients and opioid-induced constipation for v1.

Runtime blockers:

- bowel obstruction, ileus, volvulus, no flatus, abdominal distention, severe or focal abdominal pain, peritoneal signs, surgical abdomen
- persistent vomiting, inability to tolerate oral fluids, severe dehydration
- GI bleeding, black stool, rectal bleeding
- fecal impaction requiring procedure or enema-specific pathway
- opioid-induced constipation
- elderly frail or nursing-home pathway
- pregnancy, pediatric pathway, immunocompromise
- cancer or weight-loss concern
- cauda equina concern, urinary retention
- poor follow-up

Patient-facing output:

```text
DIAGNOSIS:
You were treated for constipation.

WHAT WE FOUND:
Your clinician examined you and your symptoms were consistent with constipation. No signs of an emergency cause were found on exam.

WHAT TO DO AT HOME:
- Drink fluids as your clinician said is safe for you.
- Add fiber slowly with foods like fruits, vegetables, beans, or whole grains if you can tolerate them.
- Move around as tolerated. Walking can help your bowels move.
- Try to use the toilet shortly after meals when the urge is strongest.
- Most people see improvement within one to three days of starting treatment. If you are not improving by then, follow up rather than waiting longer.

MEDICATIONS:
- Take constipation medicines only as prescribed or recommended by your clinician.
- Do not add extra laxatives, stool softeners, enemas, or supplements unless your clinician told you to.
- Do not use laxatives if you develop severe abdominal pain, repeated vomiting, or a swollen belly.

RETURN TO ED IF:
- Severe or worsening abdominal pain.
- A swollen or hard belly.
- Repeated vomiting or you cannot keep fluids down.
- Blood in your stool, black stool, or rectal bleeding.
- Fever or feeling very ill.
- You cannot pass gas, especially with worsening abdominal pain or swelling.
- New back pain, leg weakness, or trouble urinating.

FOLLOW UP:
Follow up with your primary care provider or urgent care within two to three days if your symptoms are not improving. Return to the ED sooner if any of the above symptoms develop.
```
