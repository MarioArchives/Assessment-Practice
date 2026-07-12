/**
 * Challenge 07 — Result<T, E> Discriminated Union
 * -------------------------------------------------
 * Implement a Result type for explicit error handling without exceptions.
 *
 * Types:
 *   type Result<T, E> = OkResult<T, E> | ErrResult<T, E>
 *
 * Both variants must carry these methods:
 *   isOk(): this is OkResult<T, E>
 *   isErr(): this is ErrResult<T, E>
 *   unwrap(): T                         — throws if called on ErrResult
 *   unwrapOr(defaultValue: T): T        — value if Ok, defaultValue if Err
 *   map<U>(fn: (value: T) => U): Result<U, E>
 *       applies fn if Ok; passes Err through unchanged
 *   mapErr<F>(fn: (error: E) => F): Result<T, F>
 *       applies fn if Err; passes Ok through unchanged
 *   flatMap<U>(fn: (value: T) => Result<U, E>): Result<U, E>
 *       monadic bind: applies fn if Ok; passes Err through unchanged
 *
 * Factory helpers:
 *   function ok<T, E = never>(value: T): Result<T, E>
 *   function err<E, T = never>(error: E): Result<T, E>
 *   function tryCatch<T>(fn: () => T): Result<T, unknown>
 *       wraps a throwing fn: Ok on success, Err(caught) on throw
 *
 * Usage:
 *   const r = ok<number, string>(42).map(x => x * 2);  // Ok(84)
 *   const e = err<string, number>("oops").mapErr(s => s.length); // Err(4)
 *   tryCatch(() => JSON.parse("bad")).isErr(); // true
 */
export interface OkResult<T, E> {
  readonly ok: true;
  readonly value: T;
  isOk(): this is OkResult<T, E>;
  isErr(): this is ErrResult<T, E>;
  unwrap(): T;
  unwrapOr(defaultValue: T): T;
  map<U>(fn: (value: T) => U): Result<U, E>;
  mapErr<F>(fn: (error: E) => F): Result<T, F>;
  flatMap<U>(fn: (value: T) => Result<U, E>): Result<U, E>;
}

export interface ErrResult<T, E> {
  readonly ok: false;
  readonly error: E;
  isOk(): this is OkResult<T, E>;
  isErr(): this is ErrResult<T, E>;
  unwrap(): T;
  unwrapOr(defaultValue: T): T;
  map<U>(fn: (value: T) => U): Result<U, E>;
  mapErr<F>(fn: (error: E) => F): Result<T, F>;
  flatMap<U>(fn: (value: T) => Result<U, E>): Result<U, E>;
}

export type Result<T, E> = OkResult<T, E> | ErrResult<T, E>;

export function ok<T, E = never>(value: T): Result<T, E> {
  throw new Error("not implemented");
}

export function err<E, T = never>(error: E): Result<T, E> {
  throw new Error("not implemented");
}

export function tryCatch<T>(fn: () => T): Result<T, unknown> {
  throw new Error("not implemented");
}
