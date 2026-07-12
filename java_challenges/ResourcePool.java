import java.time.Duration;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeoutException;
import java.util.function.Supplier;

/**
 * Challenge 06 — Generic Resource Pool
 * ---------------------------------------
 * Implement a generic, thread-safe resource pool that lends resources via a
 * try-with-resources pattern.
 *
 * <p>API:
 * <pre>
 *   ResourcePool(Supplier&lt;T&gt; factory, int size)
 *       Pre-creates {@code size} resources at construction time.
 *   Lease&lt;T&gt; acquire(Duration timeout) throws TimeoutException, InterruptedException
 *       Returns a Lease wrapping one resource. The lease is AutoCloseable;
 *       closing it returns the resource to the pool.
 * </pre>
 *
 * <p>Lease interface:
 * <pre>
 *   interface Lease&lt;T&gt; extends AutoCloseable {
 *       T resource();
 *       void close();  // returns resource to pool; idempotent
 *   }
 * </pre>
 *
 * <p>Rules:
 * <ul>
 *   <li>{@code acquire} blocks up to {@code timeout} if all resources are checked out.</li>
 *   <li>Closing a lease must return the resource even if an exception occurred.</li>
 *   <li>Closing a lease twice must be a no-op.</li>
 * </ul>
 *
 * <p>Usage:
 * <pre>
 *   var pool = new ResourcePool&lt;&gt;(() -&gt; createConnection(), 5);
 *   try (var lease = pool.acquire(Duration.ofSeconds(3))) {
 *       lease.resource().execute(query);
 *   }
 * </pre>
 */
public class ResourcePool<T> {

    public interface Lease<T> extends AutoCloseable {
        T resource();
        @Override
        void close();
    }

    // your fields here

    public ResourcePool(Supplier<T> factory, int size) {
        throw new UnsupportedOperationException("not implemented");
    }

    public Lease<T> acquire(Duration timeout)
            throws TimeoutException, InterruptedException {
        throw new UnsupportedOperationException("not implemented");
    }
}
