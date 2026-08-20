#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

import { SYSTEM } from '../../../netlify/functions/generate.js';

const __filename = fileURLToPath(import.meta.url);
const ROOT = path.resolve(path.dirname(__filename), '../../..');
const DEFAULT_CASES = path.join(ROOT, 'knowledge/ontology/evals/generator_batch_01_cases.json');
const DEFAULT_JSON_OUT = path.join(ROOT, 'knowledge/ontology/evals/generator_batch_01_outputs.json');
const DEFAULT_MD_OUT = path.join(ROOT, 'knowledge/ontology/evals/generator_batch_01_outputs.md');
const DEFAULT_VAULT_NOTE = '/Users/andre/Desktop/Vaults/Life/11-DC instructor/2026-05-28 Generator Batch 01 - Ontology Primitive Harvest.md';

function parseArgs(argv) {
  const args = {
    cases: DEFAULT_CASES,
    jsonOut: DEFAULT_JSON_OUT,
    mdOut: DEFAULT_MD_OUT,
    vaultNote: '',
    title: 'Generator Batch 01 Outputs',
    model: 'claude-sonnet-4-5',
    maxTokens: 2000,
    dryRun: false,
  };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--cases') args.cases = argv[++i];
    else if (arg === '--json-out') args.jsonOut = argv[++i];
    else if (arg === '--md-out') args.mdOut = argv[++i];
    else if (arg === '--fill-vault-note') args.vaultNote = argv[++i] || DEFAULT_VAULT_NOTE;
    else if (arg === '--title') args.title = argv[++i];
    else if (arg === '--model') args.model = argv[++i];
    else if (arg === '--max-tokens') args.maxTokens = Number(argv[++i]);
    else if (arg === '--dry-run') args.dryRun = true;
    else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return args;
}

function loadEnvFile(envPath) {
  if (!fs.existsSync(envPath)) return;
  const text = fs.readFileSync(envPath, 'utf8');
  for (const rawLine of text.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const match = line.match(/^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/);
    if (!match) continue;
    const [, key, rawValue] = match;
    if (process.env[key]) continue;
    process.env[key] = rawValue.replace(/^['"]|['"]$/g, '');
  }
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

async function callAnthropic({ apiKey, model, maxTokens, condition, readingLevel, language }) {
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model,
      max_tokens: maxTokens,
      stream: false,
      system: SYSTEM({ readingLevel, language }),
      messages: [{ role: 'user', content: `CONDITION: ${condition}` }],
    }),
  });
  const body = await response.text();
  if (!response.ok) {
    throw new Error(`Anthropic ${response.status}: ${body.slice(0, 600)}`);
  }
  const data = JSON.parse(body);
  return (data.content || [])
    .filter((item) => item.type === 'text')
    .map((item) => item.text)
    .join('')
    .trim();
}

function buildMarkdown(result) {
  const lines = [
    `# ${result.title}`,
    '',
    `Generated: ${result.generated_at}`,
    `Model: ${result.model}`,
    '',
  ];
  for (const item of result.cases) {
    lines.push(`## ${item.id}`, '', '### Input Given', '', '```text', item.condition, '```', '', '### Generator Output', '', '```text');
    lines.push(item.output || item.error || '');
    lines.push('```', '');
  }
  return `${lines.join('\n').trim()}\n`;
}

function replaceFirstEmptyCodeBlock(sectionText, heading, value) {
  const pattern = new RegExp(`(### ${heading}\\n\\n\`\`\`text\\n)([\\s\\S]*?)(\\n\`\`\`)`);
  return sectionText.replace(pattern, `$1${value.trim()}\n$3`);
}

function fillVaultNote(notePath, cases) {
  let note = fs.readFileSync(notePath, 'utf8');
  for (const item of cases) {
    if (!item.output || item.error) continue;
    const sectionPattern = new RegExp(`(## Case \\d+: ${item.id}\\n)([\\s\\S]*?)(?=\\n---\\n\\n## Case |\\n*$)`);
    const match = note.match(sectionPattern);
    if (!match) continue;
    let section = match[0];
    section = replaceFirstEmptyCodeBlock(section, 'Input Given', item.condition);
    section = replaceFirstEmptyCodeBlock(section, 'Generator Output', item.output);
    note = note.replace(sectionPattern, section);
  }
  fs.writeFileSync(notePath, note, 'utf8');
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  loadEnvFile(path.join(ROOT, '.env'));
  loadEnvFile(path.join(ROOT, '.env.local'));

  const cases = readJson(args.cases);
  const result = {
    generated_at: new Date().toISOString(),
    model: args.model,
    title: args.title,
    dry_run: args.dryRun,
    cases: [],
  };

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey && !args.dryRun) {
    throw new Error('ANTHROPIC_API_KEY missing. Add it to the environment, .env, or run with --dry-run.');
  }

  for (const testCase of cases) {
    const item = {
      id: testCase.id,
      condition: testCase.condition,
      reading_level: testCase.reading_level || '6th Grade',
      language: testCase.language || 'English',
    };
    if (args.dryRun) {
      item.output = '';
      result.cases.push(item);
      continue;
    }
    try {
      item.output = await callAnthropic({
        apiKey,
        model: args.model,
        maxTokens: args.maxTokens,
        condition: item.condition,
        readingLevel: item.reading_level,
        language: item.language,
      });
      console.log(`generated ${item.id}`);
    } catch (error) {
      item.error = error.message;
      console.error(`failed ${item.id}: ${error.message}`);
    }
    result.cases.push(item);
  }

  fs.writeFileSync(args.jsonOut, `${JSON.stringify(result, null, 2)}\n`, 'utf8');
  fs.writeFileSync(args.mdOut, buildMarkdown(result), 'utf8');
  console.log(`wrote ${args.jsonOut}`);
  console.log(`wrote ${args.mdOut}`);

  if (args.vaultNote) {
    fillVaultNote(args.vaultNote, result.cases);
    console.log(`filled ${args.vaultNote}`);
  }

  if (result.cases.some((item) => item.error)) process.exitCode = 2;
}

main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
