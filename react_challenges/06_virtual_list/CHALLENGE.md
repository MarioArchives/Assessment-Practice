# Challenge 06 – Virtual List

## Overview

Build a generic `<VirtualList>` component in React and TypeScript that renders **only the items currently visible** within its scroll window. This technique — called _windowing_ or _virtualization_ — makes it possible to display hundreds of thousands of rows without degrading browser performance, because the DOM only ever contains a small slice of the full dataset at any moment.

A naively rendered list of 100,000 items would create 100,000 DOM nodes, consume enormous memory, and cause sluggish scrolling. A virtual list solves this by computing which items fall inside (or just outside) the visible viewport and rendering only those, while still maintaining the correct total scroll height so the browser's scrollbar behaves naturally.

---

## Requirements

### Props

Your `VirtualList` component must accept the following props (the interface is already defined in `src/VirtualList.tsx`):

| Prop              | Type                                        | Description                                                                 |
|-------------------|---------------------------------------------|-----------------------------------------------------------------------------|
| `items`           | `T[]`                                       | The full dataset. The component is generic over `T`.                        |
| `itemHeight`      | `number`                                    | Fixed height in pixels for every item. All items have the same height.      |
| `containerHeight` | `number`                                    | Fixed height in pixels for the scrollable outer container.                  |
| `renderItem`      | `(item: T, index: number) => ReactNode`     | Render prop called for each visible item.                                   |
| `overscan`        | `number` (optional, default `3`)            | Number of extra items to render above and below the visible viewport.       |

### Structural requirements

1. **Outer div** — has `height: containerHeight`, `overflow: auto`, and a scroll event listener (`onScroll`).
2. **Inner positioning div** — has `height: items.length * itemHeight` and `position: relative`. This ensures the scrollbar is proportional to the full list length.
3. **Each rendered item** is absolutely positioned using `top: index * itemHeight`, where `index` is the item's original index in the `items` array.

### Rendering window

Only items in the range `[startIndex - overscan, endIndex + overscan]` (clamped to valid array bounds) should be rendered at any time:

- `startIndex = Math.floor(scrollTop / itemHeight)`
- `endIndex = Math.ceil((scrollTop + containerHeight) / itemHeight)`

Clamp both values so they stay within `[0, items.length - 1]`.

### State

Store only a single piece of state: `scrollTop` (a `number`, initialized to `0`). Everything else — start index, end index, the visible slice — is derived from `scrollTop` during render.

---

## Constraints

- **No virtualization libraries.** Do not install or import `react-window`, `react-virtualized`, `@tanstack/virtual`, or any other windowing library. The entire implementation must be pure React and TypeScript.
- The component must be **generic** (`VirtualList<T>`), not tied to a specific item shape.
- TypeScript strict mode is enabled — avoid `any`.

---

## Hints

- Use the `onScroll` event on the outer `div`. The handler receives a `React.UIEvent<HTMLDivElement>`. Read `scrollTop` from `event.currentTarget.scrollTop`.
- The derived indices look like this:

  ```ts
  const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - overscan)
  const endIndex = Math.min(
    items.length - 1,
    Math.ceil((scrollTop + containerHeight) / itemHeight) + overscan
  )
  ```

- Build the rendered slice with a loop from `startIndex` to `endIndex` (inclusive). For each `i`, call `renderItem(items[i], i)` and wrap the result in a `div` with:

  ```ts
  style={{ position: 'absolute', top: i * itemHeight, width: '100%' }}
  ```

- Use `useState<number>(0)` for scroll position — nothing fancier is needed.

---

## Demo

`src/App.tsx` already provides a demo harness:

- A **primary demo** with 100,000 items, `itemHeight={50}`, `containerHeight={500}`, and colored rows.
- A **secondary demo** with 500 entries of a different data shape, `itemHeight={36}`, `containerHeight={250}`, demonstrating that the component is genuinely generic.

Once your implementation is complete, run `npm run dev` and open the app. Open React DevTools and inspect the DOM — you should see only around 13–15 rendered item nodes in the primary list at any given scroll position (10 visible + 3 overscan above + 3 overscan below), not 100,000.

---

## Evaluation Criteria

Your implementation will be assessed on:

1. **Correctness of rendering window** — only `~visible + 2 * overscan` items exist in the DOM at any time. Verifiable with React DevTools or browser element inspector.
2. **Correct total scroll height** — the inner div's height equals `items.length * itemHeight`, so the scrollbar accurately represents the full list length.
3. **Correct item positioning** — each item appears at the right vertical position; no visual gaps or overlaps when scrolling at any speed.
4. **Smooth scrolling performance** — no jank on fast scroll through 100,000 items.
5. **TypeScript correctness** — strict mode passes, no `any`, the generic type parameter `T` is properly threaded through.
6. **Simplicity** — a clean, minimal implementation scores better than an over-engineered one. The solution fits comfortably in under 60 lines.
