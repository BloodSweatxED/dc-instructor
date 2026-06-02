import { useEffect, useState } from 'react';
import Header from './components/Header.jsx';
import InputPanel from './components/InputPanel.jsx';
import OutputPanel from './components/OutputPanel.jsx';
import RatingModal from './components/RatingModal.jsx';
import { generateInstructions, generateImage, verifyRedaction } from './lib/api.js';
import { redactPHI } from './lib/phiRedact.js';
import { recordGeneration, shouldShowRating } from './lib/ratingCadence.js';
import { getGenerationCount } from './lib/supabase.js';

export default function App() {
  const [condition, setCondition] = useState('');
  const [edNote, setEdNote] = useState('');
  const [level, setLevel] = useState('6th');
  const [language, setLanguage] = useState('English');
  const [imageOn, setImageOn] = useState(false);
  const [imagePrompt, setImagePrompt] = useState('');

  const [instructions, setInstructions] = useState('');
  const [image, setImage] = useState(null);
  const [imageBusy, setImageBusy] = useState(false);
  const [busy, setBusy] = useState(false);
  const [streaming, setStreaming] = useState(false);
  const [count, setCount] = useState(null);
  const [warning, setWarning] = useState(null);
  const [blocked, setBlocked] = useState(null);
  const [error, setError] = useState(null);
  const [generationMeta, setGenerationMeta] = useState(null);

  const [rating, setRating] = useState(null);
  const [redactionMeta, setRedactionMeta] = useState(null);

  useEffect(() => { getGenerationCount().then(setCount); }, []);

  const onGenerate = async () => {
    setError(null);
    setInstructions('');
    setImage(null);
    setGenerationMeta(null);
    setBusy(true);

    try {
      // Two-layer PHI redaction (only if ED note present)
      let edNoteScrubbed = '';
      if (edNote.trim()) {
        const layer1 = redactPHI(edNote);
        setRedactionMeta({ redactions: layer1.redactions, verifying: true, verified: false });
        try {
          const verify = await verifyRedaction(layer1.scrubbed);
          edNoteScrubbed = verify.scrubbed || layer1.scrubbed;
          const merged = [...layer1.redactions, ...(verify.additionalRedactions || [])];
          setRedactionMeta({ redactions: merged, verifying: false, verified: true });
        } catch {
          edNoteScrubbed = layer1.scrubbed;
          setRedactionMeta({ redactions: layer1.redactions, verifying: false, verified: false });
        }
      } else {
        setRedactionMeta(null);
      }

      const readingLevelLabel = level === 'HL-1' ? 'HL-1 (Health Literacy Level 1)' : `${level} Grade`;

      setStreaming(true);
      const meta = await generateInstructions(
        { condition, edNoteScrubbed, readingLevel: readingLevelLabel, language, hasImage: imageOn },
        (chunk) => setInstructions((prev) => prev + chunk),
      );
      setStreaming(false);

      if (meta.warning === 'approaching_limit') setWarning('approaching_limit');
      if (typeof meta.count === 'number') setCount(meta.count + 1);
      setGenerationMeta(meta);

      if (imageOn && imagePrompt.trim()) {
        setImageBusy(true);
        try {
          const img = await generateImage(imagePrompt);
          setImage(img.image);
        } catch (e) {
          // Non-fatal — instruction text already rendered
        } finally {
          setImageBusy(false);
        }
      }

      const n = recordGeneration();
      if (shouldShowRating(n) && meta.generation_id) {
        setTimeout(() => setRating({ generationId: meta.generation_id }), 8000);
      }
    } catch (e) {
      setStreaming(false);
      if (e.status === 429) {
        setBlocked(e.payload?.reason === 'expired' ? 'expired' : 'limit');
      } else {
        setError(e.message || 'Generation failed');
      }
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="bg-mesh min-h-screen">
      <div className="w-full max-w-[1800px] mx-auto px-4 sm:px-8 lg:px-12 xl:px-16 py-6 sm:py-10">
        <Header count={count} />

        {blocked && (
          <div className="mb-4 glass p-5 text-center">
            <div className="font-mono text-warn text-sm mb-2">
              Generation limit reached.
            </div>
            <div className="text-cool/70 text-sm">
              Email <span className="text-accent">drinstructor@dcinstructor.com</span> for continued access.
            </div>
          </div>
        )}

        {error && (
          <div className="mb-4 p-3 rounded-md border border-red-500/40 bg-red-500/10 text-red-300 text-xs font-mono">
            {error}
          </div>
        )}

        <main className="grid grid-cols-1 md:grid-cols-2 gap-5 md:gap-6 lg:gap-8 items-start">
          <InputPanel
            condition={condition} setCondition={setCondition}
            edNote={edNote} setEdNote={setEdNote}
            level={level} setLevel={setLevel}
            language={language} setLanguage={setLanguage}
            imageOn={imageOn} setImageOn={setImageOn}
            imagePrompt={imagePrompt} setImagePrompt={setImagePrompt}
            onGenerate={onGenerate}
            busy={busy}
            redactionMeta={redactionMeta}
          />
          <OutputPanel
            instructions={instructions}
            setInstructions={setInstructions}
            image={image}
            imageBusy={imageBusy}
            streaming={streaming}
            generationMeta={generationMeta}
          />
        </main>

        <footer className="mt-10 text-center text-[11px] font-mono text-cool/40 space-y-1">
          <div>Built by @BloodSweatxED — EM physician, clinician-developer</div>
          <div>Anonymous usage data may be used for quality improvement research.</div>
        </footer>
      </div>

      {rating && (
        <RatingModal
          generationId={rating.generationId}
          onClose={() => setRating(null)}
        />
      )}
    </div>
  );
}
