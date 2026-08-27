# Phase 51 Conjunctivitis Clinician Review Packet

Target phenotype: `conjunctivitis_uncomplicated_no_contact_lens`.

Decision: do not promote.

This packet preserves the full patient-facing draft so the reviewer does not need to reconstruct it from JSON.

Boundary requirements:

- Contact lens use must block ontology mode.
- Corneal abrasion, corneal ulcer, keratitis, trauma, foreign body, and chemical exposure must block ontology mode.
- Vision change, photophobia, severe eye pain, herpes/zoster eye concern, and acute glaucoma mimic language must block ontology mode.
- Periorbital/orbital cellulitis concern must block ontology mode.
- Immunocompromise and pregnancy must block ontology mode.
- No antibiotic eye-drop instructions may be inferred.
- Broad red eye, itchy eye, and eye discharge must not match as standalone terms.

Patient-facing output:

```text
DIAGNOSIS:
Your symptoms fit conjunctivitis, also called pink eye.

WHAT WE FOUND:
Your clinician did not document contact lens risk, eye injury, vision loss, or another eye emergency in these discharge instructions.

WHAT TO DO AT HOME:
- Wash your hands often and avoid touching or rubbing the eye.
- Do not share towels, pillowcases, makeup, or eye drops.
- Use a clean warm or cool compress if your clinician said it is safe.

MEDICATIONS:
- Use only the eye drops or medicines your clinician prescribed or said are safe for you.
- Do not use contact lenses until your clinician says it is safe.

RETURN TO ED IF:
- Eye pain, light sensitivity, vision changes, or worsening redness.
- Swelling around the eye, trouble moving the eye, fever, or feeling very ill.
- Symptoms get worse, do not improve as expected, or you were exposed to chemicals or an eye injury.

FOLLOW UP:
Follow up with primary care, urgent care, or an eye clinician as instructed.
```

Reviewer note: this remains useful as a product-layer draft, but not as reviewed runtime content.
