import { checkLimits, jsonResponse } from './_lib.js';

export const config = { path: '/api/usage' };

export default async () => {
  const limits = await checkLimits();
  return jsonResponse(200, limits);
};
