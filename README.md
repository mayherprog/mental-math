# [mental-math](https://mayherprog.github.io/mental-math)

[![tests](https://github.com/mayherprog/mental-math/actions/workflows/tests.yml/badge.svg)](https://github.com/mayherprog/mental-math/actions/workflows/tests.yml)

A timed arithmetic drill that records every answer, so improvement is measured
rather than felt. Live at
[mayherprog.github.io/mental-math](https://mayherprog.github.io/mental-math).

Grading is exact rational arithmetic throughout — every answer a ratio of two
integers, never a float. Both pages carry their own embedded test suites:
[index.html?selftest](https://mayherprog.github.io/mental-math/index.html?selftest)
(52 assertions) and
[adaptive.html?selftest](https://mayherprog.github.io/mental-math/adaptive.html?selftest)
(66 assertions).

Several trading firms screen candidates with a fast, no-calculator arithmetic
test before any interview. This tool does not claim to reproduce any firm's
assessment. It reproduces the constraint: far more questions than there is time
to answer carefully.

That distinction is not modesty. I went looking for what is actually documented
about these assessments — six firms, every claim graded by source tier, every
finding handed to a second pass whose only job was to refute it. **The widely
circulated "80 questions in 8 minutes" format has no firm-published source at
any of them.** It lives on candidate forums and test-prep vendors that
contradict each other on the pass mark, the scoring penalty, and in one case the
numbers themselves. Two research passes disagreed about which firm it even
belongs to.

The sourced write-up is in [RESEARCH.md](RESEARCH.md), including what *is*
firm-stated: Optiver's calculator ban and its 8-month single-attempt rule, and
Jane Street's own published statement that its trading interview "will not
involve complicated math."

The 80-question, 480-second default here is adjustable and is not presented as
anyone's specification. It is a round number that produces the right kind of
pressure.

## Why it is built this way

**Speed and accuracy are one metric, not two.** A slow perfect run and a fast
sloppy run both fail. The headline number here is correct answers per minute,
projected out to the full time limit.

**Grading uses exact arithmetic.** Every answer is a `Fraction`, never a float.
`0.1 + 0.2` grades as `0.3`, which naive float comparison gets wrong. Decimal
and fraction questions accept either the rounded answer or the exact one.

**Sessions are seeded.** `--seed` makes a question set reproducible, so two
sessions a week apart can be compared on identical questions instead of on a
new random draw that might have been easier.

**Per-category latency is the useful output.** Overall accuracy tells you
little. Median seconds per category tells you where the clock is actually
being lost, which is the only thing that changes what you practice tomorrow.

## Adaptive drill

`adaptive.html` is the adaptive version: the same drill, except the difficulty moves.
Every topic carries a level from 1 to 5, and the level you are asked at follows
how you are doing.

**Difficulty is chosen locally.** Answers are graded as exact rationals, unchanged
from the fixed version. Difficulty is set by a small deterministic controller: each
topic holds a rating, and every answer moves it by how the time taken compared to a
target for that topic at that level. Fast and right pushes up, wrong pushes down,
right-but-slow drifts down gently. It is arithmetic rather than inference, because
a timed drill cannot block on a network request between questions.

**Mistakes are diagnosed by rules that have to reproduce your answer.** An earlier
version of this page asked a language model what went wrong. It was replaced,
because a rule can be checked and a guess cannot.

Each rule reconstructs the wrong result its slip would cause, and fires only if
that number equals, exactly, what you typed:

| Slip | Produces |
|------|----------|
| Borrow dropped in subtraction | `532 − 178` answered `446` |
| Carries never moved left | `538 + 761` answered `299` |
| Second partial product unshifted | `37 × 24` answered `222` |
| One partial product omitted | `37 × 24` answered `148` |
| Divisor and dividend swapped | `468 ÷ 9` answered `1/52` |
| Percentage used as a whole number | `25% of 640` answered `16000` |
| The remainder, not the percentage | `25% of 640` answered `480` |

Ask a model to explain `532 − 178 = 446` and it can offer a fluent mechanism that
does not actually produce `446`. Here that is structurally impossible: a mechanism
that does not generate those digits never matches, so it is never shown. When
nothing matches, the page says "no pattern found" rather than inventing one, and
the unmatched rate is a number you can watch and drive down by adding rules.

The debrief is assembled the same way, from figures the page already computes:
your pace, the topic that cost the most clock, the slip you repeated most, and one
concrete thing to drill tomorrow.

**Nothing is sent anywhere.** The page's Content-Security-Policy sets
`default-src 'none'` with no `connect-src`, so it cannot make a network request at
all — a property you can confirm in devtools rather than take on trust. No key, no
account, no backend, no per-user cost. Serve it as a static file and any number of
people can use it at once, because each browser runs the whole thing locally.

```bash
open adaptive.html            # or adaptive.html?selftest
```

**66 assertions**, covering the exact arithmetic, round-half-to-even, answer
parsing, exactness of division and percentages at every level, monotonic
difficulty, and a worked case for every diagnosis rule including the one that must
report no pattern.

One thing the adaptive version does *not* do: reproduce a session. Difficulty depends on
your answers, so two runs from the same seed diverge the moment your timings
differ. `index.html` remains the version to use when you want two sessions on
identical questions.

## Two fixed-difficulty implementations

`index.html` is the web version: one self-contained file, no build step, no
framework, no external requests, no backend. Open it in a browser, or use the
hosted copy. The arithmetic logic is a port of the Python below, and a port is a
claim that two implementations agree. Append `?selftest` to the URL to check that
claim rather than take it: **52 assertions, each mirroring a case in
`tests/test_generator.py`**, including eleven round-half-to-even cases checked
against real Python `round(Fraction(...))` output. The result prints on the page
and to the console; `mentalMathSelfTest()` returns it as an object.

An earlier version of this README claimed 39 assertions and shipped no harness at
all, so the claim could not be run. That was the exact failure this repository's
[`RESEARCH.md`](RESEARCH.md) is an argument against, found in its own README.

One divergence worth knowing: `--seed` values are **not** comparable between the
two versions. They use different pseudo-random generators, so the same seed
produces different questions. Seeds are reproducible web-to-web and
terminal-to-terminal, never across.

## Usage

```bash
python3 -m mentalmath.cli drill
```

Full set, 80 questions in 480 seconds. Other options:

```bash
python3 -m mentalmath.cli drill -n 40 -t 240
python3 -m mentalmath.cli drill -c divide -c multiply
python3 -m mentalmath.cli drill --seed 42
python3 -m mentalmath.cli progress
```

Answers accept integers, decimals, and fractions: `36`, `0.375`, `3/8`,
`-12.5`. A blank answer skips. The session ends when the clock runs out, even
mid-question.

## Categories

| Category   | Example              | Answer form        |
|------------|----------------------|--------------------|
| `add_sub`  | `538 - 761`          | integer, may be negative |
| `multiply` | `37 x 24`            | integer            |
| `divide`   | `468 / 9`            | integer, always exact |
| `decimal`  | `70.29 + 56.79`      | 2 places           |
| `percent`  | `25% of 640`         | 2 places           |
| `fraction` | `3/8 as a decimal`   | 4 places           |

The default mix weights multiplication and division most heavily, since those
are where a clock does the most damage.

## Output

```
attempted     80/80
correct       61
accuracy      76%
elapsed       462s of 480s
rate          7.9 correct/min
projected     63 at the full time limit

category      n    acc   median
divide       16   62%     6.4s
multiply     21   71%     4.8s
fraction      6  100%     2.1s
```

## Sessions

Results are written to `sessions/` as JSON, one file per run. That directory is
gitignored: the tool is public, the performance record is personal.

## Tests

Both implementations are tested, and the two suites cover the same ground on
purpose — that is what makes them a check on each other rather than two separate
claims.

```bash
python3 -m unittest discover -s tests -t .    # 11 tests, 19 assertions
```

For the browser version, open `index.html?selftest` — 52 assertions, printed on
the page and to the console.

Both cover generation across every category, seed reproducibility, exact grading
under float-hostile inputs, and answer parsing. The browser suite adds the
round-half-to-even cases, because that is the behaviour a JavaScript port is most
likely to get wrong and least likely to notice.
