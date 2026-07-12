# Challenge 09 – State Machine Checkout UI

## Overview

In this challenge you will implement a multi-screen checkout flow driven by an **explicit state machine** that you define yourself as a plain TypeScript object — no XState, Robot, Zag.js, or any state-machine library allowed.

The goal is to practice the core idea behind all state machines: a single declarative data structure is the single source of truth for which transitions are valid, and the UI simply reflects the current state without embedding transition logic of its own.

You will write:

1. A `StateMachine` generic type and a `checkoutMachine` constant in `src/machine.ts`.
2. A `useMachine` React hook (also in `src/machine.ts`) that drives the machine with `useState`.
3. The full `CheckoutFlow` component tree in `src/CheckoutFlow.tsx`, with one screen per state.

---

## States and Transitions

The machine has six states. The initial state is `cart`.

```
cart
  PROCEED          → shipping
  CANCEL           → cart       (no-op; stays in same state)

shipping
  SUBMIT_SHIPPING  → payment
  BACK             → cart

payment
  SUBMIT_PAYMENT   → confirming
  BACK             → shipping

confirming
  PAYMENT_SUCCESS  → confirmed
  PAYMENT_FAILURE  → failed

confirmed
  RESTART          → cart

failed
  RETRY            → payment
  RESTART          → cart
```

Any event not listed for the current state must be silently ignored — the machine stays in the current state.

---

## File-by-File Requirements

### `src/machine.ts`

- **`StateMachine<S, E>`** — a mapped type where each key is a state `S` and the value is a partial record mapping events `E` to the next state `S`. Both `S` and `E` are constrained to `string`.
- **`checkoutMachine`** — a constant of type `StateMachine<CheckoutState, CheckoutEvent>` that encodes all transitions in the table above. No logic, just data.
- **`useMachine<S, E>(machine, initialState)`** — a generic hook that:
  - Holds the current state with `useState(initialState)`.
  - Returns a tuple `[currentState, send]`.
  - `send(event)` looks up `machine[currentState]?.[event]`. If a next state exists it calls `setState` with it; otherwise it does nothing (invalid transition guard).
  - The hook is completely generic — it must work for any `StateMachine`, not just `checkoutMachine`.

### `src/CheckoutFlow.tsx`

Implement the `CheckoutFlow` default export. Inside it, call `useMachine(checkoutMachine, 'cart')` to get `[state, send]`. Then render the correct screen based on `state`. **No screen component may call `send` with a transition it is not supposed to trigger — the allowed events for each state come from the machine, not from component logic.**

#### Progress Breadcrumb

Render a breadcrumb at the top showing the ordered steps: Cart → Shipping → Payment → Confirming → Done. Highlight the step that matches the current state. Hide the breadcrumb on the `confirmed` and `failed` terminal states, or show it in a completed/failed style — your choice.

#### Cart Screen (`state === 'cart'`)

- Display the three items from `DEMO_CART` (name, unit price, quantity, line total).
- Show a subtotal, a tax line (8.5 % of subtotal), and a grand total.
- A **"Proceed to Checkout"** button sends `PROCEED`.
- Optionally a **"Cancel"** button sends `CANCEL` (which is a no-op by design — good for demonstrating the guard).

#### Shipping Screen (`state === 'shipping'`)

- A form with fields: Full Name, Street Address, City, ZIP / Postal Code, Country.
- All fields are required. Validate on submit: if any field is empty, show an inline error and do **not** send the event.
- A **"Continue to Payment"** button sends `SUBMIT_SHIPPING` (only after validation passes).
- A **"← Back"** link/button sends `BACK`.

#### Payment Screen (`state === 'payment'`)

- A mock credit card form with fields: Name on Card, Card Number, Expiry (MM/YY), CVV.
- Validate format on submit:
  - Card number: 16 digits (spaces allowed for display).
  - Expiry: matches `MM/YY` pattern, month 01–12.
  - CVV: 3–4 digits.
- A **"Place Order"** button that, when validation passes:
  1. Sends `SUBMIT_PAYMENT` to move the machine to `confirming`.
  2. Calls `processPayment(data)` from `src/mockApi.ts`.
  3. When the promise resolves, sends either `PAYMENT_SUCCESS` or `PAYMENT_FAILURE` based on `result.success`.
- A **"← Back"** link/button sends `BACK`.
- Store the returned `orderNumber` or `error` somewhere (component state or a ref) so the subsequent screen can display it.

#### Confirming Screen (`state === 'confirming'`)

- Show an animated spinner (CSS animation is fine — no library needed).
- Show the text **"Processing your payment…"**.
- No buttons. The machine will transition automatically when `processPayment` resolves.

#### Confirmed Screen (`state === 'confirmed'`)

- Show a success icon or checkmark.
- Show **"Order confirmed!"** and the order number returned by `processPayment`.
- A **"Continue Shopping"** button sends `RESTART`, returning to `cart`.

#### Failed Screen (`state === 'failed'`)

- Show an error icon.
- Show **"Payment failed"** and the error message returned by `processPayment`.
- A **"Try Again"** button sends `RETRY` (goes back to `payment`).
- A **"Start Over"** button sends `RESTART` (goes back to `cart`).

---

## Constraints

- **No state machine libraries.** XState, Robot, Zag.js, and equivalents are banned. The `checkoutMachine` object and `useMachine` hook must be hand-rolled.
- **No form libraries.** React Hook Form, Formik, and equivalents are banned. Use controlled inputs with `useState`.
- **No UI component libraries** for the core challenge logic. Minimal inline styles or a plain CSS file are fine.
- **The machine is the single source of truth.** A UI component must never hard-code a target state — it can only call `send(event)`. Which event is valid in which state is dictated solely by `checkoutMachine`.
- **TypeScript strict mode is on.** The stub `tsconfig.json` enables `"strict": true`. Your types must satisfy the compiler without casting to `any`.

---

## Hints

- `StateMachine<S extends string, E extends string>` can be written as `{ [state in S]?: Partial<Record<E, S>> }`.
- Inside `useMachine`, the core of `send` is one line: `setState(prev => machine[prev]?.[event] ?? prev)`.  Using the functional form of `setState` avoids stale-closure issues.
- Keep `checkoutMachine` and the type aliases in `machine.ts`; keep all React components in `CheckoutFlow.tsx`. `App.tsx` is just a thin harness.
- For the async payment flow, send `SUBMIT_PAYMENT` *before* calling `processPayment` so the machine enters `confirming` immediately and the spinner appears. Then send `PAYMENT_SUCCESS` or `PAYMENT_FAILURE` when the promise settles.
- Store `orderNumber` and `error` in a `useRef` or a sibling `useState` inside `CheckoutFlow` (not inside the machine) — the machine only tracks state transitions, not data.
- The spinner can be a `<div>` with `border-radius: 50%`, a partially transparent border, and a CSS `@keyframes` rotation. No SVG or library required.

---

## Evaluation Criteria

| Area | What we look for |
|---|---|
| Machine definition | `checkoutMachine` is a pure data object — no functions, no logic |
| `useMachine` hook | Generic, reusable, correct guard for invalid events |
| Transition correctness | All transitions in the table work; invalid events are silently ignored |
| Async integration | `confirming` state is entered before the API call; success/failure events are sent after |
| UI completeness | Each state renders the correct screen with correct interactions |
| Separation of concerns | Zero transition logic inside UI components |
| TypeScript | Strict-mode clean; no `any`; generics used correctly |
| Code clarity | Machine, hook, and UI are easy to read and reason about independently |
