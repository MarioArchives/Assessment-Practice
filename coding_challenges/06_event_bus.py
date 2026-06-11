"""
Challenge 6 — Synchronous Event Bus (Pub/Sub)
----------------------------------------------
Implement a simple publish/subscribe event bus.

Requirements:
  - subscribe(event, handler)   — register a handler for a named event
  - unsubscribe(event, handler) — remove a specific handler
  - publish(event, *args, **kwargs) — invoke all handlers for that event
  - Handlers are called in subscription order
  - Handlers registered with the special event name "*" receive ALL events;
    they are called as handler(event_name, *args, **kwargs)
  - Publishing to an event with no subscribers is a no-op (no exception)
  - Subscribing the same handler twice for the same event adds it twice
    (and both registrations receive the event)

Usage:
    bus = EventBus()
    bus.subscribe("pod.created", lambda name: print(f"Pod {name} created"))
    bus.publish("pod.created", "nginx-abc")
"""

from typing import Any, Callable


class EventBus:
    def __init__(self) -> None:
        self.events = {}

    def subscribe(self, event: str, handler: Callable) -> None:
        if "*" in self.events.keys():
            self.events["*"].append(handler)

        if event in self.events.keys():
            self.events[event].append(handler)
        else:
            self.events[event] = [handler]

    def unsubscribe(self, event: str, handler: Callable) -> None:
        if event in self.events.keys():
            new_handler_list = []
            for handler_idx in range(len(self.events[event])):
                if self.events[event][handler_idx] != handler:
                    new_handler_list.append(self.events[event][handler_idx])
            self.events[event] = new_handler_list

    def publish(self, event: str, *args: Any, **kwargs: Any) -> None:
        if event in self.events.keys():
            for handler in self.events[event]:
                handler(*args, **kwargs)
        if "*" in self.events.keys():
            for handler in self.events["*"]:
                handler(event, *args, **kwargs)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_basic_subscribe_and_publish():
    bus = EventBus()
    received = []
    bus.subscribe("ping", lambda x: received.append(x))
    bus.publish("ping", 42)
    assert received == [42]


def test_multiple_handlers_called_in_order():
    bus = EventBus()
    log = []
    bus.subscribe("ev", lambda: log.append("first"))
    bus.subscribe("ev", lambda: log.append("second"))
    bus.publish("ev")
    assert log == ["first", "second"]


def test_unsubscribe_removes_handler():
    bus = EventBus()
    log = []
    handler = lambda: log.append("x")
    bus.subscribe("ev", handler)
    bus.unsubscribe("ev", handler)
    bus.publish("ev")
    assert log == []


def test_publish_with_no_subscribers_is_noop():
    bus = EventBus()
    bus.publish("ghost_event", "arg")  # must not raise


def test_wildcard_receives_all_events():
    bus = EventBus()
    received = []
    bus.subscribe("*", lambda event, val: received.append((event, val)))
    bus.publish("click", 1)
    bus.publish("hover", 2)
    assert ("click", 1) in received
    assert ("hover", 2) in received


def test_wildcard_and_specific_handler_both_fire():
    bus = EventBus()
    log = []
    bus.subscribe("start", lambda: log.append("specific"))
    bus.subscribe("*", lambda ev: log.append(f"wildcard:{ev}"))
    bus.publish("start")
    assert "specific" in log
    assert "wildcard:start" in log


def test_kwargs_forwarded():
    bus = EventBus()
    received = {}
    bus.subscribe("cfg", lambda **kw: received.update(kw))
    bus.publish("cfg", key="value")
    assert received == {"key": "value"}


if __name__ == "__main__":
    test_basic_subscribe_and_publish()
    test_multiple_handlers_called_in_order()
    test_unsubscribe_removes_handler()
    test_publish_with_no_subscribers_is_noop()
    test_wildcard_receives_all_events()
    test_wildcard_and_specific_handler_both_fire()
    test_kwargs_forwarded()
    print("All tests passed!")
