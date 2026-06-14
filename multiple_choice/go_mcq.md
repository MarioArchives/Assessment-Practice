# Go Multiple Choice Questions

---

**Q1.** What scheduling model does the Go runtime use for goroutines?

A) One OS thread per goroutine (1:1 threading)
B) N goroutines multiplexed onto M OS threads (M:N scheduling via the GMP model)
C) All goroutines run on a single OS thread using cooperative multitasking only
D) Goroutines are OS green threads managed directly by the kernel

---

**Q2.** What is the default initial stack size of a new goroutine, and what happens when the stack needs more space?

A) 8 MB — goroutines have fixed stacks matching OS thread defaults
B) 8 KB — the goroutine panics if the stack grows beyond this
C) 2 KB — the runtime allocates a larger contiguous stack, copies the old contents, and resumes
D) 512 bytes — the stack grows via linked segments chained together

---

**Q3.** What is printed?

```go
var ch = make(chan int)

func main() {
    close(ch)
    v, ok := <-ch
    fmt.Println(v, ok)
}
```

A) `0 true`
B) `0 false`
C) panic: send on closed channel
D) fatal error: all goroutines are asleep — deadlock

---

**Q4.** What is printed?

```go
func add(x, y int) int { return x + y }

func main() {
    x := 10
    defer fmt.Println(add(x, 5))
    x = 20
    fmt.Println("done")
}
```

A) `done` then `25`
B) `done` then `15`
C) `15` then `done`
D) `25` then `done`

---

**Q5.** Which statement about the Go memory model is correct?

A) Goroutines sharing a variable are safe as long as only one goroutine writes
B) A send on a channel happens before the corresponding receive from that channel completes
C) Memory writes in one goroutine are immediately visible in all other goroutines without synchronisation
D) Locks are unnecessary if the shared variable is only read after all goroutines are started

---

**Q6.** What is printed?

```go
func main() {
    s := []int{1, 2, 3}
    double(s)
    fmt.Println(s)
}

func double(s []int) {
    for i := range s {
        s[i] *= 2
    }
}
```

A) `[1 2 3]`
B) `[2 4 6]`
C) `[2 4 6]` only if the slice has extra capacity
D) panic: index out of range

---

**Q7.** What is the difference between a nil interface and a nil pointer stored in an interface?

A) They are identical; both evaluate to `nil` in an `if val == nil` check
B) A nil pointer stored in an interface is NOT nil because the interface has a non-nil type component
C) A nil pointer stored in an interface panics immediately on any method call
D) They are distinguishable only via reflection

---

**Q8.** What is printed?

```go
func main() {
    fns := make([]func(), 3)
    for i := 0; i < 3; i++ {
        i := i
        fns[i] = func() { fmt.Println(i) }
    }
    for _, fn := range fns {
        fn()
    }
}
```

A) `2 2 2`
B) `0 1 2`
C) `0 0 0`
D) undefined behaviour — data race

---

**Q9.** A goroutine is blocked trying to send to an unbuffered channel, but no other goroutine will ever receive from it. What happens?

A) The send times out after 30 seconds
B) The runtime detects this and panics with a deadlock error
C) The goroutine leaks — it stays blocked indefinitely, holding its stack memory
D) The runtime garbage-collects the blocked goroutine automatically

---

**Q10.** What is printed?

```go
func main() {
    m := map[string]int{"a": 1}
    fmt.Println(m["missing"])
    m["missing"]++
    fmt.Println(m["missing"])
}
```

A) panic: key not found, then panic again
B) `0` then `1`
C) `<nil>` then `1`
D) `0` then panic: assignment to nil map

---

**Q11.** What does `GOMAXPROCS` control?

A) The maximum number of goroutines that can exist simultaneously
B) The number of OS threads that can execute user-level Go code simultaneously
C) The number of CPU cores the Go process is allowed to use (set via cgroups)
D) The maximum size of the goroutine run queue before the scheduler blocks

---

**Q12.** What happens when you receive from a nil channel?

```go
var ch chan int
fmt.Println(<-ch)
```

A) Returns the zero value (0) immediately
B) panic: nil channel receive
C) Blocks forever
D) Returns 0 and false (like a closed channel)

---

**Q13.** Which statement about Go maps is correct?

A) Maps protect concurrent access internally; no external synchronisation is needed
B) Concurrent reads are safe, but any concurrent write combined with other accesses is a data race
C) `sync.Map` is a drop-in replacement and always preferred over a regular map with a mutex
D) `var m map[string]int; _ = m["key"]` panics because `m` is nil

