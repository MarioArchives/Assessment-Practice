"""
Challenge 11 — Generic Lazy Pipeline
--------------------------------------
Implement a Pipeline[T] class that wraps a lazy sequence and lets you chain
transformations. Nothing is evaluated until you iterate or call .collect().

Requirements:
  - Pipeline(iterable)         — wraps any iterable; stores it lazily
  - .map(fn) -> Pipeline[U]    — apply fn to every element; returns a new Pipeline
  - .filter(pred) -> Pipeline[T] — keep elements where pred(x) is True
  - .take(n) -> Pipeline[T]    — yield at most the first n elements
  - .collect() -> list[T]      — evaluate the full pipeline into a list
  - __iter__                   — allow: for x in pipeline: ...

Rules:
  - Each method must return a NEW Pipeline wrapping a generator — no lists in between
  - The source iterable must not be consumed until iteration begins
  - Chaining must be composable:
      Pipeline(range(100)).filter(lambda x: x % 2 == 0).map(lambda x: x * 3).take(5).collect()

Typing hints (not enforced at runtime, but your implementation should reflect them):
  T = TypeVar("T")
  U = TypeVar("U")

  class Pipeline(Generic[T]):
      def map(self, fn: Callable[[T], U]) -> "Pipeline[U]": ...
      def filter(self, pred: Callable[[T], bool]) -> "Pipeline[T]": ...
      def take(self, n: int) -> "Pipeline[T]": ...
"""

from typing import Callable, Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Pipeline(Generic[T]):
    def __init__(self, source: Iterable[T]) -> None:
        self.source = source

    def __iter__(self) -> Iterator[T]:
        return self.source.__iter__()

    def map(self, fn: Callable[[T], U]) -> "Pipeline[U]":
        return Pipeline(map(fn, self.source))

    def filter(self, pred: Callable[[T], bool]) -> "Pipeline[T]":

        return Pipeline(filter(pred, self.source))

    def take(self, n: int) -> "Pipeline[T]":
        def _gen():
            it = iter(self.source)
            for _ in range(n):
                try:
                    yield next(it)
                except StopIteration:
                    break

        return Pipeline(_gen())

    def collect(self) -> list:
        return list(self)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_collect_identity():
    result = Pipeline([1, 2, 3]).collect()
    assert result == [1, 2, 3]


def test_map_transforms_values():
    result = Pipeline([1, 2, 3]).map(lambda x: x * 10).collect()
    assert result == [10, 20, 30]


def test_filter_keeps_matching():
    result = Pipeline(range(6)).filter(lambda x: x % 2 == 0).collect()
    assert result == [0, 2, 4]


def test_take_limits_output():
    result = Pipeline(range(1000)).take(3).collect()
    assert result == [0, 1, 2]


def test_take_larger_than_source():
    result = Pipeline([1, 2]).take(10).collect()
    assert result == [1, 2]


def test_chained_map_filter():
    result = (
        Pipeline(range(10)).filter(lambda x: x % 2 == 0).map(lambda x: x**2).collect()
    )
    assert result == [0, 4, 16, 36, 64]


def test_chained_map_filter_take():
    result = (
        Pipeline(range(100))
        .filter(lambda x: x % 2 == 0)
        .map(lambda x: x * 3)
        .take(5)
        .collect()
    )
    assert result == [0, 6, 12, 18, 24]


def test_lazy_source_not_consumed_early():
    """The generator should not start until iteration begins."""
    consumed = []

    def gen():
        for i in range(5):
            consumed.append(i)
            yield i

    p = Pipeline(gen()).map(lambda x: x + 1)
    assert consumed == [], "Source must not be consumed before iteration"
    p.collect()
    assert consumed == [0, 1, 2, 3, 4]


def test_take_stops_source_early():
    """take(n) must stop consuming the source after n elements."""
    consumed = []

    def gen():
        for i in range(100):
            consumed.append(i)
            yield i

    Pipeline(gen()).take(3).collect()

    assert len(consumed) == 3, "Source should be stopped after take(3)"


def test_direct_iteration():
    results = []
    for x in Pipeline([10, 20, 30]).map(lambda x: x + 1):
        results.append(x)
    assert results == [11, 21, 31]


def test_map_type_change():
    result = Pipeline([1, 2, 3]).map(str).collect()
    assert result == ["1", "2", "3"]


def test_empty_pipeline():
    assert Pipeline([]).map(lambda x: x).filter(lambda x: True).take(5).collect() == []


def test_multiple_maps_chained():
    result = Pipeline([1, 2, 3]).map(lambda x: x * 2).map(lambda x: x + 1).collect()
    assert result == [3, 5, 7]


if __name__ == "__main__":
    test_collect_identity()
    test_map_transforms_values()
    test_filter_keeps_matching()
    test_take_limits_output()
    test_take_larger_than_source()
    test_chained_map_filter()
    test_chained_map_filter_take()
    test_lazy_source_not_consumed_early()
    test_take_stops_source_early()
    test_direct_iteration()
    test_map_type_change()
    test_empty_pipeline()
    test_multiple_maps_chained()
    print("All tests passed!")
