/**
 * Challenge 08 — Generic Lazy Pipeline with Generators
 * -------------------------------------------------------
 * Implement Pipeline<T>, a generic wrapper around a lazy sequence that lets
 * you chain transformations. Nothing is evaluated until collect() is called
 * or you iterate with for...of.
 *
 * API:
 *   constructor(source: Iterable<T>)
 *   map<U>(fn: (x: T) => U): Pipeline<U>
 *   filter(pred: (x: T) => boolean): Pipeline<T>
 *   take(n: number): Pipeline<T>
 *   flatMap<U>(fn: (x: T) => Iterable<U>): Pipeline<U>
 *   collect(): T[]                         — evaluates the chain into an array
 *   [Symbol.iterator](): Iterator<T>       — enables for...of and spread
 *
 * Rules:
 *   - Each method returns a NEW Pipeline wrapping a generator — no intermediate arrays.
 *   - The source must not be consumed until iteration begins.
 *   - Chaining must be composable:
 *       new Pipeline([1, 2, 3, 4, 5, 6])
 *         .filter(x => x % 2 === 0)
 *         .map(x => x * 3)
 *         .take(2)
 *         .collect()  // [6, 12]
 *
 * Usage:
 *   // Infinite source — only first 5 even numbers are evaluated
 *   const result = new Pipeline(function*() {
 *     let i = 0; while (true) yield i++;
 *   }())
 *   .filter(x => x % 2 === 0)
 *   .take(5)
 *   .collect(); // [0, 2, 4, 6, 8]
 */
export class Pipeline<T> {
  constructor(source: Iterable<T>) {
    throw new Error("not implemented");
  }

  map<U>(fn: (x: T) => U): Pipeline<U> {
    throw new Error("not implemented");
  }

  filter(pred: (x: T) => boolean): Pipeline<T> {
    throw new Error("not implemented");
  }

  take(n: number): Pipeline<T> {
    throw new Error("not implemented");
  }

  flatMap<U>(fn: (x: T) => Iterable<U>): Pipeline<U> {
    throw new Error("not implemented");
  }

  collect(): T[] {
    throw new Error("not implemented");
  }

  [Symbol.iterator](): Iterator<T> {
    throw new Error("not implemented");
  }
}
