import assert from 'node:assert/strict';
import { classifyMedicationProvenance, SYSTEM } from '../../../netlify/functions/generate.js';
import { addPrimaryCareCallScript, tryOntologyGeneration } from '../../../netlify/functions/ontology-runtime.js';

const prompt = SYSTEM({ readingLevel: '6th Grade', language: 'English' });

assert.match(prompt, /Use medication details as passthrough only/);
assert.match(prompt, /Do not infer, invent, or complete missing medication details/);
assert.match(prompt, /If the note says only "antibiotics"/);
assert.match(prompt, /RESOURCES:/);
assert.match(prompt, /include a concrete phone script tailored to the CONDITION\/chief complaint/);
assert.match(prompt, /I was seen in the emergency department for \[condition or chief complaint\]/);
assert.match(prompt, /Do not default every condition to a one-week timeframe/);

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
  readingLevel: '6th Grade',
  language: 'English',
});
assert.equal(ontology.mode, 'ontology');
assert.equal(ontology.output_format.ontology_text_key, 'en_6');
assert.ok(Array.isArray(ontology.source_cards_used));
assert.ok(ontology.source_cards_used.length >= 1);
assert.match(ontology.output, /Call your primary care doctor's office or clinic to make an appointment/);
assert.match(ontology.output, /I was seen in the emergency department for asthma exacerbation improved discharge/);
assert.match(ontology.output, /within 3-5 days/);
assert.equal((ontology.output.match(/\bSay,\s*"/g) || []).length, 1);

const existingScript = 'FOLLOW UP:\nCall primary care. Say, "I need a visit."\n\nRESOURCES:\n- Bring these instructions.';
assert.equal(addPrimaryCareCallScript(existingScript, 'ankle pain'), existingScript);

const specialistOnly = 'FOLLOW UP:\nCall the orthopedic clinic within 1 week.\n\nRESOURCES:\n- Bring these instructions.';
assert.equal(addPrimaryCareCallScript(specialistOnly, 'ankle pain'), specialistOnly);

const fourthGradeOntology = tryOntologyGeneration({
  condition: 'asthma exacerbation improved discharge',
  edNoteScrubbed: 'Improved after nebulizers and steroids. Breathing comfortably on room air. Has rescue inhaler access.',
  readingLevel: '4th Grade',
  language: 'English',
});
assert.equal(fourthGradeOntology.mode, 'ontology');
assert.equal(fourthGradeOntology.output_format.ontology_text_key, 'en_4');

const hl1Ontology = tryOntologyGeneration({
  condition: 'asthma exacerbation improved discharge',
  edNoteScrubbed: 'Improved after nebulizers and steroids. Breathing comfortably on room air. Has rescue inhaler access.',
  readingLevel: 'HL-1 (Health Literacy Level 1)',
  language: 'English',
});
assert.equal(hl1Ontology.mode, 'ontology');
assert.equal(hl1Ontology.output_format.ontology_text_key, 'en_hl1');

const unsupportedLanguage = tryOntologyGeneration({
  condition: 'asthma exacerbation improved discharge',
  edNoteScrubbed: 'Improved after nebulizers and steroids. Breathing comfortably on room air. Has rescue inhaler access.',
  readingLevel: '6th Grade',
  language: 'Spanish',
});
assert.equal(unsupportedLanguage.mode, 'generator');
assert.equal(unsupportedLanguage.phenotype_id, 'asthma_exacerbation_improved_discharge');
assert.equal(unsupportedLanguage.fallback_reason, 'unsupported_ontology_language');
assert.equal(unsupportedLanguage.output, undefined);

const unsupportedReadingLevel = tryOntologyGeneration({
  condition: 'asthma exacerbation improved discharge',
  edNoteScrubbed: 'Improved after nebulizers and steroids. Breathing comfortably on room air. Has rescue inhaler access.',
  readingLevel: '8th Grade',
  language: 'English',
});
assert.equal(unsupportedReadingLevel.mode, 'generator');
assert.equal(unsupportedReadingLevel.phenotype_id, 'asthma_exacerbation_improved_discharge');
assert.equal(unsupportedReadingLevel.fallback_reason, 'unsupported_ontology_reading_level');
assert.equal(unsupportedReadingLevel.output, undefined);

console.log('product tailoring contract checks passed');
