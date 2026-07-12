import InfiniteScrollFeed from './InfiniteScrollFeed';

export default function App() {
  return (
    <div
      style={{
        maxWidth: '680px',
        margin: '0 auto',
        padding: '2rem 1rem',
        fontFamily: 'system-ui, sans-serif',
      }}
    >
      <header style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.5rem', fontWeight: 700, margin: '0 0 0.5rem' }}>
          Challenge 02 – Infinite Scroll Feed
        </h1>
        <p style={{ color: '#6b7280', margin: 0, lineHeight: 1.6 }}>
          Implement <code>InfiniteScrollFeed</code> in{' '}
          <code>src/InfiniteScrollFeed.tsx</code>. Posts are loaded from the
          mock API in pages. A sentinel element near the bottom of the list
          should trigger the next page via <code>IntersectionObserver</code>.
        </p>
      </header>

      <main>
        <InfiniteScrollFeed pageSize={10} />
      </main>
    </div>
  );
}
