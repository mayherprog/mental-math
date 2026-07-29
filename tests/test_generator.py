"""Tests for question generation and grading.

The thing worth testing here is that a question is never unfair: the stated
answer must always be reachable from the prompt, and grading must not depend on
float representation.
"""

import unittest
from fractions import Fraction

from mentalmath.generator import (
    CATEGORIES,
    generate,
    make_question,
    parse_answer,
)


class TestGeneration(unittest.TestCase):
    def test_every_category_builds(self):
        import random

        rng = random.Random(7)
        for category in CATEGORIES:
            for _ in range(200):
                q = make_question(rng, category)
                self.assertEqual(q.category, category)
                self.assertTrue(q.prompt)

    def test_seed_is_reproducible(self):
        a = generate(50, seed=99)
        b = generate(50, seed=99)
        self.assertEqual([q.prompt for q in a], [q.prompt for q in b])

    def test_division_is_always_exact(self):
        for q in generate(500, seed=3, categories=["divide"]):
            self.assertEqual(q.answer.denominator, 1, q.prompt)

    def test_integer_questions_declare_no_places(self):
        for q in generate(300, seed=5, categories=["add_sub", "multiply", "divide"]):
            self.assertIsNone(q.places, q.prompt)

    def test_unknown_category_rejected(self):
        with self.assertRaises(ValueError):
            generate(5, categories=["algebra"])


class TestGrading(unittest.TestCase):
    def test_exact_integer_grading(self):
        q = make_question(__import__("random").Random(1), "multiply")
        self.assertTrue(q.is_correct(q.answer))
        self.assertFalse(q.is_correct(q.answer + 1))

    def test_decimal_rounding_is_accepted(self):
        # 1/40 = 0.025 exactly; a four-place answer and the exact value both pass.
        (q,) = [x for x in generate(400, seed=11, categories=["fraction"])
                if x.answer == Fraction(1, 40)][:1]
        self.assertTrue(q.is_correct(Fraction("0.025")))
        self.assertTrue(q.is_correct(Fraction(1, 40)))
        self.assertFalse(q.is_correct(Fraction("0.03")))

    def test_decimal_sums_avoid_float_error(self):
        # 0.1 + 0.2 must grade as 0.3, which float arithmetic would fail.
        for q in generate(400, seed=2, categories=["decimal"]):
            self.assertTrue(q.is_correct(q.answer), q.prompt)

    def test_percent_answers_are_exact(self):
        for q in generate(200, seed=4, categories=["percent"]):
            self.assertTrue(q.is_correct(q.answer), q.prompt)


class TestParsing(unittest.TestCase):
    def test_accepts_common_forms(self):
        self.assertEqual(parse_answer("36"), Fraction(36))
        self.assertEqual(parse_answer(" 0.375 "), Fraction(3, 8))
        self.assertEqual(parse_answer("3/8"), Fraction(3, 8))
        self.assertEqual(parse_answer("-12.5"), Fraction(-25, 2))
        self.assertEqual(parse_answer("1,250"), Fraction(1250))

    def test_rejects_garbage(self):
        for bad in ["", "   ", "abc", "1/0", "3..4"]:
            self.assertIsNone(parse_answer(bad), bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
