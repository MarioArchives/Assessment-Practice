# Python Coding Challenges

Self-contained practice challenges for the Canonical Python assessment.
Each file contains:
- A problem statement docstring
- A skeleton to fill in
- Runnable tests at the bottom (plain `assert` or `pytest`-compatible)

**Run a single challenge:** `python <file>.py`
**Run everything:** `pytest coding_challenges/`

## Quick drills (1–13)

Each file ships with a fairly complete test suite. Target time: a few
minutes each.

| # | File | Topic |
|---|------|-------|
| 1 | `01_ttl_cache.py` | Decorator / caching / thread safety |
| 2 | `02_retry_decorator.py` | Decorator / exception handling |
| 3 | `03_label_selector.py` | String parsing / K8s concepts |
| 4 | `04_async_rate_limiter.py` | asyncio / concurrency |
| 5 | `05_resource_pool.py` | Context manager / threading |
| 6 | `06_event_bus.py` | Pub/sub / OOP |
| 7 | `07_circuit_breaker.py` | State machine / resilience patterns |
| 8 | `08_config_validator.py` | Dataclasses / validation |
| 9 | `09_process_monitor.py` | asyncio / subprocess management |
| 10 | `10_manifest_differ.py` | Recursive diff / K8s concepts |
| 11 | `11_lazy_pipeline.py` | Generics / lazy evaluation |
| 12 | `12_result_type.py` | Generics / Result type |
| 13 | `13_resource_scope.py` | Generics / context manager |

## Assessment-style challenges (14–19)

These mirror the real test format: the file contains only a **few sample
tests, which are NOT exhaustive**. A hidden validation suite under
`validation/` plays the role of the post-submission test suite.

Workflow (practice it exactly like the real thing):
1. Read the spec, implement the skeleton (suggested time is in each file).
2. Write **your own** edge-case tests until you're confident — 100% on the
   sample tests does not mean 100% on validation.
3. Only then run the hidden suite: `pytest validation/test_<NN>_*.py`.
   Don't read the validation files beforehand.

| # | File | Topic | Time |
|---|------|-------|------|
| 14 | `14_pod_scheduler.py` | K8s: resources, nodeSelector, taints/tolerations | 40 min |
| 15 | `15_owner_gc.py` | K8s: ownerReferences / cascading deletion | 40 min |
| 16 | `16_bounded_queue.py` | Multithreading: Condition, timeouts, shutdown | 40 min |
| 17 | `17_rw_lock.py` | Multithreading: readers-writer lock, writer preference | 40 min |
| 18 | `18_type_checked.py` | Decorators: inspect.signature, runtime validation | 30 min |
| 19 | `19_timeout_decorator.py` | Decorators + threads: timeout, exception propagation | 30 min |
