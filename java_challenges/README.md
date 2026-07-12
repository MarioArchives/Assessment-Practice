# Java Coding Challenges

Self-contained practice challenges for the Canonical Java assessment.
Each file contains:
- A Javadoc spec describing the problem fully
- A skeleton class/interface to fill in
- Tests will be added in a separate `test/` directory

**Target:** Java 17+ (records, sealed classes, pattern matching are all in scope)
**Compile:** `javac *.java`  or use a Maven/Gradle project (setup TBD)
**Run tests:** `mvn test` (once test setup is added)

## Quick drills (1–8)

| # | File | Topic |
|---|------|-------|
| 1 | `TTLCache.java` | Generics / ConcurrentHashMap / TTL expiry |
| 2 | `Retry.java` | Functional interfaces / Supplier / exponential backoff |
| 3 | `CircuitBreaker.java` | State machine / AtomicReference / resilience |
| 4 | `BoundedQueue.java` | ReentrantLock / Condition / blocking queue from scratch |
| 5 | `EventBus.java` | Typed pub-sub / Class<T> dispatch / thread safety |
| 6 | `ResourcePool.java` | Generics / Semaphore / AutoCloseable lease |
| 7 | `Result.java` | Sealed classes / generics / monadic chaining |
| 8 | `ConfigValidator.java` | Custom annotations / reflection / violation reporting |

## Assessment-style challenges (9–10)

These mirror the real test format: the file contains only a **few sample tests,
which are NOT exhaustive**. A hidden validation suite plays the role of the
post-submission test suite.

Workflow:
1. Read the spec, implement the skeleton (suggested time is in each file).
2. Write **your own** edge-case tests until you're confident.
3. Only then run the hidden suite. Don't read the validation files beforehand.

| # | File | Topic | Time |
|---|------|-------|------|
| 9  | `ManifestDiffer.java` | Recursive Map diff / Kubernetes manifests | 30 min |
| 10 | `PodScheduler.java`   | Kubernetes: resources, nodeSelector, taints/tolerations | 40 min |
