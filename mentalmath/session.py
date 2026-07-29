"""Timed session runner and on-disk record format."""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .generator import Question, generate, parse_answer

SESSION_DIR = Path(__file__).resolve().parent.parent / "sessions"


@dataclass
class Attempt:
    prompt: str
    category: str
    expected: str
    given: str
    correct: bool
    seconds: float


@dataclass
class Session:
    started_at: str
    limit_seconds: int
    question_count: int
    seed: int | None
    categories: list[str] | None
    attempts: list[Attempt] = field(default_factory=list)
    elapsed_seconds: float = 0.0
    completed: bool = False

    @property
    def correct(self) -> int:
        return sum(1 for a in self.attempts if a.correct)

    @property
    def accuracy(self) -> float:
        return self.correct / len(self.attempts) if self.attempts else 0.0

    def save(self, directory: Path = SESSION_DIR) -> Path:
        directory.mkdir(parents=True, exist_ok=True)
        stamp = self.started_at.replace(":", "").replace("-", "")
        path = directory / f"session-{stamp}.json"
        payload = asdict(self)
        path.write_text(json.dumps(payload, indent=2) + "\n")
        return path


def load_sessions(directory: Path = SESSION_DIR) -> list[Session]:
    if not directory.exists():
        return []
    sessions: list[Session] = []
    for path in sorted(directory.glob("session-*.json")):
        raw = json.loads(path.read_text())
        attempts = [Attempt(**a) for a in raw.pop("attempts", [])]
        sessions.append(Session(attempts=attempts, **raw))
    return sessions


def _ask(question: Question, index: int, total: int, remaining: float) -> tuple[str, float]:
    """Prompt for one answer. Returns the raw input and seconds taken."""
    label = f"[{index}/{total}] {int(remaining):>3}s  {question.prompt} = "
    start = time.monotonic()
    try:
        given = input(label)
    except EOFError:
        given = ""
    return given, time.monotonic() - start


def run(
    *,
    count: int = 80,
    limit_seconds: int = 480,
    seed: int | None = None,
    categories: list[str] | None = None,
) -> Session:
    """Run a timed drill against the terminal.

    The clock is the point: the session ends when the time limit is hit, even
    mid-question, and unanswered questions simply do not count as attempts.
    """
    questions = generate(count, seed=seed, categories=categories)
    session = Session(
        started_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        limit_seconds=limit_seconds,
        question_count=count,
        seed=seed,
        categories=categories,
    )

    print(f"\n{count} questions, {limit_seconds}s. Blank answer skips. Ctrl-C stops.\n")
    start = time.monotonic()
    try:
        for i, question in enumerate(questions, start=1):
            remaining = limit_seconds - (time.monotonic() - start)
            if remaining <= 0:
                break
            given, taken = _ask(question, i, count, remaining)
            if time.monotonic() - start > limit_seconds:
                print("\nTime.")
                break
            value = parse_answer(given)
            correct = value is not None and question.is_correct(value)
            session.attempts.append(
                Attempt(
                    prompt=question.prompt,
                    category=question.category,
                    expected=_render(question),
                    given=given.strip(),
                    correct=correct,
                    seconds=round(taken, 3),
                )
            )
        else:
            session.completed = True
    except KeyboardInterrupt:
        print("\nStopped.")

    session.elapsed_seconds = round(time.monotonic() - start, 2)
    return session


def _render(question: Question) -> str:
    if question.places is None:
        return str(int(question.answer))
    value = float(question.answer)
    return f"{value:.{question.places}f}".rstrip("0").rstrip(".")
