# DC Instructor Ontology

This folder is the first primitive-centered knowledge layer for DC Instructor.

The goal is to assemble ED discharge instructions from reviewed, atomic instruction primitives instead of asking the model to synthesize from long patient-education articles.

## Current Scope

Phenotypes:

- `lumbar_strain_no_red_flags`
- `ankle_sprain_xray_negative`
- `viral_uri_no_pneumonia`
- `uncomplicated_cystitis_nonpregnant`
- `gastroenteritis_stable_hydrating`

Reading levels:

- `en_4`
- `en_6`
- `en_hl1`

## Run

Validate the ontology files:

```bash
python3 knowledge/ontology/scripts/validate_ontology.py
```

Assemble a lumbar strain discharge instruction:

```bash
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype lumbar_strain_no_red_flags --reading-level 6
```

Assemble an ankle sprain discharge instruction:

```bash
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype ankle_sprain_xray_negative --reading-level 6
```

Assemble the next high-frequency ED phenotypes:

```bash
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype viral_uri_no_pneumonia --reading-level 6
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype uncomplicated_cystitis_nonpregnant --reading-level 6
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype gastroenteritis_stable_hydrating --reading-level 6
```

Create clinician review files that compare the first five ontology phenotypes against the current generator case set:

```bash
python3 knowledge/ontology/scripts/compare_with_generator.py
```

To call a local Netlify generator during the comparison, pass the function URL:

```bash
python3 knowledge/ontology/scripts/compare_with_generator.py --generator-url http://localhost:8888/.netlify/functions/generate
```

Generate live Anthropic draft outputs for the 15-case primitive-harvest batch:

```bash
node knowledge/ontology/scripts/generate_batch_outputs.mjs
```

Fill the Obsidian batch note after generation:

```bash
node knowledge/ontology/scripts/generate_batch_outputs.mjs --fill-vault-note
```

Generate the second batch of 35 cases:

```bash
node knowledge/ontology/scripts/generate_batch_outputs.mjs \
  --title "Generator Batch 02 Outputs" \
  --cases knowledge/ontology/evals/generator_batch_02_cases.json \
  --json-out knowledge/ontology/evals/generator_batch_02_outputs.json \
  --md-out knowledge/ontology/evals/generator_batch_02_outputs.md
```

Build the seed knowledge graph from ontology files and generator batches:

```bash
python3 knowledge/ontology/graph/build_seed_graph.py
```

## Design

The ontology separates:

- phenotype logic
- source support
- atomic patient instructions
- reading-level variants
- review status

This lets the app move toward:

```text
condition + ED note
-> phenotype
-> reviewed primitives
-> six-section discharge instructions
```

The model can still help with phenotype classification, smoothing, translation, and unsupported conditions. It should not be the only source of return precautions, medication warnings, or follow-up logic for supported phenotypes.
