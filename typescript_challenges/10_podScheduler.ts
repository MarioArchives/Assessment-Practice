/**
 * Challenge 10 — Pod Scheduler                            (suggested time: 40 min)
 * ----------------------------------------------------------------------------------
 * Implement a simplified Kubernetes scheduler that assigns pods to nodes.
 *
 * Inputs are typed objects; optional fields may be absent:
 *
 *   interface KNode {
 *     name: string;
 *     capacity: { cpu: number; memory: number };    // millicores / Mi
 *     labels?: Record<string, string>;
 *     taints?: Array<{ key: string; value: string; effect: string }>;
 *   }
 *
 *   interface Pod {
 *     name: string;
 *     requests: { cpu: number; memory: number };
 *     nodeSelector?: Record<string, string>;
 *     tolerations?: Array<{ key: string; value?: string }>;
 *   }
 *
 * Scheduling rules (pods are scheduled one at a time, in list order):
 *   1. A node is FEASIBLE for a pod if:
 *        - It has enough free cpu AND memory. Free = capacity minus the sum of
 *          requests of pods already assigned during this schedule() call.
 *        - Its labels contain every key=value pair in the pod's nodeSelector.
 *        - Every taint with effect "NoSchedule" is tolerated by the pod.
 *          A toleration matches a taint when their keys are equal AND the
 *          toleration either has no value field or its value equals the taint's.
 *          Taints with any other effect are ignored.
 *   2. Among feasible nodes, pick the one with the MOST free cpu.
 *      Break ties by list order (prefer the earlier node).
 *   3. If no node is feasible the pod maps to null.
 *
 * API:
 *   function schedule(pods: Pod[], nodes: KNode[]): Record<string, string | null>
 *       Returns { podName: nodeName | null } for every pod.
 *
 * This is an assessment-style challenge. Sample tests ship with this file, but
 * a hidden validation suite is the real grader. Write your own edge-case tests.
 */
export interface KNode {
  name: string;
  capacity: { cpu: number; memory: number };
  labels?: Record<string, string>;
  taints?: Array<{ key: string; value: string; effect: string }>;
}

export interface Pod {
  name: string;
  requests: { cpu: number; memory: number };
  nodeSelector?: Record<string, string>;
  tolerations?: Array<{ key: string; value?: string }>;
}

export function schedule(
  pods: Pod[],
  nodes: KNode[]
): Record<string, string | null> {
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// Sample tests — NOT exhaustive. Write your own before running validation.
// ---------------------------------------------------------------------------

function test_single_pod_fits(): void {
  const pods: Pod[] = [{ name: "p1", requests: { cpu: 500, memory: 512 } }];
  const nodes: KNode[] = [{ name: "node-a", capacity: { cpu: 2000, memory: 4096 } }];
  const result = schedule(pods, nodes);
  console.assert(result["p1"] === "node-a", "p1 should be scheduled on node-a");
}

function test_pod_too_big_is_unscheduled(): void {
  const pods: Pod[] = [{ name: "p1", requests: { cpu: 4000, memory: 512 } }];
  const nodes: KNode[] = [{ name: "node-a", capacity: { cpu: 2000, memory: 4096 } }];
  const result = schedule(pods, nodes);
  console.assert(result["p1"] === null, "p1 should be unschedulable");
}

function test_node_selector_filters(): void {
  const pods: Pod[] = [{
    name: "p1",
    requests: { cpu: 100, memory: 128 },
    nodeSelector: { zone: "west" },
  }];
  const nodes: KNode[] = [
    { name: "node-a", capacity: { cpu: 2000, memory: 4096 }, labels: { zone: "east" } },
    { name: "node-b", capacity: { cpu: 2000, memory: 4096 }, labels: { zone: "west" } },
  ];
  const result = schedule(pods, nodes);
  console.assert(result["p1"] === "node-b", "p1 should land on node-b (matching zone)");
}

// Run with: npx ts-node 10_podScheduler.ts
test_single_pod_fits();
test_pod_too_big_is_unscheduled();
test_node_selector_filters();
console.log("Sample tests passed! Now write more edge-case tests.");
