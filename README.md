# Assessment Practice

Practice material for technical assessments covering Python, Kubernetes, and
Linux. The repo has three parts: hands-on coding challenges with test suites,
multiple-choice question banks with an interactive quiz runner, and scaffolding
for writing extra test rounds.

## Repository layout

```
coding_challenges/   19 self-contained Python challenges + hidden validation suites
multiple_choice/     MCQ banks (Python, Kubernetes, Linux) + CLI quiz runner
tests_2_0/           Scaffolding for writing additional test suites
```

## Coding challenges

Each file under [`coding_challenges/`](coding_challenges/) is self-contained: a
problem statement docstring, a skeleton to implement, and runnable tests at the
bottom. See the [challenge index](coding_challenges/README.md) for the full
list with topics and target times.

There are two tiers:

- **Quick drills (01–13)** — short exercises with a fairly complete test suite
  included in the file. Topics range from decorators, caching, and context
  managers to asyncio, threading, generics, and Kubernetes concepts like label
  selectors and manifest diffing.
- **Assessment-style (14–19)** — these mirror a real timed assessment. The file
  only ships a few **non-exhaustive** sample tests; a hidden suite under
  [`coding_challenges/validation/`](coding_challenges/validation/) plays the
  role of the post-submission grader. Implement the spec, write your own
  edge-case tests until you're confident, and only then run the validation
  suite — don't read it beforehand.

```sh
# Run a single challenge's built-in tests
python coding_challenges/01_ttl_cache.py

# Run everything with pytest
pytest coding_challenges/

# Grade an assessment-style challenge against the hidden suite
pytest coding_challenges/validation/test_14_pod_scheduler.py
```

Requires Python 3.10+ and `pytest` (only the standard library is needed for
the challenges themselves).

## Multiple choice

[`multiple_choice/`](multiple_choice/) holds three question banks of 40
questions each — [Python](multiple_choice/python_mcq.md),
[Kubernetes](multiple_choice/kubernetes_mcq.md), and
[Linux](multiple_choice/linux_mcq.md) — plus an
[answer key](multiple_choice/answers.md) with explanations.

[`quiz.py`](multiple_choice/quiz.py) runs the Python and Kubernetes banks as an
interactive terminal quiz and tracks which questions you get wrong (state is
kept locally in `.quiz_state.json`, which is gitignored). The Linux bank is
currently markdown-only — read it alongside the answer key.

```sh
./multiple_choice/quiz.py                  # run all questions
./multiple_choice/quiz.py --failed         # retry only previously failed questions
./multiple_choice/quiz.py --topic python   # filter by topic (python | kubernetes)
./multiple_choice/quiz.py --shuffle        # randomise order
./multiple_choice/quiz.py --stats          # show failure statistics
./multiple_choice/quiz.py --clear          # reset failure history
```

## tests_2_0

[`tests_2_0/`](tests_2_0/) is a workspace for writing fresh test suites against
the challenges — useful for a second practice round once you've seen the
original tests. It ships with a module loader (`_loader.py`) that imports
challenge files by filename (needed because names like `01_ttl_cache.py` aren't
valid module identifiers) and a `conftest.py` that wires it into pytest. Drop
`test_*.py` files in and run `pytest tests_2_0/`.