---

**Q14.** What is printed?

```go
func main() {
    s := []int{1, 2, 3, 4, 5}
    a := s[1:3]
    b := append(a, 99)
    fmt.Println(s)
    fmt.Println(b)
}
```

A) `[1 2 3 4 5]` then `[2 3 99]`
B) `[1 2 3 99 5]` then `[2 3 99]`
C) `[1 2 3 4 5]` then `[2 3 4 99]`
D) `[1 2 99 4 5]` then `[2 3 99]`

---

**Q15.** What is the zero value of a `sync.Mutex`?

A) nil — it must be initialised with `sync.NewMutex()`
B) An unlocked mutex — usable without any initialisation
C) An indeterminate state — `mutex.Init()` must be called first
D) A locked mutex — `Unlock()` must be called before first use

---

**Q16.** What is printed?

```go
func f() (result int) {
    defer func() {
        result++
    }()
    return 0
}

func main() {
    fmt.Println(f())
}
```

A) `0`
B) `1`
C) `2`
D) compile error: deferred function cannot modify named return

---

**Q17.** A PR introduces this code. What is the bug?

```go
for _, item := range items {
    go func() {
        process(item)
    }()
}
```

A) `go func()` cannot be used inside a `range` loop
B) All goroutines will likely process the same (last) value of `item` due to closure capture
C) This creates too many goroutines and will exhaust memory
D) `process` should receive a pointer to `item` to avoid copying

---

**Q18.** What does `select` do when multiple cases are ready simultaneously?

A) Executes the first case listed (top-to-bottom priority)
B) panic: ambiguous channel select
C) Blocks until exactly one case is ready
D) Chooses one at random with uniform probability

---

**Q19.** `Cat` has `Sound()` defined with a pointer receiver. Which statement is correct?

```go
type Animal interface{ Sound() string }
type Cat struct{}
func (c *Cat) Sound() string { return "meow" }
```

A) Both `Cat{}` and `&Cat{}` satisfy the `Animal` interface
B) Only `&Cat{}` satisfies the `Animal` interface; `Cat{}` does not
C) `Cat{}` satisfies the interface only when passed by value to a function
D) Pointer receiver methods are automatically promoted to value receiver types at interface boundaries

---

**Q20.** What is printed?

```go
func main() {
    var wg sync.WaitGroup
    wg.Add(1)
    go func() {
        fmt.Println("goroutine")
        wg.Done()
    }()
    wg.Wait()
    fmt.Println("main")
}
```

A) Always `goroutine` then `main`
B) Always `main` then `goroutine`
C) Non-deterministic order
D) Deadlock

---

**Q21.** What is the purpose of `context.WithCancel`?

A) It sets a hard deadline on context-aware operations
B) It returns a derived context and a `cancel` function; calling `cancel()` signals all goroutines watching `ctx.Done()` to stop
C) It cancels the current goroutine immediately
D) It prevents panics from propagating to parent goroutines

---

**Q22.** What is printed?

```go
func main() {
    ch := make(chan int, 3)
    ch <- 1
    ch <- 2
    ch <- 3
    fmt.Println(len(ch), cap(ch))
}
```

A) `3 3`
B) `3 0`
C) `0 3`
D) panic: channel buffer full

---

**Q23.** What is the idiomatic Go pattern for a channel receive with a timeout?

A) `ch.receive(timeout: 5 * time.Second)`
B) Call `time.Sleep` before the receive
C) Use `select` with a `time.After` case
D) Use `context.WithDeadline` and check `ctx.Err()` after the receive

---

**Q24.** What is printed?

```go
package main

import "fmt"

var x = 1

func init() { x++ }
func init() { x++ }

func main() {
    fmt.Println(x)
}
```

A) `1`
B) `2`
C) `3`
D) compile error: multiple `init` functions in the same file

---

**Q25.** What is printed?

```go
func main() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("recovered:", r)
        }
    }()
    panic("oops")
    fmt.Println("unreachable")
}
```

A) `unreachable` then `recovered: oops`
B) `recovered: oops`
C) Program crashes with "oops"
D) compile error: unreachable code after `panic`

---

**Q26.** A PR introduces this code. What is the bug flagged by `go vet`?

```go
type Cache struct {
    mu   sync.Mutex
    data map[string]string
}

func (c Cache) Get(key string) string {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.data[key]
}
```

