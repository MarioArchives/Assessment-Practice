/**
 * Challenge 05 — Typed Pub/Sub Event Bus
 * ----------------------------------------
 * Implement a fully type-safe publish/subscribe bus using a mapped-type
 * event registry so that handler payloads are checked at compile time.
 *
 * API:
 *   on<K extends keyof Events>(event: K, handler: (data: Events[K]) => void): void
 *   off<K extends keyof Events>(event: K, handler: (data: Events[K]) => void): void
 *       Removes the first matching handler (by reference equality).
 *   emit<K extends keyof Events>(event: K, data: Events[K]): void
 *       Calls all handlers for that event in subscription order.
 *   once<K extends keyof Events>(event: K, handler: (data: Events[K]) => void): void
 *       Like on(), but the handler fires at most once then auto-unsubscribes.
 *   listenerCount<K extends keyof Events>(event: K): number
 *
 * Rules:
 *   - Emitting to an event with no subscribers is a no-op.
 *   - Registering the same handler twice adds it twice (both fire on emit).
 *
 * Usage:
 *   interface AppEvents {
 *     "pod.created": { name: string };
 *     "pod.deleted": { name: string; reason: string };
 *   }
 *   const bus = new EventBus<AppEvents>();
 *   bus.on("pod.created", (data) => console.log(data.name)); // data is typed
 *   bus.emit("pod.created", { name: "nginx" });
 */
export class EventBus<Events extends Record<string, unknown>> {
  on<K extends keyof Events>(
    event: K,
    handler: (data: Events[K]) => void
  ): void {
    throw new Error("not implemented");
  }

  off<K extends keyof Events>(
    event: K,
    handler: (data: Events[K]) => void
  ): void {
    throw new Error("not implemented");
  }

  emit<K extends keyof Events>(event: K, data: Events[K]): void {
    throw new Error("not implemented");
  }

  once<K extends keyof Events>(
    event: K,
    handler: (data: Events[K]) => void
  ): void {
    throw new Error("not implemented");
  }

  listenerCount<K extends keyof Events>(event: K): number {
    throw new Error("not implemented");
  }
}
