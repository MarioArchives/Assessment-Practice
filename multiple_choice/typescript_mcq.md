# TypeScript Multiple Choice Questions

---

**Q1.** Which calls compile?

```typescript
interface Point { x: number; y: number }
function dist(p: Point): number { return Math.hypot(p.x, p.y); }

const q = { x: 1, y: 2, z: 3 };
dist(q);                      // (1)
dist({ x: 1, y: 2, z: 3 });   // (2)
```

A) Both (1) and (2)
B) Only (1) — the literal in (2) fails the excess property check
C) Only (2) — `q` has a property not in `Point`
D) Neither

---

**Q2.** What is the key difference between `unknown` and `any`?

A) They are identical; `unknown` is just the newer alias
B) `unknown` values cannot be used until they are narrowed; `any` disables checking entirely
C) `any` can only hold primitives, `unknown` can hold objects
D) `unknown` is a runtime check, `any` is compile-time only

---

**Q3.** What JavaScript code does this emit after compilation?

```typescript
interface User {
    name: string;
    age: number;
}
```

A) A `User` class with two properties
B) An object literal `{ name: String, age: Number }`
C) Nothing — interfaces are erased at compile time
D) A `Symbol` registered under the name `"User"`

---

**Q4.** What is the type of `s` inside the `"circle"` case?

```typescript
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "square"; side: number };

function area(s: Shape): number {
    switch (s.kind) {
        case "circle":
            return Math.PI * s.radius ** 2;  // type of s here?
        case "square":
            return s.side ** 2;
    }
}
```

A) `Shape`
B) `{ kind: "circle"; radius: number }`
C) `{ kind: string; radius: number }`
D) `any` — switch statements do not narrow

---

**Q5.** What is the inferred type of `a`?

```typescript
const a = [1, 2] as const;
```

A) `number[]`
B) `(1 | 2)[]`
C) `readonly [1, 2]`
D) `[number, number]`

---

**Q6.** What does `Partial<T>` produce?

A) A type with only the properties of `T` that are objects
B) A type with all properties of `T` made optional
C) A type with all properties of `T` made nullable (`T | null`)
D) The first declared property of `T`

---

**Q7.** Given `interface User { id: number; name: string; email: string }`, which type has only `name` and `email`?

A) `Pick<User, "id">`
B) `Omit<User, "id">`
C) `Exclude<User, "id">`
D) `Partial<User>`

---

**Q8.** What does `Record<string, number>` describe?

A) A tuple of a string followed by a number
B) An object whose keys are strings and whose values are numbers
C) A Map instance with string keys
D) A database record with two columns

---

**Q9.** What is `keyof { a: string; b: number }`?

A) `string`
B) `"a" | "b"`
C) `["a", "b"]`
D) `string | number`

---

**Q10.** What does `typeof` do in a TYPE position?

```typescript
const config = { retries: 3, verbose: true };
type Config = typeof config;
```

A) `Config` is the string `"object"` (same as runtime typeof)
B) `Config` is `{ retries: number; verbose: boolean }`
C) It is a syntax error — typeof is only a runtime operator
D) `Config` is `object`

---

**Q11.** Which call fails to compile?

```typescript
function longest<T extends { length: number }>(a: T, b: T): T {
    return a.length >= b.length ? a : b;
}
```

A) `longest("alice", "bob")`
B) `longest([1, 2], [3])`
C) `longest(10, 20)`
D) `longest({ length: 5 }, { length: 7 })`

---

**Q12.** What is the conventional use of `never` in the `default` branch?

```typescript
function area(s: Shape): number {
    switch (s.kind) {
        case "circle": return Math.PI * s.radius ** 2;
        case "square": return s.side ** 2;
        default: {
            const _exhaustive: never = s;
            return _exhaustive;
        }
    }
}
```

A) It silences runtime errors in unreachable code
B) It makes the compiler error if a new `Shape` variant is added but not handled
C) It converts `s` to `null` safely
D) It marks the branch for dead-code elimination in the emitted JS

