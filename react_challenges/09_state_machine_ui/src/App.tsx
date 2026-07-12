import CheckoutFlow from './CheckoutFlow';

export default function App() {
  return (
    <div style={{ minHeight: '100vh', background: '#f5f5f5', display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '40px 16px' }}>
      <p style={{ color: '#888', fontSize: '14px', marginBottom: '32px', textAlign: 'center', maxWidth: '480px' }}>
        Challenge 09 — State Machine Checkout UI. Implement the state machine, the{' '}
        <code>useMachine</code> hook, and all checkout screens in{' '}
        <code>src/machine.ts</code> and <code>src/CheckoutFlow.tsx</code>.
      </p>
      <CheckoutFlow />
    </div>
  );
}
