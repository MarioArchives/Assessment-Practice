# React Multiple Choice Questions

---

**Q1.** What is the virtual DOM in React?

A) A lightweight JavaScript representation of the real DOM that React diffs to compute minimal updates
B) A browser API for fast DOM manipulation that bypasses the layout engine
C) A shadow DOM tree attached to each React component
D) A WebAssembly module that proxies DOM calls to native code

---

**Q2.** React's reconciliation runs in O(n) rather than O(n³). Which two assumptions make that possible?

A) Elements always update top-down; parent nodes are never replaced
B) Only leaf nodes change; React skips subtree diffs for parent nodes
C) Elements of different types produce entirely different trees; the `key` prop identifies stable children across renders
D) React diffs only the first render and applies patches from a stored snapshot thereafter

---

**Q3.** What is React Fiber?

A) A new JSX compiler introduced in React 17
B) A built-in HTTP client for data fetching in React components
C) A reimplementation of React's reconciliation engine that splits rendering work into interruptible units
D) A CSS-in-JS utility bundled with the React package

---

**Q4.** What is the primary purpose of the `key` prop on list items?

A) It sets the HTML `id` attribute on the rendered DOM element
B) It helps React identify which items have changed, been added, or removed during reconciliation
C) It prevents the component from re-rendering if the key is unchanged
D) It is required for `React.memo` to perform its shallow comparison correctly

---

**Q5.** A PR uses array index as the `key` for a sortable list. What is the risk?

```jsx
items.map((item, index) => <Row key={index} item={item} />)
```

A) Using integers as keys is not allowed — keys must be strings
B) When items are reordered or deleted, React maps the wrong state and DOM nodes to the wrong items
C) The reconciler throws an error when two items swap positions
D) This only causes problems in development mode, not in production

---

**Q6.** What is displayed after clicking the button once?

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  function handleClick() {
    setCount(count + 1);
    setCount(count + 1);
  }
  return <button onClick={handleClick}>{count}</button>;
}
```

A) `2` — two `setState` calls produce two increments
B) `1` — both calls capture the same stale `count` from the closure
C) `0` — `setState` is async and both calls are discarded in the same batch
D) Throws: too many state updates in a single event handler

---

**Q7.** How do you fix the double-increment bug in Q6?

A) Wrap both `setCount` calls in `flushSync`
B) Call `setCount` inside a `setTimeout` to avoid batching
C) Use the functional update form: `setCount(c => c + 1)` for both calls
D) Replace `useState` with `useRef` to avoid the stale closure

---

**Q8.** What does `useEffect` with an empty dependency array `[]` do?

A) Runs the effect synchronously during the initial render, blocking paint
B) Runs the effect once after the initial render; runs cleanup once when the component unmounts
C) Skips the effect entirely — an empty array signals "no dependencies, no work"
D) Runs the effect after every render but skips the cleanup phase

---

**Q9.** What is the bug?

```jsx
function App() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    setCount(count + 1);
  });
}
```

A) `count` is always `0` inside `useEffect` due to a stale closure
B) Infinite loop: no dependency array means the effect runs after every render; each `setCount` triggers another render
C) `useState` and `useEffect` cannot be used together in the same component
D) The effect only runs once because React deduplicates consecutive renders with identical state

---

**Q10.** What is a stale closure in the context of React hooks?

A) A hook called inside a loop, violating the Rules of Hooks
B) A `useRef` value that was not updated before the component re-rendered
C) An effect or callback that closed over a variable from a previous render and uses its outdated value
D) A memoized component that has not re-rendered despite receiving new props

---

**Q11.** What is missing from this `useEffect`?

```jsx
useEffect(() => {
  const id = setInterval(() => setCount(c => c + 1), 1000);
}, []);
```

A) `count` must be listed in the dependency array
B) A cleanup function returning `clearInterval(id)` — without it the interval leaks and keeps firing after unmount
C) `setInterval` is not permitted inside `useEffect` — use `setTimeout` in a loop instead
D) The inner callback must be wrapped in `useCallback`

---

**Q12.** What does `useCallback(fn, deps)` return?

A) The result of calling `fn` immediately with no arguments
B) A debounced wrapper around `fn` that coalesces rapid calls
C) A memoized version of `fn` whose reference identity only changes when `deps` change
D) A ref object with `fn` stored at `.current`

---

**Q13.** What does `useMemo(() => compute(a, b), [a, b])` do?

A) Runs `compute` once and caches the result permanently for the lifetime of the component
B) Defers `compute` until after the browser has painted, to avoid blocking the render
C) Runs `compute` and caches the result, recomputing only when `a` or `b` changes
D) Returns a memoized React element wrapping the result of `compute`

---

**Q14.** Does mutating `ref.current` trigger a re-render?

```jsx
const ref = useRef(0);
ref.current += 1;
```

A) Yes — any mutation to a value in a component triggers a re-render
B) Yes, but only if the ref is also attached to a DOM element via the `ref` prop
C) Yes, but only if the ref value is read inside the JSX return
D) No — `useRef` stores mutable values outside React's state system; changes are invisible to the reconciler

---

**Q15.** Which of the following violates the Rules of Hooks?

A) `function useCounter() { const [n, setN] = useState(0); return [n, setN]; }`
B) `function Form() { if (isLoggedIn) { const [name, setName] = useState(''); } }`
C) `function App() { useEffect(() => {}, []); }`
D) `function useData() { useEffect(() => {}, []); return null; }`

---

**Q16.** What does `React.memo(Component)` do?

A) Prevents the component from ever re-rendering once it has mounted
B) Memoizes the component's last JSX output and replays it on subsequent renders
C) Converts the function component into a pure class component internally
D) Wraps the component so it skips re-rendering when its props are shallowly equal to the previous render

---

**Q17.** By default, what happens to a child component when its parent re-renders?

A) The child re-renders regardless of whether its props changed
B) The child re-renders only if its props changed
C) The child is unmounted and remounted with fresh state
D) The child re-renders only if it contains `useState` or `useReducer`

---

**Q18.** Will `MemoChild` re-render on every `Parent` render?

```jsx
const MemoChild = React.memo(({ style }) => <div style={style} />);

