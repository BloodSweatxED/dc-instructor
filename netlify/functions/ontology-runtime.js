import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const SECTION_ORDER = [
  ['diagnosis', 'DIAGNOSIS:'],
  ['what_we_found', 'WHAT WE FOUND:'],
  ['home_care', 'WHAT TO DO AT HOME:'],
  ['medications', 'MEDICATIONS:'],
  ['return_precautions', 'RETURN TO ED IF:'],
  ['follow_up', 'FOLLOW UP:'],
];

const NEGATIVE_CONTEXT = ['no ', 'denies ', 'without '];

const EXCLUSION_RULES = {
  airway_symptoms: ['trouble breathing', 'throat swelling', 'tongue swelling', 'drooling', 'stridor'],
  abnormal_ecg: ['st elevation', 'new ischemia', 'abnormal ecg'],
  abnormal_troponin: ['positive troponin', 'elevated troponin'],
  anticoagulated: ['warfarin', 'eliquis', 'apixaban', 'xarelto', 'rivaroxaban', 'blood thinner'],
  chest_pain: ['chest pain', 'pressure in chest'],
  deep_space_location: ['perirectal', 'neck abscess', 'hand abscess', 'deep space'],
  diabetic_foot: ['diabetic foot'],
  elderly: ['elderly', 'frail'],
  fever: ['fever', 'febrile', 'chills'],
  hypotension: ['hypotension', 'low blood pressure'],
  hypoxia: ['hypoxic', 'low oxygen', 'oxygen saturation 90', 'spo2 90', 'spo2 89'],
  immunocompromised: ['chemotherapy', 'transplant', 'immunocompromised', 'neutropenia'],
  intoxication: ['intoxicated', 'etoh'],
  loss_of_consciousness: ['loss of consciousness', 'loc'],
  near_eye_or_genitals: ['eye', 'eyelid', 'genital', 'scrotum', 'vulva'],
  neurologic_deficit: ['weakness', 'numbness', 'aphasia', 'slurred speech', 'facial droop'],
  ongoing_pain: ['ongoing pain', 'persistent chest pain', 'active chest pain'],
  peritoneal_signs: ['rebound', 'guarding', 'peritonitis'],
  poor_follow_up: ['homeless', 'unable to follow up', 'no phone'],
  pregnancy: ['pregnant', 'pregnancy'],
  rapid_progression: ['rapidly spreading', 'rapid progression'],
  sepsis: ['sepsis', 'septic', 'shock'],
  solitary_kidney: ['solitary kidney', 'transplant kidney'],
  trismus: ['trismus', 'cannot open mouth'],
  uncontrolled_pain: ['uncontrolled pain', 'intractable pain'],
  uncontrolled_vomiting: ['intractable vomiting', 'cannot keep down'],
};

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, '..', '..');
const ontologyRoot = join(repoRoot, 'knowledge', 'ontology');
const manifestPath = join(ontologyRoot, 'runtime', 'ontology_manifest.json');

function readJSON(path) {
  return JSON.parse(readFileSync(path, 'utf8'));
}

function normalize(text) {
  return String(text || '').toLowerCase().replace(/[_-]+/g, ' ').replace(/\s+/g, ' ').trim();
}

function hasNonNegated(text, term) {
  const idx = text.indexOf(term);
  if (idx < 0) return false;
  const window = text.slice(Math.max(0, idx - 16), idx);
  return !NEGATIVE_CONTEXT.some((marker) => window.includes(marker));
}

function modifierHits(text, modifiers = []) {
  const hits = [];
  for (const modifier of modifiers) {
    const terms = EXCLUSION_RULES[modifier] || [modifier.replaceAll('_', ' ')];
    if (terms.some((term) => hasNonNegated(text, term))) hits.push(modifier);
  }
  return [...new Set(hits)].sort();
}

function confidenceFor(text, terms = [], exclusions = []) {
  const matched = terms.map((term) => normalize(term)).filter((term) => text.includes(term));
  if (!matched.length) return { confidence: 0, matched };
  const score = matched.length / Math.max(terms.length, 1);
  const penalty = exclusions.length ? 0.15 : 0;
  return { confidence: Math.min(0.98, 0.55 + 0.35 * score - penalty), matched };
}

function loadManifest() {
  if (!existsSync(manifestPath)) return { phenotypes: [] };
  return readJSON(manifestPath);
}

function loadPrimitives() {
  const primitiveDir = join(ontologyRoot, 'primitives');
  const primitives = {};
  for (const file of readdirSync(primitiveDir)) {
    if (!file.endsWith('.json')) continue;
    const rows = readJSON(join(primitiveDir, file));
    if (!Array.isArray(rows)) continue;
    for (const row of rows) primitives[row.id] = row;
  }
  return primitives;
}

function assemble(phenotypeId) {
  const phenotypePath = join(ontologyRoot, 'phenotypes', `${phenotypeId}.json`);
  const phenotype = readJSON(phenotypePath);
  const primitives = loadPrimitives();
  const selected = phenotype.primitive_ids.map((id) => primitives[id]).filter(Boolean);
  const lines = [];
  for (const [section, header] of SECTION_ORDER) {
    const items = selected.filter((item) => item.section === section);
    if (!items.length) throw new Error(`Ontology phenotype missing ${section}`);
    lines.push(header);
    for (const item of items) {
      const text = item.text?.en_6 || '';
      if (['home_care', 'medications', 'return_precautions'].includes(section)) lines.push(`- ${text}`);
      else lines.push(text);
    }
    lines.push('');
  }
  return `${lines.join('\n').trim()}\n`;
}

export function classifyOntology({ condition, edNoteScrubbed = '' }) {
  const manifest = loadManifest();
  const text = normalize(`${condition} ${edNoteScrubbed}`);
  const scored = [];
  for (const phenotype of manifest.phenotypes || []) {
    const exclusions = modifierHits(text, phenotype.unsafe_modifiers);
    const { confidence, matched } = confidenceFor(text, phenotype.condition_terms, exclusions);
    if (!matched.length) continue;
    scored.push({ phenotype, confidence, matched, exclusions });
  }
  scored.sort((a, b) => b.confidence - a.confidence);
  const best = scored[0];
  if (!best) {
    return {
      mode: 'generator',
      phenotype_id: null,
      confidence: 0,
      exclusions: [],
      modifiers: [],
      fallback_reason: 'no_supported_phenotype_match',
    };
  }

  let fallbackReason = null;
  if (best.exclusions.length) fallbackReason = 'unsafe_modifier_present';
  else if (best.phenotype.status !== 'reviewed' || best.phenotype.review_status !== 'reviewed') fallbackReason = 'phenotype_not_clinician_reviewed';
  else if (best.phenotype.source_audit?.source_needed) fallbackReason = 'source_audit_not_passed';
  else if (best.confidence < 0.86) fallbackReason = 'low_confidence';

  return {
    mode: fallbackReason ? 'generator' : 'ontology',
    phenotype_id: best.phenotype.id,
    confidence: Number(best.confidence.toFixed(3)),
    exclusions: best.exclusions,
    modifiers: best.matched,
    fallback_reason: fallbackReason,
  };
}

export function tryOntologyGeneration(payload) {
  const result = classifyOntology(payload);
  if (result.mode !== 'ontology') return result;
  return { ...result, output: assemble(result.phenotype_id) };
}
