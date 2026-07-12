/**
 * Challenge 09 — Kubernetes Manifest Differ               (suggested time: 30 min)
 * ----------------------------------------------------------------------------------
 * Implement diff() that returns a list of Change objects describing what changed
 * between two manifest objects.
 *
 * type ChangeKind = "added" | "removed" | "changed"
 *
 * interface Change {
 *   path: string;
 *   kind: ChangeKind;
 *   oldValue?: unknown;
 *   newValue?: unknown;
 * }
 *
 * function diff(
 *   oldManifest: Record<string, unknown>,
 *   newManifest: Record<string, unknown>,
 *   ignorePaths?: string[]
 * ): Change[]
 *
 * Rules:
 *   - Recurse into nested plain objects ({}). Array items are matched
 *     positionally by index.
 *   - Path format: dot-separated keys/indices, e.g. "spec.containers.0.image"
 *   - Detect "added" (key in new, absent from old), "removed" (absent from new),
 *     "changed" (key in both, non-object values differ).
 *   - When old[k] and new[k] are both plain objects, recurse instead of "changed".
 *   - Paths in ignorePaths are skipped entirely (no recursion past them).
 *   - Identical manifests return [].
 *   - Return changes sorted lexicographically by path.
 *
 * This is an assessment-style challenge. Sample tests ship with this file, but
 * a hidden validation suite is the real grader. Write your own edge-case tests.
 */
export type ChangeKind = "added" | "removed" | "changed";

export interface Change {
  path: string;
  kind: ChangeKind;
  oldValue?: unknown;
  newValue?: unknown;
}

export function diff(
  oldManifest: Record<string, unknown>,
  newManifest: Record<string, unknown>,
  ignorePaths: string[] = []
): Change[] {
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// Sample tests — NOT exhaustive. Write your own before running validation.
// ---------------------------------------------------------------------------

function test_no_changes(): void {
  const manifest = { apiVersion: "v1", kind: "Pod" };
  const result = diff(manifest, { ...manifest });
  console.assert(result.length === 0, "identical manifests should return []");
}

function test_added_key(): void {
  const result = diff({ a: 1 }, { a: 1, b: 2 });
  console.assert(result.length === 1 && result[0].kind === "added" && result[0].path === "b");
}

function test_removed_key(): void {
  const result = diff({ a: 1, b: 2 }, { a: 1 });
  console.assert(result.length === 1 && result[0].kind === "removed" && result[0].path === "b");
}

// Run with: npx ts-node 09_manifestDiffer.ts
test_no_changes();
test_added_key();
test_removed_key();
console.log("Sample tests passed! Now write more edge-case tests.");
