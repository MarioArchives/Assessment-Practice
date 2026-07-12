import DataTable from './DataTable'
import { employees, columns } from './sampleData'

export default function App() {
  return (
    <div style={{ maxWidth: 1100, margin: '0 auto', padding: '2rem 1rem', fontFamily: 'system-ui, sans-serif' }}>
      <h1 style={{ fontSize: '1.75rem', fontWeight: 700, marginBottom: '0.5rem' }}>
        Employee Directory
      </h1>
      <p style={{ color: '#6b7280', marginBottom: '1.5rem' }}>
        A demo of the <code>DataTable</code> component. Try sorting columns, filtering by name or
        department, and navigating between pages.
      </p>
      <DataTable columns={columns} rows={employees} pageSize={10} />
    </div>
  )
}
