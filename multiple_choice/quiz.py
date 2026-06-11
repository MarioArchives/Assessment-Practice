#!/usr/bin/env python3
"""CLI quiz runner for multiple-choice questions with failure tracking."""

import re
import json
import argparse
import sys
import os
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPT_DIR, ".quiz_state.json")

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"


# ── Parsing ────────────────────────────────────────────────────────────────────

def parse_questions(filepath, topic):
    with open(filepath) as f:
        content = f.read()

    questions = []
    for block in re.split(r'\n---\n', content):
        block = block.strip()
        if not block.startswith("**Q"):
            continue

        m = re.match(r'\*\*Q(\d+)\.\*\*\s*(.*)', block, re.DOTALL)
        if not m:
            continue

        q_num = int(m.group(1))
        rest = m.group(2).strip()

        opt_start = re.search(r'\nA\)', rest)
        if not opt_start:
            continue

        q_text = rest[: opt_start.start()].strip()
        options_text = rest[opt_start.start() :].strip()

        options = {
            om.group(1): om.group(2).strip()
            for om in re.finditer(r'^([A-D])\)\s+(.+)$', options_text, re.MULTILINE)
        }

        if len(options) == 4:
            questions.append(
                dict(id=f"{topic}_Q{q_num}", num=q_num, topic=topic,
                     text=q_text, options=options)
            )

    return questions


def parse_answers(filepath):
    with open(filepath) as f:
        content = f.read()

    answers = {}
    for section in re.split(r'^## ', content, flags=re.MULTILINE):
        if not section.strip():
            continue
        first = section.split('\n')[0].lower()
        topic = ('python' if 'python' in first
                 else 'kubernetes' if 'kubernetes' in first
                 else None)
        if not topic:
            continue
        answers[topic] = {}
        for m in re.finditer(
            r'^\|\s*(\d+)\s*\|\s*\*\*([A-D])\*\*.*?\|\s*(.*?)\s*\|',
            section, re.MULTILINE,
        ):
            answers[topic][int(m.group(1))] = (m.group(2), m.group(3).strip())

    return answers


# ── State persistence ──────────────────────────────────────────────────────────

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"failed": []}


def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


# ── Display helpers ────────────────────────────────────────────────────────────

def _clean(text):
    """Strip inline backticks."""
    return re.sub(r'`([^`]*)`', r'\1', text)


def _render_question_text(text):
    """Convert fenced code blocks to indented plain text."""
    def indent_block(m):
        code = m.group(1).rstrip()
        indented = '\n'.join('    ' + line for line in code.split('\n'))
        return f"\n{indented}\n"

    text = re.sub(r'```\w*\n(.*?)\n```', indent_block, text, flags=re.DOTALL)
    return _clean(text)


def display_question(q, index, total):
    topic_label = q['topic'].capitalize()
    print(f"\n{CYAN}{BOLD}[{index}/{total}] {topic_label} — Q{q['num']}{RESET}")
    print(f"\n{_render_question_text(q['text'])}\n")
    for letter in 'ABCD':
        print(f"  {BOLD}{letter}){RESET} {_clean(q['options'][letter])}")
    print()


# ── Quiz loop ──────────────────────────────────────────────────────────────────

