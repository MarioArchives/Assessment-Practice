"""
Challenge 12 — Generic Result Type
-------------------------------------
Implement a Result[T, E] type that represents either a success (Ok) or a
failure (Err). This pattern (common in Rust/Haskell) avoids raising exceptions
for expected failure paths.

Implement two classes that share a common interface:

  Ok(value: T)   — wraps a successful result
  Err(error: E)  — wraps an error

Both must support:
  .is_ok()  -> bool
  .is_err() -> bool
  .unwrap() -> T            raises RuntimeError with the error value if called on Err
  .unwrap_or(default: T) -> T   returns value if Ok, default if Err
  .map(fn: Callable[[T], U]) -> Result[U, E]
      applies fn to the value if Ok, passes Err through unchanged
  .map_err(fn: Callable[[E], F]) -> Result[T, F]
      applies fn to the error if Err, passes Ok through unchanged

Typing hints:
  T = TypeVar("T")
  E = TypeVar("E")
  U = TypeVar("U")
  F = TypeVar("F")

  class Result(Generic[T, E]):  ...
  class Ok(Result[T, E]):       ...   (E is unused but keeps the interface consistent)
  class Err(Result[T, E]):      ...   (T is unused)
"""

from typing import Callable, Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
F = TypeVar("F")


class Result(Generic[T, E]):
    def is_ok(self) -> bool:
        raise NotImplementedError

    def is_err(self) -> bool:
        raise NotImplementedError

    def unwrap(self) -> T:
        raise NotImplementedError

    def unwrap_or(self, default: T) -> T:
        raise NotImplementedError

    def map(self, fn: Callable[[T], U]) -> "Result[U, E]":
        raise NotImplementedError

    def map_err(self, fn: Callable[[E], F]) -> "Result[T, F]":
        raise NotImplementedError


class Ok(Result[T, E]):
    def __init__(self, value: T) -> None:
        self.value = value

    def is_err(self) -> bool:
        return False

    def is_ok(self) -> bool:
        return True

    def unwrap(self) -> T:
        return self.value

    def unwrap_or(self, default: T) -> T:
        return self.value

    def map(self, fn: Callable[[T], U]) -> "Result[U, E]":
        try:
            return Ok(fn(self.value))
        except Exception as e:
            return Err(e)

    def map_err(self, fn: Callable[[E], F]) -> "Result[T, F]":
        return self


class Err(Result[T, E]):
    def __init__(self, error: E) -> None:
        self.error = error

    def is_err(self) -> bool:
        return True

    def is_ok(self) -> bool:
        return False

    def unwrap(self) -> T:
        raise RuntimeError(self.error)

    def unwrap_or(self, default: T) -> T:
        return default

    def map(self, fn: Callable[[T], U]) -> "Result[U, E]":
        return self

    def map_err(self, fn: Callable[[E], F]) -> "Result[T, F]":
        try:
            return Err(fn(self.error))
        except Exception as e:
            return Err(e)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_ok_is_ok():
    assert Ok(42).is_ok() is True
    assert Ok(42).is_err() is False


def test_err_is_err():
    assert Err("oops").is_err() is True
    assert Err("oops").is_ok() is False


def test_ok_unwrap_returns_value():
    assert Ok("hello").unwrap() == "hello"


def test_err_unwrap_raises():
    try:
        Err("something went wrong").unwrap()
        assert False, "Should have raised RuntimeError"
    except RuntimeError as e:
        assert "something went wrong" in str(e)


def test_unwrap_or_ok():
    assert Ok(10).unwrap_or(99) == 10


def test_unwrap_or_err():
    assert Err("bad").unwrap_or(99) == 99


def test_map_ok():
    result = Ok(5).map(lambda x: x * 2)
    assert result.is_ok()
    assert result.unwrap() == 10


def test_map_err_passthrough():
    result = Err("fail").map(lambda x: x * 2)
    assert result.is_err()


def test_map_err_transforms_error():
    result = Err("not found").map_err(lambda e: f"wrapped: {e}")
    assert result.is_err()
    try:
        result.unwrap()
    except RuntimeError as e:
        assert "wrapped: not found" in str(e)


def test_map_err_ok_passthrough():
    result = Ok(7).map_err(lambda e: "should not run")
    assert result.is_ok()
    assert result.unwrap() == 7


def test_chained_map():
    result = Ok("  hello  ").map(str.strip).map(str.upper)
    assert result.unwrap() == "HELLO"


def test_chained_map_stops_at_err():
    ran = []

    result = (
        Err("initial error")
        .map(lambda x: ran.append(x) or x)
        .map(lambda x: ran.append(x) or x)
    )
    assert result.is_err()
    assert ran == [], "map functions must not run on an Err"


def test_ok_with_none_value():
    result = Ok(None)
    assert result.is_ok()
    assert result.unwrap() is None


def test_err_with_exception_object():
    exc = ValueError("bad input")
    result = Err(exc)
    assert result.is_err()
    try:
        result.unwrap()
    except RuntimeError as e:
        assert "bad input" in str(e)


def test_map_type_change():
    result: Result = Ok(123).map(str)
    assert result.unwrap() == "123"


if __name__ == "__main__":
    test_ok_is_ok()
    test_err_is_err()
    test_ok_unwrap_returns_value()
    test_err_unwrap_raises()
    test_unwrap_or_ok()
    test_unwrap_or_err()
    test_map_ok()
    test_map_err_passthrough()
    test_map_err_transforms_error()
    test_map_err_ok_passthrough()
    test_chained_map()
    test_chained_map_stops_at_err()
    test_ok_with_none_value()
    test_err_with_exception_object()
    test_map_type_change()
    print("All tests passed!")
