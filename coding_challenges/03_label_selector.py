"""
Challenge 3 — Kubernetes Label Selector Parser
-----------------------------------------------
Implement a label selector matcher that supports the same syntax Kubernetes uses.

Supported requirements (comma-separated, all must match):
  key=value   or  key==value   — equality
  key!=value                   — inequality
  key in (v1, v2, v3)          — set membership
  key notin (v1, v2, v3)       — set exclusion
  key                          — key must exist
  !key                         — key must NOT exist

Rules:
  - Spaces around operators and commas are optional
  - An empty selector string matches everything
  - Commas separate requirements; all must be satisfied

Implement:
    matches(labels: dict[str, str], selector: str) -> bool
"""

import re
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Tuple

Requirement_Args = List[str]


class Requirement(ABC):
    def __init__(self, identifier: str):
        self.identifier = identifier

    @staticmethod
    @abstractmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def validate_args(args: Requirement_Args) -> bool:
        pass

    def split(self, arg: str):
        if self.identifier:
            split_args = arg.split(self.identifier)
            return [split_arg for split_arg in split_args if split_arg]

        return [arg]


class RequirementEquality(Requirement):
    def __init__(self, identifier: str):
        super().__init__(identifier)

    @staticmethod
    def validate_args(args: Requirement_Args) -> bool:
        return len(args) == 2 and all(args)

    @staticmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        return (
            RequirementEquality.validate_args(args)
            and args[0] in labels.keys()
            and labels[args[0]] == args[1]
        )


class RequirementInequality(RequirementEquality):
    def __init__(self, identifier: str):
        super().__init__(identifier)

    @staticmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        return (
            RequirementEquality.validate_args(args)
            and args[0] in labels.keys()
            and labels[args[0]] != args[1]
        )


class RequirementSetMembership(Requirement):
    def __init__(self, identifier: str):
        super().__init__(identifier)

    @staticmethod
    def extract_brackets(text: str):
        match = re.match("\((.*?)\)", text)
        if not match:
            raise Exception(f"{text}, is wrongly formated for set requirements")
        return match.group(1)

    @staticmethod
    def validate_args(args: Requirement_Args) -> bool | str:
        if len(args) == 2:
            return RequirementSetMembership.extract_brackets(args[1])
        return False

    @staticmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        if args_content := RequirementSetMembership.validate_args(args):
            possible_values = args_content.split(",")
            return args[0] in labels.keys() and labels[args[0]] in possible_values

        return False


class RequirementSetExclusion(RequirementSetMembership):
    def __init__(self, identifier: str):
        super().__init__(identifier)

    @staticmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        return args[
            0
        ] in labels.keys() and not RequirementSetMembership.requirement_operation(
            labels, args
        )


class RequirementExist(Requirement):
    def __init__(self, identifier: str):
        super().__init__(identifier)

    @staticmethod
    def validate_args(args: Requirement_Args) -> bool:
        return len(args) == 1

    @staticmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        if RequirementExist.validate_args(args):
            return args[0] in labels.keys()
        return False


class RequirementNotExist(RequirementExist):
    def __init__(self, identifier: str):
        super().__init__(identifier)

    @staticmethod
    def validate_args(args: Requirement_Args) -> bool:
        return super().validate_args(args)

    @staticmethod
    def requirement_operation(labels: Dict[str, str], args: Requirement_Args) -> bool:
        return not RequirementExist.requirement_operation(labels, args)


class Requirements(Enum):
    inequality = RequirementInequality("!=")
    double_equality = RequirementEquality("==")
    equality = RequirementEquality("=")
    set_exclusion = RequirementSetExclusion(" notin ")
    set_membership = RequirementSetMembership(" in ")
    key_exclusion = RequirementNotExist("!")
    key_existence = RequirementExist("")


Requirement_Operation = Tuple[Requirements, Requirement_Args]


