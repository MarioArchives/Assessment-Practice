export type ColumnId = 'todo' | 'in-progress' | 'done';

export interface Card {
  id: string;
  title: string;
  description?: string;
  columnId: ColumnId;
  order: number;
}

export interface Column {
  id: ColumnId;
  title: string;
}

export const COLUMNS: Column[] = [
  { id: 'todo', title: 'Todo' },
  { id: 'in-progress', title: 'In Progress' },
  { id: 'done', title: 'Done' },
];

export const INITIAL_CARDS: Card[] = [
  // Todo column
  {
    id: 'card-1',
    title: 'Set up CI/CD pipeline',
    description: 'Configure GitHub Actions for automated testing and deployment.',
    columnId: 'todo',
    order: 1000,
  },
  {
    id: 'card-2',
    title: 'Design database schema',
    description: 'Define tables and relationships for the new user-preferences feature.',
    columnId: 'todo',
    order: 2000,
  },
  {
    id: 'card-3',
    title: 'Write API documentation',
    description: 'Document all REST endpoints using OpenAPI 3.0 spec.',
    columnId: 'todo',
    order: 3000,
  },
  {
    id: 'card-4',
    title: 'Add end-to-end tests for checkout flow',
    description: 'Use Playwright to cover the full purchase journey.',
    columnId: 'todo',
    order: 4000,
  },
  // In Progress column
  {
    id: 'card-5',
    title: 'Implement user authentication',
    description: 'JWT-based login and refresh-token rotation.',
    columnId: 'in-progress',
    order: 1000,
  },
  {
    id: 'card-6',
    title: 'Refactor data-fetching layer',
    description: 'Replace ad-hoc fetch calls with a centralised React Query setup.',
    columnId: 'in-progress',
    order: 2000,
  },
  {
    id: 'card-7',
    title: 'Build notification service',
    description: 'Send email and in-app alerts on key user events.',
    columnId: 'in-progress',
    order: 3000,
  },
  {
    id: 'card-8',
    title: 'Migrate legacy components to TypeScript',
    description: 'Convert remaining .jsx files and add strict typings.',
    columnId: 'in-progress',
    order: 4000,
  },
  // Done column
  {
    id: 'card-9',
    title: 'Deploy staging environment',
    description: 'Provision AWS ECS cluster and wire up staging DNS.',
    columnId: 'done',
    order: 1000,
  },
  {
    id: 'card-10',
    title: 'Write unit tests for auth module',
    description: 'Achieve 90% coverage on login, logout, and token-refresh paths.',
    columnId: 'done',
    order: 2000,
  },
  {
    id: 'card-11',
    title: 'Set up error monitoring',
    description: 'Integrate Sentry and configure alert thresholds.',
    columnId: 'done',
    order: 3000,
  },
  {
    id: 'card-12',
    title: 'Accessibility audit',
    description: 'Run axe-core on all pages and fix critical a11y violations.',
    columnId: 'done',
    order: 4000,
  },
];

// TODO: implement
export default function KanbanBoard() {
  return null;
}
