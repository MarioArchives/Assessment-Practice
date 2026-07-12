import java.util.function.Predicate;

/**
 * Challenge 02 — Retry with Exponential Backoff
 * -----------------------------------------------
 * Implement a {@code Retry} utility that re-runs a fallible supplier with
 * exponential backoff.
 *
 * <p>API:
 * <pre>
 *   static &lt;T&gt; T execute(ThrowingSupplier&lt;T&gt; task, RetryConfig config) throws Exception
 * </pre>
 *
 * <p>{@code ThrowingSupplier&lt;T&gt;} is a {@code @FunctionalInterface} that declares
 * {@code T get() throws Exception}.
 *
 * <p>RetryConfig (builder pattern):
 * <pre>
 *   maxAttempts(int n)                    default 3
 *   baseDelayMs(long ms)                  default 100
 *   retryOn(Predicate&lt;Exception&gt; p)       default: always retry
 * </pre>
 *
 * <p>Backoff formula: {@code baseDelayMs * 2^attempt} (0-indexed, so attempt 0
 * has no preceding delay, attempt 1 waits baseDelayMs, attempt 2 waits 2*baseDelayMs, …)
 *
 * <p>After all attempts are exhausted, throw the last exception.
 * If {@code retryOn} returns false, rethrow immediately without further retries.
 *
 * <p>Usage:
 * <pre>
 *   String result = Retry.execute(
 *       () -&gt; callRemoteApi(),
 *       Retry.RetryConfig.builder().maxAttempts(5).baseDelayMs(50).build()
 *   );
 * </pre>
 */
public class Retry {

    @FunctionalInterface
    public interface ThrowingSupplier<T> {
        T get() throws Exception;
    }

    public static class RetryConfig {
        // your fields here

        private RetryConfig() {}

        public static Builder builder() {
            return new Builder();
        }

        public static class Builder {
            // your fields here

            public Builder maxAttempts(int n) {
                throw new UnsupportedOperationException("not implemented");
            }

            public Builder baseDelayMs(long ms) {
                throw new UnsupportedOperationException("not implemented");
            }

            public Builder retryOn(Predicate<Exception> predicate) {
                throw new UnsupportedOperationException("not implemented");
            }

            public RetryConfig build() {
                throw new UnsupportedOperationException("not implemented");
            }
        }
    }

    public static <T> T execute(ThrowingSupplier<T> task, RetryConfig config) throws Exception {
        throw new UnsupportedOperationException("not implemented");
    }
}
