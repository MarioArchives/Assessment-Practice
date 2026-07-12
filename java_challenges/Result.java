import java.util.function.Function;

/**
 * Challenge 07 — Generic Result Type
 * -------------------------------------
 * Implement a {@code Result&lt;T, E&gt;} type (inspired by Rust's Result) using Java's
 * sealed interfaces and records.
 *
 * <p>Define:
 * <pre>
 *   sealed interface Result&lt;T, E&gt; permits Result.Ok, Result.Err
 *   record Ok&lt;T, E&gt;(T value)  implements Result&lt;T, E&gt;
 *   record Err&lt;T, E&gt;(E error) implements Result&lt;T, E&gt;
 * </pre>
 *
 * <p>Both must support:
 * <pre>
 *   boolean isOk()
 *   boolean isErr()
 *   T       unwrap()                — throws RuntimeException with error value if called on Err
 *   T       unwrapOr(T defaultVal)  — value if Ok, defaultVal if Err
 *   &lt;U&gt; Result&lt;U, E&gt; map(Function&lt;T, U&gt; fn)
 *       applies fn if Ok; passes Err through unchanged
 *   &lt;F&gt; Result&lt;T, F&gt; mapErr(Function&lt;E, F&gt; fn)
 *       applies fn if Err; passes Ok through unchanged
 *   &lt;U&gt; Result&lt;U, E&gt; flatMap(Function&lt;T, Result&lt;U, E&gt;&gt; fn)
 *       monadic bind: applies fn if Ok; passes Err through unchanged
 * </pre>
 *
 * <p>Factory helpers (static methods on Result):
 * <pre>
 *   static &lt;T, E&gt; Result&lt;T, E&gt; ok(T value)
 *   static &lt;T, E&gt; Result&lt;T, E&gt; err(E error)
 *   static &lt;T&gt;    Result&lt;T, Exception&gt; of(ThrowingSupplier&lt;T&gt; fn)
 *       Ok on success, Err on exception
 * </pre>
 *
 * <p>Usage:
 * <pre>
 *   Result&lt;Integer, String&gt; r = Result.ok(42);
 *   int doubled = r.map(x -&gt; x * 2).unwrapOr(0);
 * </pre>
 */
public sealed interface Result<T, E> permits Result.Ok, Result.Err {

    @FunctionalInterface
    interface ThrowingSupplier<T> {
        T get() throws Exception;
    }

    record Ok<T, E>(T value) implements Result<T, E> {
        @Override public boolean isOk()  { throw new UnsupportedOperationException("not implemented"); }
        @Override public boolean isErr() { throw new UnsupportedOperationException("not implemented"); }
        @Override public T unwrap()      { throw new UnsupportedOperationException("not implemented"); }
        @Override public T unwrapOr(T defaultVal) { throw new UnsupportedOperationException("not implemented"); }
        @Override public <U> Result<U, E> map(Function<T, U> fn) { throw new UnsupportedOperationException("not implemented"); }
        @Override public <F> Result<T, F> mapErr(Function<E, F> fn) { throw new UnsupportedOperationException("not implemented"); }
        @Override public <U> Result<U, E> flatMap(Function<T, Result<U, E>> fn) { throw new UnsupportedOperationException("not implemented"); }
    }

    record Err<T, E>(E error) implements Result<T, E> {
        @Override public boolean isOk()  { throw new UnsupportedOperationException("not implemented"); }
        @Override public boolean isErr() { throw new UnsupportedOperationException("not implemented"); }
        @Override public T unwrap()      { throw new UnsupportedOperationException("not implemented"); }
        @Override public T unwrapOr(T defaultVal) { throw new UnsupportedOperationException("not implemented"); }
        @Override public <U> Result<U, E> map(Function<T, U> fn) { throw new UnsupportedOperationException("not implemented"); }
        @Override public <F> Result<T, F> mapErr(Function<E, F> fn) { throw new UnsupportedOperationException("not implemented"); }
        @Override public <U> Result<U, E> flatMap(Function<T, Result<U, E>> fn) { throw new UnsupportedOperationException("not implemented"); }
    }

    boolean isOk();
    boolean isErr();
    T unwrap();
    T unwrapOr(T defaultVal);
    <U> Result<U, E> map(Function<T, U> fn);
    <F> Result<T, F> mapErr(Function<E, F> fn);
    <U> Result<U, E> flatMap(Function<T, Result<U, E>> fn);

    static <T, E> Result<T, E> ok(T value) {
        throw new UnsupportedOperationException("not implemented");
    }

    static <T, E> Result<T, E> err(E error) {
        throw new UnsupportedOperationException("not implemented");
    }

    static <T> Result<T, Exception> of(ThrowingSupplier<T> fn) {
        throw new UnsupportedOperationException("not implemented");
    }
}
