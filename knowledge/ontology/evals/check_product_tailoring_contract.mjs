import assert from 'node:assert/strict';
import { classifyMedicationProvenance, SYSTEM } from '../../../netlify/functions/generate.js';
import { tryOntologyGeneration } from '../../../netlify/functions/ontology-runtime.js';

const prompt = SYSTEM({ readingLevel: '6th Grade', language: 'English' });

assert.match(prompt, /Use medication details as passthrough only/);
assert.match(prompt, /Do not infer, invent, or complete missing medication details/);
assert.match(prompt, /If the note says only "antibiotics"/);
assert.match(prompt, /RESOURCES:/);

const explicitMed = classifyMedicationProvenance({
  edNoteScrubbed: 'Discharged with amoxicillin-clavulanate 875 mg by mouth twice daily for 7 days.',
  ontologyMode: 'generator',
});
assert.equal(explicitMed.mode, 'clinician_stated_present');
assert.equal(explicitMed.clinician_stated_medications_present, true);
assert.equal(explicitMed.passthrough_only, true);
assert.equal(explicitMed.inference_allowed, false);

const vagueMed = classifyMedicationProvenance({
  edNoteScrubbed: 'Patient discharged with antibiotics and PCP follow-up.',
  ontologyMode: 'generator',
});
assert.equal(vagueMed.mode, 'general_medication_mention_only');
assert.equal(vagueMed.clinician_stated_medications_present, false);
assert.equal(vagueMed.inference_allowed, false);

const noMed = classifyMedicationProvenance({
  edNoteScrubbed: 'Symptoms improved. Discharged home.',
  ontologyMode: 'generator',
});
assert.equal(noMed.mode, 'no_clinician_med_details');

const ontologyMed = classifyMedicationProvenance({
  edNoteScrubbed: 'Asthma improved after treatments.',
  ontologyMode: 'ontology',
});
assert.equal(ontologyMed.mode, 'ontology_general');
assert.equal(ontologyMed.review_required, true);

const ontology = tryOntologyGeneration({
  condition: 'asthma exacerbation improved discharge',
  edNoteScrubbed: 'Improved after nebulizers and steroids. Breathing comfortably on room air. Has rescue inhaler access.',
});
assert.equal(ontology.mode, 'ontology');
assert.ok(Array.isArray(ontology.source_cards_used));
assert.ok(ontology.source_cards_used.length >= 1);

console.log('product tailoring contract checks passed');
