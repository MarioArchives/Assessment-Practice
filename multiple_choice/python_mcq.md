# Python Multiple Choice Questions

---

**Q1.** What is printed?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

A) `[1, 2, 3]`
B) `[1, 2, 3, 4]`
C) `TypeError`
D) `None`

---

**Q2.** What is the output?

```python
def foo(items=[]):
    items.append(1)
    return items

print(foo())
print(foo())
```

A) `[1]` then `[1]`
B) `[1]` then `[1, 1]`
C) `[1, 1]` then `[1, 1, 1]`
D) `TypeError`

---

**Q3.** Which statement about the GIL is correct?

A) The GIL prevents all parallelism in Python programs
B) The GIL is released during CPU-bound operations, enabling true parallelism
C) The GIL is released during I/O-bound operations, so threads can overlap on I/O
D) The GIL only applies to CPython extension modules

---

**Q4.** What does `yield from iterable` do inside a generator?

A) Returns the iterable directly from the generator function
B) Delegates iteration to the sub-iterable, yielding each of its values
C) Flattens nested iterables one level deep and stores them
D) It is equivalent to `return iterable`

---

**Q5.** What is the output?

```python
a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)
```

A) `True` then `True`
B) `True` then `False`
C) `False` then `False`
D) Implementation-defined for both

---

**Q6.** Which of the following correctly uses `nonlocal`?

```python
def outer():
    x = 10
    def inner():
        ???
        x += 1
    inner()
    return x
```

A) `global x`
B) `nonlocal x`
C) No keyword needed; assignments propagate outward automatically
D) `extern x`

---

**Q7.** What is the difference between `__str__` and `__repr__`?

A) `__repr__` is for human-readable display; `__str__` is for debugging
B) `__str__` is for human-readable display; `__repr__` is for unambiguous, ideally eval-able representation
C) They are identical; only naming convention differs
D) `__repr__` is only called when printing collections that contain the object

---

**Q8.** What is the output?

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B" + super().method()

class C(A):
    def method(self):
        return "C" + super().method()

class D(B, C):
    pass

print(D().method())
```

A) `BA`
B) `BCA`
C) `BCBA`
D) `TypeError`

---

**Q9.** Which line raises a `TypeError` at runtime?

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def f(x):
    return x * 2

f(1)         # line A
f([1, 2])    # line B
f((1, 2))    # line C
f("hello")   # line D
```

A) Line A
B) Line B
C) Line C
D) Line D

---

**Q10.** What does `__slots__` do when defined in a class?

A) Restricts attribute access to only those listed, preventing `__dict__` creation
B) Pre-allocates memory for all instances at class definition time
C) Makes all listed attributes read-only
D) Enables pickling of instances that would otherwise fail

---

**Q11.** What is the output?

```python
gen = (x * 2 for x in range(5))
print(list(gen))
print(list(gen))
```

A) `[0, 2, 4, 6, 8]` then `[0, 2, 4, 6, 8]`
B) `[0, 2, 4, 6, 8]` then `[]`
C) `[0, 2, 4, 6, 8]` then `TypeError`
D) Both print `[]`

---

**Q12.** What is printed?

```python
try:
    raise ValueError("original") from TypeError("cause")
except ValueError as e:
    print(type(e.__cause__))
```

A) `<class 'NoneType'>`
B) `<class 'TypeError'>`
C) `<class 'ValueError'>`
D) `AttributeError`

---

**Q13.** Which statement about `asyncio.gather` vs `asyncio.wait` is correct?

A) `gather` returns results in completion order; `wait` returns them in submission order
B) `gather` preserves input order in its results; `wait` returns sets of done/pending tasks
C) Only `wait` can be cancelled; `gather` runs to completion regardless
D) They are interchangeable; the choice is purely stylistic

---

**Q14.** What is the output?

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 10
print(p.x)
```

A) `10`
B) `1`
C) `FrozenInstanceError`
D) `AttributeError`

---

**Q15.** In the descriptor protocol, which method is called when an attribute is **read** from an instance?

A) `__set__`
B) `__get__`
C) `__getattr__`
D) `__access__`

---

**Q16.** What does the walrus operator (`:=`) do that a regular assignment cannot?

A) Assigns a value and evaluates to that value within an expression
B) Performs type-checked assignment
C) Assigns to multiple targets simultaneously
D) Creates a new scope for the assigned variable

---

**Q17.** What is the output?

```python
d = {}
d[1] = "one"
d[2] = "two"
d[1] = "ONE"
print(list(d.keys()))
```

A) `[1, 2, 1]`
B) `[2, 1]`
C) `[1, 2]`
D) `{1, 2}` (unordered)

---

**Q18.** What is the time and space complexity of `in` for a Python `list` vs `set`?

A) Both O(1) time, O(n) space
B) `list`: O(n) time; `set`: O(1) average time
C) Both O(log n) time
D) `list`: O(1) time; `set`: O(n) time

---

**Q19.** Which of the following correctly makes `MyClass` a context manager?

A) Implementing `__enter__` and `__exit__`
B) Implementing `__open__` and `__close__`
C) Inheriting from `contextlib.AbstractContextManager` only
D) Implementing `__with__`

---

**Q20.** What is printed?

```python
import threading

