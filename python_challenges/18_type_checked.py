"""
Challenge 18 — Runtime Type-Checking Decorator        (suggested time: 30 min)
------------------------------------------------------------------------------
Implement a `@type_checked` decorator that validates a function's arguments
and return value against its annotations at call time.

Rules:
  - Each argument the CALLER passes (positionally or by keyword) is checked
    against the parameter's annotation with isinstance().
  - Parameters without an annotation are not checked.
  - Default values are NOT checked when the caller does not supply that
    argument (assume the author knows their own defaults).
  - If the function has a return annotation, the return value is checked
    too. The annotation `None` (i.e. `-> None`) means the function must
    return None.
  - On a mismatch raise TypeError; the message must contain the offending
    parameter's name (or the word "return" for the return value).
  - The decorated function must keep its __name__ and __doc__
    (functools.wraps).
  - Annotations are always concrete classes (or None) — no typing generics
    like list[int]. You may assume decorated functions take no *args or
    **kwargs.

Hint: inspect.signature() and Signature.bind() do the heavy lifting of
mapping call arguments onto parameter names.

Usage:
    @type_checked
    def scale(value: int, factor: float) -> float:
        return value * factor

    scale(2, 1.5)      # ok -> 3.0
    scale("2", 1.5)    # TypeError mentioning 'value'
"""

import inspect
from functools import wraps


def type_checked(func):
    # your implementation here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Sample tests — NOT exhaustive. A hidden validation suite
# (validation/test_18_type_checked.py) checks keyword args, return values,
# defaults and metadata. Write your own tests before peeking at it.
# ---------------------------------------------------------------------------


def test_valid_call_passes_through():
    @type_checked
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5


def test_wrong_positional_arg_raises():
    @type_checked
    def add(a: int, b: int) -> int:
        return a + b

    try:
        add("2", 3)
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "a" in str(e), "Error message must name the offending parameter"


def test_unannotated_param_is_not_checked():
    @type_checked
    def greet(name, punctuation: str) -> str:
        return f"hello {name}{punctuation}"

    assert greet(42, "!") == "hello 42!"


if __name__ == "__main__":
    test_valid_call_passes_through()
    test_wrong_positional_arg_raises()
    test_unannotated_param_is_not_checked()
    print("All sample tests passed! Now run the validation suite:")
    print("  pytest validation/test_18_type_checked.py")
