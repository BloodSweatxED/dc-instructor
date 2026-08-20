# Phase 20 Medication Provenance UI Decision

Decision: keep medication provenance section-level for now.

Rationale: the current product metadata is a review aid, not medication reconciliation. Section-level provenance keeps the clinician's scan path visible without implying the system validated dose, schedule, route, indication, renal adjustment, pregnancy status, allergy status, or drug interactions.

Line-level markers should wait until the product has structured medication spans from the clinician-entered note, a line-to-source mapping contract, and a UI pattern that can mark uncertainty without making unvalidated medication text look safer than it is.

Phase 20 keeps medication-sensitive runtime cases focused on fallback behavior. They verify that medication context can block ontology mode when it changes discharge risk, while leaving prescribing logic out of scope.