A) `sync.Mutex` cannot be embedded in a struct
B) `Get` takes a value receiver, so it copies the `Cache` including the mutex — a mutex-copy bug
C) `defer c.mu.Unlock()` is incorrect; unlock must be explicit, not deferred
D) The map must be initialised before `Get` is called

---

**Q27.** What does `go build -race` do?

A) Compiles without the race detector to maximise performance
B) Instruments the binary with the race detector, which reports data races at runtime
C) Runs the race detector as a static analysis pass without executing the program
D) Recompiles only packages that changed since the last build

---

**Q28.** What is printed?

```go
func main() {
    s := "hello"
    b := []byte(s)
    b[0] = 'H'
    fmt.Println(s, string(b))
}
```

A) `Hello Hello`
B) `hello hello`
C) `hello Hello`
D) panic: strings are immutable

---

**Q29.** What is printed?

```go
type Point struct{ X, Y int }

func (p Point) Scale(factor int) Point {
    return Point{p.X * factor, p.Y * factor}
}

func main() {
    p := Point{3, 4}
    p.Scale(2)
    fmt.Println(p)
}
```

A) `{6 8}`
B) `{3 4}`
C) compile error: Scale does not modify the receiver
D) `{0 0}`

---

**Q30.** What is printed?

```go
const (
    A = iota
    B
    C = iota * 2
    D
)

func main() {
    fmt.Println(A, B, C, D)
}
```

A) `0 1 2 3`
B) `0 1 4 6`
C) `0 1 4 8`
D) `0 0 4 6`

---

**Q31.** What happens when a goroutine panics and the panic is not recovered?

A) Only that goroutine terminates; all others continue running
B) The entire program terminates
C) The goroutine is silently restarted by the runtime
D) The panic propagates to the spawning goroutine via a channel

---

**Q32.** What is the idiomatic way to wrap an error with context in Go 1.13+, preserving the original for `errors.Is`/`errors.As`?

A) `return errors.New("context: " + err.Error())`
B) `return fmt.Errorf("context: %w", err)`
C) `return &WrappedError{msg: "context", cause: err}`
D) `return errors.Wrap(err, "context")`

---

**Q33.** A PR introduces this code. What is the bug?

```go
func process(items []string) {
    var wg sync.WaitGroup
    for _, item := range items {
        wg.Add(1)
        go func() {
            defer wg.Done()
            fmt.Println(item)
        }()
    }
    wg.Wait()
}
```

A) `wg.Wait()` must be called before goroutines are launched
B) All goroutines capture `item` by reference and may print the same (last) value
C) `wg.Done()` panics if called before `wg.Add(1)` in another goroutine
D) `fmt.Println` is not safe to call from multiple goroutines

---

**Q34.** What is printed?

```go
func main() {
    m := map[string][]int{}
    m["nums"] = append(m["nums"], 1)
    m["nums"] = append(m["nums"], 2)
    fmt.Println(m["nums"])
}
```

A) panic: append to nil slice
B) `[1]` (second append creates a new key)
C) `[1 2]`
D) `[2]` (second append overwrites the first)

---

**Q35.** What is printed?

```go
func main() {
    for i := 0; i < 3; i++ {
        defer fmt.Println(i)
    }
}
```

A) `0` `1` `2`
B) `2` `1` `0`
C) `2` `2` `2`
D) compile error: `defer` is not permitted inside a `for` loop

---

**Q36.** A reviewer raises a concern about this code. What is the issue?

```go
func worker(done <-chan struct{}) {
    for {
        select {
        case <-done:
            return
        case <-time.After(1 * time.Second):
            doWork()
        }
    }
}
```

A) `time.After` channels cannot be used in `select` statements
B) Each iteration creates a new timer whose channel is only GC'd after the full duration elapses, leaking resources in tight loops
C) The `done` channel should be `chan struct{}`, not a receive-only `<-chan struct{}`
D) `doWork()` will never be called because `done` always has priority

---

**Q37.** What is printed?

```go
type MyInt int

func (m MyInt) String() string {
    return fmt.Sprintf("MyInt(%d)", int(m))
}

func main() {
    var x MyInt = 42
    fmt.Println(x)
}
```

A) `42`
B) `MyInt(42)`
C) `{42}`
D) panic: infinite recursion in String()

---

**Q38.** What is printed?

```go
func swap(a, b *int) {
    *a, *b = *b, *a
}

func main() {
    x, y := 10, 20
    swap(&x, &y)
    fmt.Println(x, y)
}
```

A) `10 20`
B) `20 10`
C) `0 0`
D) compile error: cannot assign to multiple dereferenced pointers simultaneously

---

