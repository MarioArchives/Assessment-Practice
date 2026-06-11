"""Validation suite for Challenge 16 — Bounded Blocking Queue.

DO NOT read these tests before attempting the challenge: they play the role
of the hidden post-submission suite in the real assessment.
"""

import threading
import time

from _loader import load_challenge

_mod = load_challenge("16_bounded_queue.py")
BoundedQueue = _mod.BoundedQueue
QueueClosed = _mod.QueueClosed


def test_get_timeout_raises_timeouterror():
    q = BoundedQueue(capacity=1)
    start = time.monotonic()
    try:
        q.get(timeout=0.1)
        assert False, "Should have raised TimeoutError"
    except TimeoutError:
        pass
    assert time.monotonic() - start < 1.0, "Timeout should fire promptly"


def test_put_timeout_raises_timeouterror():
    q = BoundedQueue(capacity=1)
    q.put("x")
    try:
        q.put("y", timeout=0.1)
        assert False, "Should have raised TimeoutError"
    except TimeoutError:
        pass
    assert q.get() == "x", "Failed put must not corrupt the buffer"


def test_get_blocks_until_item_arrives():
    q = BoundedQueue(capacity=1)
    received = []

    def consumer():
        received.append(q.get())

    t = threading.Thread(target=consumer, daemon=True)
    t.start()
    time.sleep(0.1)
    assert received == [], "get() must block while the queue is empty"
    q.put("hello")
    t.join(timeout=1)
    assert received == ["hello"]


def test_put_after_close_raises():
    q = BoundedQueue(capacity=2)
    q.close()
    try:
        q.put("x")
        assert False, "put() after close() must raise QueueClosed"
    except QueueClosed:
        pass


def test_get_drains_remaining_items_after_close():
    q = BoundedQueue(capacity=3)
    q.put("a")
    q.put("b")
    q.close()
    assert q.get() == "a"
    assert q.get() == "b"
    try:
        q.get()
        assert False, "get() on a closed empty queue must raise QueueClosed"
    except QueueClosed:
        pass


def test_close_is_idempotent():
    q = BoundedQueue(capacity=1)
    q.close()
    q.close()  # must not raise


def test_close_wakes_blocked_getter():
    q = BoundedQueue(capacity=1)
    outcome = []

    def consumer():
        try:
            outcome.append(q.get())
        except QueueClosed:
            outcome.append("closed")

    t = threading.Thread(target=consumer, daemon=True)
    t.start()
    time.sleep(0.1)
    q.close()
    t.join(timeout=1)
    assert outcome == ["closed"], "Blocked get() must wake and raise QueueClosed"


def test_close_wakes_blocked_putter():
    q = BoundedQueue(capacity=1)
    q.put("full")
    outcome = []

    def producer():
        try:
            q.put("more")
            outcome.append("ok")
        except QueueClosed:
            outcome.append("closed")

    t = threading.Thread(target=producer, daemon=True)
    t.start()
    time.sleep(0.1)
    q.close()
    t.join(timeout=1)
    assert outcome == ["closed"], "Blocked put() must wake and raise QueueClosed"


def test_many_producers_and_consumers_lose_nothing():
    q = BoundedQueue(capacity=4)
    n_producers, items_each = 4, 50
    consumed = []
    consumed_lock = threading.Lock()

    def producer(pid):
        for i in range(items_each):
            q.put((pid, i))

    def consumer():
        while True:
            try:
                item = q.get()
            except QueueClosed:
                return
            with consumed_lock:
                consumed.append(item)

    producers = [
        threading.Thread(target=producer, args=(p,), daemon=True)
        for p in range(n_producers)
    ]
    consumers = [threading.Thread(target=consumer, daemon=True) for _ in range(3)]
    for t in producers + consumers:
        t.start()
    for t in producers:
        t.join(timeout=5)
        assert not t.is_alive(), "Producers must finish (no deadlock)"
    q.close()
    for t in consumers:
        t.join(timeout=5)
        assert not t.is_alive(), "Consumers must finish after close()"

    assert len(consumed) == n_producers * items_each, "No item lost or duplicated"
    assert len(set(consumed)) == len(consumed), "No item duplicated"
    # Per-producer FIFO: each producer's items must come out in order.
    for p in range(n_producers):
        seq = [i for (pid, i) in consumed if pid == p]
        assert seq == sorted(seq), "FIFO order violated within a producer"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All validation tests passed!")
