import { useState } from 'react';
import { summarizeRedactions } from '../lib/phiRedact.js';

export default function PHIRedactionBadge({ redactions, verifying, verified }) {
  const [hover, setHover] = useState(false);
  if (!redactions || redactions.length === 0) {
    if (verifying) return <span className="text-[11px] font-mono text-cool/40">running PHI check…</span>;
    return null;
  }
  const summary = summarizeRedactions(redactions);
  return (
    <div
      className="relative inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full border border-accent/40 bg-accent/10 text-[11px] font-mono text-accent cursor-help"
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
    >
      <span>🛡 {redactions.length} redacted{verified ? ' · verified' : ''}</span>
      {hover && (
        <div className="absolute z-10 top-full mt-2 left-0 w-56 p-2.5 rounded-md bg-bg/95 border border-accent/30 text-cool/80 text-[11px] leading-relaxed shadow-lg">
          <div className="text-cool/50 mb-1 uppercase tracking-wider">Removed before send</div>
          {summary.map(({ type, count }) => (
            <div key={type} className="flex justify-between"><span>{type}</span><span className="text-accent">{count}</span></div>
          ))}
        </div>
      )}
    </div>
  );
}
