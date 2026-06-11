"""
Utility to load challenge modules by filename, since they start with digits
which makes them invalid Python identifiers for normal imports.
"""
import importlib.util
import os

_CHALLENGES_DIR = os.path.join(os.path.dirname(__file__), "..", "coding_challenges")


def load(filename: str):
    path = os.path.join(_CHALLENGES_DIR, filename)
    name = filename.replace(".py", "").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
