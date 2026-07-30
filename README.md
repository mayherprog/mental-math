# mental-math

A timed arithmetic drill that records every answer, so improvement is measured
rather than felt.

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

## Two implementations

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
