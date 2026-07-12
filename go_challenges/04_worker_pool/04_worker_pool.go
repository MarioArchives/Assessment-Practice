// Challenge 04 — Generic Bounded Worker Pool
// -------------------------------------------
// Implement a worker pool that fans tasks out to a fixed number of goroutines
// and streams results back through a channel.
//
// API:
//
//	NewPool[T, R any](workers int, fn func(T) R) *WorkerPool[T, R]
//
//	(p *WorkerPool[T, R]) Submit(item T) error
//	    Enqueues item for processing.
//	    Returns ErrPoolClosed if Close has already been called.
//
//	(p *WorkerPool[T, R]) Results() <-chan R
//	    Returns the channel that receives all processed results.
//	    The channel is closed when all submitted work is done and the pool is closed.
//
//	(p *WorkerPool[T, R]) Close()
//	    Signals no more items will be submitted. Waits until all workers are idle,
//	    then closes the Results channel.
//
// Rules:
//   - `workers` goroutines start as soon as NewPool is called.
//   - Submit is non-blocking as long as the internal buffer has capacity.
//   - Calling Submit after Close must return ErrPoolClosed immediately.
//   - Results ordering may differ from submission order (workers run concurrently).
//
// Usage:
//
//	pool := NewPool[string, int](4, func(s string) int { return len(s) })
//	pool.Submit("hello")
//	pool.Submit("world")
//	pool.Close()
//	for r := range pool.Results() {
//	    fmt.Println(r)
//	}

package main

import (
	"errors"
	"sync"
)

// ErrPoolClosed is returned by Submit when the pool has been closed.
var ErrPoolClosed = errors.New("worker pool is closed")

type WorkerPool[T, R any] struct {
	// your fields here
}

func NewPool[T, R any](workers int, fn func(T) R) *WorkerPool[T, R] {
	panic("not implemented")
}

func (p *WorkerPool[T, R]) Submit(item T) error {
	panic("not implemented")
}

func (p *WorkerPool[T, R]) Results() <-chan R {
	panic("not implemented")
}

func (p *WorkerPool[T, R]) Close() {
	panic("not implemented")
}

var _ sync.WaitGroup

func main() {
	pool := NewPool[int, int](3, func(n int) int { return n * n })
	for i := 1; i <= 5; i++ {
		pool.Submit(i)
	}
	pool.Close()
	for r := range pool.Results() {
		fmt.Println(r)
	}
}
