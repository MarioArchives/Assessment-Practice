"""
Challenge 4 — Async Token Bucket Rate Limiter
----------------------------------------------
Implement a `RateLimiter` using the token bucket algorithm for asyncio.

Requirements:
  - Allow at most `rate` calls per `period` seconds
  - `acquire()` is an async method; it waits until a token is available
  - Safe for concurrent use (multiple coroutines calling `acquire` simultaneously)
  - Tokens accumulate when the limiter is idle (burst up to `rate`)

Usage:
    limiter = RateLimiter(rate=10, period=1.0)

    async def handler(request):
        await limiter.acquire()
        return process(request)
"""

import asyncio
import time


class RateLimiter:
    def __init__(self, rate: int, period: float = 1.0):
        """
        :param rate:   maximum calls allowed per `period`
        :param period: length of the time window in seconds
        """
        self.rate = rate
        self.period = period
        self.recent_calls = []

    async def acquire(self) -> None:
        """Block until a token is available, then consume one."""
        allowed_to_acquire = False
        while not allowed_to_acquire:
            period_cutoff_time = time.time() - self.period
            calls_within_period = [
                call_time
                for call_time in self.recent_calls
                if call_time > period_cutoff_time
            ]
            if len(calls_within_period) >= self.rate:
                wait_time = round(calls_within_period[-self.rate] - period_cutoff_time)
                time.sleep(wait_time)
            else:
                self.recent_calls.append(time.time())
                allowed_to_acquire = True


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


async def test_burst_is_fast():
    limiter = RateLimiter(rate=5, period=1.0)
    start = time.monotonic()
    for _ in range(5):
        await limiter.acquire()
    elapsed = time.monotonic() - start
    assert elapsed < 0.3, f"Burst of 5 should be near-instant, took {elapsed:.3f}s"


async def test_rate_is_enforced():
    limiter = RateLimiter(rate=5, period=1.0)
    start = time.monotonic()
    for _ in range(10):
        await limiter.acquire()
    elapsed = time.monotonic() - start
    assert elapsed >= 0.9, f"10 calls at 5/s should take ~1s, took {elapsed:.3f}s"


async def test_concurrent_callers():
    limiter = RateLimiter(rate=3, period=1.0)
    timestamps = []

    async def task():
        await limiter.acquire()
        timestamps.append(time.monotonic())

    await asyncio.gather(*(task() for _ in range(6)))
    assert len(timestamps) == 6
    # Second batch of 3 must start at least ~1s after the first
    timestamps.sort()
    gap = timestamps[3] - timestamps[0]
    assert gap >= 0.9, f"Expected second batch after ~1s, gap was {gap:.3f}s"


if __name__ == "__main__":
    asyncio.run(test_burst_is_fast())
    asyncio.run(test_rate_is_enforced())
    asyncio.run(test_concurrent_callers())
    print("All tests passed!")
