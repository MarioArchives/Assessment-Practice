"""
Challenge 16 — Bounded Blocking Queue                 (suggested time: 40 min)
------------------------------------------------------------------------------
Implement a thread-safe bounded FIFO queue from scratch using
threading primitives (threading.Lock / threading.Condition).
Do NOT use queue.Queue.

API:

  class QueueClosed(Exception): ...

  class BoundedQueue:
      def __init__(self, capacity: int): ...
      def put(self, item, timeout: float | None = None) -> None: ...
      def get(self, timeout: float | None = None): ...
      def close(self) -> None: ...
      def __len__(self) -> int: ...        # number of buffered items

Semantics:
  - put() blocks while the queue is full; get() blocks while it is empty.
  - If `timeout` is given and expires before the operation can complete,
    raise the builtin TimeoutError.
  - close() is idempotent. After close():
      * put() raises QueueClosed immediately
      * get() keeps returning the remaining buffered items, then raises
        QueueClosed once the queue is empty
      * threads currently blocked in put() or get() must wake up and
        follow the same rules (blocked putters raise QueueClosed; blocked
        getters raise QueueClosed if nothing is buffered for them)
  - Items come out in exactly the order they were put in (FIFO), even
    with many concurrent producers and consumers (no lost or duplicated
    items).
"""

import threading


class QueueClosed(Exception):
    pass


class BoundedQueue:
    def __init__(self, capacity: int):
        # your implementation here
        raise NotImplementedError

    def put(self, item, timeout: float | None = None) -> None:
        # your implementation here
        raise NotImplementedError

    def get(self, timeout: float | None = None):
        # your implementation here
        raise NotImplementedError

    def close(self) -> None:
        # your implementation here
        raise NotImplementedError

    def __len__(self) -> int:
        # your implementation here
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Sample tests — NOT exhaustive. A hidden validation suite
# (validation/test_16_bounded_queue.py) checks timeouts, close semantics
# and concurrent producer/consumer integrity. Write your own tests first.
# ---------------------------------------------------------------------------


def test_fifo_order():
    q = BoundedQueue(capacity=3)
    q.put("a")
    q.put("b")
    q.put("c")
    assert [q.get(), q.get(), q.get()] == ["a", "b", "c"]


def test_len_reports_buffered_items():
    q = BoundedQueue(capacity=2)
    assert len(q) == 0
    q.put(1)
    assert len(q) == 1
    q.get()
    assert len(q) == 0


def test_put_blocks_until_space():
    import time

    q = BoundedQueue(capacity=1)
    q.put("first")
    done = threading.Event()

    def producer():
        q.put("second")  # must block until the consumer makes room
        done.set()

    t = threading.Thread(target=producer, daemon=True)
    t.start()
    time.sleep(0.1)
    assert not done.is_set(), "put() must block while the queue is full"
    assert q.get() == "first"
    t.join(timeout=1)
    assert done.is_set(), "put() must complete once space is available"
    assert q.get() == "second"


if __name__ == "__main__":
    test_fifo_order()
    test_len_reports_buffered_items()
    test_put_blocks_until_space()
    print("All sample tests passed! Now run the validation suite:")
    print("  pytest validation/test_16_bounded_queue.py")