---

**Q13.** What is printed?

```typescript
console.log(0 ?? "fallback");
console.log(0 || "fallback");
```

A) `0` then `0`
B) `fallback` then `fallback`
C) `0` then `fallback`
D) `fallback` then `0`

---

**Q14.** What is printed?

```typescript
enum Direction { Up }
console.log(Direction.Up);
console.log(Direction[0]);
```

A) `0` then `Up`
B) `Up` then `0`
C) `undefined` then `Up`
D) `0` then `undefined`

---

**Q15.** Which statement about `interface` vs `type` is correct?

A) Only `type` aliases can describe object shapes
B) Two `interface` declarations with the same name merge; two same-name `type` aliases are an error
C) Interfaces exist at runtime, type aliases do not
D) `type` cannot be used with generics

---

**Q16.** What happens here?

```typescript
function sum(xs: readonly number[]): number {
    xs.push(0);
    return xs.reduce((a, b) => a + b, 0);
}
```

A) Compiles; `readonly` is documentation only
B) Compile error: `push` does not exist on `readonly number[]`
C) Runtime error: the array is frozen
D) Compiles, but `push` silently returns a copy

---

**Q17.** Given `type A = { a: string }` and `type B = { b: number }`, what is assignable to `A & B`?

A) Any object with `a` OR `b`
B) Only objects with BOTH `a: string` and `b: number`
C) Nothing — intersecting two different types is always `never`
D) Only the empty object `{}`

---

**Q18.** What is the return type of `f`?

```typescript
async function f() {
    return 1;
}
```

A) `number`
B) `Promise<number>`
C) `Awaited<number>`
D) `Promise<void>`

---

**Q19.** What makes this a "type guard"?

```typescript
function isFish(pet: Fish | Bird): pet is Fish {
    return (pet as Fish).swim !== undefined;
}
```

A) The `as Fish` cast inside the body
B) The `pet is Fish` return type, which narrows `pet` in code guarded by the call
C) The function name starting with `is`
D) Returning a boolean from a function always narrows its argument

---

**Q20.** With `strictNullChecks` enabled, which line fails to compile?

```typescript
let s: string = null;          // (1)
let t: string | null = null;   // (2)
```

A) Both
B) Neither
C) Only (1)
D) Only (2)

---

**Q21.** What does `satisfies` do here that a plain annotation would not?

```typescript
const palette = {
    red: [255, 0, 0],
    green: "#00ff00",
} satisfies Record<string, string | number[]>;

palette.green.toUpperCase();
```

A) Nothing — it is identical to `const palette: Record<string, string | number[]> = ...`
B) It checks the object against the type but keeps the narrower inferred types, so `.toUpperCase()` compiles
C) It performs a runtime validation of the object
D) It widens every property to `string | number[]`

---

**Q22.** What well-known utility type is this mapped type equivalent to?

```typescript
type X<T> = { [K in keyof T]?: T[K] };
```

A) `Readonly<T>`
B) `Required<T>`
C) `Partial<T>`
D) `Pick<T, keyof T>`

---

**Q23.** What is `type R = Exclude<"a" | "b" | "c", "a">`?

A) `"b" | "c"` — conditional types distribute over union members
B) `never` — the union does not extend `"a"`
C) `"a"`
D) `"a" | "b" | "c"` — Exclude only works on object types

---

**Q24.** Which statement about function overloads is correct?

```typescript
function parse(x: string): number;
function parse(x: number): string;
function parse(x: string | number): string | number {
    return typeof x === "string" ? Number(x) : String(x);
}
```

A) Callers may match any of the three signatures, including the implementation one
B) Callers can only match the two overload signatures; the implementation signature is not externally visible
C) Overloads are resolved at runtime by argument inspection
D) This is a compile error: overloads must have identical return types

---

**Q25.** What is the type of `x` after the `if` block?

