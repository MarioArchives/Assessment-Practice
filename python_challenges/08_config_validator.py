"""
Challenge 8 — Typed Config Validator
--------------------------------------
Implement a `ServiceConfig` dataclass with validation in `__post_init__`,
and a `load_config(data: dict) -> ServiceConfig` factory function.

Validation rules:
  name      — required str, must match regex [a-z][a-z0-9-]* (lowercase, hyphens ok, start with letter)
  replicas  — required int, 1 ≤ replicas ≤ 100
  port      — required int, 1 ≤ port ≤ 65535
  image     — required str, non-empty
  namespace — optional str, defaults to "default", non-empty if provided

Raise `ValueError` with a descriptive message for each violated rule.
`load_config` should raise `ValueError` for missing required fields
(rather than a `TypeError`).
"""

import re
from dataclasses import dataclass


def is_bounded(x: int, a: int, b: int):
    return x >= a and x <= b


@dataclass
class ServiceConfig:
    name: str
    replicas: int
    port: int
    image: str
    namespace: str = "default"

    def __post_init__(self):
        validation_dict = {
            "name": (self.name, lambda x: re.fullmatch("[a-z][a-z0-9-]*", x)),
            "replicas": (self.replicas, lambda x: is_bounded(x, 1, 100)),
            "port": (self.port, lambda x: is_bounded(x, 1, 65535)),
            "image": (self.image, lambda x: type(x) == str),
            "name space": (self.namespace, lambda x: type(x) == str),
        }

        for check in validation_dict.keys():
            variable = validation_dict[check][0]
            check_func = validation_dict[check][1]
            if not variable:
                raise ValueError(f"{check} entry ({variable}) not defined")
            elif not check_func(variable):
                raise ValueError(f"{check} is not valid ({variable})")


def load_config(data: dict) -> ServiceConfig:
    """Parse and validate a config dict. Raise ValueError on missing or invalid fields."""
    return ServiceConfig(
        name=data.get("name"),
        replicas=data.get("replicas"),
        port=data.get("port"),
        image=data.get("image"),
        namespace=data.get("namespace", "default"),
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_valid_config():
    cfg = load_config(
        {
            "name": "my-service",
            "replicas": 3,
            "port": 8080,
            "image": "nginx:latest",
        }
    )
    assert cfg.name == "my-service"
    assert cfg.replicas == 3
    assert cfg.port == 8080
    assert cfg.namespace == "default"


def test_custom_namespace():
    cfg = load_config(
        {
            "name": "api",
            "replicas": 1,
            "port": 3000,
            "image": "myapp:v1",
            "namespace": "production",
        }
    )
    assert cfg.namespace == "production"


def test_invalid_name_uppercase():
    try:
        load_config({"name": "MyService", "replicas": 1, "port": 80, "image": "x"})
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "name" in str(e).lower()


def test_invalid_name_underscore():
    try:
        load_config({"name": "my_service", "replicas": 1, "port": 80, "image": "x"})
        assert False
    except ValueError:
        pass


def test_invalid_name_starts_with_digit():
    try:
        load_config({"name": "1service", "replicas": 1, "port": 80, "image": "x"})
        assert False
    except ValueError:
        pass


def test_replicas_below_minimum():
    try:
        load_config({"name": "svc", "replicas": 0, "port": 80, "image": "x"})
        assert False
    except ValueError as e:
        assert "replica" in str(e).lower()


def test_replicas_above_maximum():
    try:
        load_config({"name": "svc", "replicas": 101, "port": 80, "image": "x"})
        assert False
    except ValueError:
        pass


def test_invalid_port():
    try:
        load_config({"name": "svc", "replicas": 1, "port": 99999, "image": "x"})
        assert False
    except ValueError as e:
        assert "port" in str(e).lower()


def test_port_zero_invalid():
    try:
        load_config({"name": "svc", "replicas": 1, "port": 0, "image": "x"})
        assert False
    except ValueError:
        pass


def test_missing_required_field_raises_value_error():
    try:
        load_config({"name": "svc", "replicas": 1, "image": "x"})  # port missing
        assert False
    except ValueError:
        pass


def test_empty_image_invalid():
    try:
        load_config({"name": "svc", "replicas": 1, "port": 80, "image": ""})
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_valid_config()
    test_custom_namespace()
    test_invalid_name_uppercase()
    test_invalid_name_underscore()
    test_invalid_name_starts_with_digit()
    test_replicas_below_minimum()
    test_replicas_above_maximum()
    test_invalid_port()
    test_port_zero_invalid()
    test_missing_required_field_raises_value_error()
    test_empty_image_invalid()
    print("All tests passed!")
