import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.function.Consumer;

/**
 * Challenge 05 — Typed Event Bus (Pub/Sub)
 * ------------------------------------------
 * Implement a type-safe publish/subscribe bus that dispatches events by their
 * runtime class.
 *
 * <p>API:
 * <pre>
 *   EventBus()
 *   &lt;T&gt; void subscribe(Class&lt;T&gt; eventType, Consumer&lt;T&gt; handler)
 *   &lt;T&gt; void unsubscribe(Class&lt;T&gt; eventType, Consumer&lt;T&gt; handler)
 *       Removes the first handler registered for that type with reference equality.
 *   void publish(Object event)
 *       Dispatches to all handlers whose registered type is assignable from
 *       the event's runtime class (supertype handlers receive subtype events).
 *       Handlers are called in subscription order.
 *   List&lt;Class&lt;?&gt;&gt; subscribedTypes()
 *       Returns a list of event types that have at least one handler, in
 *       registration order (no duplicates).
 * </pre>
 *
 * <p>Thread safety: all methods must be safe for concurrent use.
 *
 * <p>Usage:
 * <pre>
 *   record PodCreated(String name) {}
 *   var bus = new EventBus();
 *   bus.subscribe(PodCreated.class, e -&gt; System.out.println("Pod: " + e.name()));
 *   bus.publish(new PodCreated("nginx-abc"));
 * </pre>
 */
public class EventBus {

    // your fields here

    public EventBus() {
        throw new UnsupportedOperationException("not implemented");
    }

    public <T> void subscribe(Class<T> eventType, Consumer<T> handler) {
        throw new UnsupportedOperationException("not implemented");
    }

    public <T> void unsubscribe(Class<T> eventType, Consumer<T> handler) {
        throw new UnsupportedOperationException("not implemented");
    }

    public void publish(Object event) {
        throw new UnsupportedOperationException("not implemented");
    }

    public List<Class<?>> subscribedTypes() {
        throw new UnsupportedOperationException("not implemented");
    }
}
