# Phase 30 Acute Bronchitis Source Plan

Status: complete.

Target phenotype: `acute_bronchitis_no_pneumonia`.

Clinical label:

Acute bronchitis or chest cold without pneumonia concern.

Source cards:

- `cdc.acute_bronchitis`
- `medlineplus.acute_bronchitis`
- `cdc.antibiotic_use_adult_outpatient`

Proposed inclusion boundary:

- Adult with cough or chest cold symptoms.
- Clinician diagnosis or discharge impression is acute bronchitis, chest cold, or viral bronchitis.
- No pneumonia diagnosis or focal pneumonia concern.
- Oxygenation and work of breathing acceptable for discharge.
- No unstable vital signs, sepsis concern, or admission need.

Hard blockers:

- Hypoxia.
- Respiratory distress.
- Pneumonia, infiltrate, consolidation, or focal lung findings concerning for pneumonia.
- COPD or asthma exacerbation pathway.
- Immunocompromised host.
- Frailty or high-risk elderly patient.
- Hemoptysis.
- Chest pain concerning for cardiac or PE workup.
- Sepsis or unstable vital signs.
- Antibiotics prescribed for suspected bacterial infection unless the phenotype is explicitly rebuilt around that clinician decision.

Harvest risks to avoid:

- Do not assert "your lungs are clear" unless the clinician note supports it.
- Do not give medication names, doses, schedules, or durations unless clinician-entered medication details are present.
- Do not promise exact symptom duration.
- Do not use "no pneumonia" unless the ED note documents clinician concern was addressed.
- Do not make return-to-work claims.

Next build step:

Create a narrow draft phenotype and runtime cases before patient-facing primitive promotion. The first runtime cases should include clean bronchitis, pneumonia blocker, hypoxia blocker, COPD/asthma overlap blocker, antibiotic-prescribed blocker, and vague cough no-match.
