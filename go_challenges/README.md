# Go Coding Challenges

Self-contained practice challenges for the Canonical Go assessment.
Each file contains:
- A problem specification comment block
- A skeleton to fill in (types, function signatures)
- Tests will be added in a separate `_test.go` file

**Run all challenges:** `go test ./...`
**Type-check only:** `go build ./...`

## Quick drills (1–8)

Each file ships with a skeleton and a clear spec. Target time: a few minutes each.

| # | File | Topic |
|---|------|-------|
| 1 | `01_ttl_cache.go` | Generics / sync.RWMutex / TTL expiry |
| 2 | `02_retry.go` | Higher-order functions / functional options / backoff |
| 3 | `03_errors.go` | Structured errors / errors.Is / errors.As / Unwrap / %w wrapping |
| 4 | `04_worker_pool.go` | Goroutines / channels / fan-out fan-in |
| 5 | `05_pub_sub.go` | Interfaces / pub-sub / concurrency |
| 6 | `06_io.go` | io.Reader / io.Writer / LimitReader / TeeReader / RingBuffer |
| 7 | `07_semaphore.go` | Channels-as-semaphore / context cancellation |
| 8 | `08_middleware.go` | http.Handler / middleware chain / Logger / Recovery / MaxBodySize |

## Assessment-style challenges (9–10)

These mirror the real test format: the file contains only a **few sample tests,
which are NOT exhaustive**. A hidden validation suite plays the role of the
post-submission test suite.

Workflow (practice it exactly like the real thing):
1. Read the spec, implement the skeleton (suggested time is in each file).
2. Write **your own** edge-case tests until you're confident — 100% on the
   sample tests does not mean 100% on validation.
3. Only then run the hidden suite: `go test ./validation/...`
   Don't read the validation files beforehand.

| # | File | Topic | Time |
|---|------|-------|------|
| 9  | `09_fanout.go`        | Fan-out / fan-in / select / context cancellation / no goroutine leaks | 35 min |
| 10 | `10_pod_scheduler.go` | Kubernetes: resources, nodeSelector, taints/tolerations | 40 min |
