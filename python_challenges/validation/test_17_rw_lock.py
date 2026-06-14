"""Validation suite for Challenge 17 — Readers-Writer Lock.

DO NOT read these tests before attempting the challenge: they play the role
of the hidden post-submission suite in the real assessment.
"""

import threading
import time

from _loader import load_challenge

RWLock = load_challenge("17_rw_lock.py").RWLock


def test_many_readers_overlap():
    lock = RWLock()
    barrier = threading.Barrier(4, timeout=2)
    overlapped = []

    def reader():
        with lock.read():
            # All 4 readers must be inside simultaneously to pass the barrier.
            barrier.wait()
            overlapped.append(True)

    threads = [threading.Thread(target=reader, daemon=True) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=3)
        assert not t.is_alive(), "Readers must not serialize each other"
    assert len(overlapped) == 4


def test_writers_are_mutually_exclusive():
    lock = RWLock()
    counter = 0

    def writer():
        nonlocal counter
        for _ in range(25):
            with lock.write():
                current = counter
                time.sleep(0.001)  # widen the race window
                counter = current + 1

    threads = [threading.Thread(target=writer, daemon=True) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=10)
        assert not t.is_alive()
    assert counter == 100, f"Lost updates: counter={counter}, expected 100"


def test_no_reader_during_write():
    lock = RWLock()
    writing = False
    violations = []

    def writer():
        nonlocal writing
        with lock.write():
            writing = True
            time.sleep(0.2)
            writing = False

    def reader():
        with lock.read():
            if writing:
                violations.append("reader overlapped a writer")

    tw = threading.Thread(target=writer, daemon=True)
    tw.start()
    time.sleep(0.05)  # let the writer acquire first
    readers = [threading.Thread(target=reader, daemon=True) for _ in range(3)]
    for t in readers:
        t.start()
    tw.join(timeout=2)
    for t in readers:
        t.join(timeout=2)
    assert not violations, violations


def test_writer_preference_blocks_new_readers():
    lock = RWLock()
    order = []
    r1_inside = threading.Event()
    release_r1 = threading.Event()

    def first_reader():
        with lock.read():
            r1_inside.set()
            release_r1.wait(timeout=3)

    def writer():
        with lock.write():
            order.append("writer")

    def second_reader():
        with lock.read():
            order.append("reader2")

    t_r1 = threading.Thread(target=first_reader, daemon=True)
    t_r1.start()
    assert r1_inside.wait(timeout=2)

    t_w = threading.Thread(target=writer, daemon=True)
    t_w.start()
    time.sleep(0.15)  # writer is now waiting on the held read lock

    t_r2 = threading.Thread(target=second_reader, daemon=True)
    t_r2.start()
    time.sleep(0.15)  # reader2 must queue behind the waiting writer

    release_r1.set()
    for t in (t_r1, t_w, t_r2):
        t.join(timeout=2)
        assert not t.is_alive(), "Deadlock in writer-preference handling"

    assert order[0] == "writer", (
        f"A waiting writer must acquire before readers that arrived later: {order}"
    )


def test_read_lock_released_on_exception():
    lock = RWLock()
    try:
        with lock.read():
            raise ValueError("boom")
    except ValueError:
        pass
    _assert_write_acquirable(lock)


def test_write_lock_released_on_exception():
    lock = RWLock()
    try:
        with lock.write():
            raise ValueError("boom")
    except ValueError:
        pass
    _assert_write_acquirable(lock)


def _assert_write_acquirable(lock):
    acquired = threading.Event()

    def writer():
        with lock.write():
            acquired.set()

    t = threading.Thread(target=writer, daemon=True)
    t.start()
    t.join(timeout=1)
    assert acquired.is_set(), "Lock was not released after an exception"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All validation tests passed!")
