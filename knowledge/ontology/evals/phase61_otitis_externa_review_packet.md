# Phase 61 Otitis Externa Clinician Review Packet

Target phenotype: `otitis_externa_no_mastoiditis`.

Decision: do not promote.

Boundary requirements:

- Mastoiditis or deep ear infection concern must block ontology mode.
- Malignant otitis externa risk, diabetes, immunocompromise, fever, and unstable vitals must block ontology mode.
- Tympanic membrane perforation or tube must block ontology mode.
- Ear trauma, foreign body, acute hearing loss, facial weakness, vertigo, or severe dizziness must block ontology mode.
- Broad ear pain and ear drainage must not match as standalone terms.

Patient-facing output:

```text
DIAGNOSIS:
Your symptoms fit otitis externa, also called swimmer's ear.

WHAT WE FOUND:
Your clinician did not document mastoiditis concern, a deep ear infection, eardrum rupture, or another ear emergency in these discharge instructions.

WHAT TO DO AT HOME:
- Keep the ear dry unless your clinician told you something different.
- Do not put cotton swabs, earbuds, or other objects into the ear canal.
- Avoid swimming until your clinician says it is safe.

MEDICATIONS:
- Use ear drops only as prescribed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, worsening pain, severe headache, confusion, or feeling very ill.
- Redness, swelling, or pain behind the ear, or the ear starts sticking out.
- New hearing loss, dizziness, facial weakness, or drainage that gets worse.

FOLLOW UP:
Follow up with primary care, urgent care, or an ear clinician as instructed.
```
