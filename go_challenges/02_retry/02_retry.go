// Challenge 02 — Retry with Exponential Backoff
// -----------------------------------------------
// Implement Retry[T any] that re-runs a fallible function with exponential backoff.
//
//	func Retry[T any](fn func() (T, error), opts ...RetryOption) (T, error)
//
// Default behaviour (no options):
//   - Max 3 attempts
//   - Base delay 100 ms, doubles each retry: 100 ms, 200 ms, 400 ms, …
//   - Retries on any non-nil error
//   - Returns the zero value and the last error after all attempts are exhausted
//
// Options (functional-options pattern):
//
//	WithMaxAttempts(n int) RetryOption
//	WithBaseDelay(d time.Duration) RetryOption
//	WithRetryOn(pred func(error) bool) RetryOption
//	    Only retry when pred(err) returns true; propagate other errors immediately.
//
// Usage:
//
//	result, err := Retry(callAPI,
//	    WithMaxAttempts(5),
//	    WithBaseDelay(50*time.Millisecond),
//	)

package main

import (
	"time"
)

// RetryOption is a functional option for Retry.
type RetryOption func(*retryConfig)

type retryConfig struct {
	// your fields here
}

func WithMaxAttempts(n int) RetryOption {
	panic("not implemented")
}

func WithBaseDelay(d time.Duration) RetryOption {
	panic("not implemented")
}

func WithRetryOn(pred func(error) bool) RetryOption {
	panic("not implemented")
}

// Retry calls fn up to the configured number of times, sleeping between attempts.
func Retry[T any](fn func() (T, error), opts ...RetryOption) (T, error) {
	panic("not implemented")
}

var _ = time.Millisecond

func main() {
	attempts := 0
	result, err := Retry(func() (string, error) {
		attempts++
		if attempts < 3 {
			return "", fmt.Errorf("transient error")
		}
		return "success", nil
	}, WithMaxAttempts(5))
	fmt.Printf("result: %v, err: %v, attempts: %d\n", result, err, attempts)
}