function Parent() {
  return <MemoChild style={{ color: 'red' }} />;
}
```

A) No — `React.memo` deep-compares objects, so structurally identical shapes are equal
B) No — inline style objects are automatically cached by the JSX transform
C) Yes — `{ color: 'red' }` is a new object reference on every render, failing the shallow equality check
D) Yes, but only in development mode when `React.StrictMode` is active

---

**Q19.** What is the correct fix for the `React.memo` / inline object issue in Q18?

A) Replace `React.memo` with `React.PureComponent`
B) Pass `style` as a CSS class string using `className` instead
C) Use `useEffect` to apply the style directly to the DOM node via the ref
D) Move the object outside the component or memoize it with `useMemo` inside the parent

---

**Q20.** What does `useLayoutEffect` do that `useEffect` does not?

A) Fires synchronously after DOM mutations but before the browser paints, enabling layout reads without visual flicker
B) Runs before the component's render output is computed
C) Gives the effect access to the DOM state from the previous render
D) Prevents the browser from painting until the effect explicitly signals completion

---

**Q21.** What is the bug?

```jsx
const [items, setItems] = useState([1, 2, 3]);

function addItem() {
  items.push(4);
  setItems(items);
}
```

A) `push` returns the new array length, not the array — `setItems` receives a number
B) React compares by reference: the array reference is unchanged, so React bails out of re-rendering
C) The mutation causes React to re-render twice due to the double-render heuristic
D) `setItems` expects a function argument, not an array value

---

**Q22.** What is the correct way to append an item to an array in state?

A) `setItems(items.push(newItem))`
B) `items[items.length] = newItem; setItems(items)`
C) `setItems([...items, newItem])`
D) `setItems(Object.assign([], items, { [items.length]: newItem }))`

---

**Q23.** What does `useReducer` provide over `useState`?

A) Built-in async support via Promises returned from the reducer function
B) Automatic persistence of state to `sessionStorage` between renders
C) Shared global state across all components without needing a context provider
D) A `(state, action) => newState` reducer for complex state transitions, and a stable `dispatch` reference

---

**Q24.** What is the bug in this `useEffect`?

```jsx
useEffect(async () => {
  const res = await fetch(url);
  setData(await res.json());
}, [url]);
```

A) `fetch` is not permitted inside `useEffect`
B) `useEffect` must not return a Promise; the `async` callback does, which prevents cleanup functions from working correctly
C) `await` syntax is not supported inside hook callbacks
D) The `url` dependency will cause the effect to re-run on every render

---

**Q25.** What is the correct pattern for async work inside `useEffect`?

A) Define an `async` function inside the effect body and call it immediately, keeping the effect callback itself synchronous
B) Mark the component function as `async`
C) Use `useMemo` instead — it natively supports async callbacks
D) Use `useLayoutEffect`, which supports returning a Promise as a cleanup

---

**Q26.** What race condition risk does this hook have?

```jsx
function useData(id) {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData(id).then(setData);
  }, [id]);
  return data;
}
```

A) `setData` changes identity on each render, causing the effect to loop
B) `fetchData` is called before `id` is fully initialised on mount
C) If `id` changes before the previous fetch resolves, the older response can overwrite the newer one
D) The effect runs twice in `StrictMode`, permanently doubling network requests

---

**Q27.** What does `React.StrictMode` do in development?

A) Enforces TypeScript type checking for component props at runtime
B) Disables `console.log` to keep the console clean during development
C) Converts all function components to class components for stricter lifecycle checking
D) Double-invokes renders and effects to surface side effects, and warns about deprecated APIs

---

**Q28.** What does React 18 automatic batching change compared to React 17?

A) State updates inside `setTimeout`, native event handlers, and Promises are now batched into a single re-render, just like React event handlers
B) All batching is removed so state updates are always fully synchronous
C) Batching now requires wrapping updates in `unstable_batchedUpdates`
D) State updates inside React event handlers are no longer batched to improve responsiveness

---

**Q29.** What does `forwardRef` enable?

A) A child to forward its internal state up to the parent component
B) Context values to propagate automatically to all descendants without a Provider
C) A `useRef` value to be shared between two sibling components
D) A parent component to pass a `ref` through a child down to a DOM element inside it

---

**Q30.** What is the purpose of `useImperativeHandle`?

A) Used with `forwardRef` to customise the ref handle exposed to the parent, rather than exposing the raw DOM node
B) Bypasses React's reconciliation to directly and imperatively patch the DOM
C) Provides an imperative API for updating a context value from a consumer
D) Allows a function component to access class component lifecycle methods

---

**Q31.** What is the problem with this context provider?

```jsx
function App() {
  const [user, setUser] = useState(null);
  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}
