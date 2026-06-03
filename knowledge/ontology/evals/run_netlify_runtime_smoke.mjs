import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { classifyOntology } from '../../../netlify/functions/ontology-runtime.js';

const cases = JSON.parse(
  readFileSync(join('knowledge', 'ontology', 'evals', 'phase14_checkpoint_runtime_cases.json'), 'utf8'),
)
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase20_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase23_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase31_acute_bronchitis_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase32_acute_bronchitis_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase38_acute_sinusitis_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase39_acute_sinusitis_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase43_acute_sinusitis_post_promotion_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase47_conjunctivitis_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase48_conjunctivitis_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase52_conjunctivitis_boundary_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase58_otitis_externa_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase59_otitis_externa_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase62_otitis_externa_boundary_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase68_epistaxis_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase69_epistaxis_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase74_migraine_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase75_migraine_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase77_migraine_boundary_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase151_broad_chief_complaint_stress_runtime_cases.json'), 'utf8')))
  .filter(
    (item) =>
      item.id.startsWith('phase14_netlify_smoke_') ||
      item.id.startsWith('phase20_netlify_smoke_') ||
      item.id.startsWith('phase20_bronchitis_') ||
      item.id.startsWith('phase20_sinusitis_') ||
      item.id.startsWith('phase26_') ||
      item.id.startsWith('phase31_') ||
      item.id.startsWith('phase32_') ||
      item.id.startsWith('phase38_') ||
      item.id.startsWith('phase39_') ||
      item.id.startsWith('phase43_') ||
      item.id.startsWith('phase47_') ||
      item.id.startsWith('phase48_') ||
      item.id.startsWith('phase52_') ||
      item.id.startsWith('phase58_') ||
      item.id.startsWith('phase59_') ||
      item.id.startsWith('phase62_') ||
      item.id.startsWith('phase68_') ||
      item.id.startsWith('phase69_') ||
      item.id.startsWith('phase74_') ||
      item.id.startsWith('phase75_') ||
      item.id.startsWith('phase77_') ||
      item.id.startsWith('phase151_'),
  );

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
  for (const missingContext of item.expected_missing_required_context || []) {
    if (!result.missing_required_context.includes(missingContext)) {
      throw new Error(`${item.id} missing required context ${missingContext}: ${JSON.stringify(result)}`);
    }
  }
  console.log(`netlify runtime smoke passed: ${item.id}`);
}

console.log('netlify runtime smoke passed');
