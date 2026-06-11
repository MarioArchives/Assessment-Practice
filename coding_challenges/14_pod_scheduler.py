"""
Challenge 14 — Pod Scheduler                          (suggested time: 40 min)
------------------------------------------------------------------------------
Implement a simplified Kubernetes scheduler that assigns pods to nodes.

Inputs are plain dicts; optional keys may be absent entirely:

  node = {
      "name": "node-a",
      "capacity": {"cpu": 2000, "memory": 4096},      # millicores / Mi
      "labels": {"zone": "us-east-1a"},               # optional
      "taints": [{"key": "dedicated", "value": "gpu", "effect": "NoSchedule"}],  # optional
  }

  pod = {
      "name": "web-1",
      "requests": {"cpu": 500, "memory": 512},
      "node_selector": {"zone": "us-east-1a"},        # optional
      "tolerations": [{"key": "dedicated", "value": "gpu"}],  # optional
  }

Scheduling rules (pods are scheduled one at a time, in list order):

  1. A node is FEASIBLE for a pod if:
       - It has enough FREE cpu AND memory. Free = capacity minus the
         requests of pods already assigned to it during this run.
       - Its labels contain every key=value pair of the pod's node_selector.
       - Every taint with effect "NoSchedule" is tolerated by the pod.
         A toleration matches a taint when their keys are equal and the
         toleration either has no "value" key or its value equals the
         taint's. Taints with any other effect are ignored.
  2. Among feasible nodes, pick the one with the MOST free cpu
     (this spreads pods). Break ties by node list order.
  3. If no node is feasible the pod is unscheduled and maps to None.

Implement:
    schedule(pods: list[dict], nodes: list[dict]) -> dict[str, str | None]
        Returns {pod_name: node_name_or_None} for every pod.
"""


def schedule(pods: list[dict], nodes: list[dict]) -> dict[str, str | None]:
    """Assign each pod to a node name (or None if unschedulable)."""
    # your implementation here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Sample tests — NOT exhaustive. Just like the real assessment, a hidden
# validation suite (validation/test_14_pod_scheduler.py) checks edge cases.
# Write your own tests before peeking at it.
# ---------------------------------------------------------------------------


def test_single_pod_fits():
    pods = [{"name": "p1", "requests": {"cpu": 500, "memory": 512}}]
    nodes = [{"name": "node-a", "capacity": {"cpu": 2000, "memory": 4096}}]
    assert schedule(pods, nodes) == {"p1": "node-a"}


def test_pod_too_big_is_unscheduled():
    pods = [{"name": "p1", "requests": {"cpu": 4000, "memory": 512}}]
    nodes = [{"name": "node-a", "capacity": {"cpu": 2000, "memory": 4096}}]
    assert schedule(pods, nodes) == {"p1": None}


def test_node_selector_filters_nodes():
    pods = [
        {
            "name": "p1",
            "requests": {"cpu": 100, "memory": 128},
            "node_selector": {"zone": "west"},
        }
    ]
    nodes = [
        {"name": "node-a", "capacity": {"cpu": 2000, "memory": 4096},
         "labels": {"zone": "east"}},
        {"name": "node-b", "capacity": {"cpu": 2000, "memory": 4096},
         "labels": {"zone": "west"}},
    ]
    assert schedule(pods, nodes) == {"p1": "node-b"}


if __name__ == "__main__":
    test_single_pod_fits()
    test_pod_too_big_is_unscheduled()
    test_node_selector_filters_nodes()
    print("All sample tests passed! Now run the validation suite:")
    print("  pytest validation/test_14_pod_scheduler.py")
