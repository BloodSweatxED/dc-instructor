const KEY = 'dci_gen_count';

export function recordGeneration() {
  const n = (parseInt(localStorage.getItem(KEY) || '0', 10) || 0) + 1;
  localStorage.setItem(KEY, String(n));
  return n;
}

export function shouldShowRating(generationNumber) {
  // Fire on 1st, 6th, 11th, 16th... — every 5th, starting with the first.
  return generationNumber >= 1 && (generationNumber - 1) % 5 === 0;
}
