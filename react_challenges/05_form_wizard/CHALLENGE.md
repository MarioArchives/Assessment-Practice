# Challenge 05 — Form Wizard

## Overview

Build a **multi-step form wizard** with three steps and per-step validation using **only React state** — no form libraries allowed. The goal is to demonstrate that you can manage complex form state, derive validation errors on demand, preserve data across navigation, integrate with an async API, and handle loading and error states gracefully.

---

## Steps

### Step 1 — Personal Info

Collect the following fields:

| Field       | Type   | Notes            |
|-------------|--------|------------------|
| `firstName` | text   | Required         |
| `lastName`  | text   | Required         |
| `email`     | email  | Required         |
| `phone`     | tel    | Optional         |

### Step 2 — Address

Collect the following fields:

| Field     | Type | Notes                        |
|-----------|------|------------------------------|
| `street`  | text | Required                     |
| `city`    | text | Required                     |
| `state`   | text | Required (state or province) |
| `zip`     | text | Required (zip or postal)     |
| `country` | text | Required                     |

### Step 3 — Review + Submit

Display a **read-only summary** of all data collected in steps 1 and 2. The user should be able to see everything they entered before committing to the submission. A **Submit** button triggers the API call.

---

## Requirements

### Step Indicator

- Display a step indicator at the top of the form showing the step number and a human-readable label (e.g. "Personal Info", "Address", "Review & Submit").
- The **current step** must be visually highlighted so the user always knows where they are in the flow.
- Completed steps may be styled differently from future steps if you wish.

### Navigation

- **Next button**: validates all fields in the current step. If any field fails validation, show the error messages and do **not** advance to the next step.
- **Back button**: returns to the previous step and **preserves all data** the user has already entered. No data should be wiped on backwards navigation.
- On step 3 there is no Next button — only a Submit button and a Back button.

### Validation Rules

Validation is triggered only when the user attempts to advance (or submit), not on every keystroke.

| Field                     | Rule                                                                 |
|---------------------------|----------------------------------------------------------------------|
| `firstName`, `lastName`   | Required; minimum 2 characters                                       |
| `email`                   | Required; must match a valid e-mail format (e.g. `user@example.com`)|
| `phone`                   | Optional; if provided, must match a phone pattern (digits, spaces, dashes, parentheses, `+`; at least 7 digits) |
| `street`, `city`, `zip`   | Required (non-empty after trimming)                                  |
| `state`                   | Required                                                             |
| `country`                 | Required                                                             |

Display each validation error message directly beneath the relevant input. The message must be linked to the input using `aria-describedby` for accessibility.

### Review Step

- Show all ten fields in a readable, labelled format (e.g. a definition list or a two-column table).
- The data must be read-only — no editing in place (the user can click Back to go back and edit).

### Submission

1. Call `submitFormData(data)` imported from `./mockApi`.
2. While the request is in-flight, show a **loading indicator** and disable the Submit button to prevent double-submission.
3. On **success**: show a success screen that includes the `confirmationNumber` returned by the API and a "Start Over" button.
4. On **error**: show the error message returned by the API and offer both a **Retry** button (re-submits without going back) and a "Start Over" button.

### Start Over

Clicking "Start Over" from either the success or error screen resets **all** state: form data, current step, loading state, and result — returning the user to step 1 with empty fields.

---

## Constraints

- **No form or validation libraries.** Do not use React Hook Form, Formik, Yup, Zod, vest, or any similar package.
- Use **pure React**: `useState` and/or `useReducer` only for state management.
- You may use any CSS approach (inline styles, CSS modules, plain `.css` files) — no CSS framework is required.

---

## Hints

- **Single state object**: Store all ten form values in one object (e.g. `WizardFormData`) rather than separate state variables per field. This makes it trivial to pass everything to the API at the end.
- **Derive errors on advance**: Rather than validating on every keystroke, compute a `ValidationErrors` object when the user clicks Next/Submit. Merge it into a piece of state; if the object is empty, advance.
- **`useReducer` for cleaner transitions**: If you find `useState` getting unwieldy, a reducer with action types like `SET_FIELD`, `NEXT_STEP`, `PREV_STEP`, `SUBMIT_START`, `SUBMIT_SUCCESS`, `SUBMIT_ERROR`, and `RESET` can make the state machine much easier to reason about.
- **Step indicator with `map`**: Define a simple array of step metadata (number + label) and `.map()` over it to render the indicator. Apply a CSS class or inline style based on whether the step index matches the current step.
- **Phone validation**: A reasonable regex for an optional phone field is `/^[+\d][\d\s\-().]{5,}$/` — feel free to adjust.
- **`aria-describedby`**: Set `id="firstName-error"` on the error `<span>` and `aria-describedby="firstName-error"` on the corresponding `<input>` so screen readers announce the error automatically.

---

## File Structure

```
05_form_wizard/
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── CHALLENGE.md          ← you are here
└── src/
    ├── main.tsx          ← entry point (do not modify)
    ├── App.tsx           ← shell layout (do not modify)
    ├── mockApi.ts        ← mock API (do not modify)
    └── FormWizard.tsx    ← implement this
```

---

## Evaluation Criteria

Your implementation will be assessed on:

1. **Correct validation** — all rules enforced, correct error messages shown beneath the right fields, errors cleared when the user fixes a field and re-advances.
2. **Data preservation on Back** — navigating backwards never wipes data; all fields retain their values.
3. **Loading and error states** — loading indicator shown during submission; error screen with retry; success screen with confirmation number.
4. **Accessibility** — every input has a `<label>`; every error message is linked via `aria-describedby`; the form can be navigated with a keyboard.
5. **Clean state management** — state transitions are predictable; no unnecessary re-renders; state is not duplicated.
6. **Code quality** — TypeScript types used correctly; components are readable; logic is reasonably separated from markup.

Good luck!
