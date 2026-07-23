import { useState } from 'react';

export default function OutputPanel({ instructions, setInstructions, image, imageBusy, streaming, generationMeta }) {
  const [tab, setTab] = useState('preview');
  const [copied, setCopied] = useState(false);
  const modeLabel = generationMeta?.ontology_mode === 'ontology'
    ? 'reviewed ontology'
    : generationMeta?.fallback_reason === 'phenotype_not_clinician_reviewed'
      ? 'draft ontology blocked'
      : 'generator fallback';
  const medicationLabel = generationMeta?.medication_provenance?.label;
  const sourceCount = generationMeta?.source_cards_used?.length || 0;
  const outputModifiers = generationMeta?.output_modifiers || [];

  const onCopy = async () => {
    try {
      await navigator.clipboard.writeText(instructions || '');
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    } catch {}
  };

  const onDownload = () => {
    if (!image) return;
    const a = document.createElement('a');
    a.href = image;
    a.download = 'dc-instructor-illustration.png';
    a.click();
  };

  return (
    <div className="glass p-5">
      <div className="flex items-center justify-between mb-3">
        <div className="flex gap-1">
          <button
            type="button"
            onClick={() => setTab('preview')}
            className={`pill ${tab === 'preview' ? 'pill-active' : ''}`}
          >Preview & Edit</button>
          <button
            type="button"
            onClick={() => setTab('image')}
            className={`pill ${tab === 'image' ? 'pill-active' : ''}`}
          >Illustration</button>
        </div>
        {tab === 'preview' && (
          <button
            type="button"
            onClick={onCopy}
            disabled={!instructions}
            className="text-xs font-mono text-cool/70 hover:text-accent disabled:opacity-40"
          >
            {copied ? 'copied ✓' : 'copy'}
          </button>
        )}
        {tab === 'image' && image && (
          <button
            type="button"
            onClick={onDownload}
            className="text-xs font-mono text-cool/70 hover:text-accent"
          >download</button>
        )}
      </div>

      {tab === 'preview' && (
        <>
          {instructions && (
            <div className="mb-2 space-y-1.5">
              <div className="px-2 py-1.5 rounded-md border border-warn/30 bg-warn/10 text-warn text-[11px] font-mono">
                Review before giving to patient. Verify medications, doses, and follow-up instructions.
              </div>
              {generationMeta?.ontology_mode && (
                <div className="px-2 py-1.5 rounded-md border border-cool/10 bg-bg/50 text-cool/60 text-[11px] font-mono">
                  Mode: {modeLabel}
                  {generationMeta.phenotype_id ? ` | phenotype: ${generationMeta.phenotype_id}` : ''}
                  {generationMeta.fallback_reason ? ` | reason: ${generationMeta.fallback_reason}` : ''}
                  {medicationLabel ? ` | meds: ${medicationLabel}` : ''}
                  {outputModifiers.length ? ` | modifiers: ${outputModifiers.map((item) => item.label || item.id).join(', ')}` : ''}
                  {sourceCount ? ` | sources: ${sourceCount}` : ''}
                </div>
              )}
              {outputModifiers.length > 0 && (
                <div className="px-2 py-1.5 rounded-md border border-warn/30 bg-warn/10 text-warn text-[11px] font-mono">
                  Modifier review: {outputModifiers.map((item) => item.note || item.label || item.id).join(' ')}
                </div>
              )}
            </div>
          )}
          <textarea
            value={instructions}
            onChange={(e) => setInstructions(e.target.value)}
            placeholder={streaming ? '…' : 'Generated instructions will appear here.'}
            rows={18}
            className="w-full min-h-[420px] lg:min-h-[600px] bg-bg/60 border border-cool/10 rounded-lg px-3 py-3 text-sm leading-relaxed font-sans focus:outline-none focus:border-accent/60 resize-y whitespace-pre-wrap"
          />
        </>
      )}

      {tab === 'image' && (
        <div className="aspect-square w-full bg-bg/60 border border-cool/10 rounded-lg flex items-center justify-center overflow-hidden">
          {imageBusy && <span className="font-mono text-xs text-cool/50">rendering…</span>}
          {!imageBusy && image && <img src={image} alt="Medical illustration" className="w-full h-full object-contain" />}
          {!imageBusy && !image && <span className="font-mono text-xs text-cool/40">No illustration yet.</span>}
        </div>
      )}
    </div>
  );
}