results = []

def task(n):
    results.append(n)

threads = [threading.Thread(target=task, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(len(results))
```

A) Always `5`
B) Between `0` and `5`, non-deterministic
C) Always `0`
D) `5`, but the values in `results` are non-deterministic

---

**Q21.** What does `__new__` do that `__init__` does not?

A) Creates and returns the new instance object
B) Initialises the instance attributes after the object is created
C) Is only called for subclasses, not for the base class
D) Is the destructor called when the object is garbage-collected

---

**Q22.** What is the output?

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(3))
```

A) `6`
B) `9`
C) `TypeError`
D) `8`

---

**Q23.** `copy.copy(obj)` vs `copy.deepcopy(obj)` — which statement is correct?

A) `deepcopy` only copies one level of nesting
B) Both produce fully independent copies of all nested objects
C) `copy` is a shallow copy; nested objects are still shared with the original
D) `copy` and `deepcopy` are identical for all mutable types

---

**Q24.** What is the output?

```python
x = 10
def f():
    print(x)
    x = 20
f()
```

A) `10`
B) `20`
C) `NameError`
D) `UnboundLocalError`

---

**Q25.** What does `typing.Optional[str]` mean?

A) The value can be `str` or `None`
B) The argument is keyword-only and need not be supplied
C) The type hint is explicitly marked as unenforced
D) The value can be any type

---

**Q26.** Is Python's `sorted()` sort stable?

A) No — equal elements may be reordered arbitrarily
B) Yes — equal elements preserve their original relative order (TimSort guarantee)
C) Only when sorting primitive types like `int` and `str`
D) Only when a `key=` function is provided

---

**Q27.** What is the key difference between `@staticmethod` and `@classmethod`?

A) `@staticmethod` receives the class as its first argument
B) They are identical; the choice is purely stylistic
C) `@classmethod` receives the class (`cls`) as its first argument; `@staticmethod` receives no implicit first argument
D) `@classmethod` can only be defined on abstract base classes

---

**Q28.** What is printed?

```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        namespace['greeting'] = 'hello'
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=Meta):
    pass

print(MyClass.greeting)
```

A) `AttributeError`
B) `Meta`
C) `None`
D) `hello`

---

**Q29.** What does `isinstance(x, T)` return that `type(x) == T` does not?

A) `True` when `x` is an instance of a subclass of `T`
B) `True` only for the exact type `T`, never subclasses
C) `True` when `x` is `None`
D) `True` for abstract base classes only

---

**Q30.** Which exception is the base class for all built-in non-system-exiting exceptions?

A) `BaseException`
B) `Exception`
C) `RuntimeError`
D) `StandardError`

---

**Q31.** What is the output?

```python
def gen():
    yield 1
    yield 2

g = gen()
print(next(g))
print(next(g))
print(next(g))
```

A) `1`, `2`, `None`
B) `1`, `2`, `1` (cycles back)
C) `1`, `2`, then raises `StopIteration`
D) `1`, `2`, `0`

---

**Q32.** In `@dataclass`, when is `__post_init__` called?

A) Before `__init__` sets any fields
B) Only when `frozen=True` is used
C) Only when the class is subclassed
D) Immediately after `__init__` completes, as its final step

---

**Q33.** What is the output?

```python
from contextlib import contextmanager

@contextmanager
def ctx():
    print("enter")
    yield 42
    print("exit")

with ctx() as v:
    print(v)
```

A) `enter`, `42`, `exit` (in that order)
B) `42`, `enter`, `exit`
C) `enter`, `exit`, `42`
D) `42` only

---

**Q34.** Which module enables CPU-bound parallelism that bypasses the GIL?

A) `threading`
B) `multiprocessing`
C) `asyncio`
D) `concurrent.futures.ThreadPoolExecutor`

---

**Q35.** What does `__all__` in a module control?

A) The order in which attributes are defined
B) Which names are accessible via `module.name` attribute access
C) Which names are exported when `from module import *` is executed
D) Which classes can be subclassed

---

**Q36.** What is the output?

```python
print(0.1 + 0.2 == 0.3)
```

A) `True`
B) `TypeError`
C) `None`
D) `False`

---

**Q37.** What is the output?

```python
from collections import defaultdict

d = defaultdict(list)
d['x'].append(1)
d['x'].append(2)
print(d['y'])
```

A) `[]`
B) `None`
C) `KeyError`
D) `[None]`

---

**Q38.** What is the output?

```python
a = [1, 2, 3]
b = a[:]
b[0] = 99
print(a[0])
```

A) `99`
B) `1`
C) `[99, 2, 3]`
D) `TypeError`

---

**Q39.** What is the output?

```python
x = []
for i in range(3):
    x.append(lambda: i)
print([f() for f in x])
```

A) `[0, 1, 2]`
B) `[0, 0, 0]`
C) `[2, 2, 2]`
D) `TypeError`

---

**Q40.** What is the output?

```python
class A:
    val = []

class B(A):
    pass

B.val.append(1)
print(A.val)
```

A) `[]`
B) `[1, 1]`
C) `AttributeError`
D) `[1]`

---