def bracket_split(string: str, separator: str) -> List[str]:
    # split that ignores instances of separator inside ()
    split_indexes = []
    bracket_open_count = 0
    split_strings = []
    for idx, char in enumerate(string):
        if char == "(":
            bracket_open_count += 1
        elif char == ")" and bracket_open_count > 0:
            bracket_open_count -= 1
        if char == separator and bracket_open_count == 0:
            split_indexes.append(idx)

    for idx in range(len(split_indexes)):
        if idx == 0:
            split_strings.append(string[: split_indexes[idx]])
        else:
            split_strings.append(
                string[split_indexes[idx - 1] + 1 : split_indexes[idx]]
            )

        if idx == len(split_indexes) - 1:
            split_strings.append(string[split_indexes[idx] + 1 :])

    return split_strings if split_strings else [string]


def extract_requirement_operation(requirement: str) -> Requirement_Operation:

    for requirement_type in Requirements:
        if requirement_type.value.identifier in requirement:
            split_args = requirement_type.value.split(requirement)
            cleaned_args = [arg.replace(" ", "") for arg in split_args]
            return (requirement_type, cleaned_args)

    raise Exception(f"Failed to retrieve appropiate requirement type for {requirement}")


def matches(labels: Dict[str, str], selector: str) -> bool:
    """Return True if labels satisfy every requirement in selector."""

    if not selector:
        return True

    requirements = bracket_split(selector, ",")
    match_result = True

    for requirement in requirements:
        requirement_type, arguments = extract_requirement_operation(requirement)
        match_result *= requirement_type.value.requirement_operation(labels, arguments)
        if not match_result:
            break

    return bool(match_result)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_smart_split():
    a = "This is, a string that (should, be, processes), accordingly"
    a_split = bracket_split(a, ",")
    assert len(a_split) == 3
    assert a_split[1] == " a string that (should, be, processes)"
    b = "a,,(),"
    b_split = bracket_split(b, ",")
    assert len(b_split) == 4
    assert b_split[1] == ""
    assert b_split[2] == "()"


def test_empty_selector_matches_all():
    assert matches({"app": "web"}, "") is True
    assert matches({}, "") is True


def test_equality():
    assert matches({"app": "web"}, "app=web") is True
    assert matches({"app": "api"}, "app=web") is False


def test_double_equality():
    assert matches({"app": "web"}, "app==web") is True


def test_inequality():
    assert matches({"env": "prod"}, "env!=dev") is True
    assert matches({"env": "dev"}, "env!=dev") is False


def test_set_in():
    assert matches({"env": "prod"}, "env in (prod, staging)") is True
    assert matches({"env": "dev"}, "env in (prod, staging)") is False


def test_set_notin():
    assert matches({"env": "prod"}, "env notin (dev, test)") is True
    assert matches({"env": "dev"}, "env notin (dev, test)") is False


def test_existence():
    assert matches({"app": "web"}, "app") is True
    assert matches({}, "app") is False


def test_non_existence():
    assert matches({}, "!debug") is True
    assert matches({"debug": "true"}, "!debug") is False


def test_missing_key_for_equality():
    assert matches({}, "app=web") is False


def test_multiple_requirements():
    labels = {"app": "web", "env": "prod", "tier": "frontend"}
    assert matches(labels, "app=web,env=prod") is True
    assert matches(labels, "app=web,env=dev") is False
    assert matches(labels, "app=web,env in (prod,staging),tier") is True


def test_whitespace_tolerance():
    assert matches({"env": "prod"}, " env = prod ") is True
    assert matches({"env": "prod"}, "env in ( prod , staging )") is True


if __name__ == "__main__":
    test_smart_split()
    test_empty_selector_matches_all()
    test_equality()
    test_double_equality()
    test_inequality()
    test_set_in()
    test_set_notin()
    test_existence()
    test_non_existence()
    test_missing_key_for_equality()
    test_multiple_requirements()
    test_whitespace_tolerance()
    print("All tests passed!")
