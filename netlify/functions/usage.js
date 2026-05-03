import { checkLimits, jsonResponse } from './_lib.js';

export default async () => {
  const limits = await checkLimits();
  return jsonResponse(200, limits);
};
