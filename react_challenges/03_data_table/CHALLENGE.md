# Challenge 03 – Data Table

## Overview

Build a generic, reusable `<DataTable>` component that supports **sorting**, **filtering**, and **pagination** entirely in React — no table libraries allowed.

The component must be fully type-safe using TypeScript generics so it can be dropped in with any row-shape dataset.

---

## Requirements

### Props

```typescript
interface DataTableProps<T extends Record<string, unknown>> {
  columns: ColumnDef<T>[];
  rows: T[];
  pageSize?: number; // default: 10
}
```

### Column Definition

```typescript
interface ColumnDef<T> {
  key: keyof T & string;     // which field to read from each row
  header: string;            // column header label
  sortable?: boolean;        // whether this column can be sorted
  render?: (value: T[keyof T], row: T) => React.ReactNode; // optional custom cell renderer
}
```

### Sorting

- Clicking a sortable column header cycles through three states: **ascending → descending → unsorted**.
- Display a sort direction indicator in the header cell: `↑` for ascending, `↓` for descending, nothing (or a neutral indicator) for unsorted.
- Only one column may be sorted at a time; clicking a new column resets the previous sort.
- Sorting must be **stable**: rows with equal values in the sorted column retain their original relative order.
- Changing sort direction must reset the current page to page 1.

### Filtering

- Render a text `<input>` above the table for a global search filter.
- Filtering applies across **all string-valued columns** simultaneously (case-insensitive substring match).
- Non-string columns (numbers, dates, etc.) are not matched by the filter but are still displayed.
- Changing the filter value must reset the current page to page 1.

### Pagination

- `pageSize` prop controls how many rows appear per page (default `10`).
- Render **Previous** and **Next** buttons.
- Display the current page number and total page count, e.g. `Page 2 of 8`.
- Include a **jump-to-page** input that lets the user type a page number and navigate directly.
- Disable the Previous button on page 1; disable the Next button on the last page.
- If the filter reduces the result set to zero rows, show a friendly empty-state message instead of the table body.

### Row Count Summary

- Display a summary line such as `Showing 11–20 of 75 results` that reflects the **filtered** total (not the raw total).
- When no filter is active, the total equals `rows.length`.

---

## Data Pipeline

Apply transformations in this exact order:

```
raw rows
  → filter  (apply global text filter)
  → sort    (apply column sort, if any)
  → paginate (slice to current page)
  → render
```

Use `useMemo` for each stage so re-renders are efficient.

---

## Constraints

- **No table libraries**: TanStack Table, AG Grid, React Table, and similar are not allowed.
- **No utility libraries for sort/filter**: lodash, ramda, underscore, etc. are not allowed. Use native JS array methods (`filter`, `sort`, `slice`).
- **Pure React + TypeScript**: state management via `useState` / `useMemo` / `useCallback` only — no external state libraries.

---

## File to Implement

```
src/DataTable.tsx
```

The stub already contains the exported interfaces (`ColumnDef`, `DataTableProps`) and internal types (`SortDirection`, `SortState`). Replace the `// TODO: implement` stub and `return null` with a working implementation.

Do **not** modify `src/sampleData.ts` or `src/App.tsx` — they are the harness that exercises your component.

---

## Hints

- Chain `useMemo` calls:
  ```typescript
  const filteredRows = useMemo(() => /* filter logic */, [rows, filterText]);
  const sortedRows   = useMemo(() => /* sort logic */,   [filteredRows, sortState]);
  const pageRows     = useMemo(() => /* slice logic */,  [sortedRows, page, pageSize]);
  ```
- Reset `page` to `1` inside the filter-change handler and the sort-change handler (not inside `useMemo`).
- For the sort cycle, a clean approach is a lookup:
  ```typescript
  const nextDirection: Record<SortDirection, SortDirection> = {
    none: 'asc', asc: 'desc', desc: 'none',
  };
  ```
- For stable sort, copy the array before sorting (`[...filteredRows].sort(...)`) and compare with `localeCompare` for strings, direct subtraction for numbers.
- The generic component signature looks like:
  ```typescript
  function DataTable<T extends Record<string, unknown>>(props: DataTableProps<T>): React.ReactElement | null
  ```
- For accessible markup, use `<th scope="col">` for column headers and `<caption>` on the `<table>` element (can be visually hidden with CSS if desired).

---

## Evaluation Criteria

| Criterion | What is checked |
|---|---|
| Sort cycling | asc → desc → none, single-column at a time |
| Sort direction indicators | ↑ / ↓ appear and disappear correctly |
| Stable sort | Rows with equal values don't swap unnecessarily |
| Filter scope | Matches any string column, case-insensitive |
| Filter resets pagination | Page returns to 1 on filter change |
| Sort resets pagination | Page returns to 1 on sort change |
| Pagination accuracy | Correct slice, correct disabled states |
| Jump-to-page | Navigates correctly, clamps to valid range |
| Row count summary | "Showing X–Y of Z results" is always accurate |
| Empty state | Graceful message when filter yields 0 rows |
| TypeScript correctness | No `any`, generics flow through without casts |
| Accessible markup | `<th scope="col">`, `<caption>`, button labels |
| Custom render | `columns[n].render` is called when provided |

---

## Getting Started

```bash
npm install
npm run dev
```

The app renders a 75-row employee dataset. Use it to manually verify all the criteria above before considering the challenge complete.
