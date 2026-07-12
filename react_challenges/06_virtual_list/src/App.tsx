import VirtualList from './VirtualList'

interface Item {
  id: number
  label: string
  color: string
}

const COLORS = ['#fde68a', '#a7f3d0', '#bfdbfe', '#fca5a5', '#ddd6fe', '#fbcfe8']

const LARGE_LIST: Item[] = Array.from({ length: 100_000 }, (_, i) => ({
  id: i + 1,
  label: `Item #${i + 1}`,
  color: COLORS[i % COLORS.length],
}))

const SMALL_LIST = Array.from({ length: 500 }, (_, i) => ({
  id: i,
  name: `Entry ${i}`,
  score: Math.round(Math.random() * 100),
}))

export default function App() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '2rem', maxWidth: 700 }}>
      <h1 style={{ marginBottom: '0.25rem' }}>06 – Virtual List Challenge</h1>

      {/* Primary demo */}
      <section style={{ marginBottom: '3rem' }}>
        <h2 style={{ marginBottom: '0.5rem' }}>
          Large list —{' '}
          <span style={{ color: '#6366f1', fontWeight: 700 }}>
            {LARGE_LIST.length.toLocaleString()} items
          </span>
        </h2>
        <p style={{ marginBottom: '0.75rem', color: '#555', fontSize: 14 }}>
          itemHeight=50 · containerHeight=500 · only ~visible items are in the DOM
        </p>
        <VirtualList
          items={LARGE_LIST}
          itemHeight={50}
          containerHeight={500}
          overscan={3}
          renderItem={(item, index) => (
            <div
              style={{
                height: 50,
                display: 'flex',
                alignItems: 'center',
                padding: '0 1rem',
                background: item.color,
                borderBottom: '1px solid rgba(0,0,0,0.06)',
                boxSizing: 'border-box',
              }}
            >
              <span style={{ color: '#374151', fontSize: 14 }}>
                <strong style={{ marginRight: 8, color: '#6b7280' }}>#{index}</strong>
                {item.label}
              </span>
            </div>
          )}
        />
      </section>

      {/* Second instance — different shape, different itemHeight */}
      <section>
        <h2 style={{ marginBottom: '0.5rem' }}>
          Reusability demo —{' '}
          <span style={{ color: '#10b981', fontWeight: 700 }}>
            {SMALL_LIST.length.toLocaleString()} entries
          </span>
        </h2>
        <p style={{ marginBottom: '0.75rem', color: '#555', fontSize: 14 }}>
          itemHeight=36 · containerHeight=250 · different data shape
        </p>
        <VirtualList
          items={SMALL_LIST}
          itemHeight={36}
          containerHeight={250}
          overscan={5}
          renderItem={(entry, index) => (
            <div
              style={{
                height: 36,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '0 1rem',
                background: index % 2 === 0 ? '#f9fafb' : '#ffffff',
                borderBottom: '1px solid #e5e7eb',
                boxSizing: 'border-box',
                fontSize: 13,
              }}
            >
              <span>{entry.name}</span>
              <span
                style={{
                  fontWeight: 600,
                  color: entry.score >= 75 ? '#059669' : entry.score >= 50 ? '#d97706' : '#dc2626',
                }}
              >
                {entry.score}
              </span>
            </div>
          )}
        />
      </section>
    </div>
  )
}
