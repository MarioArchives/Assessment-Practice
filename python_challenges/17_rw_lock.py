"""
Challenge 17 — Readers-Writer Lock                    (suggested time: 40 min)
------------------------------------------------------------------------------
Implement a readers-writer lock using threading primitives
(threading.Lock / threading.Condition).

API:

  class RWLock:
      def read(self):  ...   # returns a context manager acquiring a READ lock
      def write(self): ...   # returns a context manager acquiring a WRITE lock

Usage:
    lock = RWLock()
    with lock.read():
        ...  # shared access
    with lock.write():
        ...  # exclusive access

Semantics:
  - Any number of readers may hold the lock simultaneously.
  - A writer holds the lock exclusively: no readers and no other writer.
  - Writer preference: once a writer is WAITING, newly arriving readers
    must block until that writer has acquired and released the lock
    (prevents writer starvation).
  - The lock must be released correctly even if the with-block raises.
  - Hint: contextlib.contextmanager makes read()/write() easy to expose,
    or implement small helper objects with __enter__/__exit__.

You do not need to support reentrancy (a thread acquiring the lock twice)
or read-to-write upgrades.
"""

import threading
from contextlib import contextmanager


class RWLock:
    def __init__(self):
        # your implementation here
        raise NotImplementedError

    def read(self):
        """Context manager for shared (read) access."""
        # your implementation here
        raise NotImplementedError

    def write(self):
        """Context manager for exclusive (write) access."""
        # your implementation here
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Sample tests — NOT exhaustive. A hidden validation suite
# (validation/test_17_rw_lock.py) checks concurrency, writer preference and
# exception safety. Write your own tests before peeking at it.
# ---------------------------------------------------------------------------


def test_basic_read_then_write():
    lock = RWLock()
    with lock.read():
        pass
    with lock.write():
        pass  # must not deadlock after a read


def test_two_readers_can_overlap():
    import time

    lock = RWLock()
    inside = threading.Event()
    overlapped = threading.Event()

    def reader_one():
        with lock.read():
            inside.set()
            overlapped.wait(timeout=1)

    def reader_two():
        inside.wait(timeout=1)
        with lock.read():           # must succeed while reader_one holds it
            overlapped.set()

    t1 = threading.Thread(target=reader_one, daemon=True)
    t2 = threading.Thread(target=reader_two, daemon=True)
    t1.start()
    t2.start()
    t1.join(timeout=2)
    t2.join(timeout=2)
    assert overlapped.is_set(), "Two readers must be able to hold the lock at once"


def test_writer_excludes_reader():
    import time

    lock = RWLock()
    holding = threading.Event()
    read_acquired = threading.Event()

    def writer():
        with lock.write():
            holding.set()
            time.sleep(0.3)

    def reader():
        holding.wait(timeout=1)
        with lock.read():
            read_acquired.set()

    tw = threading.Thread(target=writer, daemon=True)
    tr = threading.Thread(target=reader, daemon=True)
    tw.start()
    tr.start()
    holding.wait(timeout=1)
    time.sleep(0.1)
    assert not read_acquired.is_set(), "Reader must wait while a writer holds the lock"
    tw.join(timeout=2)
    tr.join(timeout=2)
    assert read_acquired.is_set()


if __name__ == "__main__":
    test_basic_read_then_write()
    test_two_readers_can_overlap()
    test_writer_excludes_reader()
    print("All sample tests passed! Now run the validation suite:")
    print("  pytest validation/test_17_rw_lock.py")
