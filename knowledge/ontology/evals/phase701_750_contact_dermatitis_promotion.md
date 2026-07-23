# Phase 701-750 Contact Dermatitis Promotion

Status: complete.

Starting point:

- Phase 651-700 opened `contact_dermatitis_uncomplicated` as a source-supported active draft.
- Clinician review returned revise.
- The revise items were applied: plain-language `WHAT WE FOUND`, recovery timeline, and return precaution cleanup.
- User then gave explicit clinician-owner promotion approval: "Promote. Run 701-750."

Promotion decision:

Promoted:

```text
contact_dermatitis_uncomplicated
```

Clinical boundary preserved:

- Shared irritant/allergic contact dermatitis v1.
- Adult only.
- Requires clinician diagnosis or discharge impression.
- Requires contact trigger or distribution context.
- Requires documented absence of dangerous rash features.
- Blocks anaphylaxis, airway symptoms, hypotension, epinephrine use, mucosal lesions, skin peeling/target lesions/SJS-TEN concern, infection concern, rapid progression, fever, sepsis, eye/genital location, chemical burn, immunocompromise, pregnancy, and pediatric pathway.

Patient-facing content preserved:

- No static hydrocortisone dosing.
- No static prednisone language.
- No static antihistamine dosing.
- No automatic antibiotic ointment advice.
- Plain-language finding sentence remains:

```text
Your clinician examined your rash and confirmed it is a skin reaction from contact with something, not an infection, allergic emergency, or serious medication reaction.
```

701-750 hardening:

- Added reviewed clean contact dermatitis and poison ivy dermatitis cases.
- Added genital location, chemical burn, immunocompromised host, target lesion/mucosal lesion, and rapid progression blockers.
- Added broad itchy-rash no-match guard.
- Preserved hives/allergic reaction routing.
- Preserved cellulitis as a separate low-confidence near miss, not contact dermatitis.
- Added two metadata-only output modifiers:
  - `occupational_recurrent_contact_dermatitis`
  - `frail_elderly_large_bsa_contact_dermatitis`

Files added:

- `knowledge/ontology/evals/phase701_750_contact_dermatitis_promotion_runtime_cases.json`
- `knowledge/ontology/evals/check_phase701_750_contact_dermatitis_promotion.py`

Files updated:

- `knowledge/ontology/scripts/promote_reviewed_phenotypes.py`
- `knowledge/ontology/scripts/classify_phenotype.py`
- `netlify/functions/ontology-runtime.js`
- `knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `knowledge/ontology/evals/check_low_confidence_near_misses.py`
- `knowledge/ontology/evals/check_phase651_700_contact_dermatitis_draft.py`
- `knowledge/ontology/evals/phase651_700_contact_dermatitis_runtime_cases.json`
- Generated phenotype, primitive, manifest, review sheet, runtime result, gate, and graph artifacts.

Verification:

- `knowledge/.venv/bin/python knowledge/ontology/scripts/build_expanded_draft_packs.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/promote_reviewed_phenotypes.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/run_runtime_cases.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/build_phase21_expansion_gate.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase651_700_contact_dermatitis_draft.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase701_750_contact_dermatitis_promotion.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase352_360_sprain_maintenance.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase602_650_wound_reviewed_stress.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase532_550_elbow_acute_traumatic_draft.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase551_600_elbow_review_queue.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_low_confidence_near_misses.py`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `node knowledge/ontology/evals/check_product_prompt_policy.mjs`
- `knowledge/.venv/bin/python knowledge/ontology/graph/build_seed_graph.py`
- `npm run build`
- `git diff --check`

Note:

Adjacent phase checkers were rerun serially after the generator/promote chain. A first parallel attempt caught expected mid-regeneration churn, then passed from the settled state.

Gate state:

- Reviewed runtime clean: true
- Phenotype expansion allowed: true
- Reviewed source gaps: 0
- Draft source gaps: 0
- Active draft phenotypes: 0
- Approved low-confidence near misses: 9
- Runtime cases: 471

Graph count:

- Nodes: 2265
- Edges: 3589
- Phenotype nodes: 61
- Primitive nodes: 446
- Candidate primitive nodes: 1099
- Source card nodes: 50

Next recommendation:

Run the next 50-phase macrocycle with the gate open. Best candidates remain source audit and boundary work before opening another draft:

- constipation source/boundary audit
- urticaria split product-need audit
- broad rash false-positive stress
- reviewed contact dermatitis post-promotion monitoring
