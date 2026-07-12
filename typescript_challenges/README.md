# TypeScript Coding Challenges

Self-contained practice challenges for the Canonical TypeScript assessment.
Each file contains:
- A JSDoc spec describing the problem fully
- A skeleton class/function to fill in
- Tests will be added in a separate `__tests__/` directory

**Type-check:** `npx tsc --noEmit`
**Run tests:** `npx jest` (test setup TBD)

## Quick drills (1–8)

| # | File | Topic |
|---|------|-------|
| 1 | `01_ttlCache.ts` | Generics / Map / TTL expiry |
| 2 | `02_retry.ts` | Async/await / generics / exponential backoff |
| 3 | `03_circuitBreaker.ts` | State machine / async / resilience |
| 4 | `04_rateLimiter.ts` | Async token bucket / Promise queue |
| 5 | `05_eventBus.ts` | Mapped types / typed pub-sub / generics |
| 6 | `06_labelSelector.ts` | String parsing / Kubernetes label selectors |
| 7 | `07_result.ts` | Discriminated unions / monadic chaining / type guards |
| 8 | `08_pipeline.ts` | Generators / Symbol.iterator / lazy evaluation |

## Assessment-style challenges (9–10)

These mirror the real test format: the file contains only a **few sample tests,
which are NOT exhaustive**. A hidden validation suite plays the role of the
post-submission test suite.

Workflow (practice it exactly like the real thing):
1. Read the spec, implement the skeleton (suggested time is in each file).
2. Write **your own** edge-case tests until you're confident — 100% on the
   sample tests does not mean 100% on validation.
3. Only then run the hidden suite. Don't read the validation files beforehand.

| # | File | Topic | Time |
|---|------|-------|------|
| 9  | `09_manifestDiffer.ts` | Recursive object diff / Kubernetes manifests | 30 min |
| 10 | `10_podScheduler.ts`   | Kubernetes: resources, nodeSelector, taints/tolerations | 40 min |
