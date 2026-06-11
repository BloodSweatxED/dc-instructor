import { describe, it, expect } from 'vitest';
import { shouldShowRating } from './ratingCadence.js';

describe('shouldShowRating', () => {
  it('fires on 1st, 6th, 11th generations', () => {
    expect(shouldShowRating(1)).toBe(true);
    expect(shouldShowRating(6)).toBe(true);
    expect(shouldShowRating(11)).toBe(true);
  });

  it('does not fire between cadence points', () => {
    for (const n of [2, 3, 4, 5, 7, 10]) {
      expect(shouldShowRating(n)).toBe(false);
    }
  });

  it('does not fire for zero or negative counts', () => {
    expect(shouldShowRating(0)).toBe(false);
    expect(shouldShowRating(-4)).toBe(false);
  });
});
