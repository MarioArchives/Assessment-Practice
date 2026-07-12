import React, { useState } from 'react';
import Tabs from './Tabs';

// ─── Demo 1: Uncontrolled tabs ───────────────────────────────────────────────

function UncontrolledDemo() {
  return (
    <section style={{ marginBottom: '3rem' }}>
      <h2 style={{ marginBottom: '0.5rem' }}>Demo 1 – Uncontrolled Tabs</h2>
      <p style={{ marginBottom: '1rem', color: '#555', fontSize: '0.9rem' }}>
        Uses <code>defaultValue</code> to set the initial active tab. The component
        owns its own state — no external wiring needed. The "Security" tab is{' '}
        <strong>disabled</strong>: it cannot be clicked or reached via arrow keys.
        Try keyboard navigation: Tab into the tab list, then use ArrowLeft/Right,
        Home, End, and Enter/Space.
      </p>

      <Tabs defaultValue="profile">
        <Tabs.List aria-label="Account sections (uncontrolled)">
          <Tabs.Tab value="profile">Profile</Tabs.Tab>
          <Tabs.Tab value="billing">Billing</Tabs.Tab>
          <Tabs.Tab value="notifications">Notifications</Tabs.Tab>
          <Tabs.Tab value="security" disabled>
            Security (disabled)
          </Tabs.Tab>
        </Tabs.List>

        <Tabs.Panels>
          <Tabs.Panel value="profile">
            <h3>Profile Settings</h3>
            <p>
              Update your display name, avatar, and bio here. Changes are saved
              automatically when you leave the field.
            </p>
            <label style={{ display: 'block', marginTop: '1rem' }}>
              Display name
              <input
                type="text"
                defaultValue="Ada Lovelace"
                style={{ display: 'block', marginTop: '0.25rem', padding: '0.4rem 0.6rem' }}
              />
            </label>
          </Tabs.Panel>

          <Tabs.Panel value="billing">
            <h3>Billing &amp; Subscription</h3>
            <p>Current plan: <strong>Pro – $12 / month</strong></p>
            <ul>
              <li>Unlimited projects</li>
              <li>Priority support</li>
              <li>Advanced analytics</li>
            </ul>
            <button style={{ marginTop: '0.75rem', padding: '0.4rem 1rem' }}>
              Manage subscription
            </button>
          </Tabs.Panel>

          <Tabs.Panel value="notifications">
            <h3>Notification Preferences</h3>
            <fieldset style={{ border: 'none', padding: 0, margin: 0 }}>
              <legend style={{ fontWeight: 600, marginBottom: '0.5rem' }}>
                Notify me about:
              </legend>
              {['New comments', 'Mentions', 'Weekly digest', 'Security alerts'].map(
                (label) => (
                  <label
                    key={label}
                    style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.4rem' }}
                  >
                    <input type="checkbox" defaultChecked={label !== 'Weekly digest'} />
                    {label}
                  </label>
                ),
              )}
            </fieldset>
          </Tabs.Panel>

          <Tabs.Panel value="security">
            <h3>Security</h3>
            <p>This panel is unreachable because the tab is disabled.</p>
          </Tabs.Panel>
        </Tabs.Panels>
      </Tabs>
    </section>
  );
}

// ─── Demo 2: Controlled tabs ─────────────────────────────────────────────────

const STEPS = ['Overview', 'Configuration', 'Review', 'Deploy'] as const;
type Step = (typeof STEPS)[number];

