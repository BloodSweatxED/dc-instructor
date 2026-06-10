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
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase156_acute_otitis_media_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase157_acute_otitis_media_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase163_acute_otitis_media_second_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase169_broad_ear_complaint_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase175_suture_wound_check_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase176_suture_wound_check_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase193_broad_wound_complaint_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase202_215_reviewed_revision_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase217_sprain_site_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase302_350_wrist_sprain_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase371_390_elbow_overuse_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase391_420_elbow_overuse_review_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase421_450_elbow_overuse_hardening_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase481_510_foot_sprain_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase532_550_elbow_acute_traumatic_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase551_600_elbow_review_queue_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase602_650_wound_reviewed_stress_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase651_700_contact_dermatitis_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase701_750_contact_dermatitis_promotion_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase801_850_urticaria_split_runtime_cases.json'), 'utf8')))
  .concat(JSON.parse(readFileSync(join('knowledge', 'ontology', 'evals', 'phase851_constipation_promotion_runtime_cases.json'), 'utf8')))
  .filter(
    (item) =>
      item.id.startsWith('phase14_netlify_smoke_') ||
      item.id.startsWith('phase20_netlify_smoke_') ||
      item.id.startsWith('phase20_aom_') ||
      item.id.startsWith('phase20_skin_avulsion_') ||
      item.id.startsWith('phase20_suture_wound_check_') ||
      item.id.startsWith('phase20_bronchitis_') ||
      item.id.startsWith('phase20_sinusitis_') ||
      item.id.startsWith('phase20_sprain_strain_knee_or_shoulder_') ||
      item.id.startsWith('phase20_elbow_overuse_') ||
      item.id.startsWith('phase20_elbow_acute_traumatic_') ||
      item.id.startsWith('phase20_foot_sprain_') ||
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
      item.id.startsWith('phase151_') ||
      item.id.startsWith('phase156_') ||
      item.id.startsWith('phase157_') ||
      item.id.startsWith('phase163_') ||
      item.id.startsWith('phase169_') ||
      item.id.startsWith('phase175_') ||
      item.id.startsWith('phase176_') ||
      item.id.startsWith('phase193_') ||
      item.id.startsWith('phase202_') ||
      item.id.startsWith('phase203_') ||
      item.id.startsWith('phase204_') ||
      item.id.startsWith('phase205_') ||
      item.id.startsWith('phase217_') ||
      item.id.startsWith('phase221_') ||
      item.id.startsWith('phase302_') ||
      item.id.startsWith('phase303_') ||
      item.id.startsWith('phase304_') ||
      item.id.startsWith('phase305_') ||
      item.id.startsWith('phase306_') ||
      item.id.startsWith('phase307_') ||
      item.id.startsWith('phase308_') ||
      item.id.startsWith('phase309_') ||
      item.id.startsWith('phase310_') ||
      item.id.startsWith('phase311_') ||
      item.id.startsWith('phase312_') ||
      item.id.startsWith('phase313_') ||
      item.id.startsWith('phase314_') ||
      item.id.startsWith('phase315_') ||
      item.id.startsWith('phase316_') ||
      item.id.startsWith('phase317_') ||
      item.id.startsWith('phase318_') ||
      item.id.startsWith('phase319_') ||
      item.id.startsWith('phase320_') ||
      item.id.startsWith('phase321_') ||
      item.id.startsWith('phase322_') ||
      item.id.startsWith('phase323_') ||
      item.id.startsWith('phase324_') ||
      item.id.startsWith('phase371_') ||
      item.id.startsWith('phase372_') ||
      item.id.startsWith('phase373_') ||
      item.id.startsWith('phase374_') ||
      item.id.startsWith('phase375_') ||
      item.id.startsWith('phase376_') ||
      item.id.startsWith('phase377_') ||
      item.id.startsWith('phase378_') ||
      item.id.startsWith('phase379_') ||
      item.id.startsWith('phase380_') ||
      item.id.startsWith('phase381_') ||
      item.id.startsWith('phase382_') ||
      item.id.startsWith('phase383_') ||
      item.id.startsWith('phase384_') ||
      item.id.startsWith('phase391_') ||
      item.id.startsWith('phase392_') ||
      item.id.startsWith('phase393_') ||
      item.id.startsWith('phase394_') ||
      item.id.startsWith('phase395_') ||
      item.id.startsWith('phase396_') ||
      item.id.startsWith('phase397_') ||
      item.id.startsWith('phase398_') ||
      item.id.startsWith('phase399_') ||
      item.id.startsWith('phase400_') ||
      item.id.startsWith('phase401_') ||
      item.id.startsWith('phase402_') ||
      item.id.startsWith('phase403_') ||
      item.id.startsWith('phase404_') ||
      item.id.startsWith('phase405_') ||
      item.id.startsWith('phase406_') ||
      item.id.startsWith('phase421_') ||
      item.id.startsWith('phase422_') ||
      item.id.startsWith('phase423_') ||
      item.id.startsWith('phase424_') ||
      item.id.startsWith('phase425_') ||
      item.id.startsWith('phase426_') ||
      item.id.startsWith('phase427_') ||
      item.id.startsWith('phase428_') ||
      item.id.startsWith('phase429_') ||
      item.id.startsWith('phase430_') ||
      item.id.startsWith('phase481_') ||
      item.id.startsWith('phase482_') ||
      item.id.startsWith('phase483_') ||
      item.id.startsWith('phase484_') ||
      item.id.startsWith('phase485_') ||
      item.id.startsWith('phase486_') ||
      item.id.startsWith('phase487_') ||
      item.id.startsWith('phase488_') ||
      item.id.startsWith('phase489_') ||
      item.id.startsWith('phase490_') ||
      item.id.startsWith('phase491_') ||
      item.id.startsWith('phase492_') ||
      item.id.startsWith('phase532_') ||
      item.id.startsWith('phase533_') ||
      item.id.startsWith('phase534_') ||
      item.id.startsWith('phase535_') ||
      item.id.startsWith('phase536_') ||
      item.id.startsWith('phase537_') ||
      item.id.startsWith('phase538_') ||
      item.id.startsWith('phase539_') ||
      item.id.startsWith('phase540_') ||
      item.id.startsWith('phase541_') ||
      item.id.startsWith('phase542_') ||
      item.id.startsWith('phase543_') ||
      item.id.startsWith('phase544_') ||
      item.id.startsWith('phase545_') ||
      item.id.startsWith('phase546_') ||
      item.id.startsWith('phase551_') ||
      item.id.startsWith('phase552_') ||
      item.id.startsWith('phase553_') ||
      item.id.startsWith('phase554_') ||
      item.id.startsWith('phase555_') ||
      item.id.startsWith('phase556_') ||
      item.id.startsWith('phase557_') ||
      item.id.startsWith('phase558_') ||
      item.id.startsWith('phase559_') ||
      item.id.startsWith('phase560_') ||
      item.id.startsWith('phase602_') ||
      item.id.startsWith('phase603_') ||
      item.id.startsWith('phase604_') ||
      item.id.startsWith('phase605_') ||
      item.id.startsWith('phase606_') ||
      item.id.startsWith('phase607_') ||
      item.id.startsWith('phase608_') ||
      item.id.startsWith('phase609_') ||
      item.id.startsWith('phase610_') ||
      item.id.startsWith('phase611_') ||
      item.id.startsWith('phase651_') ||
      item.id.startsWith('phase652_') ||
      item.id.startsWith('phase653_') ||
      item.id.startsWith('phase654_') ||
      item.id.startsWith('phase655_') ||
      item.id.startsWith('phase656_') ||
      item.id.startsWith('phase657_') ||
      item.id.startsWith('phase658_') ||
      item.id.startsWith('phase659_') ||
      item.id.startsWith('phase660_') ||
      item.id.startsWith('phase661_') ||
      item.id.startsWith('phase662_') ||
      item.id.startsWith('phase701_') ||
      item.id.startsWith('phase702_') ||
      item.id.startsWith('phase703_') ||
      item.id.startsWith('phase704_') ||
      item.id.startsWith('phase705_') ||
      item.id.startsWith('phase706_') ||
      item.id.startsWith('phase707_') ||
      item.id.startsWith('phase708_') ||
      item.id.startsWith('phase709_') ||
      item.id.startsWith('phase710_') ||
      item.id.startsWith('phase711_') ||
      item.id.startsWith('phase712_') ||
      item.id.startsWith('phase801_') ||
      item.id.startsWith('phase802_') ||
      item.id.startsWith('phase803_') ||
      item.id.startsWith('phase804_') ||
      item.id.startsWith('phase805_') ||
      item.id.startsWith('phase806_') ||
      item.id.startsWith('phase807_') ||
      item.id.startsWith('phase808_') ||
      item.id.startsWith('phase809_') ||
      item.id.startsWith('phase851_') ||
      item.id.startsWith('phase852_') ||
      item.id.startsWith('phase853_') ||
      item.id.startsWith('phase854_') ||
      item.id.startsWith('phase855_') ||
      item.id.startsWith('phase856_') ||
      item.id.startsWith('phase857_') ||
      item.id.startsWith('phase858_') ||
      item.id.startsWith('phase859_') ||
      item.id.startsWith('phase860_') ||
      item.id.startsWith('phase861_') ||
      item.id.startsWith('phase862_') ||
      item.id.startsWith('phase863_') ||
      item.id.startsWith('phase864_') ||
      item.id.startsWith('phase865_') ||
      item.id.startsWith('phase866_')
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
  const outputModifierIds = (result.output_modifiers || []).map((modifier) => modifier.id);
  for (const outputModifier of item.expected_output_modifiers || []) {
    if (!outputModifierIds.includes(outputModifier)) {
      throw new Error(`${item.id} missing output modifier ${outputModifier}: ${JSON.stringify(result)}`);
    }
  }
  console.log(`netlify runtime smoke passed: ${item.id}`);
}

console.log('netlify runtime smoke passed');
