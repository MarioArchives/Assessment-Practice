// Challenge 09 — Fan-out / Fan-in Pipeline with Context    (suggested time: 35 min)
// ----------------------------------------------------------------------------------
// The canonical Go concurrency pattern: generate work on a channel, spread it
// across N goroutines (fan-out), then merge results back into one channel (fan-in).
// Everything respects context cancellation and must not leak goroutines.
//
// Implement three composable functions:
//
// ── Generate ─────────────────────────────────────────────────────────────────
//
//	func Generate[T any](ctx context.Context, items []T) <-chan T
//
//	Sends each item into the returned channel in a goroutine, then closes it.
//	Stops immediately if ctx is cancelled (never blocks on a full send).
//
// ── FanOut ───────────────────────────────────────────────────────────────────
//
//	func FanOut[T, R any](
//	    ctx     context.Context,
//	    in      <-chan T,
//	    workers int,
//	    fn      func(ctx context.Context, item T) R,
//	) []<-chan R
//
//	Starts `workers` goroutines. Each reads from `in`, calls fn, and sends
//	the result to its own output channel. Returns one channel per worker.
//	Each worker's channel closes when that worker exits.
//	Workers exit when `in` is closed or ctx is cancelled.
//
// ── Merge ────────────────────────────────────────────────────────────────────
//
//	func Merge[T any](ctx context.Context, channels ...<-chan T) <-chan T
//
//	Merges all input channels into one output channel using select.
//	The output channel closes when all inputs are drained or ctx is done.
//	Use a sync.WaitGroup + goroutine-per-input approach.
//
// ── Full pipeline usage ───────────────────────────────────────────────────────
//
//	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
//	defer cancel()
//
//	src     := Generate(ctx, []string{"a", "bb", "ccc"})
//	workers := FanOut(ctx, src, 3, func(ctx context.Context, s string) int {
//	    return len(s)
//	})
//	for n := range Merge(ctx, workers...) {
//	    fmt.Println(n) // prints 1, 2, 3 in some order
//	}
//
// Rules:
//   - No goroutine may leak after ctx is cancelled or all input is consumed.
//   - Result ordering may differ from input ordering.
//   - Cancelling ctx must cause all goroutines to exit promptly.
//   - Do not use errgroup or any third-party package.
//
// This is an assessment-style challenge. A few sample tests ship with this file,
// but a hidden validation suite (validation/) is the real grader.
// Write your own edge-case tests before checking the validation suite.

package main

import (
	"context"
	"sync"
)

// Generate sends each item from items into a new channel, then closes it.
// It stops early if ctx is cancelled.
func Generate[T any](ctx context.Context, items []T) <-chan T {
	panic("not implemented")
}

// FanOut spreads items from in across workers goroutines, applying fn to each.
// It returns one output channel per worker.
func FanOut[T, R any](
	ctx context.Context,
	in <-chan T,
	workers int,
	fn func(ctx context.Context, item T) R,
) []<-chan R {
	panic("not implemented")
}

// Merge combines multiple input channels into a single output channel.
func Merge[T any](ctx context.Context, channels ...<-chan T) <-chan T {
	panic("not implemented")
}

var _ sync.WaitGroup
var _ context.Context

func main() {
	ctx := context.Background()
	in := Generate(ctx, []int{1, 2, 3, 4, 5})
	results := FanIn(ctx, FanOut(ctx, in, 3, func(n int) int { return n * n })...)
	for r := range results {
		fmt.Println(r)
	}
}
