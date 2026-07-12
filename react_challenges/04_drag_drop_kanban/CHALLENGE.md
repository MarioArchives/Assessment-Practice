# Challenge 04 – Drag & Drop Kanban Board

## Overview

Build a fully functional Kanban board with three columns — **Todo**, **In Progress**, and **Done** — using only the **HTML5 Drag and Drop API**. No third-party drag-and-drop libraries are permitted. Cards must be draggable both across columns and within a single column to reorder them. State must persist across page refreshes via `localStorage`.

---

## Requirements

### Columns

- Render exactly three columns with the IDs `todo`, `in-progress`, and `done`.
- Each column displays its title and a count of how many cards it currently contains.
- Each column has an **"Add Card"** button that opens an inline form (or modal) allowing the user to enter a card title and an optional description. Submitting the form appends the new card to the bottom of that column.

### Cards

- Each card displays its **title** prominently and, if present, its **description** in smaller text below.
- Each card has a **delete button** (×) that removes it permanently.
- Cards are `draggable` (the HTML attribute must be set to `"true"`).

### Drag and Drop Behaviour

- **Cross-column drag**: Dragging a card from one column and dropping it onto another column moves the card to that column. The card is inserted at the position indicated by the drop target (see below).
- **Within-column reorder**: Dragging a card within its own column and dropping it above or below another card reorders the list correctly.
- **Column drop zone indicator**: While a card is being dragged over a column, that column should display a visible highlight (e.g., a coloured border or background tint) to show it is a valid drop target.
- **Card insertion indicator**: While dragging over an existing card, show a horizontal line **above** or **below** that card to indicate where the dragged card will be inserted. The decision of above vs. below is made by comparing `e.clientY` to the midpoint of the hovered card (`rect.top + rect.height / 2`). If `clientY < midpoint`, insert above; otherwise insert below.
- **Drag end cleanup**: Remove all drag-state visual feedback (`dragend` event or equivalent) regardless of whether the drop succeeded.

### Persistence

- On every state change, serialise the full card array to `localStorage` under the key `"kanban-board"`.
- On initial mount, read from `localStorage`. If no saved data exists, populate the board with the **seed data** defined in `INITIAL_CARDS`.
- The shape stored in `localStorage` must round-trip cleanly — no data loss between saves and loads.

### Seed Data

Provide at least **12 realistic project-task cards** spread across all three columns (e.g., 4 in Todo, 4 in In Progress, 4 in Done). Cards should look like real software-project tasks: "Set up CI pipeline", "Write unit tests for auth module", "Deploy staging environment", etc.

---

## Constraints

- **No drag-and-drop libraries.** The following packages (and any forks or wrappers of them) are explicitly banned:
  - `dnd-kit` / `@dnd-kit/*`
  - `react-beautiful-dnd`
  - `react-dnd`
  - `Sortable.js` / `react-sortablejs`
  - Any other library whose primary purpose is drag-and-drop
- Use only the **HTML5 native drag-and-drop API**:
  - The `draggable="true"` attribute on card elements
  - `dragstart`, `dragover`, `dragleave`, `drop`, `dragend` event handlers
  - `dataTransfer.setData` / `dataTransfer.getData` to pass card identity

---

## Implementation Hints

1. **Carry card identity via `dataTransfer`:**
   ```ts
   // dragstart
   e.dataTransfer.setData('text/plain', card.id);

   // drop
   const cardId = e.dataTransfer.getData('text/plain');
   ```

2. **Enable drop by preventing default on `dragover`:**
   ```ts
   e.preventDefault(); // without this, drop never fires
   ```

3. **Track drag state in React state (or a ref):**
   ```ts
   const [draggingId, setDraggingId] = useState<string | null>(null);
   const [dragOverColumn, setDragOverColumn] = useState<ColumnId | null>(null);
   const [dragOverCardId, setDragOverCardId] = useState<string | null>(null);
   const [insertPosition, setInsertPosition] = useState<'above' | 'below'>('below');
   ```

4. **Calculate above/below insertion from mouse position:**
   ```ts
   const rect = (e.currentTarget as HTMLElement).getBoundingClientRect();
   const midpoint = rect.top + rect.height / 2;
   const position = e.clientY < midpoint ? 'above' : 'below';
   ```

5. **Compute new order on drop:**
   - Collect all cards in the target column sorted by `order`.
   - Find the index of `dragOverCardId` in that sorted list.
   - Splice the dragged card in at `index` (above) or `index + 1` (below).
   - Re-assign `order` values (e.g., multiply index by 1000 or use array index directly).

6. **Clean up in `dragend`:**
   ```ts
   setDraggingId(null);
   setDragOverColumn(null);
   setDragOverCardId(null);
   ```
   `dragend` fires on the **drag source** element even if the drop was cancelled, making it a reliable cleanup hook.

7. **`localStorage` helper pattern:**
   ```ts
   useEffect(() => {
     localStorage.setItem('kanban-board', JSON.stringify(cards));
   }, [cards]);
   ```

---

## File Structure

```
04_drag_drop_kanban/
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
├── CHALLENGE.md          ← this file
└── src/
    ├── main.tsx          ← entry point
    ├── App.tsx           ← renders <KanbanBoard />
    └── KanbanBoard.tsx   ← implement everything here (or split into sub-components)
```

You may create additional files (e.g., `KanbanColumn.tsx`, `KanbanCard.tsx`, `types.ts`) if you wish to split the implementation across components. The grader only imports `KanbanBoard` from `./KanbanBoard`.

---

## Evaluation Criteria

| Criterion | Weight |
|-----------|--------|
| Cards can be dragged to a different column and land in the correct position | 25% |
| Cards can be reordered within the same column with correct above/below placement | 20% |
| Visual drop-zone feedback during drag (column highlight + insertion line) | 15% |
| `localStorage` persistence: data survives a full page refresh | 15% |
| Add Card functionality (title required, description optional) | 10% |
| Delete Card functionality | 5% |
| Seed data present on first load (no saved state) | 5% |
| No drag-and-drop library used | 5% |

**Total: 100%**

Good luck!
