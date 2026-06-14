"""Validation suite for Challenge 19 — Timeout Decorator.

DO NOT read these tests before attempting the challenge: they play the role
of the hidden post-submission suite in the real assessment.
"""

import time

from _loader import load_challenge

timeout = load_challenge("19_timeout_decorator.py").timeout


def test_timeout_fires_promptly():
    @timeout(0.2)
    def sleepy():
        time.sleep(2.0)

    start = time.monotonic()
    try:
        sleepy()
        assert False, "Should have raised TimeoutError"
    except TimeoutError:
        pass
    elapsed = time.monotonic() - start
    assert elapsed < 1.0, (
        f"TimeoutError must be raised at ~0.2s, not after the function "
        f"finishes (took {elapsed:.2f}s)"
    )


def test_timeout_message_contains_function_name():
    @timeout(0.05)
    def very_slow_fetch():
        time.sleep(1.0)

    try:
        very_slow_fetch()
        assert False, "Should have raised TimeoutError"
    except TimeoutError as e:
        assert "very_slow_fetch" in str(e)


def test_same_exception_object_propagates():
    sentinel = ValueError("original failure")

    @timeout(1.0)
    def boom():
        raise sentinel

    try:
        boom()
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert e is sentinel, "The ORIGINAL exception object must propagate"


def test_exception_type_is_not_converted():
    @timeout(1.0)
    def bad_lookup():
        return {}["missing"]

    try:
        bad_lookup()
        assert False, "Should have raised KeyError"
    except KeyError:
        pass


def test_result_and_arguments_forwarded():
    @timeout(1.0)
    def combine(a, b, *, sep="-"):
        return f"{a}{sep}{b}"

    assert combine(1, 2) == "1-2"
    assert combine("x", "y", sep="+") == "x+y"


def test_none_result_is_returned_not_mistaken_for_timeout():
    @timeout(1.0)
    def returns_none():
        return None

    assert returns_none() is None


def test_metadata_preserved():
    @timeout(1.0)
    def documented():
        """I have a docstring."""

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "I have a docstring."


def test_decorated_function_is_reusable():
    calls = []

    @timeout(1.0)
    def quick(n):
        calls.append(n)
        return n * 2

    assert quick(1) == 2
    assert quick(2) == 4
    assert quick(3) == 6
    assert calls == [1, 2, 3]


def test_independent_decorations_do_not_interfere():
    @timeout(0.1)
    def slow():
        time.sleep(1.0)

    @timeout(1.0)
    def fast():
        return "ok"

    try:
        slow()
        assert False, "Should have raised TimeoutError"
    except TimeoutError:
        pass
    assert fast() == "ok"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All validation tests passed!")
