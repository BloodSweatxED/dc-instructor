import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { classifyOntology } from '../../../netlify/functions/ontology-runtime.js';

const cases = JSON.parse(
  readFileSync(join('knowledge', 'ontology', 'evals', 'phase14_checkpoint_runtime_cases.json'), 'utf8'),
).filter((item) => item.id.startsWith('phase14_netlify_smoke_'));

for (const item of cases) {
  const result = classifyOntology({ condition: item.condition, edNoteScrubbed: item.ed_note });
  if (result.phenotype_id !== item.expected_phenotype_id || result.fallback_reason !== item.expected_fallback_reason) {
    throw new Error(`${item.id} mismatch: ${JSON.stringify(result)}`);
  }
  for (const exclusion of item.expected_exclusions || []) {
    if (!result.exclusions.includes(exclusion)) {
      throw new Error(`${item.id} missing exclusion ${exclusion}: ${JSON.stringify(result)}`);
    }
  }
  console.log(`netlify runtime smoke passed: ${item.id}`);
}

console.log('netlify runtime smoke passed');
