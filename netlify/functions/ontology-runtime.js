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
  ['resources', 'RESOURCES:'],
];

const NEGATIVE_CONTEXT = ['no ', 'denies ', 'without '];
const NEGATION_PATTERN = /(?:\bno|\bdenies|\bwithout)\s+$/;

const EXCLUSION_RULES = {
  airway_symptoms: ['trouble breathing', 'throat swelling', 'tongue swelling', 'drooling', 'stridor'],
  abnormal_ecg: ['st elevation', 'new ischemia', 'abnormal ecg'],
  abnormal_troponin: ['positive troponin', 'elevated troponin'],
  anaphylaxis: ['anaphylaxis', 'anaphylactic', 'two system reaction'],
  anticoagulated: ['warfarin', 'eliquis', 'apixaban', 'xarelto', 'rivaroxaban', 'blood thinner'],
  antibiotic_prescribed: ['antibiotic prescribed', 'started antibiotics', 'given antibiotics'],
  athlete_return_to_play: ['return to play', 'same day sports', 'athlete', 'game today', 'practice today'],
  biphasic_reaction_concern: ['biphasic', 'recurrent reaction', 'symptoms returned'],
  bacterial_infection_suspected: ['bacterial infection', 'strep', 'pneumonia', 'sinusitis'],
  bite_wound: ['bite wound', 'dog bite', 'cat bite', 'human bite'],
  c_diff_risk: ['c diff', 'c. diff', 'recent antibiotics', 'clostridioides'],
  cancer_red_flag: ['cancer', 'malignancy', 'weight loss', 'night sweats'],
  cauda_equina_concern: ['urinary retention', 'bowel incontinence', 'saddle anesthesia', 'saddle numbness', 'groin numbness'],
  chest_pain: ['chest pain', 'pressure in chest'],
  complicated_uti: ['complicated uti', 'urinary obstruction', 'urologic procedure'],
  deep_space_location: ['perirectal', 'neck abscess', 'hand abscess', 'deep space', 'orbital', 'joint'],
  deep_space_swelling: ['floor of mouth', 'neck swelling', 'jaw swelling', 'facial swelling', 'submandibular', 'deep space'],
  diabetic_foot: ['diabetic foot'],
  dirty_wound: ['dirty wound', 'contaminated wound', 'soil', 'rusty', 'crush injury'],
  drooling: ['drooling', 'cannot handle secretions'],
  elderly_frail: ['frail', 'elderly', 'nursing home'],
  elderly: ['elderly', 'frail'],
  fever: ['fever', 'febrile', 'chills'],
  flank_pain: ['flank pain', 'cva tenderness', 'side pain'],
  fracture_or_trauma_concern: ['fall', 'trauma', 'crash', 'fracture', 'midline tenderness'],
  fracture_seen: ['fracture seen', 'broken bone', 'ankle fracture', 'distal fibula fracture', 'distal tibia fracture'],
  gi_bleeding: ['bloody stool', 'black stool', 'blood in stool', 'vomit blood', 'coffee grounds'],
  hypotension: ['hypotension', 'low blood pressure'],
  hypoxia: ['hypoxic', 'low oxygen', 'oxygen saturation 90', 'spo2 90', 'spo2 89'],
  immunocompromised: ['chemotherapy', 'transplant', 'immunocompromised', 'neutropenia'],
  indwelling_catheter: ['foley', 'catheter'],
  joint_violation: ['joint violation', 'joint capsule', 'traumatic arthrotomy', 'over joint'],
  intoxication: ['intoxicated', 'etoh'],
  kidney_transplant: ['kidney transplant', 'renal transplant'],
  loss_of_consciousness: ['loss of consciousness', 'loc'],
  male_patient: ['male patient', 'man with uti', 'male with uti'],
  mono_complication_concern: ['mono', 'splenomegaly', 'left upper quadrant pain'],
  mucosal_lesions: ['mucosal lesions', 'mouth sores', 'skin peeling', 'target lesions'],
  near_eye_or_genitals: ['eye', 'eyelid', 'genital', 'scrotum', 'vulva'],
  necrotizing_infection_concern: ['necrotizing', 'pain out of proportion', 'crepitus', 'bullae'],
  neurovascular_compromise: ['numb foot', 'numb toes', 'no pulse', 'cold foot', 'blue toes', 'pale toes', 'decreased sensation'],
  no_xray_performed: ['no xray', 'no x ray', 'no imaging', 'xray not done', 'x ray not done'],
  neurologic_deficit: ['weakness', 'numbness', 'aphasia', 'slurred speech', 'facial droop'],
  new_neurologic_deficit: ['new weakness', 'leg weakness', 'foot drop', 'new numbness', 'numb leg'],
  ongoing_pain: ['ongoing pain', 'persistent chest pain', 'active chest pain'],
  open_wound: ['open wound', 'open fracture', 'bone exposed', 'laceration over ankle'],
  open_fracture: ['open fracture', 'bone exposed'],
  packing_required: ['packing', 'packed wound', 'wick'],
  peritoneal_signs: ['rebound', 'guarding', 'peritonitis'],
  peritonsillar_abscess_concern: ['peritonsillar abscess', 'uvula deviation', 'hot potato voice', 'unilateral tonsil'],
  poor_follow_up: ['homeless', 'unable to follow up', 'poor follow up', 'no phone'],
  poor_inhaler_access: ['no inhaler', 'lost inhaler', 'cannot afford inhaler', 'no rescue inhaler', 'no access to inhaler'],
  persistent_vomiting: ['persistent vomiting', 'repeated vomiting', 'vomiting repeatedly'],
  pregnancy: ['is pregnant', 'patient is pregnant', 'pregnancy'],
  pneumonia: ['pneumonia', 'infiltrate', 'consolidation'],
  positive_strep_test: ['positive strep', 'strep positive', 'positive rapid strep'],
  rapid_progression: ['rapidly spreading', 'rapid progression'],
  sepsis: ['sepsis', 'septic', 'shock'],
  severe_dehydration: ['severe dehydration', 'syncope', 'very dry', 'shock'],
  epiglottitis_concern: ['epiglottitis', 'tripod', 'stridor'],
  solitary_kidney: ['solitary kidney', 'transplant kidney'],
  spinal_infection_concern: ['ivdu', 'injection drug', 'epidural abscess', 'spinal infection', 'fever with back pain'],
  surgical_abdomen: ['appendicitis', 'obstruction', 'peritonitis', 'surgical abdomen', 'localized abdominal pain'],
  trismus: ['trismus', 'cannot open mouth'],
  hand_tendon_risk: ['tendon injury', 'cannot extend', 'cannot flex', 'hand laceration', 'finger laceration'],
  retained_foreign_body: ['foreign body', 'glass retained', 'splinter retained', 'object stuck'],
  uncontrolled_pain: ['uncontrolled pain', 'intractable pain'],
  uncontrolled_vomiting: ['intractable vomiting', 'cannot keep down'],
  unable_to_bear_weight: ['unable to bear weight', 'cannot bear weight', 'cannot walk at all'],
  unable_to_tolerate_oral_fluids: ['cannot keep fluids down', 'unable to tolerate oral', 'failed po challenge'],
  unable_to_walk: ['unable to walk', 'cannot walk', 'nonambulatory'],
  unstable_vitals: ['unstable vitals', 'hypotension', 'tachycardia', 'toxic appearing'],
  urinary_obstruction: ['urinary obstruction', 'obstructing stone', 'retention'],
  unknown_trigger: ['unknown trigger', 'unclear trigger', 'trigger unclear'],
  voice_change: ['voice change', 'muffled voice', 'hoarse voice', 'hot potato voice'],
  vomiting_unable_to_take_meds: ['vomiting', 'cannot take pills', 'cannot keep meds down'],
  epinephrine_given: ['epinephrine given', 'epi given', 'epipen used', 'used epipen', 'received epinephrine'],
  renal_failure: ['renal failure', 'kidney failure', 'aki', 'acute kidney injury', 'creatinine elevated'],
  respiratory_distress: ['respiratory distress', 'tripoding', 'unable to speak full sentences', 'accessory muscle use'],
  skull_fracture_concern: ['skull fracture', 'basilar skull', 'periorbital ecchymosis', 'csf leak'],
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
  let start = 0;
  while (true) {
    const idx = text.indexOf(term, start);
    if (idx < 0) return false;
    const window = text.slice(Math.max(0, idx - 16), idx);
    if (!NEGATION_PATTERN.test(window)) return true;
    start = idx + term.length;
  }
}

