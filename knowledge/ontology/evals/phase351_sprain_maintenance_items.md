# Phase 351 Sprain Segment Maintenance Items

Date: 2026-06-04

Status: resolved in Phase 352-360.

## Item 1: Knee/Shoulder Infection Return-Precaution Tail

The reviewed `sprain_strain_knee_or_shoulder_xray_negative` patient-facing output still includes:

```text
Fever, redness, warmth, pus, severe pain with movement, or symptoms that get worse instead of better.
```

Prior review flagged "symptoms that get worse instead of better" as weak language. This is not a blocker for promoting `wrist_sprain_xray_negative`, but it should not remain indefinitely.

Maintenance action:

- Replace the vague tail with a more concrete infection or worsening-pain return precaution during the next sprain maintenance pass.

Resolution:

- Completed in Phase 352-360. Current reviewed knee/shoulder output uses: "Fever, spreading redness or warmth, pus, or severe pain with movement."

## Item 2: Elbow/Foot Strings In Knee/Shoulder Matching Terms

`sprain_strain_knee_or_shoulder_xray_negative` still carries elbow and foot strings in matching terms for auditability, while `elbow_or_foot_site_pending_split` routes those cases out of ontology output.

This is acceptable only while blocker behavior remains reliable.

Maintenance action:

- Before opening the next phenotype batch, confirm elbow and foot cases reliably trigger `elbow_or_foot_site_pending_split`.
- If elbow or foot matching ever clears the site-pending blocker at low confidence, remove those strings from knee/shoulder matching terms or split elbow/foot into site-specific phenotypes before expansion.

Resolution:

- Completed in Phase 352-360 for the currently tracked elbow and foot sprain strings.
- Elbow and foot remain excluded until an intentional split.

Current confirmation:

- Phase 217 elbow and foot site-stress fixtures verify that clean elbow and foot strings route to `unsafe_modifier_present` with `elbow_or_foot_site_pending_split`.
- Phase 251-301 sprain boundary check re-verifies this behavior.
