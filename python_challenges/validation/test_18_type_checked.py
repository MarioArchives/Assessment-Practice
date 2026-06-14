"""Validation suite for Challenge 18 — Runtime Type-Checking Decorator.

DO NOT read these tests before attempting the challenge: they play the role
of the hidden post-submission suite in the real assessment.
"""

from _loader import load_challenge

type_checked = load_challenge("18_type_checked.py").type_checked


def test_keyword_argument_is_checked():
    @type_checked
    def scale(value: int, factor: float) -> float:
        return value * factor

    try:
        scale(2, factor="big")
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "factor" in str(e)


def test_positional_arg_passed_by_keyword():
    @type_checked
    def scale(value: int, factor: float) -> float:
        return value * factor

    assert scale(value=2, factor=1.5) == 3.0
    try:
        scale(value="2", factor=1.5)
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "value" in str(e)


def test_return_value_is_checked():
    @type_checked
    def bad() -> int:
        return "not an int"

    try:
        bad()
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "return" in str(e).lower()


def test_none_return_annotation():
    @type_checked
    def proper() -> None:
        return None

    @type_checked
    def leaky() -> None:
        return 42

    assert proper() is None
    try:
        leaky()
        assert False, "Should have raised TypeError"
    except TypeError:
        pass


def test_missing_return_annotation_not_checked():
    @type_checked
    def anything(x: int):
        return object()

    anything(1)  # must not raise


def test_default_value_is_not_checked_when_not_passed():
    @type_checked
    def f(x: int, flag: str = 0):  # author's bad default — not our problem
        return x

    assert f(5) == 5  # default not supplied by caller -> not validated
    try:
        f(5, flag=1)  # but the caller's value IS validated
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "flag" in str(e)


def test_metadata_preserved():
    @type_checked
    def documented(x: int) -> int:
        """I have a docstring."""
        return x

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "I have a docstring."


def test_subclass_instances_are_accepted():
    class Animal:
        pass

    class Dog(Animal):
        pass

    @type_checked
    def pet(a: Animal) -> Animal:
        return a

    d = Dog()
    assert pet(d) is d  # isinstance semantics: subclasses pass


def test_multiple_bad_args_reports_a_param_name():
    @type_checked
    def f(a: int, b: str) -> None:
        return None

    try:
        f("x", 1)
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "a" in str(e) or "b" in str(e)


def test_valid_complex_call():
    @type_checked
    def join(items: list, sep: str = ", ") -> str:
        return sep.join(str(i) for i in items)

    assert join([1, 2], sep="-") == "1-2"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All validation tests passed!")
