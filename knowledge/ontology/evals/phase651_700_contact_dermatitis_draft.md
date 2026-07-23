# Phase 651-700 Contact Dermatitis Draft

Status: complete.

Starting point:

- Phase 602-650 left the Phase 21 gate open.
- Active draft queue was empty.
- Next recommendation was candidate ranking and source audit.

Candidate decision:

Selected `contact_dermatitis_uncomplicated` as the next draft candidate.

Why:

- It is common.
- It is non-sprain and non-wound.
- It has source support from MedlinePlus.
- It is narrower and safer than syncope, chest pain, hypertension, BPPV, constipation, or viral syndrome.
- Runtime can require clinician diagnosis, trigger/distribution context, and documented absence of dangerous rash features.

Deferred:

- `constipation_uncomplicated`: source support exists, but abdominal obstruction, GI bleeding, medication-specific laxative advice, elderly/frailty, and abdominal pain overlap make it a higher-risk static draft.
- `asymptomatic_hypertension_no_end_organ_damage`: clinically common but medication and follow-up decisions are too clinician-dependent.
- `peripheral_vertigo_bppv_likely`: high posterior circulation stroke miss risk.
- `syncope_low_risk_discharge` and `chest_pain_low_risk_negative_ed_workup`: remain too risk-stratification-dependent.
- `urticaria_no_anaphylaxis`: overlaps with reviewed allergic reaction pathway and needs a clearer product reason before splitting.

Files added:

- `knowledge/ontology/source_cards/medlineplus.contact_dermatitis.json`
- `knowledge/ontology/evals/phase651_700_contact_dermatitis_runtime_cases.json`
- `knowledge/ontology/evals/check_phase651_700_contact_dermatitis_draft.py`
- `knowledge/ontology/review_sheets/contact_dermatitis_uncomplicated_v1_review_packet.md`

Files updated:

- `knowledge/ontology/scripts/build_expanded_draft_packs.py`
- `knowledge/ontology/scripts/classify_phenotype.py`
- `netlify/functions/ontology-runtime.js`
- `knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- Phase 532, 551, and 602 checkers now tolerate unrelated later active drafts while still protecting their own reviewed phenotype contracts.
- Generated phenotype, primitive, manifest, review sheet, runtime result, gate, and graph artifacts.

Review queue:

| ID | Phase | Phenotype | Review Type | Decision Needed | Agent Recommendation | Blocked Action | Safe Work Continued |
|---|---:|---|---|---|---|---|---|
| contact_dermatitis_v1 | 651 | `contact_dermatitis_uncomplicated` | clinical boundary and patient-facing wording | confirm revised draft, promote/revise/retire/hold | clinician review returned revise; targeted wording fixes are applied; promotion still requires explicit approval | promotion | runtime hardening, broad rash stress, source audit |

Clinician review result:

- Verdict: revise.
- Keep a shared irritant/allergic contact dermatitis v1 phenotype.
- Keep eye/genital involvement as a hard blocker.
- Keep medication guidance clinician-entered only.
- Applied plain-language `WHAT WE FOUND` rewrite.
- Added recovery timeline to home care.
- Trimmed third return precaution to remove eye/genital language.

Assembled patient note:

```text
knowledge/ontology/review_sheets/contact_dermatitis_uncomplicated_v1_review_packet.md
```

Verification:

- `knowledge/.venv/bin/python knowledge/ontology/scripts/build_expanded_draft_packs.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/promote_reviewed_phenotypes.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/run_runtime_cases.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/build_phase21_expansion_gate.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase651_700_contact_dermatitis_draft.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase352_360_sprain_maintenance.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase602_650_wound_reviewed_stress.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase532_550_elbow_acute_traumatic_draft.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase551_600_elbow_review_queue.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `node knowledge/ontology/evals/check_product_prompt_policy.mjs`
- `knowledge/.venv/bin/python knowledge/ontology/graph/build_seed_graph.py`
- `npm run build`
- `git diff --check`

Expected gate state after macrocycle:

- Reviewed runtime clean: true
- Phenotype expansion allowed: false
- Reviewed source gaps: 0
- Draft source gaps: 0
- Active draft phenotypes: `contact_dermatitis_uncomplicated`
- Runtime cases: 459

Graph count:

- Nodes: 2265
- Edges: 3589
- Phenotype nodes: 61
- Primitive nodes: 446
- Candidate primitive nodes: 1099
- Source card nodes: 50

Next recommendation:

Pause promotion until explicit clinician approval of revised `contact_dermatitis_uncomplicated`.

Safe next macrocycle:

- Harden broad rash false positives.
- Add additional contact dermatitis trap cases if needed.
- Source-audit a backup candidate such as constipation without opening another draft.
