// Challenge 10 — Pod Scheduler                              (suggested time: 40 min)
// ----------------------------------------------------------------------------------
// Implement a simplified Kubernetes scheduler that assigns pods to nodes.
//
// Inputs are plain maps; optional keys may be absent entirely:
//
//	node = map[string]any{
//	    "name":     "node-a",
//	    "capacity": map[string]int{"cpu": 2000, "memory": 4096},  // millicores / Mi
//	    "labels":   map[string]string{"zone": "us-east-1a"},       // optional
//	    "taints":   []map[string]string{                            // optional
//	        {"key": "dedicated", "value": "gpu", "effect": "NoSchedule"},
//	    },
//	}
//
//	pod = map[string]any{
//	    "name":          "web-1",
//	    "requests":      map[string]int{"cpu": 500, "memory": 512},
//	    "node_selector": map[string]string{"zone": "us-east-1a"},  // optional
//	    "tolerations":   []map[string]string{                       // optional
//	        {"key": "dedicated", "value": "gpu"},
//	    },
//	}
//
// Scheduling rules (pods are scheduled one at a time, in list order):
//
//  1. A node is FEASIBLE for a pod if:
//     - It has enough free cpu AND memory. Free = capacity minus the sum of
//     requests of pods already assigned during this Schedule call.
//     - Its labels contain every key=value pair from the pod's node_selector.
//     - Every taint with effect "NoSchedule" is tolerated by the pod.
//     A toleration matches a taint when their keys are equal AND the
//     toleration either has no "value" key or its value equals the taint's.
//     Taints with any other effect are ignored.
//
//  2. Among feasible nodes, pick the one with the MOST free cpu.
//     Break ties by list order (prefer the earlier node).
//
//  3. If no node is feasible the pod maps to "" (empty string).
//
// API:
//
//	Schedule(pods []map[string]any, nodes []map[string]any) map[string]string
//	    Returns {podName: nodeName} for every pod ("" if unschedulable).
//
// This is an assessment-style challenge. A few sample tests ship with this file,
// but a hidden validation suite (validation/) is the real grader.
// Write your own edge-case tests before checking the validation suite.

package main

// Schedule assigns each pod to a node (or "" if unschedulable).
func Schedule(pods []map[string]any, nodes []map[string]any) map[string]string {
	panic("not implemented")
}

// ---------------------------------------------------------------------------
// Sample tests — NOT exhaustive. Write your own before running validation.
// ---------------------------------------------------------------------------

// (tests will live in 10_pod_scheduler_test.go)

func main() {
	nodes := []map[string]any{
		{"name": "node-a", "capacity": map[string]int{"cpu": 2000, "memory": 4096}},
	}
	pods := []map[string]any{
		{"name": "web-1", "requests": map[string]int{"cpu": 500, "memory": 512}},
	}
	assignments, err := Schedule(nodes, pods)
	fmt.Printf("assignments: %v, err: %v\n", assignments, err)
}
