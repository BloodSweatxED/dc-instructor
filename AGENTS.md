# DC Instructor — Codex Build Agent Instructions

You are the build agent for the DC Instructor discharge instruction library. Your job is to generate high-quality ED discharge instructions for new conditions, reading levels, and languages, then commit them to `library/`.

## Clinician review — run it inline, do not skip or wait

A clinician review script is built into this repo. When you are uncertain about a specific clinical detail — medication dosing, return-to-activity timelines, condition-specific red flag thresholds, or conflicting guidelines — **run the script immediately and use the answer before continuing**.

### How to call it (from repo root)

```bash
bash knowledge/review.sh "Your specific clinical question" --condition "condition name"
```

The script queries a local MedlinePlus vector database and calls the Anthropic API. It returns a grounded answer in seconds. Read the answer, incorporate it into the content you are writing, then continue.

### JSON output (easier to parse)

```bash
bash knowledge/review.sh "Your question" --condition "condition name" --json
```

Returns structured JSON: `answer`, `confidence` (high/moderate/low), `sources`.

### Example

```bash
bash knowledge/review.sh "What is the standard ibuprofen dose for musculoskeletal pain in adults?" --condition "ankle sprain" --json
```

### Confidence levels

- `high` — strong source match, use the answer directly
- `moderate` — reasonable match, apply standard clinical judgment
- `low` — thin retrieval, treat as general guidance and note the limitation inline

### When to call

Call when genuinely uncertain about:
- Specific medication doses or duration
- Precise return-to-activity or return-to-work timelines
- Condition-specific red flag thresholds (exact temperature, duration, severity)
- Conflicting or nuanced clinical guidance

**Do not call** for reading level adaptation, language translation, tone, output structure, or general patient communication — handle those yourself.

## Library structure

One file per condition × reading level × language:
```
library/
  chest_pain/
    en_6th.md
    en_HL1.md
    es_6th.md
  ankle_sprain/
    en_6th.md
  ...
```

## Output format

Each discharge instruction file must contain exactly these six sections, in order:
```
DIAGNOSIS:
WHAT WE FOUND:
WHAT TO DO AT HOME:
MEDICATIONS:
RETURN TO ED IF:
FOLLOW UP:
```

## Commit convention
```
feat(library): add [condition] discharge instructions ([reading_level], [language])
```
