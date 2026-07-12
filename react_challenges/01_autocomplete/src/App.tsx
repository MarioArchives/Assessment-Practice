import { useState } from 'react'
import Autocomplete from './Autocomplete'

const PROGRAMMING_LANGUAGES = [
  'TypeScript',
  'JavaScript',
  'Python',
  'Rust',
  'Go',
  'Java',
  'Kotlin',
  'Swift',
  'C',
  'C++',
  'C#',
  'Ruby',
  'Elixir',
  'Haskell',
  'Scala',
  'Clojure',
  'Dart',
  'Zig',
  'Lua',
  'Erlang',
]

const US_CITIES = [
  'New York',
  'Los Angeles',
  'Chicago',
  'Houston',
  'Phoenix',
  'Philadelphia',
  'San Antonio',
  'San Diego',
  'Dallas',
  'San Jose',
  'Austin',
  'Jacksonville',
  'Denver',
  'Seattle',
  'Nashville',
]

const containerStyle: React.CSSProperties = {
  maxWidth: 640,
  margin: '48px auto',
  padding: '0 24px',
  display: 'flex',
  flexDirection: 'column',
  gap: 32,
}

const headingStyle: React.CSSProperties = {
  fontSize: 28,
  fontWeight: 700,
  letterSpacing: '-0.5px',
}

const descStyle: React.CSSProperties = {
  fontSize: 15,
  lineHeight: 1.6,
  color: '#444',
  marginTop: 8,
}

const cardStyle: React.CSSProperties = {
  background: '#fff',
  border: '1px solid #e0e0e0',
  borderRadius: 10,
  padding: '24px',
  display: 'flex',
  flexDirection: 'column',
  gap: 12,
}

const cardTitleStyle: React.CSSProperties = {
  fontSize: 13,
  fontWeight: 600,
  textTransform: 'uppercase',
  letterSpacing: '0.05em',
  color: '#666',
}

const selectedStyle: React.CSSProperties = {
  fontSize: 14,
  color: '#555',
  minHeight: 20,
}

const selectedValueStyle: React.CSSProperties = {
  fontWeight: 600,
  color: '#111',
}

export default function App() {
  const [selectedLanguage, setSelectedLanguage] = useState<string | null>(null)
  const [selectedCity, setSelectedCity] = useState<string | null>(null)

  return (
    <div style={containerStyle}>
      <header>
        <h1 style={headingStyle}>Autocomplete Challenge</h1>
        <p style={descStyle}>
          Implement the <code>&lt;Autocomplete&gt;</code> component in{' '}
          <code>src/Autocomplete.tsx</code>. It should filter the provided{' '}
          <code>data</code> list as the user types, support keyboard navigation
          (ArrowUp / ArrowDown / Enter / Escape), handle click-outside to close,
          and expose the correct ARIA attributes for screen reader accessibility.
          See <code>CHALLENGE.md</code> for the full requirements.
        </p>
      </header>

      <div style={cardStyle}>
        <span style={cardTitleStyle}>Programming Languages</span>
        <Autocomplete
          data={PROGRAMMING_LANGUAGES}
          placeholder="Search languages…"
          onSelect={setSelectedLanguage}
          id="languages"
        />
        <p style={selectedStyle}>
          Selected value:{' '}
          {selectedLanguage ? (
            <span style={selectedValueStyle}>{selectedLanguage}</span>
          ) : (
            <span style={{ color: '#aaa' }}>none</span>
          )}
        </p>
      </div>

      <div style={cardStyle}>
        <span style={cardTitleStyle}>US Cities</span>
        <Autocomplete
          data={US_CITIES}
          placeholder="Search cities…"
          onSelect={setSelectedCity}
          id="cities"
        />
        <p style={selectedStyle}>
          Selected value:{' '}
          {selectedCity ? (
            <span style={selectedValueStyle}>{selectedCity}</span>
          ) : (
            <span style={{ color: '#aaa' }}>none</span>
          )}
        </p>
      </div>
    </div>
  )
}
