export interface Post {
  id: number;
  title: string;
  author: string;
  body: string;
  avatarColor: string;
}

export interface FetchPostsResult {
  posts: Post[];
  nextPage: number | null; // null means no more pages
  totalPages: number;
}

const COLORS = ['#6366f1', '#ec4899', '#14b8a6', '#f59e0b', '#ef4444', '#8b5cf6'];
const AUTHORS = ['Alice Chen', 'Bob Martinez', 'Carol White', 'Dave Kim', 'Eve Johnson', 'Frank Lee'];

const TITLES = [
  'The Hidden Cost of Premature Optimization',
  'Why Your Abstractions Are Probably Wrong',
  'Rethinking State Management in 2024',
  'A Deep Dive into the Event Loop',
  'Functional Patterns for the Pragmatic Developer',
  'How to Stop Writing Clever Code',
  'The Case Against Microservices (Sometimes)',
  'Understanding Memory Leaks in Long-Lived Apps',
  'Accessibility Is Not an Afterthought',
  'On Writing Code That Reads Like Prose',
  'Composition vs Inheritance: A Practical Guide',
  'The Forgotten Power of CSS Custom Properties',
  'Async/Await Patterns You Might Not Know',
  'Why I Stopped Using Object-Oriented Design',
  'Testing at the Right Level of Abstraction',
  'The Quiet Complexity of Time Zones',
  'Building Resilient UIs with Error Boundaries',
  'Semantic HTML Is Still Underrated',
  'A Field Guide to Debugging Network Requests',
  'Data Normalization and When to Break the Rules',
  'The Myth of the 10x Developer',
  'TypeScript Generics Without the Headache',
  'Why Code Reviews Fail (And How to Fix Them)',
  'Progressive Enhancement in a SPA World',
  'Controlled vs Uncontrolled Components Explained',
  'The Art of the Good Commit Message',
  'React Hooks: Common Pitfalls and How to Avoid Them',
  'CSS Grid vs Flexbox: When to Use Which',
  'Immutability as a Design Principle',
  'Logging, Tracing, and the Observability Mindset',
  'Why Your Bundle Is Larger Than You Think',
  'Designing APIs That Won\'t Haunt You Later',
  'An Honest Assessment of Server-Side Rendering',
  'The Surprising Depth of Array Methods',
  'Race Conditions in the Browser',
  'When useEffect Is the Wrong Tool',
  'The Philosophy of Good Error Messages',
  'Lazy Loading: More Than Just Images',
  'Understanding CORS Without Losing Your Mind',
  'Declarative vs Imperative UI Thinking',
  'The Underappreciated Semicolon Debate',
  'Cache Invalidation Is Hard. Here\'s a Framework.',
  'Building Forms That Don\'t Frustrate Users',
  'The Real Cost of Third-Party Scripts',
  'Dependency Injection Without a Framework',
  'Web Performance Metrics That Actually Matter',
  'Lessons Learned from a Year of Pair Programming',
];

