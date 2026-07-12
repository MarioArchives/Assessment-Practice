/**
 * Challenge 06 — Kubernetes Label Selector Parser
 * -------------------------------------------------
 * Implement a label selector matcher that supports the same syntax Kubernetes uses.
 *
 * Supported requirements (comma-separated, ALL must match):
 *   key=value  or  key==value  — equality
 *   key!=value                 — inequality
 *   key in (v1, v2, v3)        — set membership
 *   key notin (v1, v2, v3)     — set exclusion
 *   key                        — key must exist
 *   !key                       — key must NOT exist
 *
 * Rules:
 *   - Spaces around operators and commas are optional.
 *   - An empty selector string matches everything.
 *   - Commas separate requirements; all must be satisfied.
 *   - Throw SelectorSyntaxError for syntactically invalid selectors.
 *
 * API:
 *   function matches(labels: Record<string, string>, selector: string): boolean
 *   class SelectorSyntaxError extends Error
 *
 * Usage:
 *   matches({ env: "prod" }, "env=prod,!debug");           // true
 *   matches({ env: "dev"  }, "env in (prod, staging)");    // false
 *   matches({}, "");                                        // true
 */
export class SelectorSyntaxError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "SelectorSyntaxError";
  }
}

export function matches(
  labels: Record<string, string>,
  selector: string
): boolean {
  throw new Error("not implemented");
}
