"""
Challenge 7 — Circuit Breaker
-------------------------------
Implement the Circuit Breaker resilience pattern.

States:
  CLOSED    — normal operation; failures are counted
  OPEN      — calls immediately raise `CircuitOpenError` for `recovery_timeout` secs
  HALF_OPEN — one probe call is allowed through:
                success → reset to CLOSED
                failure → back to OPEN (restart timer)

Transitions:
  CLOSED  → OPEN      after `failure_threshold` consecutive failures
  OPEN    → HALF_OPEN after `recovery_timeout` seconds have elapsed
  HALF_OPEN → CLOSED  on success
  HALF_OPEN → OPEN    on failure

Any successful call resets the consecutive failure counter.

Usage:
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=30.0)

    @cb
    def call_external_api():
        ...
"""

import time
from enum import Enum, auto
from functools import wraps


class CircuitState(Enum):
    CLOSED = auto()
    OPEN = auto()
    HALF_OPEN = auto()


class CircuitOpenError(Exception):
    """Raised when a call is attempted while the circuit is OPEN."""


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: float = 1.0):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.last_opened = None

    def __call__(self, func):

        @wraps(func)
        def circuit_breaker(*args, **kwargs):
            result = None

            if self.state == CircuitState.OPEN:
                raise CircuitOpenError

            try:
                result = func(*args, **kwargs)
                self.failure_count = 0
                self.last_opened = None

            except Exception as e:
                self.failure_count += 1
                if self.state == CircuitState.OPEN:
                    self.last_opened = time.time()
                elif self.state == CircuitState.HALF_OPEN:
                    self.failure_count = self.failure_threshold
                    self.last_opened = time.time()
                raise e

            return result

        return circuit_breaker

    @property
    def state(self) -> CircuitState:
        """Return the current state (accounting for timeout transitions)."""
        state = None
        time_since_open = time.time() - self.last_opened if self.last_opened else 0

        if (
            self.failure_count >= self.failure_threshold
            and time_since_open < self.recovery_timeout
        ):
            state = CircuitState.OPEN

        elif time_since_open and time_since_open > self.recovery_timeout:
            state = CircuitState.HALF_OPEN

        elif self.failure_count < self.failure_threshold:
            state = CircuitState.CLOSED

        return state


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_passes_through_when_closed():
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=1)

    @cb
    def fn():
        return "ok"

    assert fn() == "ok"
    assert cb.state == CircuitState.CLOSED


def test_opens_after_threshold():
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=1)

    @cb
    def fn():
        raise RuntimeError("fail")

    for _ in range(3):
        try:
            fn()
        except RuntimeError:
            pass

    assert cb.state == CircuitState.OPEN

    try:
        fn()
        assert False, "Should raise CircuitOpenError"
    except CircuitOpenError:
        pass


def test_success_resets_failure_count():
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=1)
    fail = [True, False, True, True]
    idx = [0]

    @cb
    def fn():
        result = fail[idx[0]]
        idx[0] += 1
        if result:
            raise RuntimeError("fail")
        return "ok"

    try:
        fn()
    except RuntimeError:
        pass
    fn()  # success — resets counter
    try:
        fn()
    except RuntimeError:
        pass
    try:
        fn()
    except RuntimeError:
        pass
    # Only 2 consecutive failures since the success; should still be CLOSED
    assert cb.state == CircuitState.CLOSED


def test_transitions_to_half_open_after_timeout():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)

    @cb
    def fn():
        raise RuntimeError("fail")

    for _ in range(2):
        try:
            fn()
        except RuntimeError:
            pass

    assert cb.state == CircuitState.OPEN
    time.sleep(0.15)
    assert cb.state == CircuitState.HALF_OPEN


def test_half_open_success_closes_circuit():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)
    should_fail = [True]

    @cb
    def fn():
        if should_fail[0]:
            raise RuntimeError("fail")
        return "ok"

    for _ in range(2):
        try:
            fn()
        except RuntimeError:
            pass

    time.sleep(0.15)
    should_fail[0] = False
    result = fn()
    assert result == "ok"
    assert cb.state == CircuitState.CLOSED


def test_half_open_failure_reopens_circuit():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)

    @cb
    def fn():
        raise RuntimeError("always fails")

    for _ in range(2):
        try:
            fn()
        except RuntimeError:
            pass

    time.sleep(0.15)
    assert cb.state == CircuitState.HALF_OPEN

    try:
        fn()
    except RuntimeError:
        pass

    assert cb.state == CircuitState.OPEN


if __name__ == "__main__":
    test_passes_through_when_closed()
    test_opens_after_threshold()
    test_success_resets_failure_count()
    test_transitions_to_half_open_after_timeout()
    test_half_open_success_closes_circuit()
    test_half_open_failure_reopens_circuit()
    print("All tests passed!")
