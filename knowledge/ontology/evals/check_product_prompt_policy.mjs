import { SYSTEM } from '../../../netlify/functions/generate.js';

const prompt = SYSTEM({ readingLevel: '6th Grade', language: 'English' });

const required = [
  'Use medication details as passthrough only',
  'Do not infer, invent, or complete missing medication details',
  'If the note says only "antibiotics" or "pain medicine," do not choose a drug, dose, route, frequency, or duration',
];

const forbidden = [
  'Include OTC recommendations (acetaminophen, ibuprofen) with concrete dosing',
  'take ibuprofen 400 mg every 6 hours with food',
];

const failures = [];
for (const phrase of required) {
  if (!prompt.includes(phrase)) failures.push(`missing product prompt policy: ${phrase}`);
}
for (const phrase of forbidden) {
  if (prompt.includes(phrase)) failures.push(`forbidden product prompt policy remains: ${phrase}`);
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}

console.log('product prompt medication policy checks passed');
