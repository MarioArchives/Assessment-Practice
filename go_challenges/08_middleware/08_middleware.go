// Challenge 08 — HTTP Middleware Chain
// --------------------------------------
// http.Handler is Go's most ubiquitous interface. Middleware is the idiomatic
// way to compose cross-cutting concerns around handlers.
//
//	type Middleware func(http.Handler) http.Handler
//
// ── Chain ────────────────────────────────────────────────────────────────────
//
//	func Chain(middlewares ...Middleware) Middleware
//
//	Composes middlewares left-to-right so that the leftmost runs first:
//	    Chain(A, B, C)(h)  ≡  A(B(C(h)))
//	Chain with zero arguments returns an identity middleware.
//
// ── Logger ───────────────────────────────────────────────────────────────────
//
//	func Logger(log *log.Logger) Middleware
//
//	Logs one line per request after the handler returns:
//	    "<METHOD> <path> → <status> <duration>"
//	    e.g. "GET /api/pods → 200 1.23ms"
//
//	Must capture the actual status code written by the downstream handler.
//	Hint: wrap http.ResponseWriter with a small struct that intercepts
//	WriteHeader; default to 200 if WriteHeader is never called.
//
// ── Recovery ─────────────────────────────────────────────────────────────────
//
//	func Recovery(log *log.Logger) Middleware
//
//	Catches any panic from the downstream handler, logs the value and stack
//	trace, and writes http.StatusInternalServerError (500) to the client.
//	The server must not crash.
//
// ── MaxBodySize ───────────────────────────────────────────────────────────────
//
//	func MaxBodySize(n int64) Middleware
//
//	Replaces r.Body with http.MaxBytesReader(w, r.Body, n) before calling
//	next, so downstream handlers cannot read more than n bytes from the body.
//
// Usage:
//
//	mux := http.NewServeMux()
//	mux.HandleFunc("/", myHandler)
//	handler := Chain(
//	    Logger(log.Default()),
//	    Recovery(log.Default()),
//	    MaxBodySize(1 << 20),
//	)(mux)
//	http.ListenAndServe(":8080", handler)

package main

import (
	"log"
	"net/http"
	"runtime/debug"
	"time"
)

// Middleware wraps an http.Handler with additional behaviour.
type Middleware func(http.Handler) http.Handler

// Chain composes middlewares so that the leftmost runs outermost.
func Chain(middlewares ...Middleware) Middleware {
	panic("not implemented")
}

// Logger returns a Middleware that logs method, path, status, and duration.
func Logger(logger *log.Logger) Middleware {
	panic("not implemented")
}

// Recovery returns a Middleware that catches panics and returns 500.
func Recovery(logger *log.Logger) Middleware {
	panic("not implemented")
}

// MaxBodySize returns a Middleware that limits request body reads to n bytes.
func MaxBodySize(n int64) Middleware {
	panic("not implemented")
}

var _ = debug.Stack
var _ = time.Since

func main() {
	logger := log.New(os.Stdout, "", 0)
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	})
	chain := Chain(Logger(logger), Recoverer(logger))
	srv := httptest.NewServer(chain(handler))
	defer srv.Close()
	resp, _ := http.Get(srv.URL)
	fmt.Println("status:", resp.StatusCode)
}
