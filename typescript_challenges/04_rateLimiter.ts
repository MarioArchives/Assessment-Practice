/**
 * Challenge 04 — Async Token Bucket Rate Limiter
 * ------------------------------------------------
 * Implement a RateLimiter using the token bucket algorithm.
 *
 * interface RateLimiterOptions {
 *   rate: number;      // max tokens (= max burst capacity)
 *   periodMs: number;  // window over which `rate` tokens accumulate
 * }
 *
 * class RateLimiter:
 *   constructor(options: RateLimiterOptions)
 *   async acquire(): Promise<void>
 *       Resolves when a token is available. Multiple concurrent callers
 *       are served in FIFO order.
 *
 * Rules:
 *   - Tokens refill continuously (not in discrete windows).
 *   - Up to `rate` tokens may accumulate when the limiter is idle (burst).
 *   - FIFO: if multiple callers are waiting, they are released in the order
 *     they called acquire().
 *   - No spinning: use setTimeout/clearTimeout, not busy-waiting.
 *
 * Usage:
 *   const limiter = new RateLimiter({ rate: 10, periodMs: 1_000 });
 *   await limiter.acquire();   // at most 10 times per second on average
 */
export interface RateLimiterOptions {
  rate: number;
  periodMs: number;
}

export class RateLimiter {
  constructor(options: RateLimiterOptions) {
    throw new Error("not implemented");
  }

  async acquire(): Promise<void> {
    throw new Error("not implemented");
  }
}
