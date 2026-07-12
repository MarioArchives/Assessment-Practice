export type MetricName = 'cpu' | 'memory' | 'requestsPerSecond' | 'errorRate';

export interface MetricUpdate {
  metric: MetricName;
  value: number;
  timestamp: number; // Date.now()
  severity: 'normal' | 'warning' | 'critical';
}

export interface MetricsStream {
  subscribe: (callback: (update: MetricUpdate) => void) => void;
  unsubscribe: () => void;
}

// Current simulated values for random-walk behaviour
const currentValues: Record<MetricName, number> = {
  cpu: 40,
  memory: 55,
  requestsPerSecond: 3000,
  errorRate: 1,
};

// Per-metric configuration used for random-walk bounds and severity thresholds
const metricConfig: Record<
  MetricName,
  { min: number; max: number; step: number; warning: number; critical: number }
> = {
  cpu: { min: 0, max: 100, step: 8, warning: 70, critical: 90 },
  memory: { min: 0, max: 100, step: 5, warning: 75, critical: 90 },
  requestsPerSecond: { min: 0, max: 10000, step: 600, warning: 7000, critical: 9000 },
  errorRate: { min: 0, max: 10, step: 0.8, warning: 2, critical: 5 },
};

function randomWalk(metric: MetricName): number {
  const cfg = metricConfig[metric];
  const delta = (Math.random() * 2 - 1) * cfg.step;
  const next = currentValues[metric] + delta;
  currentValues[metric] = Math.min(cfg.max, Math.max(cfg.min, next));
  return parseFloat(currentValues[metric].toFixed(2));
}

function getSeverity(metric: MetricName, value: number): MetricUpdate['severity'] {
  const cfg = metricConfig[metric];
  if (value >= cfg.critical) return 'critical';
  if (value >= cfg.warning) return 'warning';
  return 'normal';
}

function pickMetrics(count: number): MetricName[] {
  const all: MetricName[] = ['cpu', 'memory', 'requestsPerSecond', 'errorRate'];
  // Shuffle via sort with random comparator, then take `count`
  return all
    .map(m => ({ m, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .slice(0, count)
    .map(x => x.m);
}

export function createMetricsStream(): MetricsStream {
  let intervalId: ReturnType<typeof setInterval> | null = null;
  let activeCallback: ((update: MetricUpdate) => void) | null = null;

  function subscribe(callback: (update: MetricUpdate) => void): void {
    // Guard: clear any existing interval before starting a new subscription
    if (intervalId !== null) {
      clearInterval(intervalId);
      intervalId = null;
    }

    activeCallback = callback;

    intervalId = setInterval(() => {
      if (activeCallback === null) return;

      // Update 1–3 randomly chosen metrics per tick
      const count = Math.floor(Math.random() * 3) + 1;
      const metrics = pickMetrics(count);

      for (const metric of metrics) {
        const value = randomWalk(metric);
        const update: MetricUpdate = {
          metric,
          value,
          timestamp: Date.now(),
          severity: getSeverity(metric, value),
        };
        activeCallback(update);
      }
    }, 500);
  }

  function unsubscribe(): void {
    if (intervalId !== null) {
      clearInterval(intervalId);
      intervalId = null;
    }
    activeCallback = null;
  }

  return { subscribe, unsubscribe };
}
