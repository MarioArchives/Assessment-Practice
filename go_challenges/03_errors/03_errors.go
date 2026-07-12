// Challenge 03 — Structured Errors with Is / As / Unwrap
// --------------------------------------------------------
// Go's error handling is built on a small set of conventions that let errors
// survive wrapping. This challenge drills them all.
//
// Define a base error type:
//
//	type APIError struct {
//	    Code    int
//	    Reason  string
//	    Message string
//	}
//	func (e *APIError) Error() string  // "status <code> <reason>: <message>"
//
// Define two typed errors that embed *APIError:
//
//	type NotFoundError struct{ *APIError }
//	type ConflictError  struct{ *APIError }
//
// Implement:
//
//	func NewNotFound(resource, name string) error
//	    Returns a *NotFoundError{Code:404, Reason:"NotFound",
//	    Message: `<resource> "<name>" not found`}
//
//	func NewConflict(resource, name string) error
//	    Returns a *ConflictError{Code:409, Reason:"Conflict",
//	    Message: `<resource> "<name>" already exists`}
//
//	func IsNotFound(err error) bool   // must use errors.As internally
//	func IsConflict(err error) bool
//
//	func Wrap(err error, msg string) error
//	    Returns fmt.Errorf("%s: %w", msg, err).
//	    Callers use this to add context while keeping the error unwrappable.
//
// Critical requirement: after multiple Wrap() layers, both errors.Is and
// errors.As must still reach the underlying typed error. For example:
//
//	err := Wrap(Wrap(NewNotFound("Pod", "nginx"), "get"), "reconcile")
//	IsNotFound(err)         // true
//	var nfe *NotFoundError
//	errors.As(err, &nfe)    // true; nfe.Code == 404
//
// Bonus: implement (e *APIError) Is(target error) bool so that
// errors.Is(err, &APIError{Code: 404}) is true for any 404 error
// regardless of wrapping.

package main

import (
	"errors"
	"fmt"
)

// APIError is the base structured error for API operations.
type APIError struct {
	Code    int
	Reason  string
	Message string
}

func (e *APIError) Error() string {
	panic("not implemented")
}

// NotFoundError wraps an APIError with Code 404.
type NotFoundError struct{ *APIError }

// ConflictError wraps an APIError with Code 409.
type ConflictError struct{ *APIError }

// NewNotFound returns a *NotFoundError for the given resource and name.
func NewNotFound(resource, name string) error {
	panic("not implemented")
}

// NewConflict returns a *ConflictError for the given resource and name.
func NewConflict(resource, name string) error {
	panic("not implemented")
}

// IsNotFound reports whether err (or any error in its chain) is a *NotFoundError.
func IsNotFound(err error) bool {
	panic("not implemented")
}

// IsConflict reports whether err (or any error in its chain) is a *ConflictError.
func IsConflict(err error) bool {
	panic("not implemented")
}

// Wrap adds msg as context around err while keeping err unwrappable.
func Wrap(err error, msg string) error {
	panic("not implemented")
}

var _ = errors.As
var _ = fmt.Errorf

func main() {
	err := NewNotFoundError(404, "Not Found", "user 42 not found")
	fmt.Println(err)
	var nfe *NotFoundError
	fmt.Printf("Is NotFoundError: %v\n", errors.As(err, &nfe))
}
