// Challenge 06 — io.Reader / io.Writer Implementations
// -------------------------------------------------------
// io.Reader and io.Writer are Go's canonical small-interface examples.
// Almost everything in the standard library composes through them.
// Implement three types from scratch (do not call the stdlib equivalents).
//
// ── LimitReader ──────────────────────────────────────────────────────────────
//
//	type LimitReader struct { ... }
//	func NewLimitReader(r io.Reader, n int64) *LimitReader
//	func (lr *LimitReader) Read(p []byte) (int, error)
//
//	Wraps r; delivers at most n bytes total, then returns (0, io.EOF).
//	Partial reads are fine; reduce the remaining budget after each Read.
//	If the underlying reader returns EOF before n bytes, pass that through.
//
// ── TeeReader ────────────────────────────────────────────────────────────────
//
//	type TeeReader struct { ... }
//	func NewTeeReader(r io.Reader, w io.Writer) *TeeReader
//	func (tr *TeeReader) Read(p []byte) (int, error)
//
//	Wraps r; every byte successfully read is also written to w.
//	If Write returns fewer bytes than Read returned, return io.ErrShortWrite.
//	Errors from w are returned to the caller.
//
// ── RingBuffer ───────────────────────────────────────────────────────────────
//
//	type RingBuffer struct { ... }
//	func NewRingBuffer(capacity int) *RingBuffer
//	func (rb *RingBuffer) Write(p []byte) (int, error)
//	func (rb *RingBuffer) Read(p []byte)  (int, error)
//	func (rb *RingBuffer) Len() int          // bytes currently buffered
//	func (rb *RingBuffer) Cap() int          // total capacity
//
//	Fixed-capacity circular buffer satisfying both io.Reader and io.Writer.
//	Write: if len(p) > available space, return (0, ErrBufferFull).
//	       Writes are all-or-nothing — no partial writes.
//	Read:  copies available bytes into p; returns (0, io.EOF) when empty.
//
//	var ErrBufferFull = errors.New("ring buffer is full")
//
// Rules:
//   - Only import "errors" and "io". No other packages.
//   - Do not call io.LimitReader, io.TeeReader, or any ring-buffer from stdlib.

package main

import (
	"errors"
	"io"
)

// ErrBufferFull is returned by RingBuffer.Write when there is not enough space.
var ErrBufferFull = errors.New("ring buffer is full")

// ── LimitReader ──────────────────────────────────────────────────────────────

type LimitReader struct {
	// your fields here
}

func NewLimitReader(r io.Reader, n int64) *LimitReader {
	panic("not implemented")
}

func (lr *LimitReader) Read(p []byte) (int, error) {
	panic("not implemented")
}

// ── TeeReader ────────────────────────────────────────────────────────────────

type TeeReader struct {
	// your fields here
}

func NewTeeReader(r io.Reader, w io.Writer) *TeeReader {
	panic("not implemented")
}

func (tr *TeeReader) Read(p []byte) (int, error) {
	panic("not implemented")
}

// ── RingBuffer ───────────────────────────────────────────────────────────────

type RingBuffer struct {
	// your fields here
}

func NewRingBuffer(capacity int) *RingBuffer {
	panic("not implemented")
}

func (rb *RingBuffer) Write(p []byte) (int, error) {
	panic("not implemented")
}

func (rb *RingBuffer) Read(p []byte) (int, error) {
	panic("not implemented")
}

func (rb *RingBuffer) Len() int {
	panic("not implemented")
}

func (rb *RingBuffer) Cap() int {
	panic("not implemented")
}

var _ io.Reader = (*LimitReader)(nil)
var _ io.Reader = (*TeeReader)(nil)
var _ io.Reader = (*RingBuffer)(nil)
var _ io.Writer = (*RingBuffer)(nil)

func main() {
	src := strings.NewReader("hello world")
	lr := NewLimitReader(src, 5)
	buf := make([]byte, 10)
	n, _ := lr.Read(buf)
	fmt.Printf("LimitReader: %q\n", buf[:n])
}
