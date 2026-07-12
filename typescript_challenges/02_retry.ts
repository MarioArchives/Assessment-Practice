/**
 * Challenge 02 — Async Retry with Exponential Backoff
 * -----------------------------------------------------
 * Implement an async retry utility.
 *
 * async function retry<T>(fn: () => Promise<T>, options?: RetryOptions): Promise<T>
 *
 * interface RetryOptions {
 *   maxAttempts?: number;                          // default 3
 *   baseDelayMs?: number;                          // default 100
 *   shouldRetry?: (err: unknown) => boolean;       // default: always retry
 * }
 *
 * Backoff formula: baseDelayMs * 2^attempt  (attempt is 0-indexed, so the first
 * call has no preceding delay, the first retry waits baseDelayMs, the second
 * retry waits 2*baseDelayMs, etc.)
 *
 * Rules:
 *   - After all attempts are exhausted, reject with the last error.
 *   - If shouldRetry(err) returns false, reject immediately with that error.
 *   - The original call counts as attempt 0; retries start at attempt 1.
 *
 * Usage:
 *   const result = await retry(() => fetchData(url), { maxAttempts: 5 });
 */
export interface RetryOptions {
  maxAttempts?: number;
  baseDelayMs?: number;
  shouldRetry?: (err: unknown) => boolean;
}

export async function retry<T>(
  fn: () => Promise<T>,
  options?: RetryOptions
): Promise<T> {
  throw new Error("not implemented");
}
