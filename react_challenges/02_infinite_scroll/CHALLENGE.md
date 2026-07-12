# Challenge 02 – Infinite Scroll Feed

## Overview

Build an infinite-scrolling post feed in React using the native `IntersectionObserver` API. The feed should automatically load additional pages of posts as the user scrolls toward the bottom of the list, providing a smooth, continuous reading experience without any manual "Load more" button clicks (though a retry button on error is acceptable and required).

This challenge tests your ability to manage asynchronous side effects correctly inside React's rendering model, avoid common pitfalls like duplicate requests and stale closures, and keep the user experience polished even in loading and error states.

---

## Requirements

### Functional Requirements

1. **Post rendering** – Render posts returned by `fetchPosts(page, pageSize)` from `src/mockApi.ts`. Each post card must display:
   - Post title (prominent heading)
   - Author name with a colored circular avatar showing the author's first initial
   - A body excerpt (first 120 characters of the body, followed by an ellipsis if truncated)
   - The avatar's background color must match the `avatarColor` field returned by the API

2. **Auto-pagination** – When a sentinel `<div>` element placed _after_ the last rendered post enters the viewport (within a **200 px root margin**), automatically fetch the next page. The user should never need to scroll all the way to the very bottom edge — the fetch should begin slightly before they get there.

3. **Loading state** – While a fetch is in flight, render a `<LoadingSpinner />` component below the current list of posts. The spinner should be visually meaningful (not just the text "Loading…") and accessible (use `role="status"` and an `aria-label`).

4. **End-of-feed state** – When the API returns `nextPage: null`, stop observing the sentinel and display a "No more posts" message at the bottom of the feed. This message should be visually distinct from the post cards.

5. **Error handling** – If `fetchPosts` rejects, display an error message and a **Retry** button. Clicking Retry should re-attempt the failed page fetch. The already-loaded posts must remain visible during and after an error — do not wipe the feed on failure.

6. **No duplicate fetches** – Re-renders must not trigger additional API calls. The `IntersectionObserver` callback should only fire a new fetch when the sentinel is intersecting _and_ there is no fetch currently in progress.

### Technical Constraints

- **No data-fetching libraries** – Do not use `react-query`, `SWR`, `Apollo`, `RTK Query`, or any library that manages async data for you. All fetching logic must be written with plain `useEffect`, `useCallback`, `useRef`, and `useState`.
- **No virtualization** – All loaded posts must be present in the DOM simultaneously. You do not need to recycle DOM nodes.
- **`IntersectionObserver` only** – Do not use scroll event listeners (`window.addEventListener('scroll', …)`) to trigger pagination. The observer must be the sole mechanism.

---

## File Structure

```
src/
  mockApi.ts           – Provided. Do not modify.
  App.tsx              – Demo harness. Minor tweaks allowed.
  InfiniteScrollFeed.tsx  – Your primary implementation file.
  main.tsx             – Entry point. Do not modify.
```

---

## Hints

### Sentinel Ref Pattern

Attach the `IntersectionObserver` to a sentinel `<div>` at the bottom of your list using the **ref callback** pattern rather than `useRef` + `useEffect`:

```tsx
const sentinelRef = useCallback((node: HTMLDivElement | null) => {
  if (!node) return;
  const observer = new IntersectionObserver(callback, { rootMargin: '200px' });
  observer.observe(node);
  return () => observer.disconnect();
}, [/* deps */]);
```

This gives you automatic cleanup without needing a separate `useEffect` for the observer lifecycle.

### Preventing Duplicate Fetches

The most common bug in this challenge is firing duplicate requests. The `IntersectionObserver` callback can be invoked multiple times, and re-renders can re-mount the sentinel. Guard every fetch attempt:

```ts
if (isLoading || !hasMore) return;
```

Consider disconnecting the observer when `isLoading` is `true` and reconnecting it once the fetch completes, or use a `useRef` to track in-flight state without causing re-renders.

### State Shape

A reasonable starting state shape:

```ts
const [posts, setPosts] = useState<Post[]>([]);
const [page, setPage] = useState(1);
const [isLoading, setIsLoading] = useState(false);
const [hasMore, setHasMore] = useState(true);
const [error, setError] = useState<string | null>(null);
```

### Cleanup on Unmount

Always disconnect the `IntersectionObserver` in a cleanup function. If you use `useEffect` to manage the observer, return a cleanup from that effect. If you use a ref callback, disconnect inside the ref callback's returned teardown.

---

## API Reference

```ts
// src/mockApi.ts
fetchPosts(page: number, pageSize?: number): Promise<FetchPostsResult>

interface FetchPostsResult {
  posts: Post[];
  nextPage: number | null; // null = end of feed
  totalPages: number;
}

interface Post {
  id: number;
  title: string;
  author: string;
  body: string;
  avatarColor: string; // CSS hex color, e.g. "#6366f1"
}
```

The mock API simulates a 600–900 ms network delay and contains **47 total posts** (not a round number — this intentionally tests the edge case where the last page is smaller than `pageSize`).

---

## Evaluation Criteria

| Criterion | What we look for |
|---|---|
| No duplicate requests | Exactly one fetch per page, regardless of re-renders or rapid scrolling |
| Smooth UX | Spinner appears promptly; posts appear without layout shift |
| Proper cleanup | Observer disconnected on unmount; no memory leaks or React warnings |
| Error handling | Failed fetch shows error + retry; existing posts are preserved |
| Accessible loading states | Spinner has `role="status"` and a descriptive `aria-label` |
| Code clarity | Logic is easy to follow; effects have clear dependency arrays |

---

## Stretch Goals (optional, ungraded)

- Animate post cards in as they load (CSS `@keyframes` or a small CSS transition)
- Debounce the intersection callback to avoid rapid repeated triggers during fast scrolling
- Support a configurable `pageSize` prop on `<InfiniteScrollFeed />`
- Persist loaded posts to `sessionStorage` so a browser back-navigation restores position
