import java.time.Duration;
import java.time.Instant;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Challenge 01 — Generic TTL Cache
 * ----------------------------------
 * Implement a generic, thread-safe cache where every entry expires after a
 * fixed duration.
 *
 * <p>API:
 * <pre>
 *   TTLCache(Duration ttl)
 *   void          put(K key, V value)   — stores value; resets TTL if key exists
 *   Optional&lt;V&gt;  get(K key)            — empty if absent or expired (lazy eviction)
 *   void          remove(K key)
 *   int           size()               — count of non-expired entries
 *   void          clear()
 * </pre>
 *
 * <p>Thread safety: all methods must be safe for concurrent use.
 *
 * <p>Lazy eviction: expired entries are removed on {@code get}. An optional
 * background sweep is allowed but not required.
 *
 * <p>Usage:
 * <pre>
 *   var cache = new TTLCache&lt;String, Integer&gt;(Duration.ofSeconds(5));
 *   cache.put("hits", 42);
 *   cache.get("hits"); // Optional.of(42)
 * </pre>
 */
public class TTLCache<K, V> {

    // your fields here

    public TTLCache(Duration ttl) {
        throw new UnsupportedOperationException("not implemented");
    }

    public void put(K key, V value) {
        throw new UnsupportedOperationException("not implemented");
    }

    public Optional<V> get(K key) {
        throw new UnsupportedOperationException("not implemented");
    }

    public void remove(K key) {
        throw new UnsupportedOperationException("not implemented");
    }

    public int size() {
        throw new UnsupportedOperationException("not implemented");
    }

    public void clear() {
        throw new UnsupportedOperationException("not implemented");
    }
}
