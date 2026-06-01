# Asthma Exacerbation Live Tool Golden Output

Phenotype: `asthma_exacerbation_improved_discharge`

Input condition:

```text
adult asthma exacerbation
```

Input ED note:

```text
Adult with asthma exacerbation. Improved after nebulizers and steroids. Breathing comfortably on room air. No chest pain. No fever. Has albuterol inhaler at home. Discharged with steroid course and PCP follow-up.
```

Live DC Instructor output captured 2026-06-01:

```text
DIAGNOSIS:
You had an asthma flare-up that made it hard to breathe.

WHAT WE FOUND:
You came to the ED because your asthma got worse and you were having trouble breathing. We listened to your lungs and gave you breathing treatments with medicine that opens your airways. We also gave you steroids to reduce swelling in your lungs. After treatment, you were breathing comfortably on your own and ready to go home.

WHAT TO DO AT HOME:
• Rest for the next 1-2 days and avoid hard exercise until your breathing feels normal
• Stay away from things that trigger your asthma like smoke, strong smells, cold air, and dust
• Use your rescue inhaler before exercise once you start being active again
• Sleep with your head raised on 2 pillows if that helps you breathe easier
• Drink plenty of water to help thin the mucus in your lungs
• Wash your hands often and avoid people who are sick

MEDICATIONS:
Prednisone 40 mg by mouth once daily for 5 days — take with food in the morning. Watch for trouble sleeping and increased appetite.

Albuterol inhaler 2 puffs every 4-6 hours as needed for wheezing or shortness of breath. Use more often if needed over the next few days, then cut back as you feel better.

RETURN TO ED IF:
• You need to use your inhaler more than every 2 hours
• Your breathing gets worse or you feel short of breath at rest
• You have chest pain or tightness that does not go away after using your inhaler
• Your lips or fingernails turn blue or gray
• You feel confused or very sleepy
• You cannot speak in full sentences because of shortness of breath

FOLLOW UP:
See your primary care doctor within 3-5 days. Call their office tomorrow to make an appointment. Your doctor needs to check your breathing and may adjust your daily asthma medicines to prevent another flare-up.
```

Calibration notes:

- Preserve the ED-course narrative.
- Preserve concrete home actions when source-supported and clinically reasonable.
- Do not copy medication dosing into static ontology primitives until medication policy supports clinician-provided dose extraction.
- Follow-up interval needs local-policy review before applying broadly.
