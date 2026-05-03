async function postJSON(path, body, { stream = false } = {}) {
  const res = await fetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    const e = new Error(err.error || `HTTP ${res.status}`);
    e.status = res.status;
    e.payload = err;
    throw e;
  }
  if (stream) return res;
  return res.json();
}

export async function generateInstructions(payload, onChunk) {
  const res = await postJSON('/.netlify/functions/generate', payload, { stream: true });
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  let metadata = null;
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split('\n');
    buffer = lines.pop() || '';
    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const evt = JSON.parse(line);
        if (evt.type === 'meta') metadata = evt;
        else if (evt.type === 'chunk' && onChunk) onChunk(evt.text);
        else if (evt.type === 'done') metadata = { ...metadata, ...evt };
      } catch {}
    }
  }
  return metadata || {};
}

export async function verifyRedaction(scrubbedText) {
  return postJSON('/.netlify/functions/redact-verify', { text: scrubbedText });
}

export async function generateImage(prompt) {
  return postJSON('/.netlify/functions/generate-image', { prompt });
}
