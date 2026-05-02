import { useState } from 'react';
import { submitRating } from '../lib/supabase.js';

export default function RatingModal({ generationId, onClose }) {
  const [stars, setStars] = useState(0);
  const [comment, setComment] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const submit = async () => {
    if (!stars) return;
    await submitRating({ generation_id: generationId, stars, comment });
    setSubmitted(true);
    setTimeout(onClose, 800);
  };

  return (
    <div className="fixed inset-x-0 bottom-0 z-40 px-4 pb-4 sm:left-auto sm:right-4 sm:max-w-sm">
      <div className="glass p-4 shadow-2xl">
        <div className="flex items-center justify-between">
          <div className="font-mono text-xs text-cool/60">How were these instructions?</div>
          <button onClick={onClose} className="text-cool/50 hover:text-cool text-sm">×</button>
        </div>
        <div className="mt-2 flex gap-1.5">
          {[1, 2, 3, 4, 5].map((n) => (
            <button
              key={n}
              type="button"
              onClick={() => setStars(n)}
              className={`text-xl transition ${n <= stars ? 'text-accent' : 'text-cool/30 hover:text-cool/60'}`}
              aria-label={`${n} stars`}
            >★</button>
          ))}
        </div>
        <input
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Anything to add? (optional)"
          className="mt-2 w-full bg-bg/60 border border-cool/15 focus:border-accent rounded-md px-2.5 py-1.5 text-xs focus:outline-none"
        />
        <div className="mt-3 flex items-center justify-between">
          <button onClick={onClose} className="text-xs text-cool/50 hover:text-cool">Skip</button>
          <button
            onClick={submit}
            disabled={!stars || submitted}
            className="text-xs font-mono px-3 py-1.5 rounded-md bg-accent text-bg disabled:opacity-40"
          >{submitted ? 'thanks ✓' : 'Submit'}</button>
        </div>
      </div>
    </div>
  );
}
