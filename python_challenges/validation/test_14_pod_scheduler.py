"""Validation suite for Challenge 14 — Pod Scheduler.

DO NOT read these tests before attempting the challenge: they play the role
of the hidden post-submission suite in the real assessment.
"""

from _loader import load_challenge

schedule = load_challenge("14_pod_scheduler.py").schedule


def _node(name, cpu=2000, memory=4096, labels=None, taints=None):
    node = {"name": name, "capacity": {"cpu": cpu, "memory": memory}}
    if labels is not None:
        node["labels"] = labels
    if taints is not None:
        node["taints"] = taints
    return node


def _pod(name, cpu=500, memory=512, node_selector=None, tolerations=None):
    pod = {"name": name, "requests": {"cpu": cpu, "memory": memory}}
    if node_selector is not None:
        pod["node_selector"] = node_selector
    if tolerations is not None:
        pod["tolerations"] = tolerations
    return pod


def test_memory_is_checked_independently_of_cpu():
    result = schedule([_pod("p1", cpu=100, memory=8192)],
                      [_node("node-a", cpu=2000, memory=4096)])
    assert result == {"p1": None}


def test_no_nodes_means_unscheduled():
    assert schedule([_pod("p1")], []) == {"p1": None}


def test_empty_pod_list():
    assert schedule([], [_node("node-a")]) == {}


def test_selector_requires_all_pairs():
    nodes = [_node("node-a", labels={"zone": "east"})]
    pod = _pod("p1", node_selector={"zone": "east", "disk": "ssd"})
    assert schedule([pod], nodes) == {"p1": None}


def test_selector_against_node_with_no_labels():
    nodes = [_node("node-a")]  # no "labels" key at all
    pod = _pod("p1", node_selector={"zone": "east"})
    assert schedule([pod], nodes) == {"p1": None}


def test_noschedule_taint_blocks_untolerating_pod():
    taint = {"key": "dedicated", "value": "gpu", "effect": "NoSchedule"}
    result = schedule([_pod("p1")], [_node("node-a", taints=[taint])])
    assert result == {"p1": None}


def test_matching_toleration_admits_pod():
    taint = {"key": "dedicated", "value": "gpu", "effect": "NoSchedule"}
    pod = _pod("p1", tolerations=[{"key": "dedicated", "value": "gpu"}])
    assert schedule([pod], [_node("node-a", taints=[taint])]) == {"p1": "node-a"}


def test_toleration_without_value_matches_any_taint_value():
    taint = {"key": "dedicated", "value": "gpu", "effect": "NoSchedule"}
    pod = _pod("p1", tolerations=[{"key": "dedicated"}])
    assert schedule([pod], [_node("node-a", taints=[taint])]) == {"p1": "node-a"}


def test_toleration_with_wrong_value_does_not_match():
    taint = {"key": "dedicated", "value": "gpu", "effect": "NoSchedule"}
    pod = _pod("p1", tolerations=[{"key": "dedicated", "value": "fpga"}])
    assert schedule([pod], [_node("node-a", taints=[taint])]) == {"p1": None}


def test_all_noschedule_taints_must_be_tolerated():
    taints = [
        {"key": "a", "value": "1", "effect": "NoSchedule"},
        {"key": "b", "value": "2", "effect": "NoSchedule"},
    ]
    pod = _pod("p1", tolerations=[{"key": "a", "value": "1"}])
    assert schedule([pod], [_node("node-a", taints=taints)]) == {"p1": None}


def test_other_taint_effects_are_ignored():
    taint = {"key": "soft", "value": "x", "effect": "PreferNoSchedule"}
    assert schedule([_pod("p1")], [_node("node-a", taints=[taint])]) == {
        "p1": "node-a"
    }


def test_pods_spread_across_equal_nodes():
    nodes = [_node("node-a"), _node("node-b")]
    result = schedule([_pod("p1"), _pod("p2")], nodes)
    # p1 ties on free cpu -> node-a (list order); node-b then has more free
    # cpu, so p2 must land there.
    assert result == {"p1": "node-a", "p2": "node-b"}


def test_most_free_cpu_wins():
    nodes = [_node("small", cpu=1000), _node("big", cpu=4000)]
    assert schedule([_pod("p1")], nodes) == {"p1": "big"}


def test_allocations_accumulate_within_run():
    nodes = [_node("node-a", cpu=1000)]
    result = schedule([_pod("p1", cpu=600), _pod("p2", cpu=600)], nodes)
    assert result == {"p1": "node-a", "p2": None}


def test_exact_fit_is_feasible():
    nodes = [_node("node-a", cpu=500, memory=512)]
    assert schedule([_pod("p1", cpu=500, memory=512)], nodes) == {"p1": "node-a"}


def test_zero_request_pod_fits_a_full_node():
    nodes = [_node("node-a", cpu=500, memory=512)]
    result = schedule(
        [_pod("p1", cpu=500, memory=512), _pod("p2", cpu=0, memory=0)], nodes
    )
    assert result == {"p1": "node-a", "p2": "node-a"}


def test_later_pod_can_still_fit_smaller_node():
    nodes = [_node("big", cpu=4000), _node("small", cpu=800)]
    result = schedule(
        [_pod("p1", cpu=3500), _pod("p2", cpu=700)], nodes
    )
    # p1 -> big (most free). p2: big has 500 free, small has 800 -> small.
    assert result == {"p1": "big", "p2": "small"}


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All validation tests passed!")
