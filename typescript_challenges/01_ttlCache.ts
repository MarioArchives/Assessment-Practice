/**
 * Challenge 01 — Generic TTL Cache
 * ----------------------------------
 * Implement TTLCache<K, V>, a generic cache where every entry expires after
 * a fixed number of milliseconds.
 *
 * API:
 *   constructor(ttlMs: number)
 *   set(key: K, value: V): void       — stores value; resets TTL if key exists
 *   get(key: K): V | undefined        — undefined if absent or expired (lazy eviction)
 *   delete(key: K): boolean           — true if key existed and was removed
 *   size(): number                    — count of non-expired entries
 *   clear(): void
 *
 * Rules:
 *   - Lazy eviction: an expired entry is removed when get() is called for it.
 *   - size() must not count expired entries.
 *   - Thread safety is not required (single-threaded JS runtime).
 *
 * Usage:
 *   const cache = new TTLCache<string, number>(5_000);
 *   cache.set("hits", 42);
 *   cache.get("hits"); // 42
 *   // (after 5 seconds)
 *   cache.get("hits"); // undefined
 */
export class TTLCache<K, V> {
  constructor(private readonly ttlMs: number) {
    throw new Error("not implemented");
  }

  set(key: K, value: V): void {
    throw new Error("not implemented");
  }

  get(key: K): V | undefined {
    throw new Error("not implemented");
  }

  delete(key: K): boolean {
    throw new Error("not implemented");
  }

  size(): number {
    throw new Error("not implemented");
  }

  clear(): void {
    throw new Error("not implemented");
  }
}
