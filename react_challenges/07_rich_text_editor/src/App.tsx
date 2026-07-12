import { useState } from 'react'
import RichTextEditor from './RichTextEditor'

const SAMPLE_HTML = `<p>Welcome to the <strong>Rich Text Editor</strong> challenge!</p><p>This sample content includes <em>italic text</em>, <strong>bold text</strong>, and a list:</p><ul><li>First item</li><li>Second item</li><li>Third item</li></ul><p>Try placing your cursor inside the list or bold regions to see the toolbar update its active state.</p>`

export default function App() {
  const [controlledValue, setControlledValue] = useState<string>('')
  const [previewValue, setPreviewValue] = useState<string>('')

  const handleLoadSample = () => {
    setControlledValue(SAMPLE_HTML)
  }

  const handleClear = () => {
    setControlledValue('')
  }

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', maxWidth: 1100, margin: '0 auto', padding: '2rem 1rem' }}>
      <h1 style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: '0.25rem' }}>
        Challenge 07 – Rich Text Editor
      </h1>
      <p style={{ color: '#666', marginBottom: '2rem', fontSize: '0.9rem' }}>
        Build a <code>{'<RichTextEditor value onChange />'}</code> component backed by a{' '}
        <code>contenteditable</code> div.
      </p>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        {/* Left column: controlled editor */}
        <section>
          <h2 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '0.75rem' }}>
            Controlled Editor
          </h2>

          <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '0.75rem' }}>
            <button
              onClick={handleLoadSample}
              style={{
                padding: '0.35rem 0.75rem',
                fontSize: '0.8rem',
                border: '1px solid #ccc',
                borderRadius: 4,
                cursor: 'pointer',
                background: '#f9f9f9',
              }}
            >
              Load sample content
            </button>
            <button
              onClick={handleClear}
              style={{
                padding: '0.35rem 0.75rem',
                fontSize: '0.8rem',
                border: '1px solid #ccc',
                borderRadius: 4,
                cursor: 'pointer',
                background: '#f9f9f9',
              }}
            >
              Clear
            </button>
          </div>

          <RichTextEditor
            value={controlledValue}
            onChange={setControlledValue}
            placeholder="Start typing here..."
            minHeight={180}
          />

          <div style={{ marginTop: '1rem' }}>
            <h3 style={{ fontSize: '0.8rem', fontWeight: 600, color: '#555', marginBottom: '0.4rem' }}>
              Raw HTML output
            </h3>
            <pre
              style={{
                background: '#f4f4f4',
                border: '1px solid #ddd',
                borderRadius: 4,
                padding: '0.75rem',
                fontSize: '0.72rem',
                overflowX: 'auto',
                whiteSpace: 'pre-wrap',
                wordBreak: 'break-all',
                minHeight: 60,
                color: '#333',
              }}
            >
              {controlledValue || <span style={{ color: '#aaa' }}>(empty)</span>}
            </pre>
          </div>
        </section>

        {/* Right column: preview editor + rendered preview */}
        <section>
          <h2 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '0.75rem' }}>
            Live Preview Editor
          </h2>

          <RichTextEditor
            value={previewValue}
            onChange={setPreviewValue}
            placeholder="Type here to see the rendered preview below..."
            minHeight={180}
          />

          <div style={{ marginTop: '1rem' }}>
            <h3 style={{ fontSize: '0.8rem', fontWeight: 600, color: '#555', marginBottom: '0.4rem' }}>
              Rendered preview
            </h3>
            <div
              dangerouslySetInnerHTML={{ __html: previewValue || '<span style="color:#aaa">(empty)</span>' }}
              style={{
                background: '#fff',
                border: '1px solid #ddd',
                borderRadius: 4,
                padding: '0.75rem',
                fontSize: '0.9rem',
                minHeight: 60,
                lineHeight: 1.6,
              }}
            />
          </div>
        </section>
      </div>

      {/* Read-only demo */}
      <section style={{ marginTop: '2.5rem' }}>
        <h2 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '0.5rem' }}>
          Read-only Mode
        </h2>
        <p style={{ fontSize: '0.8rem', color: '#666', marginBottom: '0.75rem' }}>
          The editor below is initialised with sample content and <code>readOnly</code> set to{' '}
          <code>true</code>. The toolbar should be hidden and the content should not be editable.
        </p>
        <RichTextEditor
          value={SAMPLE_HTML}
          onChange={() => {}}
          readOnly
          minHeight={120}
        />
      </section>
    </div>
  )
}
