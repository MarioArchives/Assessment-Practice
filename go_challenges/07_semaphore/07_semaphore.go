// Challenge 07 — Context-Aware Counting Semaphore
// ------------------------------------------------
// Implement a counting semaphore using a buffered channel (not sync.Mutex).
//
// API:
//
//	NewSemaphore(n int) *Semaphore
//	    Creates a semaphore with n permits.
//
//	(s *Semaphore) Acquire(ctx context.Context) error
//	    Blocks until a permit is available or ctx is cancelled/timed out.
//	    Returns ctx.Err() if the context is done before a permit is acquired.
//
//	(s *Semaphore) Release()
//	    Returns one permit. Panics if more permits are released than the
//	    semaphore was initialised with.
//
//	(s *Semaphore) TryAcquire() bool
//	    Acquires a permit without blocking. Returns false if none are available.
//
//	(s *Semaphore) Available() int
//	    Current number of available permits (a snapshot; may be stale).
//
// Implementation note:
//   Use a buffered channel of size n. Acquiring = sending into the channel;
//   releasing = receiving from the channel. This is idiomatic Go.
//
// Usage:
//
//	sem := NewSemaphore(3)
//	if err := sem.Acquire(ctx); err != nil {
//	    return err
//	}
//	defer sem.Release()

package main

import (
	"context"
)

type Semaphore struct {
	// your fields here
}

func NewSemaphore(n int) *Semaphore {
	panic("not implemented")
}

func (s *Semaphore) Acquire(ctx context.Context) error {
	panic("not implemented")
}

func (s *Semaphore) Release() {
	panic("not implemented")
}

func (s *Semaphore) TryAcquire() bool {
	panic("not implemented")
}

func (s *Semaphore) Available() int {
	panic("not implemented")
}

var _ context.Context

func main() {
	sem := NewSemaphore(2)
	ctx := context.Background()
	sem.Acquire(ctx)
	sem.Acquire(ctx)
	fmt.Println("acquired 2 permits")
	ok := sem.TryAcquire()
	fmt.Printf("TryAcquire (should be false): %v\n", ok)
	sem.Release()
	ok = sem.TryAcquire()
	fmt.Printf("TryAcquire after release (should be true): %v\n", ok)
}