const BODY_FRAGMENTS = [
  'When we talk about performance, we often jump straight to benchmarks and profiling tools. But the most impactful optimizations are rarely the ones we measure first.',
  'Abstraction is one of the most powerful tools in a developer\'s toolkit, yet it is also one of the most frequently misapplied. The line between helpful and harmful abstraction is thinner than most tutorials suggest.',
  'State management has become a cottage industry in the JavaScript ecosystem. Before reaching for a library, it is worth asking what problem you are actually trying to solve.',
  'The event loop sits at the heart of every Node.js and browser application. Understanding it is not optional — it is the foundation on which everything else is built.',
  'Pure functions, immutability, and higher-order functions are not academic curiosities. They solve real problems in production codebases when applied with care and intention.',
  'Clever code is code that makes you feel smart when you write it and confused when you read it six months later. The goal should be the opposite: boring code that is obviously correct.',
  'Microservices offer real benefits at scale. They also introduce real costs at every scale. The question is not whether to adopt them but whether your context justifies those costs.',
  'Memory leaks in long-lived single-page applications are insidious. They build gradually, invisible until a user complains that the tab is consuming gigabytes of RAM.',
  'Every accessibility fix you defer is a user you are currently excluding. WCAG compliance is a floor, not a ceiling, and the extra effort required is smaller than most teams assume.',
  'Code is read far more often than it is written. Optimizing for the reader — not the writer — is one of the highest-leverage investments a development team can make.',
  'The choice between composition and inheritance shapes entire architectures. Favor composition for flexibility, but do not dogmatically avoid inheritance where it genuinely simplifies the model.',
  'CSS custom properties — also known as CSS variables — enable dynamic theming, responsive design, and component isolation in ways that preprocessors never could at runtime.',
  'Async/await makes asynchronous code look synchronous. It does not make it simpler. The same edge cases that plagued promises — error handling, cancellation, concurrency — all remain.',
  'Object-oriented design gave us decades of patterns and vocabulary. It also gave us deep inheritance hierarchies and coupling that defies untangling. There are better defaults.',
  'Testing at too low a level gives you fast tests that do not catch real bugs. Testing at too high a level gives you slow tests that are expensive to maintain. The sweet spot is narrow.',
  'Time zones are not offsets. Daylight saving transitions, historical rule changes, and political boundary shifts make a seemingly trivial problem genuinely hard.',
  'Error boundaries in React let you isolate failures to a subtree of the component hierarchy. Used well, they are the difference between a partially degraded UI and a completely blank screen.',
  'A well-structured HTML document communicates meaning to screen readers, search engines, and future developers — without a single line of JavaScript or CSS.',
  'Network debugging is a skill, not just a toolset. Knowing what to look for in the DevTools Network panel turns a frustrating mystery into a solvable puzzle.',
  'Data normalization reduces redundancy and keeps updates consistent. But in read-heavy UIs, denormalized data is often simpler, faster, and easier to reason about.',
  'The mythology of the exceptional individual obscures the systemic factors that determine whether a team ships good software: process, culture, tooling, and clear requirements.',
  'TypeScript generics unlock powerful reuse patterns. They also introduce a new class of errors that are harder to read than the bugs they prevent. Start simple and add complexity only when needed.',
  'Most code review feedback is either too nitpicky or too high-level. Effective reviews focus on correctness, clarity, and maintainability — in that order.',
  'Progressive enhancement means starting with what works everywhere and layering on enhancements for capable environments. It is not a constraint; it is a resilience strategy.',
  'Controlled components give React full ownership of form state. Uncontrolled components let the DOM manage its own state. Neither is universally correct; context determines the trade-off.',
  'A commit message that says "fix bug" is worse than no message at all. A good message explains why the change was made, not what changed — the diff already shows that.',
  'The dependency array in useEffect is a contract. Violating that contract — by omitting dependencies or including objects that change on every render — introduces bugs that are notoriously hard to trace.',
  'CSS Grid and Flexbox are not competitors. Grid excels at two-dimensional layout; Flexbox excels at one-dimensional alignment. Use both, often on the same page.',
  'Immutability does not prevent all bugs, but it eliminates an entire class of them: unexpected state mutations that cause components to render stale data.',
  'Logs tell you what happened. Traces tell you where it happened across services. Metrics tell you how often it happens. You need all three to truly understand a production system.',
  'Modern bundlers are remarkably good at eliminating dead code. But they cannot eliminate code you imported unnecessarily in the first place. Tree shaking has limits.',
  'A well-designed API is one that makes the easy things trivial, the hard things possible, and the wrong things difficult. Most APIs achieve only the first, sometimes at the expense of the other two.',
  'Server-side rendering improves perceived performance and SEO. It also complicates deployment, increases server costs, and introduces a class of hydration bugs with no client-side equivalent.',
  'Array methods like `reduce`, `flatMap`, and `findIndex` are not obscure — they are workhorses. Reaching for a `for` loop first is often a sign that the right method has not been considered.',
  'Race conditions in the browser arise when asynchronous operations complete in an unexpected order. They are reproducible only under specific timing conditions, making them among the hardest bugs to diagnose.',
  'useEffect is for synchronizing with external systems: the DOM, network, timers, subscriptions. Using it to derive state from props or trigger internal logic is almost always the wrong choice.',
  'Error messages are part of your product\'s UX. Vague messages like "Something went wrong" are a failure of design, not just implementation.',
  'Lazy loading images, routes, and components reduces initial bundle size and improves time-to-interactive. The browser\'s native lazy loading attribute makes the common case trivially easy.',
  'CORS is enforced by the browser, not the server. Understanding the difference between simple and preflight requests clarifies why some CORS issues are subtle and others are obvious.',
  'Declarative UI describes what the screen should look like given the current state. Imperative UI describes how to change the screen. React\'s declarative model shifts complexity from you to the framework.',
  'The semicolon debate has been settled by formatters. The real debate — one worth having — is about naming, structure, and which problems deserve the most careful design.',
  'Cache invalidation is famously hard because it mixes two concerns: knowing when data is stale and knowing who needs to be notified. Separating these concerns makes each one tractable.',
  'Forms are the primary interface between users and your data. Every unnecessary field, confusing label, or missing error message is friction that directly reduces conversion and trust.',
  'Third-party scripts are the leading cause of unpredictable page performance. Each one you add is a dependency you do not control, running code with the same privileges as your own.',
  'Dependency injection is a technique, not a framework. You can achieve loose coupling and testability with plain constructor arguments and interfaces, no container required.',
  'Core Web Vitals — LCP, INP, and CLS — measure the dimensions of performance that users actually feel. Optimizing for these metrics means optimizing for the user, not the benchmark.',
  'Pair programming is not about typing together. It is about shared context, immediate feedback, and the surprisingly high quality of decisions made when two people must agree before committing.',
];

const TOTAL_POSTS = 47;

function generatePost(id: number): Post {
  const authorIndex = (id - 1) % AUTHORS.length;
  const colorIndex = (id - 1) % COLORS.length;
  const titleIndex = (id - 1) % TITLES.length;
  const bodyIndex = (id - 1) % BODY_FRAGMENTS.length;
  const secondBodyIndex = (id + 2) % BODY_FRAGMENTS.length;

  return {
    id,
    title: TITLES[titleIndex],
    author: AUTHORS[authorIndex],
    body: `${BODY_FRAGMENTS[bodyIndex]} ${BODY_FRAGMENTS[secondBodyIndex]}`,
    avatarColor: COLORS[colorIndex],
  };
}

const ALL_POSTS: Post[] = Array.from({ length: TOTAL_POSTS }, (_, i) => generatePost(i + 1));

function randomDelay(): Promise<void> {
  const ms = 600 + Math.random() * 300; // 600–900 ms
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function fetchPosts(page: number, pageSize = 10): Promise<FetchPostsResult> {
  await randomDelay();

  const start = (page - 1) * pageSize;
  const end = start + pageSize;
  const posts = ALL_POSTS.slice(start, end);
  const totalPages = Math.ceil(TOTAL_POSTS / pageSize);
  const nextPage = end < TOTAL_POSTS ? page + 1 : null;

  return { posts, nextPage, totalPages };
}
