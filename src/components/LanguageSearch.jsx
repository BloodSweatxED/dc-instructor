import { useState } from 'react';

export default function LanguageSearch({ value, onChange }) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');

  if (!open) {
    return (
      <button type="button" onClick={() => setOpen(true)} className="pill">+ Search</button>
    );
  }
  return (
    <div className="flex items-center gap-1">
      <input
        autoFocus
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="e.g. Wolof"
        className="bg-transparent border border-accent/40 rounded-full px-3 py-1.5 text-xs focus:outline-none focus:border-accent w-32"
      />
      <button
        type="button"
        onClick={() => { if (query.trim()) { onChange(query.trim()); setOpen(false); } }}
        className="pill pill-active"
      >
        set
      </button>
      <button type="button" onClick={() => setOpen(false)} className="text-cool/50 text-xs px-1">×</button>
    </div>
  );
}
