# Phase 371-390 Elbow Overuse Draft

Status: draft complete, not promoted.

Phenotype:

`elbow_sprain_overuse_xray_negative`

Confirmed scope:

- Adult lateral epicondylitis, medial epicondylitis, elbow overuse strain, or subacute/chronic elbow overuse injury.
- X-ray performed and negative.
- Neurovascular exam intact, including hand motor function.
- Affirmative clinician attestation of no acute traumatic mechanism.
- Affirmative clinician attestation of no elbow instability concern.

Hard blockers:

- Acute traumatic mechanism, dislocation, fracture, open wound, high-energy trauma, crush injury.
- UCL/LCL concern or elbow instability concern.
- Distal biceps or triceps tendon concern.
- Ulnar nerve pattern.
- Olecranon bursitis or posterior elbow swelling pathway.
- Neurovascular compromise or hand motor deficit.
- Septic joint/infection concern, compartment syndrome concern.
- Pediatric growth plate pathway.
- Elderly/osteoporotic high-risk elbow injury.
- Specialist-directed orthopedic plan.

Patient-facing draft shape:

- Home care centers on activity modification and gradual return.
- Explicitly avoids routine immobilization unless clinician-directed.
- Recovery language sets days-to-weeks improvement but months-long full recovery expectation.
- Follow-up prefers sports medicine or orthopedics in 1 to 2 weeks for rehab and return-to-activity planning.

Verification:

```bash
python3 knowledge/ontology/evals/check_phase371_390_elbow_overuse_draft.py
python3 knowledge/ontology/evals/run_runtime_cases.py
node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs
```

Decision:

Do not promote yet. Next step is Phase 391-400 stress/review packet and clinician decision.
