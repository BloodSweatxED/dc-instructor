# Phase 801-850 Urticaria Split Audit

Status: complete.

Starting point:

- Phase 751-800 held constipation and left the Phase 21 gate open.
- Active draft queue was empty.
- The next recommendation was urticaria split audit or broad rash false-positive stress.

Decision:

Do not open a separate `urticaria_uncomplicated` draft in this macrocycle.

Reason:

The reviewed `allergic_reaction_resolved_no_anaphylaxis` phenotype already includes hives and urticaria as condition terms, but bare hives or bare urticaria currently route as low confidence unless the note documents the reviewed allergic-reaction boundary. That is the correct static v1 behavior.

Source support added:

- `medlineplus.hives`

Source-supported concepts:

- Hives are itchy raised skin bumps and are also called urticaria.
- Hives can be allergic, but can also occur with infections, stress, or other triggers.
- Many cases resolve, while more serious cases may need medicine or a shot.
- Airway swelling or trouble breathing with hives is an emergency.

Boundary finding:

A separate urticaria phenotype is not needed yet unless product usage shows frequent ED discharges where the clinician diagnosis is specifically acute urticaria rather than broader allergic reaction.

If reopened later, the safer candidate name is:

```text
acute_urticaria_reassuring_ed_assessment_no_anaphylaxis_or_angioedema
```

Possible inclusion boundary:

- adult
- clinician diagnosis or discharge impression of acute urticaria or hives
- symptoms improved or stable for discharge
- no anaphylaxis
- no airway symptoms
- no hypotension
- no epinephrine use or observation-level biphasic concern
- no mucosal lesions, target lesions, skin peeling, fever, infection concern, or severe cutaneous adverse reaction concern
- medication instructions entered by clinician only

Likely blockers:

- anaphylaxis, two-system allergic reaction, epinephrine use, hypotension, airway symptoms, throat swelling, tongue or lip swelling needing observation
- angioedema with airway concern or unclear disposition
- mucosal lesions, target lesions, skin peeling, SJS/TEN concern, serum sickness concern
- fever, cellulitis, purulence, sepsis, or infection concern
- pregnancy, pediatric pathway, immunocompromised host, frail elderly patient
- recurrent or chronic urticaria needing allergy workup rather than ED static discharge text
- unclear trigger when clinician wants close follow-up or observation

Runtime stress result:

- Explicit reviewed allergic-reaction discharge impression with hives still routes to `allergic_reaction_resolved_no_anaphylaxis`.
- Bare hives and bare urticaria remain low-confidence generator fallback, not reviewed ontology output.
- Broad itchy rash remains no-match.
- Hives with epinephrine, airway symptoms, mucosal lesions, or severe cutaneous adverse reaction language is blocked.
- Contact dermatitis and cellulitis routing remain separate.

Agent recommendation:

Hold. Do not draft or promote a separate urticaria phenotype yet.

Best next step if urticaria is reopened:

- Build only the narrow acute urticaria phenotype above.
- Keep medications clinician-entered.
- Require explicit no-anaphylaxis/no-airway/no-epinephrine/no-dangerous-rash context.
- Assemble a clinician review packet before promotion.

Verification:

- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase801_850_urticaria_split_audit.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/build_expanded_draft_packs.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/promote_reviewed_phenotypes.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/run_runtime_cases.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/build_phase21_expansion_gate.py`

Gate expectation:

- No active drafts.
- No `urticaria_uncomplicated` phenotype file.
- Phase 21 gate remains open.