function ControlledDemo() {
  const [activeTab, setActiveTab] = useState<Step>('Overview');

  return (
    <section style={{ marginBottom: '3rem' }}>
      <h2 style={{ marginBottom: '0.5rem' }}>Demo 2 – Controlled Tabs</h2>
      <p style={{ marginBottom: '1rem', color: '#555', fontSize: '0.9rem' }}>
        The active tab is driven by external React state via the <code>value</code>{' '}
        and <code>onChange</code> props. The dropdown <em>outside</em> the{' '}
        <code>&lt;Tabs&gt;</code> component syncs bidirectionally: changing the tab
        updates the dropdown, and changing the dropdown updates the tab.
      </p>

      {/* External control outside the Tabs component */}
      <div style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
        <label htmlFor="step-select" style={{ fontWeight: 600 }}>
          External control:
        </label>
        <select
          id="step-select"
          value={activeTab}
          onChange={(e) => setActiveTab(e.target.value as Step)}
          style={{ padding: '0.35rem 0.6rem' }}
        >
          {STEPS.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>
        <span style={{ color: '#777', fontSize: '0.85rem' }}>
          Active tab state: <code>{activeTab}</code>
        </span>
      </div>

      <Tabs value={activeTab} onChange={(v) => setActiveTab(v as Step)}>
        <Tabs.List aria-label="Deployment wizard steps">
          {STEPS.map((step) => (
            <Tabs.Tab key={step} value={step}>
              {step}
            </Tabs.Tab>
          ))}
        </Tabs.List>

        <Tabs.Panels>
          <Tabs.Panel value="Overview">
            <h3>Overview</h3>
            <p>
              This wizard will guide you through deploying your application to
              production. Make sure you have reviewed the checklist before
              continuing.
            </p>
            <ul>
              <li>All tests passing</li>
              <li>Environment variables set</li>
              <li>Database migrations ready</li>
            </ul>
          </Tabs.Panel>

          <Tabs.Panel value="Configuration">
            <h3>Configuration</h3>
            <p>Choose the target environment and region for your deployment.</p>
            <label style={{ display: 'block', marginBottom: '0.75rem' }}>
              Environment
              <select style={{ display: 'block', marginTop: '0.25rem', padding: '0.35rem 0.6rem' }}>
                <option>production</option>
                <option>staging</option>
              </select>
            </label>
            <label style={{ display: 'block' }}>
              Region
              <select style={{ display: 'block', marginTop: '0.25rem', padding: '0.35rem 0.6rem' }}>
                <option>us-east-1</option>
                <option>eu-west-1</option>
                <option>ap-southeast-1</option>
              </select>
            </label>
          </Tabs.Panel>

          <Tabs.Panel value="Review">
            <h3>Review</h3>
            <dl style={{ display: 'grid', gridTemplateColumns: 'auto 1fr', gap: '0.4rem 1.5rem' }}>
              <dt style={{ fontWeight: 600 }}>Environment</dt>
              <dd>production</dd>
              <dt style={{ fontWeight: 600 }}>Region</dt>
              <dd>us-east-1</dd>
              <dt style={{ fontWeight: 600 }}>Image tag</dt>
              <dd>sha256:a1b2c3d4</dd>
            </dl>
          </Tabs.Panel>

          <Tabs.Panel value="Deploy">
            <h3>Deploy</h3>
            <p>Click the button below to trigger the deployment pipeline.</p>
            <button
              style={{
                marginTop: '0.5rem',
                padding: '0.5rem 1.5rem',
                background: '#2563eb',
                color: '#fff',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer',
                fontWeight: 600,
              }}
            >
              Deploy to production
            </button>
          </Tabs.Panel>
        </Tabs.Panels>
      </Tabs>
    </section>
  );
}

// ─── Demo 3: Nested tabs ─────────────────────────────────────────────────────

function NestedDemo() {
  return (
    <section style={{ marginBottom: '3rem' }}>
      <h2 style={{ marginBottom: '0.5rem' }}>Demo 3 – Nested Tabs</h2>
      <p style={{ marginBottom: '1rem', color: '#555', fontSize: '0.9rem' }}>
        A <code>&lt;Tabs&gt;</code> instance nested inside a panel of another{' '}
        <code>&lt;Tabs&gt;</code> instance. Each has its own independent context —
        activating a tab in the inner set does not affect the outer set, and vice
        versa. Keyboard navigation must stay contained to the correct tab list.
      </p>

      <Tabs defaultValue="docs">
        <Tabs.List aria-label="Outer tab group">
          <Tabs.Tab value="docs">Documentation</Tabs.Tab>
          <Tabs.Tab value="api">API Reference</Tabs.Tab>
          <Tabs.Tab value="changelog">Changelog</Tabs.Tab>
        </Tabs.List>

        <Tabs.Panels>
          <Tabs.Panel value="docs">
            <h3 style={{ marginTop: 0 }}>Documentation</h3>
            <p style={{ marginBottom: '1rem' }}>
              The documentation is split by topic. Use the inner tabs to navigate.
            </p>

            {/* ── Inner tabs ── */}
            <Tabs defaultValue="getting-started">
              <Tabs.List aria-label="Documentation sections (inner)">
                <Tabs.Tab value="getting-started">Getting Started</Tabs.Tab>
                <Tabs.Tab value="guides">Guides</Tabs.Tab>
                <Tabs.Tab value="concepts">Core Concepts</Tabs.Tab>
              </Tabs.List>

              <Tabs.Panels>
                <Tabs.Panel value="getting-started">
                  <h4>Getting Started</h4>
                  <p>Install the package and follow the quickstart tutorial.</p>
                  <pre
                    style={{
                      background: '#f3f4f6',
                      padding: '0.75rem',
                      borderRadius: '4px',
                      fontSize: '0.85rem',
                    }}
                  >
                    npm install my-library
                  </pre>
                </Tabs.Panel>

                <Tabs.Panel value="guides">
                  <h4>Guides</h4>
                  <ul>
                    <li>Authentication guide</li>
                    <li>Data fetching patterns</li>
                    <li>Testing best practices</li>
                  </ul>
                </Tabs.Panel>

                <Tabs.Panel value="concepts">
                  <h4>Core Concepts</h4>
                  <p>
                    Learn about the compound component pattern, context propagation,
                    and the roving tabindex technique used in this very component.
                  </p>
                </Tabs.Panel>
              </Tabs.Panels>
            </Tabs>
          </Tabs.Panel>

          <Tabs.Panel value="api">
            <h3 style={{ marginTop: 0 }}>API Reference</h3>
            <p>Full API documentation for every exported component and hook.</p>
          </Tabs.Panel>

          <Tabs.Panel value="changelog">
            <h3 style={{ marginTop: 0 }}>Changelog</h3>
            <ul>
              <li><strong>v1.2.0</strong> – Added controlled mode support</li>
              <li><strong>v1.1.0</strong> – Keyboard navigation improvements</li>
              <li><strong>v1.0.0</strong> – Initial release</li>
            </ul>
          </Tabs.Panel>
        </Tabs.Panels>
      </Tabs>
    </section>
  );
}

// ─── App root ────────────────────────────────────────────────────────────────

export default function App() {
  return (
    <div
      style={{
        fontFamily: 'system-ui, sans-serif',
        maxWidth: '860px',
        margin: '0 auto',
        padding: '2rem 1.5rem',
        color: '#111',
      }}
    >
      <header style={{ marginBottom: '2.5rem' }}>
        <h1 style={{ margin: 0, fontSize: '1.6rem' }}>
          Challenge 10 – Compound Component Tabs
        </h1>
        <p style={{ marginTop: '0.5rem', color: '#555' }}>
          Implement <code>src/Tabs.tsx</code> so that all three demos below work
          correctly, including keyboard navigation and full ARIA support.
        </p>
      </header>

      <UncontrolledDemo />
      <ControlledDemo />
      <NestedDemo />
    </div>
  );
}
