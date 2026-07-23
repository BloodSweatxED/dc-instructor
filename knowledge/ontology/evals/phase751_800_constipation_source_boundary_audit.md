# Phase 751-800 Constipation Source Boundary Audit

Status: complete.

Starting point:

- Phase 701-750 promoted `contact_dermatitis_uncomplicated`.
- Phase 21 gate was open.
- Active draft queue was empty.
- Next recommendation was constipation source/boundary audit, urticaria split audit, or broad rash false-positive stress.

Decision:

Do not open `constipation_uncomplicated` as a draft in this macrocycle.

Reason:

Constipation is source-supported, but the existing generator candidate is not safe enough for ontology v1. It includes static medication dosing and a broad reassurance frame that would be unsafe unless obstruction, GI bleeding, surgical abdomen, fecal impaction, frailty, pregnancy, pediatric pathway, opioid/medication-specific constipation, urinary retention or neurologic red flags, immunocompromise, cancer concern, and unreliable follow-up are explicitly handled.

Source cards added:

- `medlineplus.constipation_self_care`
- `niddk.constipation_adults`
- `medlineplus.intestinal_obstruction`

Source-supported concepts:

- Constipation can mean infrequent stool, hard/dry/lumpy stool, difficult or painful passage, or incomplete emptying.
- Self-care can include hydration, fiber, physical activity, regular bathroom routine, and responding to the urge to stool.
- Laxatives and stool softeners are not a simple static field in ED ontology. Sources support clinician-directed, time-limited use and warnings against laxative use when severe abdominal pain, nausea, or vomiting is present.
- Red flags include rectal bleeding or blood in stool, continual abdominal pain, nausea/vomiting, bloating or abdominal pain, and no bowel movement for several days.
- Obstruction is a must-not-miss pathway and can present with severe abdominal pain or cramping, vomiting, bloating, abdominal swelling, inability to pass gas, and constipation.

Candidate boundary if rebuilt later:

Only consider a future draft if it is framed as:

```text
adult_constipation_reassuring_ed_assessment_no_obstruction_or_bleeding
```

Possible inclusion boundary:

- adult
- clinician diagnosis or discharge impression of constipation
- benign abdominal exam or reassuring ED assessment
- passing gas or no obstruction concern documented
- no GI bleeding or melena
- no persistent vomiting
- no severe or focal abdominal pain
- no fecal impaction requiring procedure
- no pregnancy or pediatric pathway
- medication instructions entered by clinician only

Likely hard blockers:

- bowel obstruction, ileus, volvulus, no flatus, abdominal distention, severe abdominal pain, peritoneal signs, surgical abdomen
- persistent vomiting, inability to tolerate oral intake, dehydration requiring ongoing ED care
- blood in stool, melena, rectal bleeding with instability, anemia concern
- fecal impaction requiring disimpaction or enema-specific plan
- opioid-induced constipation requiring medication-specific counseling
- older/frail or nursing-home patient with new constipation
- pregnancy
- pediatric pathway
- immunocompromised host
- cancer or weight loss concern
- neurologic red flags, cauda equina concern, urinary retention
- unreliable follow-up when clinician wants recheck

Patient-facing language risks in the generator candidate:

- Static polyethylene glycol, docusate, and ibuprofen dosing.
- "No signs of blockage" requires an explicit ED assessment gate, not a generic statement.
- "The constipation is from..." overstates causation unless the clinician documented it.
- "7 days without a bowel movement" is too permissive for some ED contexts, especially if pain, vomiting, distention, frailty, or no flatus is present.

Agent recommendation:

Hold. Do not draft or promote constipation yet.

Best next step if constipation is chosen later:

- Build a narrow draft with clinician-entered medications only.
- Require explicit no-obstruction/no-bleeding/no-vomiting context.
- Use obstruction and GI bleeding as hard runtime blockers.
- Create a clinician review packet before any promotion.

Verification:

- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase751_800_constipation_source_audit.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/build_expanded_draft_packs.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/promote_reviewed_phenotypes.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/run_runtime_cases.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/build_phase21_expansion_gate.py`

Gate expectation:

- No active drafts.
- `constipation_uncomplicated` remains absent from reviewed/draft phenotype files.
- Phase 21 gate remains open.
