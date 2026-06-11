"""Validation suite for Challenge 15 — Owner-Reference Garbage Collector.

DO NOT read these tests before attempting the challenge: they play the role
of the hidden post-submission suite in the real assessment.
"""

from _loader import load_challenge

collect_garbage = load_challenge("15_owner_gc.py").collect_garbage


def _o(uid, owners=None):
    obj = {"uid": uid}
    if owners is not None:
        obj["owners"] = owners
    return obj


def test_deep_chain_cascades():
    objects = [
        _o("rs-1", ["deploy-1"]),
        _o("pod-1", ["rs-1"]),
        _o("pod-2", ["rs-1"]),
        _o("log-1", ["pod-1"]),
    ]
    assert collect_garbage(objects, {"deploy-1"}) == {
        "rs-1", "pod-1", "pod-2", "log-1",
    }


def test_dangling_owner_is_garbage():
    # The owner uid never existed among objects and is not in deleted.
    objects = [_o("pod-1", ["ghost"])]
    assert collect_garbage(objects, set()) == {"pod-1"}


def test_diamond_with_one_living_owner_survives():
    objects = [
        _o("rs-1", ["deploy-1"]),
        _o("rs-2"),                      # alive: no owners
        _o("pod-1", ["rs-1", "rs-2"]),
    ]
    # rs-1 collected, but rs-2 still owns pod-1.
    assert collect_garbage(objects, {"deploy-1"}) == {"rs-1"}


def test_diamond_with_both_owners_gone_is_garbage():
    objects = [
        _o("rs-1", ["deploy-1"]),
        _o("rs-2", ["deploy-1"]),
        _o("pod-1", ["rs-1", "rs-2"]),
    ]
    assert collect_garbage(objects, {"deploy-1"}) == {"rs-1", "rs-2", "pod-1"}


def test_pure_cycle_survives():
    objects = [
        _o("a", ["b"]),
        _o("b", ["a"]),
    ]
    assert collect_garbage(objects, set()) == set()


def test_cycle_anchored_by_living_member_survives_deleted_root():
    objects = [
        _o("a", ["b", "root"]),
        _o("b", ["a"]),
    ]
    # root is gone, but a is still owned by b (alive) and vice versa.
    assert collect_garbage(objects, {"root"}) == set()


def test_deleted_uid_present_in_objects_is_excluded_from_result():
    objects = [
        _o("deploy-1"),
        _o("rs-1", ["deploy-1"]),
    ]
    result = collect_garbage(objects, {"deploy-1"})
    assert result == {"rs-1"}
    assert "deploy-1" not in result


def test_empty_owner_list_behaves_like_no_owners():
    objects = [_o("standalone", [])]
    assert collect_garbage(objects, {"anything"}) == set()


def test_multiple_independent_roots():
    objects = [
        _o("rs-1", ["deploy-1"]),
        _o("rs-2", ["deploy-2"]),
        _o("rs-3", ["deploy-3"]),
        _o("deploy-3"),
    ]
    assert collect_garbage(objects, {"deploy-1", "deploy-2"}) == {"rs-1", "rs-2"}


def test_empty_objects_list():
    assert collect_garbage([], {"deploy-1"}) == set()


def test_cascade_order_does_not_matter():
    # Children listed before their parents: a single forward pass would miss
    # these; the fixpoint must still catch them.
    objects = [
        _o("pod-1", ["rs-1"]),
        _o("rs-1", ["deploy-1"]),
    ]
    assert collect_garbage(objects, {"deploy-1"}) == {"rs-1", "pod-1"}


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All validation tests passed!")
