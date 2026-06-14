"""
Challenge 15 — Owner-Reference Garbage Collector      (suggested time: 40 min)
------------------------------------------------------------------------------
Kubernetes garbage-collects objects whose owners are gone (cascading
deletion via ownerReferences). Implement that resolution logic.

Each object is a dict:

    {"uid": "rs-1", "owners": ["deploy-1"]}     # "owners" may be absent or []

Implement:
    collect_garbage(objects: list[dict], deleted: set[str]) -> set[str]

`deleted` is the set of uids that have already been deleted externally.
Return the set of uids (from `objects`) that the garbage collector must
now delete.

Rules:
  - An owner reference is ABSENT if the referenced uid is in `deleted`,
    OR it does not appear among `objects` at all (a dangling reference).
  - An object that has at least one owner reference becomes garbage when
    ALL of its owners are absent or are themselves garbage. Apply this
    repeatedly until nothing changes (a fixpoint), so deletions cascade
    down chains: Deployment -> ReplicaSet -> Pods.
  - An object with no owner references is never garbage.
  - Objects that merely reference each other in a cycle (with at least one
    member kept alive by the rules above, or no absent owners at all) must
    NOT be collected: starting from "nothing is garbage", only objects
    that the rule above marks become garbage.
  - If a uid appears both in `objects` and in `deleted`, it is already
    gone: treat it as absent and do not include it in the result.

Example:
    objects = [
        {"uid": "rs-1", "owners": ["deploy-1"]},
        {"uid": "pod-1", "owners": ["rs-1"]},
    ]
    collect_garbage(objects, {"deploy-1"}) == {"rs-1", "pod-1"}
"""


def collect_garbage(objects: list[dict], deleted: set[str]) -> set[str]:
    """Return the uids of all objects that must be cascade-deleted."""
    # your implementation here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Sample tests — NOT exhaustive. A hidden validation suite
# (validation/test_15_owner_gc.py) checks edge cases (diamonds, cycles,
# dangling refs, ...). Write your own tests before peeking at it.
# ---------------------------------------------------------------------------


def test_simple_cascade():
    objects = [
        {"uid": "rs-1", "owners": ["deploy-1"]},
        {"uid": "pod-1", "owners": ["rs-1"]},
        {"uid": "pod-2", "owners": ["rs-1"]},
    ]
    assert collect_garbage(objects, {"deploy-1"}) == {"rs-1", "pod-1", "pod-2"}


def test_object_without_owners_survives():
    objects = [{"uid": "standalone"}]
    assert collect_garbage(objects, {"deploy-1"}) == set()


def test_nothing_deleted_nothing_collected():
    objects = [
        {"uid": "rs-1", "owners": ["deploy-1"]},
        {"uid": "deploy-1", "owners": []},
    ]
    assert collect_garbage(objects, set()) == set()


if __name__ == "__main__":
    test_simple_cascade()
    test_object_without_owners_survives()
    test_nothing_deleted_nothing_collected()
    print("All sample tests passed! Now run the validation suite:")
    print("  pytest validation/test_15_owner_gc.py")
