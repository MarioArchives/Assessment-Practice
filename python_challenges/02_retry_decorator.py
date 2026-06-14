"""
Challenge 2 — Retry with Exponential Backoff
---------------------------------------------
Implement a `retry` decorator that:
  - Retries the wrapped function up to `max_retries` times on failure
  - Waits `base_delay * (2 ** attempt)` seconds between retries (exponential backoff)
  - Only catches exceptions listed in `exceptions` (default: all exceptions)
  - Raises the last exception if all retries are exhausted
  - Preserves the original function's name and docstring

Usage:
    @retry(max_retries=3, base_delay=0.5, exceptions=(IOError, TimeoutError))
    def call_api():
        ...
"""
import time
from functools import wraps
from typing import Tuple, Type


def retry(
    max_retries: int = 3,
    base_delay: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
):
    def decorator(func):
        @wraps(func)
        def retry(*args, **kwargs):
            response = None
            attempt = 0
            while not attempt > max_retries:
                try:
                    response = func(*args,**kwargs)
                    break
                except exceptions as e:
                    if attempt == max_retries:
                        raise e
                    time.sleep(base_delay*(2**attempt))
                attempt += 1

            return response
        return retry 
    return decorator
    


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_succeeds_first_try():
    calls = []

    @retry(max_retries=3, base_delay=0)
    def fn():
        calls.append(1)
        return "ok"

    result = fn()
    assert result == "ok"
    assert len(calls) == 1


def test_retries_until_success():
    calls = []

    @retry(max_retries=5, base_delay=0)
    def fn():
        calls.append(1)
        if len(calls) < 3:
            raise ValueError("not yet")
        return "ok"

    result = fn()
    assert result == "ok"
    assert len(calls) == 3


def test_raises_after_max_retries():
    @retry(max_retries=2, base_delay=0)
    def fn():
        raise RuntimeError("always fails")

    try:
        fn()
        assert False, "Should have raised"
    except RuntimeError as e:
        assert str(e) == "always fails"


def test_only_catches_specified_exceptions():
    @retry(max_retries=3, base_delay=0, exceptions=(ValueError,))
    def fn():
        raise TypeError("unhandled")

    try:
        fn()
        assert False, "Should have raised TypeError"
    except TypeError:
        pass


def test_preserves_function_metadata():
    @retry()
    def my_func():
        """My docstring."""
        pass

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == "My docstring."


def test_exponential_backoff_timing():
    attempts = []

    @retry(max_retries=3, base_delay=0.1, exceptions=(ValueError,))
    def fn():
        attempts.append(time.monotonic())
        raise ValueError("fail")

    try:
        fn()
    except ValueError:
        pass
    print(attempts)

    assert len(attempts) == 4  # initial + 3 retries
    # Gaps should grow: ~0.1s, ~0.2s, ~0.4s
    gaps = [attempts[i + 1] - attempts[i] for i in range(len(attempts) - 1)]
    assert gaps[1] > gaps[0] * 1.5, "Second delay should be longer than first"


if __name__ == "__main__":
    test_succeeds_first_try()
    test_retries_until_success()
    test_raises_after_max_retries()
    test_only_catches_specified_exceptions()
    test_preserves_function_metadata()
    test_exponential_backoff_timing()
    print("All tests passed!")