function modifierHits(text, modifiers = []) {
  const hits = [];
  for (const modifier of modifiers) {
    const terms = EXCLUSION_RULES[modifier] || [modifier.replaceAll('_', ' ')];
    if (terms.some((term) => hasNonNegated(text, term))) hits.push(modifier);
  }
  return [...new Set(hits)].sort();
}

function confidenceFor(text, phenotype, exclusions = []) {
  const terms = phenotype.condition_terms || [];
  const matched = terms.map((term) => normalize(term)).filter((term) => text.includes(term));
  if (!matched.length) return { confidence: 0, matched };
  const score = matched.length / Math.max(terms.length, 1);
  const exactTerms = [normalize(phenotype.id), normalize(phenotype.label)];
  const exactMatch = exactTerms.some((term) => text.includes(term));
  const penalty = exclusions.length ? 0.15 : 0;
  const baseConfidence = exactMatch ? 0.93 : 0.55 + 0.35 * score;
  return { confidence: Math.min(0.98, baseConfidence - penalty), matched };
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

function phenotypePrimitiveSet(phenotypeId) {
  const phenotypePath = join(ontologyRoot, 'phenotypes', `${phenotypeId}.json`);
  const phenotype = readJSON(phenotypePath);
  const primitives = loadPrimitives();
  const selected = phenotype.primitive_ids.map((id) => primitives[id]).filter(Boolean);
  return { phenotype, selected };
}

function assemble(phenotypeId) {
  const { selected } = phenotypePrimitiveSet(phenotypeId);
  const lines = [];
  for (const [section, header] of SECTION_ORDER) {
    const items = selected.filter((item) => item.section === section);
    if (!items.length) {
      if (section === 'resources') continue;
      throw new Error(`Ontology phenotype missing ${section}`);
    }
    lines.push(header);
    for (const item of items) {
      const text = item.text?.en_6 || '';
      if (['home_care', 'medications', 'return_precautions', 'resources'].includes(section)) lines.push(`- ${text}`);
      else lines.push(text);
    }
    lines.push('');
  }
  return `${lines.join('\n').trim()}\n`;
}

export function sourceCardsForPhenotype(phenotypeId) {
  const { phenotype, selected } = phenotypePrimitiveSet(phenotypeId);
  return [...new Set([
    ...(phenotype.source_card_ids || []),
    ...selected.flatMap((primitive) => primitive.source_card_ids || []),
  ])].sort();
}

export function classifyOntology({ condition, edNoteScrubbed = '' }) {
  const manifest = loadManifest();
  const text = normalize(`${condition} ${edNoteScrubbed}`);
  const scored = [];
  for (const phenotype of manifest.phenotypes || []) {
    const exclusions = modifierHits(text, phenotype.unsafe_modifiers);
    const { confidence, matched } = confidenceFor(text, phenotype, exclusions);
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
  return {
    ...result,
    output: assemble(result.phenotype_id),
    source_cards_used: sourceCardsForPhenotype(result.phenotype_id),
  };
}
