import type { MetricName, MetricUpdate } from './metricsStream';

export interface MetricConfig {
  name: MetricName;
  label: string;
  unit: string;
  max: number;
  thresholds: { warning: number; critical: number };
  color: string;
}

export const METRIC_CONFIGS: MetricConfig[] = [
  {
    name: 'cpu',
    label: 'CPU Usage',
    unit: '%',
    max: 100,
    thresholds: { warning: 70, critical: 90 },
    color: '#6366f1',
  },
  {
    name: 'memory',
    label: 'Memory Usage',
    unit: '%',
    max: 100,
    thresholds: { warning: 75, critical: 90 },
    color: '#14b8a6',
  },
  {
    name: 'requestsPerSecond',
    label: 'Requests/sec',
    unit: 'req/s',
    max: 10000,
    thresholds: { warning: 7000, critical: 9000 },
    color: '#f59e0b',
  },
  {
    name: 'errorRate',
    label: 'Error Rate',
    unit: '%',
    max: 10,
    thresholds: { warning: 2, critical: 5 },
    color: '#ef4444',
  },
];

interface MetricState {
  current: number;
  min: number;
  max: number;
  history: number[]; // last 60 values
}

// TODO: implement the Dashboard component
// Requirements (see CHALLENGE.md for full details):
//
// 1. Create a MetricsStream with createMetricsStream() and store it in a useRef so
//    the instance is stable across renders.
//
// 2. In a useEffect, call stream.subscribe(callback) and return a cleanup function
//    that calls stream.unsubscribe(). This is critical for avoiding memory leaks
//    and duplicate subscriptions in React StrictMode.
//
// 3. Track metric state as Record<MetricName, MetricState>. On each MetricUpdate:
//    - Update current value, session min/max
//    - Append to history and slice to the last 60 entries
//    - If paused (see #5), ignore the update entirely
//
// 4. For each metric, render a card showing:
//    - Current value (1 decimal place) + unit
//    - Session min / max
//    - A severity badge (green=normal, yellow=warning, red=critical)
//    - A sparkline: an <svg> containing a <polyline> built from the history array.
//      Use METRIC_CONFIGS[i].color for the stroke and fill="none".
//      Example points formula:
//        history.map((v, i) => `${i * (WIDTH / 60)},${HEIGHT - (v / max * HEIGHT)}`).join(' ')
//
// 5. Maintain a paused boolean (useState). When paused, skip state updates in the
//    subscription callback. Add a Pause/Resume button in the header that toggles it.
//    Do NOT unsubscribe/resubscribe on pause — keep the stream running.
//
// 6. In a second useEffect (separate from the subscription), run a setInterval every
//    1000 ms that increments an uptime counter (seconds since mount). Clear this
//    interval in the cleanup. Display the uptime in the header as "Uptime: Xs".
//
// 7. Keep a live event log (useState): prepend each incoming MetricUpdate as a
//    log entry and cap the array at 50 entries. Render the log below the cards,
//    most-recent first, showing: timestamp (HH:MM:SS), metric label, value+unit,
//    severity badge. Skip log updates when paused.

export default function Dashboard(): null {
  // TODO: replace `return null` with your implementation
  return null;
}
