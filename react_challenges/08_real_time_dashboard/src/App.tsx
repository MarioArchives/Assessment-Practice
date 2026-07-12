import Dashboard from './Dashboard';

export default function App() {
  return (
    <div style={{ minHeight: '100vh', background: '#0f172a', color: '#e2e8f0', fontFamily: 'system-ui, sans-serif' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '2rem 1rem' }}>
        <p style={{ marginBottom: '2rem', color: '#94a3b8', fontSize: '0.875rem', lineHeight: 1.6 }}>
          <strong style={{ color: '#e2e8f0' }}>Challenge 08 — Real-Time Dashboard.</strong>{' '}
          Implement the <code style={{ background: '#1e293b', padding: '0 4px', borderRadius: 3 }}>Dashboard</code> component
          inside <code style={{ background: '#1e293b', padding: '0 4px', borderRadius: 3 }}>src/Dashboard.tsx</code> so
          that it subscribes to the metrics stream, renders four metric cards with live sparklines, a scrolling event log,
          a pause/resume toggle, and an uptime counter. See <code style={{ background: '#1e293b', padding: '0 4px', borderRadius: 3 }}>CHALLENGE.md</code> for
          full requirements and evaluation criteria.
        </p>
        <Dashboard />
      </div>
    </div>
  );
}
