import { useState } from 'react';

export default function OutputPanel({ instructions, setInstructions, image, imageBusy, streaming }) {
  const [tab, setTab] = useState('preview');
  const [copied, setCopied] = useState(false);

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
        <textarea
          value={instructions}
          onChange={(e) => setInstructions(e.target.value)}
          placeholder={streaming ? '…' : 'Generated instructions will appear here.'}
          rows={18}
          className="w-full bg-bg/60 border border-cool/10 rounded-lg px-3 py-3 text-sm leading-relaxed font-sans focus:outline-none focus:border-accent/60 resize-y whitespace-pre-wrap"
        />
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
