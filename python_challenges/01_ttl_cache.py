"""
Challenge 1 — TTL Cache Decorator
----------------------------------
Implement a `ttl_cache(seconds)` decorator that:
  - Caches a function's return value per unique set of arguments
  - Returns the cached value if called again within `seconds`
  - Re-executes the function and refreshes the cache after the TTL expires
  - Is thread-safe

Usage:
    @ttl_cache(seconds=5)
    def fetch_config(env: str) -> dict:
        ...
"""

import threading
import time
from functools import wraps


def ttl_cache(seconds: int):
    def decorator(func):
        global_cache = {}

        @wraps(func)
        def caching(*args, **kargs):

            if (
                entry := f"{args},{kargs}"
            ) not in global_cache.keys() or time.time() - global_cache[entry][
                1
            ] >= seconds:
                if entry in global_cache:
                    print(time.time() - global_cache[entry][1] >= seconds)

                answer = func(*args, **kargs)
                global_cache[entry] = (answer, time.time())

            return global_cache[entry][0]

        return caching

    return decorator


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_basic_caching():
    call_count = 0

    @ttl_cache(seconds=10)
    def compute(n):
        nonlocal call_count
        call_count += 1
        return n * 2

    assert compute(5) == 10
    assert compute(5) == 10
    assert call_count == 1, (
        f"Should only call the function once within TTL, it was called {call_count}"
    )


def test_cache_expiry():
    call_count = 0

    @ttl_cache(seconds=1)
    def compute(n):
        nonlocal call_count
        call_count += 1
        return n * 2

    compute(5)
    time.sleep(1.1)
    compute(5)
    assert call_count == 2, "Should re-call the function after TTL expires"


def test_different_args_have_separate_caches():
    @ttl_cache(seconds=10)
    def compute(n):
        return n * 2

    assert compute(3) == 6
    assert compute(4) == 8


def test_thread_safety():
    call_count = 0
    lock = threading.Lock()

    @ttl_cache(seconds=10)
    def slow_compute(n):
        nonlocal call_count
        time.sleep(0.05)
        with lock:
            call_count += 1
        return n * 2

    threads = [threading.Thread(target=slow_compute, args=(1,)) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert slow_compute(1) == 2
    # All concurrent calls may trigger the function, but after settling
    # subsequent calls must use the cache.
    count_after = call_count
    slow_compute(1)
    test_different_args_have_separate_caches()
    assert call_count == count_after, "Cached result should be returned"


if __name__ == "__main__":
    test_basic_caching()
    test_cache_expiry()
    test_different_args_have_separate_caches()
    test_different_args_have_separate_caches()
    test_different_args_have_separate_caches()
    test_thread_safety()
    print("All tests passed!")
