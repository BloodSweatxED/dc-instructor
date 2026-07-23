# Phase 391-420 Elbow Overuse Review Packet

Date: 2026-06-04

Phenotype: `elbow_sprain_overuse_xray_negative`

Decision: revise then promote.

## Scope

This draft is limited to adult elbow overuse injury, including lateral epicondylitis, medial epicondylitis, tennis elbow, golfer elbow, and subacute or chronic elbow overuse strain.

Required chart context:

- X-ray performed and negative.
- Neurovascular exam intact, including hand motor.
- No acute traumatic mechanism.
- No elbow instability concern.

Hard blockers:

- Acute traumatic elbow mechanism, direct blow, sudden injury, dislocation, fracture, open wound, high-energy trauma, or crush injury.
- UCL/LCL or instability concern.
- Distal biceps or triceps tendon concern.
- Ulnar nerve pattern or hand motor deficit.
- Olecranon bursitis or posterior elbow swelling pathway.
- Septic joint or infection concern.
- Compartment syndrome concern.
- Pediatric growth plate pathway.
- Osteoporotic or fragility-risk pathway.
- Specialist-directed orthopedic plan.
- No x-ray performed.

## Runtime Review

Phase 391-420 added 16 stress cases:

- Clean tennis elbow and golfer elbow route to reviewed ontology output after clinician approval.
- Missing adult elbow overuse diagnosis blocks by required context.
- No imaging, direct blow, posterior elbow fluid, hand weakness, infection concern, pediatric pathway, osteoporotic risk, specialist plan, distal biceps concern, and ulnar nerve pattern all block through unsafe modifiers.
- Shoulder overuse does not match.
- Foot sprain and acute elbow sprain still route out through the reviewed knee/shoulder sprain phenotype with `elbow_or_foot_site_pending_split`.

## Full Assembled Patient-Facing Note

```text
DIAGNOSIS:
Your clinician diagnosed an elbow overuse injury, such as tendon irritation or strain. Your x-ray did not show a fracture.

WHAT WE FOUND:
Your x-ray did not show a fracture. Your blood flow, feeling, and hand movement were intact. This was not caused by a sudden injury, and your elbow showed no signs of instability.

WHAT TO DO AT HOME:
- Reduce or pause the activity that triggers elbow pain, especially gripping, lifting, twisting, pulling, pushing, or repetitive wrist and forearm motion.
- Keep the elbow moving gently during normal daily activity. Do not immobilize it unless your clinician gave you a brace or splint plan.
- Use ice or heat if it helps. Stop any exercise or activity that causes sharp pain, new weakness, or symptoms into the hand.
- Return to work, lifting, sports, or gym activity gradually. Start with lighter loads and shorter sessions, then increase only if pain stays controlled.
- Some symptoms may improve over days to weeks, but elbow tendon overuse can take weeks to months to fully settle down and often improves best with a rehab plan.

MEDICATIONS:
- Use only the medicines your clinician prescribed or said are safe for you.
- Do not take extra doses or combine medicines unless your clinician told you to.

RETURN TO ED IF:
- New numbness, tingling, weakness, color change, coldness, or trouble moving the hand or fingers.
- A pop, sudden worsening after an injury, new bruising, new swelling, or weakness bending or straightening the elbow.
- The elbow feels unstable, locks, cannot fully move, or pain becomes severe despite rest.
- Fever, spreading redness or warmth, pus, or a swollen painful bump over the back of the elbow.

FOLLOW UP:
Follow up with primary care, occupational medicine, sports medicine, or orthopedics in 1 to 2 weeks, especially if pain is limiting work, sports, or daily activity. Follow-up can help build a rehab and return-to-activity plan. Go sooner if pain is worsening, hand symptoms develop, or your clinician gave a specific plan.
```

## Clinician Review Questions

- Is the phenotype boundary right for ED discharge, or should lateral and medial epicondylitis split from nonspecific elbow overuse strain?
- Should the runtime require explicit no-instability attestation for all cases, or is a documented stable elbow exam sufficient?
- Is 1 to 2 week primary care, occupational medicine, sports medicine, or orthopedics follow-up appropriate as the default?
- Is the no-routine-immobilization language correct, or should it mention counterforce strap or wrist brace only if clinician-directed?
- Are months-long recovery expectations useful patient counseling, or too strong for milder ED presentations?

## Decision Rationale

Promote after clinician approval on 2026-06-04. The runtime shape is clean, and the clinician-requested patient-facing revisions have been applied.
