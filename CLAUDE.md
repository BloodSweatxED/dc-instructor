# DC Instructor — Build Agent Instructions

You are the build agent for the DC Instructor discharge instruction library. Your job is to generate high-quality, grounded discharge instructions for new conditions, reading levels, and languages, then commit them to the library.

## Clinician review loop

When you're uncertain about a specific clinical detail — medication dosing, return-to-activity timelines, condition-specific red flag thresholds, or conflicting guidelines — **do not stop**. Use the automated review loop instead:

### Flag and continue (inline)
Place a comment in the generated content so it can be found later:
```
<!-- [CLINICIAN_REVIEW_NEEDED]: {your specific question here} -->
```
Continue generating with your best-effort answer using conservative standard guidance.

### Enqueue the question
From the repo root:
```bash
cd knowledge && python batch_review.py \
  --enqueue "Your specific clinical question" \
  --condition "condition name" \
  --source "brief session label"
```
The question enters the queue and will be answered by RAG + Anthropic API on the next batch run. You do not need to wait.

### Check for answers
Processed answers land in `knowledge/review_output/`. Check that directory at the start of each session — if answers are available for questions you previously flagged, update the flagged content.

### Queue status
```bash
cd knowledge && python batch_review.py --status
```

## When to flag
Flag when you're genuinely unsure about:
- Specific medication doses or duration
- Precise return-to-activity or return-to-work timelines
- Condition-specific red flag thresholds
- Conflicting or nuanced clinical guidance

**Do not flag** for: tone, reading level adaptation, language translation, output structure, or general patient communication — handle those yourself.

## Commit convention
```
feat(library): add [condition] discharge instructions ([reading_level])
```

## Library structure
Discharge instruction notes live in `library/`. One file per condition × reading-level × language combination:
```
library/
  chest_pain/
    en_6th.md
    en_HL1.md
    es_6th.md
  ...
```

## Knowledge base
The RAG retrieval database is at `knowledge/db/dc_medline_db/`. It covers MedlinePlus health topics. To expand coverage (add more conditions to the retrieval index):
```bash
cd knowledge && python ingest_medlineplus.py --ingest-v1
```
This pulls newly added topics from `ALLOWED_TOPICS` in `ingest_medlineplus.py`.