```typescript
function f(x: string | number) {
    if (typeof x === "string") {
        return x.length;
    }
    // type of x here?
}
```

A) `string | number`
B) `string`
C) `number`
D) `unknown`

---

**Q26.** What are the inferred types of `s` and `c`?

```typescript
let s = "hello";
const c = "hello";
```

A) Both are `string`
B) `s` is `string` (widened), `c` is the literal type `"hello"`
C) Both are `"hello"`
D) `s` is `string`, `c` is `String`

---

**Q27.** What is `ClassName`?

```typescript
type Size = "small" | "large";
type ClassName = `btn-${Size}`;
```

A) `string`
B) `"btn-small" | "btn-large"`
C) `"btn-${Size}"` — a literal string containing the placeholder
D) A syntax error — template literals cannot appear in type position

---

**Q28.** What are `A` and `B`?

```typescript
type Unwrap<T> = T extends Promise<infer U> ? U : T;

type A = Unwrap<Promise<string>>;
type B = Unwrap<number>;
```

A) `A = string`, `B = number`
B) `A = Promise<string>`, `B = number`
C) `A = string`, `B = never`
D) `A = unknown`, `B = unknown`

---

**Q29.** What is `R`?

```typescript
function make() {
    return { id: 1, name: "x" };
}
type R = ReturnType<typeof make>;
```

A) `{ id: number; name: string }`
B) `object`
C) `make` — the function type itself
D) A compile error: `ReturnType` requires an explicit annotation on `make`

---

**Q30.** Which line fails to compile?

```typescript
let pair: [string, number] = ["a", 1];
pair[0].toUpperCase();   // (1)
pair[1].toFixed(2);      // (2)
pair = ["b"];            // (3)
```

A) (1) — tuple elements are `string | number`
B) (2) — `toFixed` does not exist on tuples
C) (3) — the tuple type requires exactly two elements
D) None; all three compile

---

**Q31.** What is the type of `r`?

```typescript
interface Opts {
    retries?: number;
}
function f(o: Opts) {
    const r = o.retries;
}
```

A) `number`
B) `number | undefined`
C) `number | null`
D) `Optional<number>`

---

**Q32.** What happens?

```typescript
function len(s?: string): number {
    return s!.length;
}
len(undefined);
```

A) Compile error: `s` may be undefined
B) Compiles; returns 0
C) Compiles, but throws a TypeError at runtime
D) Compile error: `!` cannot be applied to parameters

---

**Q33.** What is the type of `x` inside the `if` block?

```typescript
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function move(x: Fish | Bird) {
    if ("swim" in x) {
        // type of x here?
    }
}
```

A) `Fish | Bird`
B) `Fish`
C) `Bird`
D) `{ swim: unknown }`

---

**Q34.** Does this compile?

```typescript
const fn: () => void = () => 42;
```

A) No — the function returns `number`, not `void`
B) Yes — a `void` return type means the result is ignored, so returning a value is allowed
C) Only with `// @ts-ignore`
D) Yes, but calling `fn()` throws at runtime

---

**Q35.** Which statement about `private secret` vs `#secret` class fields is correct?

A) Both are enforced at runtime
B) `private` is a compile-time-only check; `#secret` is enforced at runtime by JavaScript itself
C) Both are erased and purely advisory
D) `#secret` is a TypeScript syntax error

---

**Q36.** What does the constructor parameter do?

```typescript
class User {
    constructor(private name: string) {}
}
const u = new User("ada");
```

A) Compile error: constructor parameters cannot have modifiers
B) Declares a property `name` AND assigns the argument to it — shorthand for declare + `this.name = name`
C) Creates a local variable only visible inside the constructor
D) Creates a static property shared by all instances

---

**Q37.** What happens?

```typescript
abstract class Base {
    abstract run(): void;
}
const b = new Base();
```

A) Compiles; `b.run` is `undefined`
B) Compile error: cannot create an instance of an abstract class
C) Runtime error only
D) Compiles only if `run` is given a default body

