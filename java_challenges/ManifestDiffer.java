import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Challenge 09 — Kubernetes Manifest Differ               (suggested time: 30 min)
 * ----------------------------------------------------------------------------------
 * Implement {@code diff} that returns a list of {@link Change} objects describing
 * what changed between two manifest maps.
 *
 * <p>Types:
 * <pre>
 *   enum ChangeKind { ADDED, REMOVED, CHANGED }
 *   record Change(String path, ChangeKind kind, Object oldValue, Object newValue)
 * </pre>
 *
 * <p>API:
 * <pre>
 *   List&lt;Change&gt; diff(Map&lt;String, Object&gt; oldManifest,
 *                      Map&lt;String, Object&gt; newManifest,
 *                      Set&lt;String&gt; ignorePaths)
 * </pre>
 *
 * <p>Rules:
 * <ul>
 *   <li>Recurse into nested {@code Map&lt;String, Object&gt;}; List items are matched
 *       positionally by index.</li>
 *   <li>Path format: dot-separated keys/indices, e.g. {@code "spec.containers.0.image"}.</li>
 *   <li>Detect ADDED (key in new, absent from old), REMOVED (absent from new),
 *       CHANGED (key in both, non-map values differ).</li>
 *   <li>When old[k] and new[k] are both {@code Map&lt;String, Object&gt;}, recurse instead
 *       of emitting CHANGED.</li>
 *   <li>Paths in {@code ignorePaths} are skipped entirely (no recursion past them).</li>
 *   <li>Identical manifests return an empty list.</li>
 *   <li>Return changes sorted lexicographically by path.</li>
 * </ul>
 *
 * <p>This is an assessment-style challenge. Sample tests ship with this file, but
 * a hidden validation suite is the real grader. Write your own edge-case tests.
 */
public class ManifestDiffer {

    public enum ChangeKind { ADDED, REMOVED, CHANGED }

    public record Change(String path, ChangeKind kind, Object oldValue, Object newValue) {}

    public List<Change> diff(
            Map<String, Object> oldManifest,
            Map<String, Object> newManifest,
            Set<String> ignorePaths) {
        throw new UnsupportedOperationException("not implemented");
    }

    // ---------------------------------------------------------------------------
    // Sample tests — NOT exhaustive. Write your own before running validation.
    // ---------------------------------------------------------------------------
}
