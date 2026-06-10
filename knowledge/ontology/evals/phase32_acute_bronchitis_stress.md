# Phase 32 Acute Bronchitis Stress Cases

Phase 32 expands the bronchitis runtime boundary before promotion.

Added coverage:

- Phase 20 contradictory-note case for bronchitis.
- Phase 20 vague-chief-complaint no-match case for bronchitis.
- Clean `chest cold` match.
- Hemoptysis blocker.
- Cardiac or pulmonary embolism chest-pain concern blocker.
- Immunocompromised blocker.
- Frail elderly blocker.
- Sepsis blocker.
- Unstable-vitals blocker.

Decision: bronchitis may proceed to clinician review only if these cases pass in both Python and Netlify runtime paths.
