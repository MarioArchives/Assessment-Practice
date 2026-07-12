import KanbanBoard from './KanbanBoard';

export default function App() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '2rem' }}>
      <h1>04 – Drag &amp; Drop Kanban Board</h1>
      <p>
        Implement a Kanban board with three columns (Todo, In Progress, Done) using
        only the HTML5 Drag and Drop API. Cards must be draggable across columns and
        reorderable within columns. State must persist via <code>localStorage</code>.
      </p>
      <KanbanBoard />
    </div>
  );
}