**Q39.** What is printed (and what is the synchronisation concern)?

```go
func main() {
    ch := make(chan int)
    go func() {
        for v := range ch {
            fmt.Println(v)
        }
        fmt.Println("done")
    }()
    ch <- 1
    ch <- 2
    close(ch)
    time.Sleep(10 * time.Millisecond)
}
```

A) `1` `2` are printed; "done" may or may not print before main returns
B) `1` `2` `done` are always printed in that order
C) Deadlock — `close(ch)` blocks
D) `1` `2` are printed; "done" is never reached

---

**Q40.** What does escape analysis do in the Go compiler?

A) Detects and removes unreachable code (dead code elimination)
B) Determines whether a variable can live on the goroutine's stack or must be heap-allocated
C) Tracks which objects have been promoted out of their goroutine's scope at runtime
D) Moves frequently accessed objects from heap to stack to reduce GC pressure

---

**Q41.** Which of the following Go types is NOT comparable with `==`?

A) `struct{ X, Y int }`
B) `[3]int`
C) `map[string]int`
D) `interface{}`

---

**Q42.** What does `sync.Once` guarantee?

A) A function runs at most once per goroutine
B) A function runs exactly once across all goroutines, even with concurrent calls to `Do`
C) A function is called once during package initialisation
D) A function is idempotent and safe to call any number of times

---

**Q43.** What is printed?

```go
func main() {
    a := [3]int{1, 2, 3}
    b := a
    b[0] = 99
    fmt.Println(a[0], b[0])
}
```

A) `99 99`
B) `1 99`
C) `1 1`
D) compile error: arrays are reference types

---

**Q44.** What is printed?

```go
func main() {
    s := []int{1, 2, 3}
    s2 := s[:2]
    s2 = append(s2, 99)
    fmt.Println(s)
}
```

A) `[1 2 3]`
B) `[1 2 99]`
C) `[1 99 3]`
D) `[99 2 3]`

---

**Q45.** A reviewer flags this code as a potential data race. Are they correct?

```go
func fetchAll(urls []string) []string {
    results := make([]string, len(urls))
    var wg sync.WaitGroup
    for i, url := range urls {
        wg.Add(1)
        go func(i int, url string) {
            defer wg.Done()
            results[i] = fetch(url)
        }(i, url)
    }
    wg.Wait()
    return results
}
```

A) Yes — multiple goroutines writing to the same slice is always a race
B) Yes — `results` must be protected by a mutex even when indices are distinct
C) No — writing to distinct indices of a slice from concurrent goroutines is safe; there is no bug here
D) Yes — `wg.Done()` and `wg.Wait()` do not provide the required memory ordering

---

**Q46.** What happens when this code runs?

```go
func main() {
    var mu sync.Mutex
    mu.Lock()
    mu.Lock()
    fmt.Println("done")
}
```

A) Prints "done" — Go mutexes are reentrant
B) Deadlock — `sync.Mutex` is not reentrant; the second `Lock()` blocks forever
C) panic: mutex already locked
D) The second `Lock()` is a no-op if the current goroutine already holds it

---

**Q47.** What is printed?

```go
func main() {
    for i := range []int{1, 2, 3} {
        fmt.Print(i, " ")
    }
}
```

A) `1 2 3 `
B) `0 1 2 `
C) compile error: range over slice requires two variables
D) `1 2 3` (no trailing space)

---

**Q48.** What is the purpose of the two-value form of a type assertion?

```go
v, ok := x.(T)
```

A) It discards the error message if the assertion fails
B) It makes the assertion non-panicking — if `x` is not of type `T`, `ok` is `false` instead of panicking
C) It casts `x` to `interface{}` before the assertion
D) The two-value and one-value forms are identical; `ok` is always `true`

---

**Q49.** What is printed?

```go
func main() {
    ch := make(chan struct{})
    go func() {
        time.Sleep(10 * time.Millisecond)
        close(ch)
    }()

    select {
    case <-ch:
        fmt.Println("channel closed")
    case <-time.After(1 * time.Second):
        fmt.Println("timeout")
    }
}
```

A) Always `timeout`
B) Always `channel closed`
C) Non-deterministic — either could print
D) Deadlock

---

**Q50.** Which statement about Go's garbage collector is correct?

A) It uses reference counting, similar to CPython
B) It is a concurrent tri-color mark-and-sweep collector that runs mostly alongside the application
C) It is a fully stop-the-world collector that freezes all goroutines for the entire GC cycle
D) It only runs when explicitly triggered by calling `runtime.GC()`