```

A) Context providers cannot receive values that include functions
B) `setUser` is re-created on every render, making the value always reference-unequal
C) Only primitive types can safely be used as a context `value`
D) A new object literal is created on every render; all consumers re-render even when `user` has not changed

---

**Q32.** How do you fix the unnecessary re-renders caused by the context provider in Q31?

A) Memoize the value: `const value = useMemo(() => ({ user, setUser }), [user])`
B) Replace `useState` with `useRef` so `user` does not participate in React's reactivity
C) Wrap the `Provider` in `React.memo`
D) Split `user` and `setUser` into separate context files

---

**Q33.** What happens when you change the `key` prop of an already-mounted component to a new value?

A) React updates the component instance in place, as it would for any prop change
B) The component re-renders with the new key but preserves all its existing state
C) The component's effects re-run but its local state is preserved
D) React unmounts the existing instance and mounts a completely fresh one, resetting all state

---

**Q34.** What is a React Portal?

A) A built-in routing mechanism for single-page applications
B) A pattern for lifting state up to a common ancestor between siblings
C) A way to render children into a DOM node that exists outside the parent component's DOM hierarchy
D) A higher-order component that injects props from a global store

---

**Q35.** What is an error boundary?

A) A class component implementing `componentDidCatch` and/or `getDerivedStateFromError` to catch rendering errors in its subtree
B) A `try/catch` block wrapping a component's JSX return statement
C) A hook that catches errors thrown inside `useEffect`
D) A TypeScript type guard that narrows error types in JSX

---

**Q36.** What does `React.lazy(() => import('./Component'))` do?

A) Preloads the component's bundle in the background before it is needed
B) Code-splits the component into a separate chunk that is only downloaded when the component first renders
C) Renders the component at the next idle animation frame to avoid blocking
D) Caches the component module in memory across route navigations

---

**Q37.** `React.lazy` components must be wrapped in which component?

A) `React.Suspense` with a `fallback` prop
B) `React.StrictMode`
C) `React.Fragment`
D) A custom error boundary component

---

**Q38.** What does `flushSync` do?

A) Flushes the browser's layout and paint queues synchronously
B) Cancels all pending state updates queued in the current batch
C) Forces React to process all state updates inside the callback synchronously and commit them to the DOM before returning
D) Converts a deferred `startTransition` update into an urgent synchronous one

---

**Q39.** What is the primary advantage of `createRoot` (React 18) over the legacy `ReactDOM.render`?

A) It enables server-side rendering for the first time
B) It skips the virtual DOM diff for faster initial mounts
C) It allows multiple isolated React roots to share the same module instance
D) It unlocks concurrent features: automatic batching, `startTransition`, and improved Suspense

---

**Q40.** What does wrapping a state update in `startTransition` tell React?

A) The update is non-urgent; React may interrupt and deprioritise it to keep the UI responsive to user input
B) The update should be deferred to the next microtask queue tick
C) The update bypasses memoization in all `React.memo` children
D) The update must be flushed synchronously before the next browser paint

---

**Q41.** What is the purpose of `act()` in React unit tests?

A) It simulates user interactions such as clicks and keyboard input
B) It mocks React's reconciliation to make test output fully deterministic
C) It ensures all state updates and effects triggered by the wrapped code are fully flushed before assertions run
D) It wraps the component under test in a context provider automatically

---

**Q42.** What defines a custom hook?

A) A JavaScript function whose name starts with `use` and that may call other hooks
B) A class that extends `React.Hook`
C) A hook registered globally via `React.createHook()`
D) A component that returns another hook rather than JSX

---

**Q43.** What does `useContext(MyContext)` return, and when does it cause a re-render?

A) Returns a subscription handle; consumers explicitly opt into specific fields
B) Returns the context object itself; re-renders only when a new Provider mounts above
C) Returns the Provider component; re-renders on every parent render
D) Returns the current context value; re-renders whenever that value changes (by reference)

---

**Q44.** What is the difference between React's render phase and commit phase?

A) Render = computing the new virtual DOM tree (pure, no side effects); commit = applying DOM changes and running effects
B) Render = writing to the DOM; commit = diffing the virtual DOM trees
C) Render = running `useLayoutEffect`; commit = running `useEffect`
D) Render and commit are the same phase split across two consecutive animation frames

---

**Q45.** What is prop drilling?

A) Destructuring props at multiple levels of nesting within a single component
B) Passing data through several layers of intermediate components that do not use it themselves, just to reach a deep consumer
C) Passing a `ref` through multiple component layers using `forwardRef`
D) A performance pattern where props are lazily evaluated only on first access

---

**Q46.** A reviewer adds `React.memo` to a component to prevent re-renders. Under what condition will it still re-render on every parent render?

A) When the component uses `useState` or `useReducer` internally
B) When more than five props are passed to the component
C) When a prop that is an object or function is created inline in the parent, producing a new reference each render
D) When the component's children include other memoized components

---

**Q47.** What is the second argument to `React.memo` used for?

A) Providing a fallback component to render if the memo comparison fails
B) Passing a dependency array, similar to `useMemo` and `useCallback`
C) Setting the display name of the wrapped component for DevTools
D) A custom comparison function `(prevProps, nextProps) => boolean` — return `true` to skip the re-render

---

**Q48.** What is wrong with reading a DOM layout property immediately after calling a state setter?

```jsx
setVisible(true);
console.log(ref.current.offsetHeight); // may log a stale value
```

A) `ref.current` becomes `null` as soon as a state setter is called
B) State updates are asynchronous; the DOM has not been updated yet — read layout inside `useLayoutEffect` after the update
C) `offsetHeight` is not a valid DOM property when accessed from inside a React component
D) Calling a state setter clears all refs attached to the component

---

**Q49.** What renders while a `React.lazy` component's bundle is still loading inside a `<Suspense>` boundary?

A) `null` — the component tree is blank until loading completes
B) The `fallback` prop of the nearest `<Suspense>` ancestor
C) The previous render's output is preserved in place until the new one is ready
D) The nearest error boundary catches the loading state and renders its own fallback

---

**Q50.** Which pair of class lifecycle methods does `useEffect(() => { setup(); return cleanup; }, [])` most closely replace?

A) `shouldComponentUpdate` + `componentWillUnmount`
B) `componentDidUpdate` + `componentWillUnmount`
C) `render` + `componentDidMount`
D) `componentDidMount` + `componentWillUnmount`