---

**Q38.** What is the type of `b.value`?

```typescript
interface Box<T = string> {
    value: T;
}
declare const b: Box;
```

A) `unknown`
B) `any`
C) `string` — the generic parameter defaults to `string`
D) Compile error: `Box` requires a type argument

---

**Q39.** What does a `const enum` compile to?

```typescript
const enum Level { Low, High }
const l = Level.High;
```

A) The same runtime object as a regular enum
B) Member accesses are inlined as literals (`const l = 1;`) and no enum object is emitted
C) A frozen object (`Object.freeze`)
D) A class with static readonly fields

---

**Q40.** What does `import type` do?

```typescript
import type { User } from "./models";
```

A) Imports the class lazily on first use
B) A type-only import: it is erased from the emitted JS, and using `User` as a runtime value is an error
C) Identical to a normal import
D) Imports the type and its runtime implementation under different names

---

**Q41.** Which assertion compiles?

```typescript
const n = "hello" as number;             // (1)
const m = "hello" as unknown as number;  // (2)
```

A) Both
B) Only (1)
C) Only (2) — going through `unknown` bypasses the overlap check
D) Neither

---

**Q42.** What is the type of `x`?

```typescript
declare const p: Promise<Promise<number>>;

async function f() {
    const x = await p;
}
```

A) `Promise<number>`
B) `number` — `await` unwraps nested promises recursively
C) `Promise<Promise<number>>`
D) `unknown`

---

**Q43.** Which line fails to compile?

```typescript
type Config = Readonly<{ nested: { value: number } }>;
declare const c: Config;

c.nested = { value: 1 };   // (1)
c.nested.value = 5;        // (2)
```

A) Both — `Readonly` is deep
B) Only (1) — `Readonly` is shallow, so nested objects stay mutable
C) Only (2)
D) Neither

---

**Q44.** What is `T`?

```typescript
type T = NonNullable<string | null | undefined>;
```

A) `string`
B) `string | null`
C) `string | undefined`
D) `never`

---

**Q45.** What is the type of `s` inside the `if` block?

```typescript
function f(s: string | null) {
    if (s) {
        // type of s here?
    }
}
```

A) `string | null`
B) `string` — truthiness narrowing removes `null`
C) A special "non-empty string" type, since `""` is falsy
D) `boolean`

---

**Q46.** What is `K`?

```typescript
enum Color { Red, Green }
type K = keyof typeof Color;
```

A) `number`
B) `Color`
C) `"Red" | "Green"`
D) `0 | 1`

---

**Q47.** Which assignment fails?

```typescript
const mixed = [1, "two", 3];
const a: (string | number)[] = mixed;   // (1)
const b: string[] | number[] = mixed;   // (2)
```

A) (1) — element order must match the union order
B) (2) — a mixed array is neither purely `string[]` nor purely `number[]`
C) Both
D) Neither

---

**Q48.** What does the `!` in `bar!: string` do?

```typescript
class Foo {
    bar!: string;
}
```

A) Makes `bar` non-nullable at runtime by throwing if unset
B) Definite assignment assertion: tells the compiler `bar` is initialised elsewhere, silencing the strict initialisation error; no runtime effect
C) Marks `bar` as required in object literals
D) It is a syntax error outside constructors

---

**Q49.** Does this compile?

```typescript
const handler: (a: number, b: number) => void = (a) => console.log(a);
```

A) No — the target type requires exactly two parameters
B) Yes — a function with FEWER parameters is assignable; extra arguments are simply ignored
C) Only if `b` is marked optional in the target type
D) No — arrow functions cannot be assigned to function types

---

**Q50.** What happens?

```typescript
class Dog { name = ""; }
class Cat { name = ""; }

const d: Dog = new Cat();
```

A) Compile error: `Cat` is not `Dog`
B) Compiles — classes are compared structurally, and the shapes are identical
C) Compiles only with `as Dog`
D) Runtime error: invalid cast
