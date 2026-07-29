"""Question generation for timed arithmetic drills.

Every question carries an exact answer as a Fraction, so grading never depends
on float representation. A question also declares how it should be answered
(integer, decimal to N places, or exact) which determines the tolerance.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction

# Question categories. The mix is deliberately weighted toward the operations
# that cost the most time under a clock: multiplication and division.
CATEGORIES = (
    "add_sub",
    "multiply",
    "divide",
    "decimal",
    "percent",
    "fraction",
)

DEFAULT_WEIGHTS = {
    "add_sub": 0.22,
    "multiply": 0.26,
    "divide": 0.20,
    "decimal": 0.14,
    "percent": 0.10,
    "fraction": 0.08,
}


@dataclass(frozen=True)
class Question:
    prompt: str
    answer: Fraction
    category: str
    places: int | None = None  # None means the answer is an exact integer

    def is_correct(self, given: Fraction) -> bool:
        if self.places is None:
            return given == self.answer
        # Accept the answer rounded to the requested number of places, and also
        # accept a fully exact answer from someone who did not round.
        if given == self.answer:
            return True
        scale = Fraction(10) ** self.places
        return round(self.answer * scale) == round(given * scale)


def _add_sub(rng: random.Random) -> Question:
    a = rng.randint(17, 899)
    b = rng.randint(17, 899)
    if rng.random() < 0.45:
        # Subtraction, sometimes crossing into negatives on purpose.
        if rng.random() < 0.25:
            a, b = min(a, b), max(a, b)
        return Question(f"{a} - {b}", Fraction(a - b), "add_sub")
    return Question(f"{a} + {b}", Fraction(a + b), "add_sub")


def _multiply(rng: random.Random) -> Question:
    style = rng.random()
    if style < 0.45:
        a, b = rng.randint(11, 99), rng.randint(3, 9)
    elif style < 0.85:
        a, b = rng.randint(11, 49), rng.randint(11, 29)
    else:
        a, b = rng.randint(101, 499), rng.randint(3, 9)
    return Question(f"{a} x {b}", Fraction(a * b), "multiply")


def _divide(rng: random.Random) -> Question:
    """Integer division that always resolves exactly."""
    divisor = rng.randint(3, 25)
    quotient = rng.randint(4, 60)
    dividend = divisor * quotient
    return Question(f"{dividend} / {divisor}", Fraction(quotient), "divide")


def _decimal(rng: random.Random) -> Question:
    a = Fraction(rng.randint(105, 9950), 100)
    b = Fraction(rng.randint(105, 9950), 100)
    if rng.random() < 0.5:
        return Question(f"{float(a)} + {float(b)}", a + b, "decimal", places=2)
    return Question(f"{float(a)} - {float(b)}", a - b, "decimal", places=2)


def _percent(rng: random.Random) -> Question:
    pct = rng.choice([5, 10, 12, 15, 20, 25, 30, 40, 60, 75, 80, 125, 150])
    base = rng.choice([40, 60, 80, 120, 140, 160, 240, 320, 480, 640, 900])
    answer = Fraction(pct * base, 100)
    return Question(f"{pct}% of {base}", answer, "percent", places=2)


def _fraction(rng: random.Random) -> Question:
    num, den = rng.choice(
        [
            (1, 8), (3, 8), (5, 8), (7, 8),
            (1, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5),
            (1, 16), (3, 16), (1, 20), (7, 20), (1, 40), (3, 40),
        ]
    )
    return Question(
        f"{num}/{den} as a decimal", Fraction(num, den), "fraction", places=4
    )


_BUILDERS = {
    "add_sub": _add_sub,
    "multiply": _multiply,
    "divide": _divide,
    "decimal": _decimal,
    "percent": _percent,
    "fraction": _fraction,
}


def make_question(rng: random.Random, category: str) -> Question:
    try:
        return _BUILDERS[category](rng)
    except KeyError:
        raise ValueError(f"unknown category: {category}") from None


def generate(
    count: int,
    *,
    seed: int | None = None,
    categories: list[str] | None = None,
) -> list[Question]:
    """Build a question set.

    Passing a single category produces a targeted drill; passing none uses the
    weighted mix. A seed makes a set reproducible, which is what lets two
    sessions be compared honestly.
    """
    rng = random.Random(seed)
    if categories:
        unknown = set(categories) - set(CATEGORIES)
        if unknown:
            raise ValueError(f"unknown categories: {sorted(unknown)}")
        pool, weights = categories, [1.0] * len(categories)
    else:
        pool = list(CATEGORIES)
        weights = [DEFAULT_WEIGHTS[c] for c in pool]

    picks = rng.choices(pool, weights=weights, k=count)
    return [make_question(rng, category) for category in picks]


def parse_answer(text: str) -> Fraction | None:
    """Parse typed input as an exact value. Accepts 36, 0.375, 3/8, -12.5."""
    text = text.strip().replace(",", "")
    if not text:
        return None
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError):
        return None
