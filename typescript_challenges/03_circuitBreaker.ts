/**
 * Challenge 03 — Async Circuit Breaker
 * --------------------------------------
 * Implement the Circuit Breaker resilience pattern for async operations.
 *
 * States:
 *   "closed"    — normal operation; consecutive failures are counted
 *   "open"      — calls immediately throw CircuitOpenError for recoveryTimeoutMs
 *   "half-open" — one probe call is allowed through:
 *                   success → "closed"; failure → "open" (restart timer)
 *
 * Transitions:
 *   closed    → open      after failureThreshold consecutive failures
 *   open      → half-open after recoveryTimeoutMs ms have elapsed
 *   half-open → closed    on success
 *   half-open → open      on failure
 *
 * Any successful call resets the consecutive failure counter.
 *
 * API:
 *   constructor(options: CircuitBreakerOptions)
 *   async call<T>(fn: () => Promise<T>): Promise<T>
 *   get state(): CircuitState
 *
 * interface CircuitBreakerOptions {
 *   failureThreshold: number;
 *   recoveryTimeoutMs: number;
 * }
 *
 * type CircuitState = "closed" | "open" | "half-open"
 * class CircuitOpenError extends Error
 */
export type CircuitState = "closed" | "open" | "half-open";

export class CircuitOpenError extends Error {
  constructor() {
    super("Circuit breaker is open");
    this.name = "CircuitOpenError";
  }
}

export interface CircuitBreakerOptions {
  failureThreshold: number;
  recoveryTimeoutMs: number;
}

export class CircuitBreaker {
  constructor(options: CircuitBreakerOptions) {
    throw new Error("not implemented");
  }

  async call<T>(fn: () => Promise<T>): Promise<T> {
    throw new Error("not implemented");
  }

  get state(): CircuitState {
    throw new Error("not implemented");
  }
}
