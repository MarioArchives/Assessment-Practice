# Challenge 01 – Accessible Autocomplete

## Overview

Your task is to build a reusable `<Autocomplete data={string[]} />` React component that behaves like a proper accessible combobox. Autocomplete widgets are everywhere — search bars, address pickers, tag selectors — and implementing one correctly is deceptively tricky. Getting the keyboard navigation right, keeping screen readers informed at every step, and handling edge cases gracefully separates a polished implementation from a rushed one.

The component accepts an array of string options via a `data` prop and filters them in real time as the user types. It must be fully operable by keyboard alone and must expose the correct ARIA attributes so assistive technologies can announce state changes without visual inspection.

You are implementing the component in `src/Autocomplete.tsx`. A demo harness in `src/App.tsx` already mounts two instances so you can test interactively. The props interface (`AutocompleteProps`) is already defined and exported from the stub — do not change its shape.

---

## Requirements

- **Input rendering**: Render a standard `<input type="text">` element. The input must be the only focusable element in the component when the dropdown is closed.
- **Filtering**: As the user types, filter the `data` array case-insensitively and display matching options. Filtering must happen on every keystroke. An empty input may show all options or none — either is acceptable, but be consistent.
- **Dropdown list**: Render the filtered matches in a list below the input. The list must not be present in the DOM (or must be hidden from assistive technology) when there are no matches or when the dropdown is closed.
- **"No results" state**: When the user has typed something and no options match, display a "No results" message inside the dropdown area.
- **Keyboard navigation — ArrowDown**: Move the highlighted option one position downward. When the last option is highlighted, wrap to the first, or stay at the last — your choice, but be consistent.
- **Keyboard navigation — ArrowUp**: Move the highlighted option one position upward. When the first option is highlighted, wrap to the last, or stay at the first — your choice, but be consistent.
- **Keyboard navigation — Enter**: If an option is highlighted, select it: write its value into the input, close the dropdown, and call `onSelect` if provided.
- **Keyboard navigation — Escape**: Close the dropdown without selecting anything. The input retains whatever the user typed.
- **Mouse interaction**: Clicking an option selects it the same way Enter does — updates the input value, closes the dropdown, calls `onSelect`.
- **Click-outside to close**: Clicking anywhere outside the component closes the dropdown. The input value should remain unchanged.
- **`aria-activedescendant`**: The `<input>` must set `aria-activedescendant` to the `id` of the currently highlighted option element while the dropdown is open and an option is highlighted. Clear it (or omit it) when nothing is highlighted or the dropdown is closed.
- **`role="combobox"`**: Apply `role="combobox"` to the `<input>` element.
- **`aria-expanded`**: Set `aria-expanded="true"` on the combobox input when the dropdown is open, `aria-expanded="false"` when closed.
- **`aria-controls`**: Set `aria-controls` on the input pointing to the `id` of the listbox element.
- **`role="listbox"`**: The dropdown container must have `role="listbox"`.
- **`role="option"`**: Each item in the dropdown list must have `role="option"`.
- **`aria-selected`**: Set `aria-selected="true"` on the currently highlighted option; `aria-selected="false"` on all others.
- **Selecting updates the input**: After a selection, the input's value becomes the selected string and the dropdown closes.
- **`onSelect` callback**: Call the `onSelect` prop (if provided) with the selected string whenever a selection is made.

---

## Constraints

- **No external UI libraries.** Do not install or import Headless UI, Radix UI, Downshift, React Aria, React Select, or any other component library that provides autocomplete/combobox primitives. The goal is to implement the behaviour from scratch.
- **No CSS-in-JS.** Do not use styled-components, Emotion, vanilla-extract, or similar. Inline styles or a plain `.css` file are both acceptable.
- **Plain React + TypeScript only.** You may use any React hook from the standard library. External state management libraries (Redux, Zustand, Jotai, etc.) are unnecessary and should be avoided.
- **No modifications to `App.tsx` or `main.tsx`** beyond what is needed to wire up `onSelect`. The `AutocompleteProps` interface shape in `Autocomplete.tsx` must remain stable.

---

## Hints

- **Click-outside detection**: Use a `ref` attached to a wrapper `<div>` around the entire component. In a `useEffect`, attach a `mousedown` listener to `document` that checks whether `ref.current.contains(event.target)` — if not, close the dropdown. Remember to remove the listener on cleanup.
- **ARIA id linkage**: Use React's `useId()` hook to generate stable, unique ids for the listbox and each option. This prevents collisions when multiple instances of `<Autocomplete>` exist on the same page — as is the case in the demo harness.
- **State shape**: Keep `activeIndex` (a `number | null`) separate from `inputValue` (a `string`). Do not conflate them. Reset `activeIndex` to `null` whenever the input value changes so keyboard navigation always starts fresh.
- **Preventing cursor jump**: Call `e.preventDefault()` inside the `keydown` handler for `ArrowUp` and `ArrowDown`. Without this, the browser moves the text cursor to the start or end of the input, which is surprising and disruptive.
- **Filtered list stability**: Derive the filtered list directly in the render function (or with `useMemo`) rather than storing it in state. Storing filtered results in state means you need an extra `useEffect` to keep them in sync, which introduces off-by-one render issues.
- **Closing vs clearing**: Escape should close the dropdown but NOT clear the input. This matches the ARIA Authoring Practices Guide (APG) pattern for combobox with list autocomplete.
- **`aria-autocomplete`**: For completeness, set `aria-autocomplete="list"` on the combobox input to signal to screen readers that a list of suggestions filters as the user types.

---

## Evaluation Criteria

1. **Functional filtering**: Does typing progressively narrow the list? Is the match case-insensitive? Does it handle the empty-input state gracefully?
2. **Keyboard navigation**: Can a user operate the entire widget without touching the mouse? Does focus never escape the input unexpectedly? Do arrow keys wrap (or clamp) consistently?
3. **ARIA correctness**: Run the page through the [axe DevTools browser extension](https://www.deque.com/axe/devtools/) or Chrome's built-in accessibility tree. Zero violations is the target. Verify with a screen reader (VoiceOver, NVDA, or JAWS) that option changes are announced as you arrow through the list.
4. **Edge cases**:
   - An empty `data` array — no dropdown, no crash.
   - All options filtered out — "No results" shown, no JS error.
   - Rapid typing — no stale closures, no mis-highlighted options.
   - Two instances on the same page — independent state, no id collisions.
5. **Code quality**: Clear naming, minimal state, no unnecessary `useEffect`s, TypeScript strict mode with zero `any` escapes.
