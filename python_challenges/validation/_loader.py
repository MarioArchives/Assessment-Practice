"""Helper to import the numbered challenge modules (their filenames start
with digits, so a plain `import` statement cannot load them)."""

import importlib.util
from pathlib import Path

CHALLENGES_DIR = Path(__file__).resolve().parent.parent


def load_challenge(filename: str):
    path = CHALLENGES_DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
