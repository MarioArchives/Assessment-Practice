"""
Challenge 13 — Generic Resource Scope
----------------------------------------
Implement a ResourceScope[T] context manager that accumulates typed resources
during a with-block and guarantees they are all cleaned up in REVERSE
registration order when the block exits (even on exception).

This is a simplified, typed version of contextlib.ExitStack.

Requirements:
  - ResourceScope is a context manager (supports `with` statement)
  - Inside the with-block, call scope.register(resource, cleanup_fn) to
    enroll a resource and its teardown callable
  - On exit (normal or exception), call cleanup_fn(resource) for every
    registered resource, in reverse registration order
  - If a cleanup function itself raises, continue cleaning up the remaining
    resources, then re-raise the LAST cleanup exception (after all cleanups run)
  - scope.resources is a list of the currently registered resources (in order)

Types:
  T = TypeVar("T")

  class ResourceScope(Generic[T]):
      resources: list[T]
      def register(self, resource: T, cleanup: Callable[[T], None]) -> T: ...
          # registers and RETURNS the resource so callers can use it inline:
          # conn = scope.register(open_connection(), close_connection)
      def __enter__(self) -> "ResourceScope[T]": ...
      def __exit__(self, *exc_info) -> bool: ...   # return False (don't suppress exceptions)

Usage:
    with ResourceScope() as scope:
        f = scope.register(open("a.txt"), lambda f: f.close())
        db = scope.register(connect_db(), lambda db: db.close())
        # use f and db here
    # db.close() called first, then f.close()
"""

from queue import LifoQueue
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class ResourceScope(Generic[T]):
    def __init__(self) -> None:
        self.registry = LifoQueue()
        self.resources = []

    def register(self, resource: T, cleanup: Callable[[T], None]) -> T:
        """Enroll resource and return it for immediate use."""
        # your implementation here
        self.registry.put((resource, cleanup))
        self.resources.append(resource)
        return resource

    def __enter__(self) -> "ResourceScope[T]":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        # your implementation here
        err = None
        while not self.registry.empty():
            resource, cleanup = self.registry._get()
            try:
                cleanup(resource)
            except Exception as e:
                err = e
        if err:
            raise err
        return False


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_basic_cleanup_called():
    cleaned = []

    with ResourceScope() as scope:
        scope.register("res-a", lambda r: cleaned.append(r))

    assert cleaned == ["res-a"]


def test_cleanup_called_on_exception():
    cleaned = []

    try:
        with ResourceScope() as scope:
            scope.register("res", lambda r: cleaned.append(r))
            raise ValueError("boom")
    except ValueError:
        pass

    assert "res" in cleaned, "Cleanup must run even when the body raises"


def test_cleanup_reverse_order():
    order = []

    with ResourceScope() as scope:
        scope.register("first", lambda r: order.append(r))
        scope.register("second", lambda r: order.append(r))
        scope.register("third", lambda r: order.append(r))

    assert order == ["third", "second", "first"], (
        f"Expected reverse registration order, got {order}"
    )


def test_register_returns_resource():
    with ResourceScope() as scope:
        r = scope.register({"key": "value"}, lambda _: None)
        assert r == {"key": "value"}, "register() must return the resource"


def test_resources_list_populated():
    with ResourceScope() as scope:
        scope.register("a", lambda _: None)
        scope.register("b", lambda _: None)
        assert scope.resources == ["a", "b"]


def test_exception_not_suppressed():
    try:
        with ResourceScope() as scope:
            scope.register("x", lambda _: None)
            raise RuntimeError("original")
        assert False, "Exception should propagate"
    except RuntimeError as e:
        assert str(e) == "original"


def test_multiple_resources_all_cleaned():
    cleaned = []

    with ResourceScope() as scope:
        for i in range(5):
            scope.register(i, lambda r: cleaned.append(r))

    assert sorted(cleaned) == [0, 1, 2, 3, 4]


def test_cleanup_exception_does_not_skip_remaining():
    cleaned = []

    try:
        with ResourceScope() as scope:
            scope.register("a", lambda r: cleaned.append(r))
            scope.register(
                "b", lambda r: (_ for _ in ()).throw(RuntimeError("cleanup fail"))
            )
            scope.register("c", lambda r: cleaned.append(r))
    except RuntimeError:
        pass

    assert "a" in cleaned, (
        "Earlier resources must still be cleaned after a later cleanup fails"
    )
    assert "c" in cleaned, "Resources before the failing one must still be cleaned"


def test_cleanup_exception_is_reraised():
    try:
        with ResourceScope() as scope:
            scope.register(
                "x", lambda r: (_ for _ in ()).throw(RuntimeError("cleanup error"))
            )
    except RuntimeError as e:
        assert "cleanup error" in str(e)
    else:
        assert False, "Cleanup exception should be re-raised"


def test_empty_scope_exits_cleanly():
    with ResourceScope() as scope:
        pass  # no registrations — must not raise


def test_inline_register_usage():
    results = []

    class FakeConn:
        def query(self):
            return "data"

    def close(conn):
        results.append("closed")

    with ResourceScope() as scope:
        conn = scope.register(FakeConn(), close)
        results.append(conn.query())

    assert results == ["data", "closed"]


if __name__ == "__main__":
    test_basic_cleanup_called()
    test_cleanup_called_on_exception()
    test_cleanup_reverse_order()
    test_register_returns_resource()
    test_resources_list_populated()
    test_exception_not_suppressed()
    test_multiple_resources_all_cleaned()
    test_cleanup_exception_does_not_skip_remaining()
    test_cleanup_exception_is_reraised()
    test_empty_scope_exits_cleanly()
    test_inline_register_usage()
    print("All tests passed!")
