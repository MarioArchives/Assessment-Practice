# Challenge 10 – Compound Component Tabs

## Overview

Build a fully accessible `<Tabs>` system using the **compound component pattern** with React Context. The component must support both **controlled** and **uncontrolled** modes, full **keyboard navigation**, and **disabled tabs** — all without any accessible component library.

The compound component pattern lets consumers compose the UI in a declarative, ergonomic way while the root component owns all shared state and distributes it via context. No prop drilling allowed.

---

## Components to Implement

### `Tabs` (root provider)

The root component manages state and provides context to all descendants.

**Props:**
- `defaultValue?: string` — initial active tab for uncontrolled mode
- `value?: string` — active tab for controlled mode (makes the component controlled when provided)
- `onChange?: (value: string) => void` — callback fired when the active tab changes (used in controlled mode)
- `children: React.ReactNode`

When `value` is provided, the component is in **controlled mode**: it must not update its own internal state, but must call `onChange` and let the parent drive the value.

When only `defaultValue` is provided (or neither), the component is in **uncontrolled mode**: it manages its own internal state starting at `defaultValue`.

---

### `Tabs.List`

Wraps the tab buttons. Renders a `<div role="tablist">` (or `<div>` with the role attribute). Handles keyboard navigation for all child `Tabs.Tab` elements.

**Props:**
- `children: React.ReactNode`
- `aria-label?: string` — accessible label for the tablist

---

### `Tabs.Tab`

Renders an individual tab button.

**Props:**
- `value: string` — the value this tab represents; used to match against the active value
- `children: React.ReactNode` — tab label content
- `disabled?: boolean` — when true, the tab cannot receive focus via arrow keys and cannot be activated

---

### `Tabs.Panels`

A simple wrapper around all panel elements. No logic required beyond rendering children.

**Props:**
- `children: React.ReactNode`

---

### `Tabs.Panel`

Renders an individual content panel. Panels that do not match the active value must be hidden — not just visually, but in the accessibility tree. Use the `hidden` attribute or `aria-hidden="true"` rather than `display: none` via CSS alone (the `hidden` HTML attribute is preferred as it removes the element from the accessibility tree automatically).

**Props:**
- `value: string` — the value this panel represents
- `children: React.ReactNode`

---

## Keyboard Navigation

All keyboard handling lives in `Tabs.List` (on the container, using a single `onKeyDown` handler — do not attach individual handlers to each tab button for navigation).

| Key | Behaviour |
|-----|-----------|
| `ArrowRight` | Move focus to the next tab, skipping disabled tabs. Wraps from last to first. |
| `ArrowLeft` | Move focus to the previous tab, skipping disabled tabs. Wraps from first to last. |
| `Home` | Move focus to the first non-disabled tab. |
| `End` | Move focus to the last non-disabled tab. |
| `Enter` / `Space` | Activate the currently focused tab (set it as the active value). |

**Important distinction:** Arrow keys move *focus*, not the active tab. `Enter`/`Space` activates the focused tab. This follows the [ARIA Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) "manual activation" model.

---

## ARIA Requirements

Your implementation must satisfy the following ARIA attributes for screen reader compatibility. These will be verified with axe-core.

- `role="tablist"` on the list container
- `role="tab"` on each tab button
- `aria-selected="true"` on the currently active tab; `aria-selected="false"` on all others
- `aria-disabled="true"` on disabled tabs (do not use the native `disabled` attribute on the button — it removes it from the tab sequence entirely in some browsers, which interferes with keyboard navigation; use `aria-disabled` instead and handle the behaviour manually)
- `role="tabpanel"` on each panel
- `aria-controls="<panel-id>"` on each tab, pointing to its corresponding panel's `id`
- `aria-labelledby="<tab-id>"` on each panel, pointing back to its corresponding tab's `id`
- `tabIndex={0}` on the active tab; `tabIndex={-1}` on all other tabs (this is the "roving tabindex" pattern)
- Panels not matching the active value must be hidden from both the visual and accessibility tree — use the `hidden` HTML attribute on the panel element

### Generating stable IDs

Use `React.useId()` in the `Tabs` root to generate a `baseId`. Derive tab and panel IDs from it:
- Tab button id: `${baseId}-tab-${value}`
- Panel id: `${baseId}-panel-${value}`

This ensures IDs are stable across renders and unique when multiple `<Tabs>` instances exist on the same page.

---

## Constraints

- **No accessible component libraries.** Radix UI, Headless UI, Reach UI, Ark UI, and similar libraries are all off-limits.
- **No prop drilling.** All shared state (active value, setter, base id) must travel through React Context only. Sub-components must not accept active-state props directly from a parent component.
- **The compound API shape must match exactly** as described. Consumers must be able to write:

```tsx
<Tabs defaultValue="profile">
  <Tabs.List aria-label="Account sections">
    <Tabs.Tab value="profile">Profile</Tabs.Tab>
    <Tabs.Tab value="billing">Billing</Tabs.Tab>
    <Tabs.Tab value="security" disabled>Security</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panels>
    <Tabs.Panel value="profile">Profile content</Tabs.Panel>
    <Tabs.Panel value="billing">Billing content</Tabs.Panel>
    <Tabs.Panel value="security">Security content</Tabs.Panel>
  </Tabs.Panels>
</Tabs>
```

---

## Implementation Hints

1. **Context shape** — create a `TabsContext` that holds `{ activeValue, setActiveValue, baseId }`. The `setActiveValue` function should handle the controlled/uncontrolled split: in controlled mode, call `onChange` and do nothing else; in uncontrolled mode, update the internal state.

2. **Roving tabindex** — in `Tabs.Tab`, set `tabIndex={isActive ? 0 : -1}`. Do not add `tabIndex={0}` to disabled tabs.

3. **Focus management** — in `Tabs.List`, attach a `ref` to the list container and query `[role="tab"]:not([aria-disabled="true"])` to find focusable tabs, then call `.focus()` on the target element. Alternatively, collect refs to each tab button in a `useRef` registry inside context.

4. **Skipping disabled tabs** — when navigating with arrow keys, walk the list of tab value refs and skip any that are marked disabled. Continue walking until a non-disabled tab is found or the list is exhausted.

5. **`aria-disabled` vs `disabled`** — use `aria-disabled="true"` on the button element and check `event.target` or your own state to prevent activation. Never use the native `disabled` boolean on a tab button used with roving tabindex.

6. **Panel visibility** — add the `hidden` attribute conditionally: `<div role="tabpanel" hidden={!isActive} ...>`. This is more robust than `display: none` from a CSS class.

7. **Nested tabs** — if you support nested `<Tabs>` instances (bonus), each must have its own context. Because `React.createContext` returns a single context object, nested providers will correctly shadow the parent context for their descendants.

---

## Evaluation Criteria

| Criterion | Weight |
|-----------|--------|
| Context-only data flow — no prop drilling at all | High |
| Uncontrolled mode works with `defaultValue` | High |
| Controlled mode works — external state drives the tab, `onChange` fires | High |
| Keyboard navigation wraps correctly and skips disabled tabs | High |
| All required ARIA attributes present and correct (verify with axe) | High |
| Disabled tabs cannot be activated by click or keyboard | Medium |
| Roving tabindex implemented correctly | Medium |
| Clean TypeScript types — no `any`, props interfaces exported | Medium |
| Compound API is ergonomic and matches the prescribed shape | Medium |
| Nested tabs work independently without context bleed | Bonus |
