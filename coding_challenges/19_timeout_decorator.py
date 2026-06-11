"""
Challenge 19 — Timeout Decorator (threads)            (suggested time: 30 min)
------------------------------------------------------------------------------
Implement a `@timeout(seconds)` decorator that runs the wrapped function in
a separate thread and aborts the WAIT (not the thread — Python threads
cannot be killed) if it takes too long.

Rules:
  - If the function finishes within `seconds`, return its result normally.
  - If it does not finish in time, raise the builtin TimeoutError. The
    message must contain the function's __name__. The worker thread may
    keep running in the background (use a daemon thread so it cannot block
    interpreter exit).
  - If the wrapped function raises, re-raise that SAME exception object in
    the caller's thread (not a wrapped/converted one).
  - Arguments and keyword arguments are forwarded unchanged.
  - The decorated function keeps its __name__ and __doc__
    (functools.wraps) and can be called multiple times.

Usage:
    @timeout(0.5)
    def fetch():
        ...

    fetch()   # result, or TimeoutError after ~0.5s
"""

import threading
from functools import wraps


def timeout(seconds: float):
    # your implementation here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Sample tests — NOT exhaustive. A hidden validation suite
# (validation/test_19_timeout_decorator.py) checks exception propagation,
# promptness and metadata. Write your own tests before peeking at it.
# ---------------------------------------------------------------------------


def test_fast_function_returns_result():
    @timeout(1.0)
    def double(n):
        return n * 2

    assert double(21) == 42


def test_slow_function_raises_timeout():
    import time

    @timeout(0.1)
    def sleepy():
        time.sleep(1.0)
        return "done"

    try:
        sleepy()
        assert False, "Should have raised TimeoutError"
    except TimeoutError:
        pass


def test_kwargs_are_forwarded():
    @timeout(1.0)
    def fmt(template, name="world"):
        return template.format(name)

    assert fmt("hi {}", name="there") == "hi there"


if __name__ == "__main__":
    test_fast_function_returns_result()
    test_slow_function_raises_timeout()
    test_kwargs_are_forwarded()
    print("All sample tests passed! Now run the validation suite:")
    print("  pytest validation/test_19_timeout_decorator.py")
