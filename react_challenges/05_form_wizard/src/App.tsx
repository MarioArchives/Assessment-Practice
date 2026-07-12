import FormWizard from './FormWizard'

export default function App() {
  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem',
        fontFamily: 'system-ui, sans-serif',
        backgroundColor: '#f5f5f5',
      }}
    >
      <h1 style={{ marginBottom: '0.5rem', fontSize: '1.75rem' }}>
        Form Wizard Challenge
      </h1>
      <p style={{ marginBottom: '2rem', color: '#555', textAlign: 'center' }}>
        A multi-step form with validation, data persistence across steps, and a
        mock API submission — built with pure React state.
      </p>
      <FormWizard />
    </div>
  )
}
