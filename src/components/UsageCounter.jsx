export default function UsageCounter({ count }) {
  const display = typeof count === 'number' ? count.toLocaleString() : '—';
  return (
    <div className="flex items-center gap-2 font-mono text-xs text-cool/70">
      <span className="relative flex h-2 w-2">
        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-accent opacity-60" />
        <span className="relative inline-flex rounded-full h-2 w-2 bg-accent" />
      </span>
      <span>▲ {display} generations</span>
    </div>
  );
}