def run_quiz(questions, answers):
    total = len(questions)
    correct = 0
    wrong_ids = set()

    for i, q in enumerate(questions, 1):
        display_question(q, i, total)

        while True:
            try:
                raw = input("Answer [A/B/C/D]  (q = quit): ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                print("\nQuiz interrupted.")
                sys.exit(0)
            if raw == 'Q':
                print("\nQuiz interrupted.")
                sys.exit(0)
            if raw in ('A', 'B', 'C', 'D'):
                break
            print("  Please enter A, B, C, or D.")

        correct_ans, explanation = answers[q['topic']][q['num']]

        if raw == correct_ans:
            print(f"\n  {GREEN}{BOLD}✓  Correct!{RESET}")
            correct += 1
        else:
            opt_text = _clean(q['options'][correct_ans])
            print(f"\n  {RED}{BOLD}✗  Wrong.{RESET}  Correct answer: "
                  f"{BOLD}{correct_ans}) {opt_text}{RESET}")
            wrong_ids.add(q['id'])

        if explanation:
            print(f"  {DIM}{_clean(explanation)}{RESET}")

    return correct, wrong_ids


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Multiple-choice quiz with failure tracking',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  quiz.py                   run all questions
  quiz.py --failed          retry only previously failed questions
  quiz.py --topic python    only Python questions
  quiz.py --shuffle         randomise order
  quiz.py --stats           show failure stats and exit
  quiz.py --clear           reset failure history
""",
    )
    parser.add_argument('--failed',  '-f', action='store_true',
                        help='Only show previously failed questions')
    parser.add_argument('--topic',   '-t', choices=['python', 'kubernetes'],
                        help='Filter by topic')
    parser.add_argument('--shuffle', '-s', action='store_true',
                        help='Randomise question order')
    parser.add_argument('--stats',         action='store_true',
                        help='Show failure statistics and exit')
    parser.add_argument('--clear',         action='store_true',
                        help='Reset failed-questions history')
    args = parser.parse_args()

    state = load_state()
    failed_ids = set(state.get('failed', []))

    if args.clear:
        save_state({'failed': []})
        print("Failed-questions history cleared.")
        return

    py_qs  = parse_questions(os.path.join(SCRIPT_DIR, 'python_mcq.md'),    'python')
    k8s_qs = parse_questions(os.path.join(SCRIPT_DIR, 'kubernetes_mcq.md'),'kubernetes')
    all_qs = py_qs + k8s_qs
    answers = parse_answers(os.path.join(SCRIPT_DIR, 'answers.md'))

    if args.stats:
        all_ids = {q['id'] for q in all_qs}
        still_failed = failed_ids & all_ids
        py_failed  = {fid for fid in still_failed if fid.startswith('python')}
        k8s_failed = {fid for fid in still_failed if fid.startswith('kubernetes')}
        print(f"\n{BOLD}Quiz statistics{RESET}")
        print(f"  Total questions : {len(all_qs)}")
        print(f"  On failed list  : {len(still_failed)}")
        if py_failed:
            nums = sorted(int(fid.split('_Q')[1]) for fid in py_failed)
            print(f"  {RED}Python failed   :{RESET} Q{', Q'.join(map(str, nums))}")
        if k8s_failed:
            nums = sorted(int(fid.split('_Q')[1]) for fid in k8s_failed)
            print(f"  {RED}Kubernetes failed:{RESET} Q{', Q'.join(map(str, nums))}")
        if not still_failed:
            print(f"  {GREEN}No failures on record.{RESET}")
        print()
        return

    # Apply filters
    if args.topic:
        all_qs = [q for q in all_qs if q['topic'] == args.topic]

    if args.failed:
        all_qs = [q for q in all_qs if q['id'] in failed_ids]
        if not all_qs:
            print(f"\n{GREEN}No failed questions to retry — you're all caught up!{RESET}\n")
            return
        print(f"\n{YELLOW}{BOLD}Retrying {len(all_qs)} previously failed question(s)...{RESET}")
    else:
        print(f"\n{CYAN}{BOLD}Starting quiz — {len(all_qs)} question(s){RESET}")

    if args.shuffle:
        random.shuffle(all_qs)

    correct, wrong_ids = run_quiz(all_qs, answers)
    total = len(all_qs)

    # Update persistent failure list:
    #   - remove questions answered correctly this run
    #   - add questions answered incorrectly this run
    answered_ids = {q['id'] for q in all_qs}
    failed_ids = (failed_ids - (answered_ids - wrong_ids)) | wrong_ids
    save_state({'failed': sorted(failed_ids)})

    pct = int(100 * correct / total) if total else 0
    color = GREEN if pct >= 70 else (YELLOW if pct >= 50 else RED)
    print(f"\n{BOLD}{'━' * 44}{RESET}")
    print(f"  Score : {color}{BOLD}{correct}/{total}  ({pct}%){RESET}")
    if wrong_ids:
        nums_by_topic = {}
        for q in all_qs:
            if q['id'] in wrong_ids:
                nums_by_topic.setdefault(q['topic'], []).append(q['num'])
        for topic, nums in sorted(nums_by_topic.items()):
            label = topic.capitalize()
            print(f"  {RED}Failed {label}{RESET}: Q{', Q'.join(map(str, sorted(nums)))}")
        print(f"\n  Run {BOLD}quiz.py --failed{RESET} to retry these questions.")
    else:
        print(f"  {GREEN}All correct — no new failures recorded.{RESET}")
    print()


if __name__ == '__main__':
    main()
