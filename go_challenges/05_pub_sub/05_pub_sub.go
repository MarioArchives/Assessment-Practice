// Challenge 05 — Pub/Sub Event Bus
// ----------------------------------
// Implement a synchronous, thread-safe publish/subscribe bus.
//
// API:
//
//	NewBus() *Bus
//
//	(b *Bus) Subscribe(topic string, handler func(msg any))
//
//	(b *Bus) Unsubscribe(topic string, handler func(msg any))
//	    Removes the FIRST registration whose handler has the same pointer.
//
//	(b *Bus) Publish(topic string, msg any)
//	    Calls all handlers registered for `topic` in subscription order.
//	    Also calls all handlers registered for the wildcard topic "*".
//	    Wildcard handlers are called with a [2]any{topic, msg} as the msg argument.
//
//	(b *Bus) Topics() []string
//	    Returns a sorted list of topics with at least one subscriber.
//	    The wildcard "*" is included if it has subscribers.
//
// Rules:
//   - Publishing to a topic with no subscribers is a no-op.
//   - Subscribing the same handler twice adds it twice (both fire on Publish).
//   - Thread safety: all methods must be safe for concurrent use.
//
// Usage:
//
//	bus := NewBus()
//	bus.Subscribe("pod.created", func(msg any) { fmt.Println(msg) })
//	bus.Publish("pod.created", "nginx-abc")

package main

import (
	"sort"
	"sync"
)

type Bus struct {
	// your fields here
}

func NewBus() *Bus {
	panic("not implemented")
}

func (b *Bus) Subscribe(topic string, handler func(msg any)) {
	panic("not implemented")
}

func (b *Bus) Unsubscribe(topic string, handler func(msg any)) {
	panic("not implemented")
}

func (b *Bus) Publish(topic string, msg any) {
	panic("not implemented")
}

func (b *Bus) Topics() []string {
	panic("not implemented")
}

var _ = sort.Strings
var _ sync.RWMutex

func main() {
	bus := NewBus()
	bus.Subscribe("greet", func(msg any) { fmt.Println("handler:", msg) })
	bus.Publish("greet", "hello world")
	fmt.Println("topics:", bus.Topics())
}
