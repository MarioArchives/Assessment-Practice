import java.util.concurrent.Callable;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;

/**
 * Challenge 03 — Circuit Breaker
 * --------------------------------
 * Implement the Circuit Breaker resilience pattern.
 *
 * <p>States:
 * <ul>
 *   <li>CLOSED    — normal operation; consecutive failures are counted</li>
 *   <li>OPEN      — calls immediately throw {@link CircuitOpenException}</li>
 *   <li>HALF_OPEN — one probe call is allowed through:
 *       success → CLOSED; failure → OPEN (restart timer)</li>
 * </ul>
 *
 * <p>Transitions:
 * <ul>
 *   <li>CLOSED → OPEN after {@code failureThreshold} consecutive failures</li>
 *   <li>OPEN → HALF_OPEN after {@code recoveryTimeoutMs} ms have elapsed</li>
 *   <li>HALF_OPEN → CLOSED on success</li>
 *   <li>HALF_OPEN → OPEN on failure</li>
 * </ul>
 * Any successful call resets the consecutive failure counter.
 *
 * <p>API:
 * <pre>
 *   CircuitBreaker(int failureThreshold, long recoveryTimeoutMs)
 *   &lt;T&gt; T call(Callable&lt;T&gt; fn) throws Exception
 *   State getState()
 * </pre>
 *
 * <p>Thread safety: {@code call} and {@code getState} must be safe for concurrent
 * use. Use {@link AtomicReference} and {@link AtomicInteger} for the state machine.
 *
 * <p>{@link CircuitOpenException} must extend {@link RuntimeException}.
 */
public class CircuitBreaker {

    public enum State { CLOSED, OPEN, HALF_OPEN }

    public static class CircuitOpenException extends RuntimeException {
        public CircuitOpenException() {
            super("Circuit breaker is OPEN");
        }
    }

    // your fields here

    public CircuitBreaker(int failureThreshold, long recoveryTimeoutMs) {
        throw new UnsupportedOperationException("not implemented");
    }

    public <T> T call(Callable<T> fn) throws Exception {
        throw new UnsupportedOperationException("not implemented");
    }

    public State getState() {
        throw new UnsupportedOperationException("not implemented");
    }
}
