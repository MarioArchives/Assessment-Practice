// Challenge 01 — Generic TTL Cache
// ----------------------------------
// Implement TTLCache[K comparable, V any], a generic cache where each entry
// expires after a fixed duration.
//
// API:
//
//	NewTTLCache[K, V](ttl time.Duration) *TTLCache[K, V]
//
//	(c *TTLCache[K, V]) Set(key K, value V)
//	    Stores value under key. Resets the TTL if the key already exists.
//
//	(c *TTLCache[K, V]) Get(key K) (V, bool)
//	    Returns (value, true) if the key exists and has not expired.
//	    Returns (zero, false) otherwise. Expired entries are removed lazily.
//
//	(c *TTLCache[K, V]) Delete(key K)
//
//	(c *TTLCache[K, V]) Len() int
//	    Number of non-expired entries.
//
// Thread safety: Set, Get, Delete, and Len must be safe for concurrent use.
//
// Usage:
//
//	cache := NewTTLCache[string, int](5 * time.Second)
//	cache.Set("hits", 42)
//	v, ok := cache.Get("hits") // v=42, ok=true

package main

import (
	"sync"
	"time"
)

type TTLCache[K comparable, V any] struct {
	// your fields here
}

func NewTTLCache[K comparable, V any](ttl time.Duration) *TTLCache[K, V] {
	panic("not implemented")
}

func (c *TTLCache[K, V]) Set(key K, value V) {
	panic("not implemented")
}

func (c *TTLCache[K, V]) Get(key K) (V, bool) {
	panic("not implemented")
}

func (c *TTLCache[K, V]) Delete(key K) {
	panic("not implemented")
}

func (c *TTLCache[K, V]) Len() int {
	panic("not implemented")
}

// keep imports used
var (
	_ sync.RWMutex
	_ = time.Second
)

func main() {
	cache := NewTTLCache[string, int](2 * time.Second)
	cache.Set("a", 1)
	v, ok := cache.Get("a")
	fmt.Printf("Get a: %v, found: %v\n", v, ok)
	time.Sleep(3 * time.Second)
	v, ok = cache.Get("a")
	fmt.Printf("Get a after TTL: %v, found: %v\n", v, ok)
}
