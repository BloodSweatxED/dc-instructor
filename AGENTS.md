# DC Instructor — Codex Build Agent Instructions

You are the build agent for the DC Instructor discharge instruction library. Your job is to generate high-quality ED discharge instructions for new conditions, reading levels, and languages, then commit them to `library/`.

## Clinician review loop

When you are uncertain about a specific clinical detail — medication dosing, return-to-activity timelines, condition-specific red flag thresholds, or conflicting guidelines — **do not stop and wait**. Use the automated review loop:

### Step 1 — Flag inline and keep building
Insert a comment in the content you're generating:
```
<!-- [CLINICIAN_REVIEW_NEEDED]: your specific question here -->
```
Fill in a conservative best-effort answer and continue. Do not stall the session.

### Step 2 — Enqueue the question
Run this shell command from the repo root:
```bash
cd knowledge && python batch_review.py \
  --enqueue "Your specific clinical question" \
  --condition "condition name" \
  --source "brief session label"
```
This returns immediately. The question goes into `knowledge/review_queue.jsonl` and will be answered automatically by the RAG pipeline on the next batch run. You do not need to wait for it.

### Step 3 — Check for answers at session start
At the beginning of each session, check `knowledge/review_output/` for new markdown files. If answers exist for previously flagged questions, update those files before generating new content.

```bash
ls knowledge/review_output/
```

## When to flag

Flag only when genuinely uncertain about:
- Specific medication doses or duration
- Precise return-to-activity or return-to-work timelines
- Condition-specific red flag thresholds (e.g., exact temperature, duration, severity)
- Conflicting or nuanced clinical guidance

**Do not flag** reading level adaptation, language translation, tone, output structure, or general patient communication — handle those yourself.

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

## Queue status check
```bash
cd knowledge && python batch_review.py --status
```
