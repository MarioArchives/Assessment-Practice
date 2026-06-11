"""
Challenge 10 — Kubernetes Manifest Differ
------------------------------------------
Implement `diff(old, new, ignore_paths)` that returns a list of `Change` objects
describing what changed between two manifest dicts.

Rules:
  - Recurse into nested dicts; list items are matched positionally by index
  - Path format: dot-separated keys/indices, e.g. "spec.containers.0.image"
  - Detect three kinds of changes:
      "added"   — key present in new but not in old
      "removed" — key present in old but not in new
      "changed" — key present in both but value differs (for non-dict values)
  - When old[k] and new[k] are both dicts, recurse rather than emit "changed"
  - Paths listed in `ignore_paths` are skipped entirely (no change recorded,
    no recursion past them)
  - Identical manifests produce an empty list
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional


class ChangeType(Enum):
    ADDED = "added"
    REMOVED = "removed"
    CHANGED = "changed"


@dataclass
class Change:
    path: str
    old: Any
    new: Any
    kind: ChangeType


def handle_different_keys(
    all_valid_keys: List[str], new: Dict, old: Dict, parent_dir: str
) -> List[Change]:
    changes_list = []

    for key in all_valid_keys:
        dir_name = parent_dir + f".{key}" if parent_dir else f"{key}"
        if key in old.keys() and key not in new.keys():
            c = Change(path=dir_name, old=old[key], new=None, kind=ChangeType.REMOVED)
            changes_list.append(c)

        elif key in new.keys() and key not in old.keys():
            c = Change(path=dir_name, old=None, new=new[key], kind=ChangeType.ADDED)
            changes_list.append(c)

    return changes_list


def handle_list_entries(
    new: List,
    old: List,
    parent_dir: str,
    ignore_paths: Optional[str] = [],
) -> List[Change]:

    longer_list, shorter_list = (old, new) if len(old) >= len(new) else (new, old)
    change_list = []

    for i in range(len(longer_list)):
        dir_name = parent_dir + f".{i}" if parent_dir else f"{i}"
        if i >= len(shorter_list):
            change_kind = (
                ChangeType.ADDED if shorter_list == old else ChangeType.REMOVED
            )
            old_entry, new_entry = (
                (None, new[i]) if change_kind == ChangeType.ADDED else (old[i], None)
            )
            c = Change(path=dir_name, old=old_entry, new=new_entry, kind=change_kind)
            change_list.append(c)
        elif longer_list[i] != shorter_list[i]:
            if handled_iter_type := handle_iter_types(
                new[i], old[i], dir_name, ignore_paths
            ):
                change_list.extend(handled_iter_type)

    return change_list


def handle_iter_types(
    new: Dict | List,
    old: Dict | List,
    parent_dir: str,
    ignore_paths: Optional[str] = [],
) -> List[Change]:
    change_list = []

    if isinstance(old, Dict) and isinstance(new, Dict):
        deeper_changes = diff(old, new, ignore_paths, parent_dir)
        change_list.extend(deeper_changes)

    elif isinstance(old, List) and isinstance(new, List):
        deeper_changes = handle_list_entries(new, old, parent_dir, parent_dir)
        change_list.extend(deeper_changes)

    return change_list


def handle_same_keys(
    mutual_keys: List[str],
    new: Dict,
    old: Dict,
    parent_dir: str,
    ignore_paths: Optional[str] = [],
) -> List[Change]:
    change_list = []
    for key in mutual_keys:
        if old[key] != new[key]:
            dir_name = parent_dir + f".{key}" if parent_dir else f"{key}"
            if handled_iter_type := handle_iter_types(
                new[key], old[key], dir_name, ignore_paths
            ):
                change_list.extend(handled_iter_type)

            else:
                c = Change(
                    path=dir_name, old=old[key], new=new[key], kind=ChangeType.CHANGED
                )
                change_list.append(c)
    return change_list


def get_keys_not_ignored(
    all_keys: List[str], ignore_paths: List[str], parent_dir: str = ""
) -> List[str]:
    path_prefix = parent_dir + "." if parent_dir else parent_dir
    valid_keys = []

    for key in set(all_keys):
        if path_prefix + key not in ignore_paths:
            valid_keys.append(key)

    return valid_keys


def diff(
    old: Dict, new: Dict, ignore_paths: Optional[List[str]] = [], parent_dir: str = ""
) -> List[Change]:
    """Return a list of Change objects between old and new."""
    differences = []
    all_keys = list(old.keys()) + list(new.keys())

    all_keys_valid_unique = get_keys_not_ignored(all_keys, ignore_paths, parent_dir)

    keys_in_both = [
        key for key in all_keys_valid_unique if key in old.keys() and key in new.keys()
    ]

    differences = handle_different_keys(all_keys_valid_unique, new, old, parent_dir)
    differences.extend(
        handle_same_keys(keys_in_both, new, old, parent_dir, ignore_paths)
    )

    return differences


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_no_changes():
    d = {"spec": {"replicas": 3}}
    assert diff(d, d) == []


def test_changed_scalar():
    changes = diff({"spec": {"replicas": 2}}, {"spec": {"replicas": 3}})
    assert len(changes) == 1
    c = changes[0]
    assert c.path == "spec.replicas"
    assert c.old == 2
    assert c.new == 3
    assert c.kind == ChangeType.CHANGED


def test_added_key():
    changes = diff(
        {"metadata": {"name": "svc"}},
        {"metadata": {"name": "svc", "labels": {"app": "web"}}},
    )
    assert any(
        c.path == "metadata.labels" and c.kind == ChangeType.ADDED for c in changes
    )


def test_removed_key():
    changes = diff(
        {"metadata": {"name": "svc", "labels": {}}},
        {"metadata": {"name": "svc"}},
    )
    assert any(
        c.path == "metadata.labels" and c.kind == ChangeType.REMOVED for c in changes
    )


def test_nested_list_diff():
    old = {"spec": {"containers": [{"image": "nginx:1.0", "name": "web"}]}}
    new = {"spec": {"containers": [{"image": "nginx:2.0", "name": "web"}]}}
    changes = diff(old, new)
    assert any(
        c.path == "spec.containers.0.image" and c.kind == ChangeType.CHANGED
        for c in changes
    )
    assert not any(c.path == "spec.containers.0.name" for c in changes)


def test_ignore_paths():
    old = {"metadata": {"resourceVersion": "100", "name": "svc"}}
    new = {"metadata": {"resourceVersion": "200", "name": "svc"}}
    changes = diff(old, new, ignore_paths=["metadata.resourceVersion"])
    assert not any(c.path == "metadata.resourceVersion" for c in changes)


def test_top_level_added_and_removed():
    changes = diff({"a": 1}, {"b": 2})
    paths = {c.path: c.kind for c in changes}
    assert paths.get("a") == ChangeType.REMOVED
    assert paths.get("b") == ChangeType.ADDED


def test_deeply_nested_change():
    old = {"a": {"b": {"c": {"d": 1}}}}
    new = {"a": {"b": {"c": {"d": 2}}}}
    changes = diff(old, new)
    assert len(changes) == 1
    assert changes[0].path == "a.b.c.d"


def test_list_length_change():
    old = {"items": [1, 2, 3]}
    new = {"items": [1, 2]}
    changes = diff(old, new)
    # Index 2 was removed
    assert any(c.path == "items.2" and c.kind == ChangeType.REMOVED for c in changes)


if __name__ == "__main__":
    test_no_changes()
    test_changed_scalar()
    test_added_key()
    test_removed_key()
    test_nested_list_diff()
    test_ignore_paths()
    test_top_level_added_and_removed()
    test_deeply_nested_change()
    test_list_length_change()
    print("All tests passed!")
