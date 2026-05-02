import UsageCounter from './UsageCounter.jsx';

export default function Header({ count }) {
  return (
    <header className="flex items-start justify-between gap-4 mb-6">
      <div>
        <div className="font-mono text-xl font-semibold tracking-tight">
          DC <span className="text-accent">Instructor</span>
        </div>
        <p className="text-xs text-cool/55 mt-1 max-w-xs leading-relaxed">
          Plain language discharge instructions. Any reading level. Any language.
        </p>
      </div>
      <UsageCounter count={count} />
    </header>
  );
}
