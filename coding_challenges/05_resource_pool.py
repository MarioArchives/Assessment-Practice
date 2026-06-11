"""
Challenge 5 — Thread-Safe Resource Pool
-----------------------------------------
Implement a generic, thread-safe resource pool with context manager support.

Requirements:
  - Pre-create `size` resources using a `factory` callable at construction time
  - `acquire(timeout)` is a context manager that lends one resource
  - Blocks (up to `timeout` seconds) if all resources are in use
  - Returns the resource to the pool on context exit (even on exception)
  - Raises `TimeoutError` if no resource becomes available within `timeout`

Usage:
    pool = ResourcePool(factory=create_db_connection, size=5)

    with pool.acquire(timeout=3.0) as conn:
        conn.execute(query)
"""

import queue
import threading
import time
from contextlib import contextmanager
from typing import Callable, Generic, Iterator, TypeVar

T = TypeVar("T")


class ResourcePool(Generic[T]):
    def __init__(self, factory: Callable[[], T], size: int):
        # your implementation here
        self._pool = queue.Queue()
        for _ in range(size):
            self._pool.put(factory())
        self.attempts_max = 3

    @contextmanager
    def acquire(self, timeout: float = 5.0) -> Iterator[T]:
        """Yield a resource; return it to the pool on exit."""
        try:
            resource = self._pool.get(timeout=timeout)
        except queue.Empty:
            raise TimeoutError("could not get resource")

        try:
            yield resource
        finally:
            self._pool.put(resource)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_basic_acquire_and_release():
    pool = ResourcePool(factory=lambda: {"id": id(object())}, size=2)
    with pool.acquire() as r:
        assert r is not None


def test_pool_limits_concurrent_use():
    pool = ResourcePool(factory=object, size=1)
    holder_started = threading.Event()
    holder_done = threading.Event()

    def hold():
        with pool.acquire(timeout=5.0):
            holder_started.set()
            holder_done.wait()

    t = threading.Thread(target=hold)
    t.start()
    holder_started.wait()

    start = time.monotonic()
    try:
        with pool.acquire(timeout=0.2):
            pass
        assert False, "Should have raised TimeoutError"
    except TimeoutError:
        elapsed = time.monotonic() - start
        assert elapsed >= 0.15, "Should have blocked for ~timeout seconds"

    holder_done.set()
    t.join()


def test_resource_returned_on_exception():
    pool = ResourcePool(factory=object, size=1)

    try:
        with pool.acquire(timeout=1.0):
            raise RuntimeError("boom")
    except RuntimeError:
        pass

    # Resource must be back; this should not block
    with pool.acquire(timeout=0.5) as r:
        assert r is not None


def test_all_resources_used_concurrently():
    pool = ResourcePool(factory=object, size=3)
    acquired = []
    barrier = threading.Barrier(3)

    def task():
        with pool.acquire(timeout=2.0) as r:
            acquired.append(r)
            barrier.wait()  # all 3 hold resources simultaneously

    threads = [threading.Thread(target=task) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(acquired) == 3
    assert len(set(id(r) for r in acquired)) == 3, "Each thread got a distinct resource"


if __name__ == "__main__":
    test_basic_acquire_and_release()
    test_pool_limits_concurrent_use()
    test_resource_returned_on_exception()
    test_all_resources_used_concurrently()
    print("All tests passed!")
