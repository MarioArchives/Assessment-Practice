import java.time.Duration;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Challenge 04 — Bounded Blocking Queue (from scratch)
 * -------------------------------------------------------
 * Implement a thread-safe bounded FIFO queue using {@link ReentrantLock} and
 * {@link Condition}. Do NOT use {@code java.util.concurrent.BlockingQueue} or
 * any concurrent collection as the backing store.
 *
 * <p>API:
 * <pre>
 *   BoundedQueue(int capacity)
 *   void put(T item, Duration timeout)
 *       throws InterruptedException, TimeoutException, QueueClosedException
 *       Blocks while full; inserts when space is available.
 *   T take(Duration timeout)
 *       throws InterruptedException, TimeoutException, QueueClosedException
 *       Blocks while empty; removes and returns the head when available.
 *   void close()
 *       Marks the queue closed. Subsequent put() throws QueueClosedException
 *       immediately. Pending take() drains remaining items, then throws
 *       QueueClosedException once the queue is empty.
 *   int size()
 *   boolean isEmpty()
 * </pre>
 *
 * <p>{@link QueueClosedException} must extend {@link RuntimeException}.
 *
 * <p>Usage:
 * <pre>
 *   var q = new BoundedQueue&lt;String&gt;(10);
 *   q.put("hello", Duration.ofSeconds(1));
 *   String s = q.take(Duration.ofSeconds(1));
 * </pre>
 */
public class BoundedQueue<T> {

    public static class QueueClosedException extends RuntimeException {
        public QueueClosedException() {
            super("Queue is closed");
        }
    }

    // your fields here

    public BoundedQueue(int capacity) {
        throw new UnsupportedOperationException("not implemented");
    }

    public void put(T item, Duration timeout)
            throws InterruptedException, TimeoutException {
        throw new UnsupportedOperationException("not implemented");
    }

    public T take(Duration timeout)
            throws InterruptedException, TimeoutException {
        throw new UnsupportedOperationException("not implemented");
    }

    public void close() {
        throw new UnsupportedOperationException("not implemented");
    }

    public int size() {
        throw new UnsupportedOperationException("not implemented");
    }

    public boolean isEmpty() {
        throw new UnsupportedOperationException("not implemented");
    }
}
