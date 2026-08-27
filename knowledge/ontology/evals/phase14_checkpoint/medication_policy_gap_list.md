# Phase 14 Medication-Policy Gap List

Medication dosing, duration, route, contraindication handling, renal adjustment, pregnancy adjustment, pediatric adjustment, and allergy substitution remain out of scope for V1 reviewed ontology output.

| Area | Current ontology behavior | Needed before dosing-ready output |
| --- | --- | --- |
| Antibiotics | Says to take antibiotics only when prescribed, or exactly as prescribed. | Medication policy with indication-specific regimen, dose, duration, allergy, pregnancy, renal, and local-resistance logic. |
| Asthma medications | Mentions rescue inhaler, steroids, and controller medicines only as prescribed. | Asthma medication policy with inhaler access, steroid plan, controller plan, and return thresholds. |
| Analgesics and antipyretics | Uses label-following language for acetaminophen or ibuprofen if safe. | Contraindication and dosing policy for renal disease, anticoagulation, pregnancy, liver disease, age, and weight. |
| Antiemetics and pain prescriptions | Refers to prescribed pain or nausea medicine without naming dose. | Condition-specific prescription policy and safety rules. |

Reviewed medication primitives currently covered by non-dosing policy language: 34.
