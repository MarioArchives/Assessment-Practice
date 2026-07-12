# Challenge 08 – Real-Time Dashboard

## Overview

Build a real-time metrics dashboard that subscribes to a continuous stream of metric updates and renders live charts, summary cards, and an event log — all updating smoothly without any external charting or reactive-stream library.

The finished dashboard should feel like a lightweight server-monitoring panel: numbers ticking in real time, sparklines showing recent trends at a glance, and a scrolling log of notable events.

---

## Requirements

### Metric Stream

Use `createMetricsStream()` exported from `src/metricsStream.ts`. It returns an object with two methods:

- `subscribe(callback)` — starts emitting `MetricUpdate` objects to `callback` approximately every 500 ms.
- `unsubscribe()` — stops all emissions and clears the internal interval.

Call `subscribe` inside a `useEffect`, and call `stream.unsubscribe()` in the cleanup function returned from that effect. **This is the single most important correctness requirement in the challenge.**

### Metric Cards (4 total)

Render one card per metric:

| Metric | Label | Unit | Max | Warning | Critical |
|---|---|---|---|---|---|
| `cpu` | CPU Usage | % | 100 | 70 | 90 |
| `memory` | Memory Usage | % | 100 | 75 | 90 |
| `requestsPerSecond` | Requests/sec | req/s | 10 000 | 7 000 | 9 000 |
| `errorRate` | Error Rate | % | 10 | 2 | 5 |

Each card must display:

1. **Current value** — formatted to one decimal place, with its unit.
2. **Session min / max** — the lowest and highest values seen since the component mounted.
3. **Color-coded status badge** — green (`normal`), yellow (`warning`), or red (`critical`), derived from the metric's threshold config and the most recent severity delivered by the stream.

### Sparkline Charts

Each metric card also contains a **sparkline**: a narrow SVG `<polyline>` showing the last 60 data points for that metric. Rules:

- No Recharts, Chart.js, D3, Victory, or any other charting library — raw SVG only.
- Keep a `history: number[]` array (max length 60) per metric in component state.
- Derive the `points` attribute from the history array. A starting formula:

  ```
  points.map((v, i) => `${i * (width / 60)},${height - (v / max * height)}`).join(' ')
  ```

  Adjust `width`, `height`, and `max` to match your card layout.
- The polyline should be styled with the metric's `color` and a stroke width of 1.5–2 px, with `fill="none"`.

### Live Event Log

Below the metric cards, render a scrolling event log:

- Keep the **last 50 events** only (drop older ones when the list exceeds 50).
- Display events **most recent first**.
- Each row shows:
  - Formatted timestamp (e.g., `HH:MM:SS`).
  - Metric label (human-readable, not the raw key).
  - Current value with unit.
  - A **severity badge** — styled consistently with the card status badges.

### Pause / Resume Toggle

Add a **Pause / Resume** button in the dashboard header. When paused:

- New updates from the stream are **ignored** (the stream keeps running internally — do not unsubscribe; use a ref or state flag to gate state updates).
- The button label changes to "Resume".
- Cards and sparklines remain frozen at the last received values.

When resumed, updates flow again immediately.

### Uptime Counter

The dashboard header also shows an **uptime counter** — the number of whole seconds elapsed since the `Dashboard` component first mounted. Increment it with a `setInterval` (1 000 ms) in a separate `useEffect`, and clear it on unmount.

---

## Constraints

- **No chart/graphing libraries.** SVG only for the sparklines.
- **No RxJS or reactive-stream libraries.** The provided `MetricsStream` interface is sufficient.
- **TypeScript throughout.** No `any` types; use the exported types from `metricsStream.ts`.
- Use **React 18** hooks only (`useState`, `useEffect`, `useRef`, `useCallback`). No class components.

---

## Hints

### Subscription cleanup and StrictMode

React 18 StrictMode intentionally mounts → unmounts → remounts every component in development. This means your `useEffect` cleanup **will** run before the effect fires again. If `createMetricsStream()` is called inside the effect, you'll get a fresh stream each time — which is correct. Store the stream instance in a `useRef` if you call `createMetricsStream()` outside the effect so the reference stays stable.

The guard inside `MetricsStream` (clearing any existing interval before starting a new one) is a second line of defence, but your cleanup must be the primary mechanism.

### History array

Keep metric state as a `Record<MetricName, MetricState>` where `MetricState` has `{ current, min, max, history }`. On each update, append the new value and slice to the last 60 entries:

```ts
history: [...prev.history, value].slice(-60)
```

### SVG viewBox vs fixed dimensions

Using a fixed `viewBox="0 0 120 40"` and `preserveAspectRatio="none"` on the SVG lets the sparkline stretch to fill its container without recalculating pixel coordinates.

### Event log immutability

Use the functional updater form of `setState` for the log to avoid stale closure issues:

```ts
setLog(prev => [newEvent, ...prev].slice(0, 50));
```

---

## Evaluation Criteria

Your solution will be assessed on:

1. **No memory leaks** — the stream's interval is always cleared on unmount. Verified by unmounting the component and confirming no further state updates occur.
2. **No duplicate subscriptions in StrictMode** — mounting in StrictMode must result in exactly one active subscription at any time.
3. **Sparklines update smoothly** — all 4 polylines redraw on each tick without visible stuttering or layout shift.
4. **Pause / Resume correctness** — pausing freezes the UI; resuming immediately reflects new data.
5. **Event log cap** — the log never exceeds 50 entries; oldest entries are dropped.
6. **Uptime counter** — increments every second from 0, independent of metric updates, and stops on unmount.
7. **TypeScript correctness** — no `any`, no `@ts-ignore`, and `tsc --noEmit` passes cleanly.
