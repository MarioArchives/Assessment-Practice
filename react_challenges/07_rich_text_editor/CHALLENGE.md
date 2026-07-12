# Challenge 07 – Rich Text Editor

## Overview

Build a `<RichTextEditor value onChange />` component backed by a `contenteditable` div. The component must support **bold**, **italic**, and **unordered list** toggling via both keyboard shortcuts and toolbar buttons — without reaching for any rich text library.

This challenge tests your ability to work directly with browser APIs (`contenteditable`, `execCommand`, `queryCommandState`, `Selection`) and to reason carefully about React's rendering lifecycle in the context of imperatively managed DOM.

---

## Requirements

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `string` | Yes | The current HTML content of the editor (HTML string) |
| `onChange` | `(html: string) => void` | Yes | Callback fired on every `input` event with the editor's `innerHTML` |
| `placeholder` | `string` | No | Placeholder text shown when the editor is empty |
| `readOnly` | `boolean` | No | When `true`, disables editing and hides the toolbar |
| `minHeight` | `number` | No | Minimum height of the editable area in pixels (default: `150`) |
| `maxHeight` | `number` | No | Maximum height of the editable area in pixels (optional, enables scrolling) |

### Toolbar

The toolbar must contain exactly three buttons:

1. **Bold** — labelled `B`, triggers `bold` formatting
2. **Italic** — labelled `I`, triggers `italic` formatting
3. **Unordered List** — labelled `•≡`, triggers `insertUnorderedList` formatting

Each button must visually reflect the **active state** of the format at the current cursor position or selection.

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+B` | Toggle bold on the current selection |
| `Ctrl+I` | Toggle italic on the current selection |
| `Ctrl+Shift+L` | Toggle unordered list |

All keyboard shortcuts must be intercepted with `event.preventDefault()` so the browser's default behaviour does not interfere.

### Active State Detection

Use `document.queryCommandState('bold')`, `document.queryCommandState('italic')`, and `document.queryCommandState('insertUnorderedList')` to determine whether the cursor is currently inside a formatted region. Update toolbar button styles accordingly. Listen to the `selectionchange` event on `document` to keep the toolbar in sync as the user moves the caret.

### onChange Behaviour

The `onChange` callback must fire on every `input` event (not just `blur`). Pass `editorRef.current.innerHTML` as the argument. Do **not** fire `onChange` during programmatic value syncs that originate from the parent.

### Cursor Preservation

When the parent component re-renders and passes the same `value` back in, the editor must **not** reset the cursor position. Only sync `innerHTML` from `value` when `ref.current.innerHTML !== value`. This is the most common pitfall — setting `innerHTML` unconditionally on every render causes the cursor to jump to the start.

Use `useLayoutEffect` (not `useEffect`) for the initial value sync so the DOM is ready before the browser paints.

### Placeholder

Show placeholder text when `ref.current.innerHTML` is empty or equals `<br>`. The placeholder should be styled with muted colour and positioned absolutely so it does not affect layout. Hide it as soon as the user types.

### Character Count

Display a character count below the editor. Count only the **text content** (i.e. `ref.current.textContent?.length ?? 0`), not the HTML markup. Update the count on every `input` event.

---

## Constraints

- **No rich text libraries.** Do not use Slate.js, Quill, TipTap, ProseMirror, Draft.js, Lexical, or any library that abstracts `contenteditable`.
- Use raw `contenteditable` + `document.execCommand` only.
- `execCommand` is marked deprecated in the MDN spec but remains universally supported across all major browsers. It is the **intended approach** for this exercise. Do not reach for `Selection` and `Range` manipulation to replicate what `execCommand` does for free.
- Do not use `dangerouslySetInnerHTML` on every render — only on mount (or never, if you use `useLayoutEffect` to set `innerHTML` imperatively). Re-setting `innerHTML` via React props on every render is the anti-pattern this challenge is designed to surface.

---

## Hints

- Use `useRef` to hold the DOM reference to the `contenteditable` div.
- Set `innerHTML` imperatively inside a `useLayoutEffect` on mount (with an empty dependency array), then let `contenteditable` own the DOM from that point forward.
- To avoid cursor jumps on subsequent renders, guard the sync: only write `ref.current.innerHTML = value` when `ref.current.innerHTML !== value`.
- Listen for `selectionchange` on `document` (not the editor element) inside a `useEffect` to update the toolbar active state. Remember to remove the listener on cleanup.
- `document.queryCommandState` takes a string command name: `'bold'`, `'italic'`, `'insertUnorderedList'`.
- For the placeholder, consider using a CSS `::before` pseudo-element with `content: attr(data-placeholder)` when the editor is empty, or manage it with a React state boolean.
- The `input` event on a `contenteditable` element bubbles and fires reliably after every change; prefer it over `keyup` or `keydown` for triggering `onChange`.
- When `readOnly` is `true`, set `contentEditable="false"` on the div and conditionally render the toolbar as `null`.

---

## Evaluation Criteria

| Criterion | What reviewers look for |
|-----------|------------------------|
| Formatting correctness | Bold, italic, and list toggling work via both keyboard and toolbar |
| Keyboard shortcuts | All three shortcuts correctly call `execCommand` and prevent default |
| Active state | Toolbar buttons reflect the format state at the current cursor position |
| Cursor stability | Cursor does not jump when the parent re-renders with the same value |
| onChange correctness | Callback fires on every keystroke with accurate `innerHTML` |
| Placeholder | Appears when empty, disappears on first input |
| readOnly mode | Disables editing and hides toolbar |
| Character count | Updates live, counts text characters not HTML characters |
| Code structure | Clean separation of concerns, no magic numbers, typed props |
| TypeScript | No `any`, no `@ts-ignore`, all props and internal state fully typed |

---

## Getting Started

```bash
npm install
npm run dev
```

Open `http://localhost:5173` and start building. The demo harness in `src/App.tsx` shows two editor instances: one controlled (with raw HTML output) and one preview. Use the "Load sample content" button to pre-populate with formatted HTML and verify your cursor-preservation logic.
