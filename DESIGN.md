# Design system

The rules this interface follows, and what does and does not transfer to sibling
projects. Tokens live as CSS custom properties in the `:root` block of `index.html`;
this file is their contract.

## The direction, and why it changed

The first version was built as test equipment: monospace throughout, square corners,
cool slate, oversized tabular digits, uppercase tracked labels. It was internally
consistent and it failed, because the result read as a countdown to something ominous
rather than as a maths practice tool. A landing page whose largest element was
`80 / 8:00` in a departure-board face is a timer, whatever the copy says.

The current direction reverses each of those specific choices. It is worth stating
them as reversals rather than as preferences, because each one was a real decision
that produced a real problem.

| Was | Now | Why |
|---|---|---|
| Monospace as the page voice | Sans; mono only for aligned digits | Monospace *is* the terminal signal. Words set in it look like machine output. |
| Cool slate, cobalt accent | Warm neutrals, green accent | Cool grey plus blue on near-black is the science-fiction recipe. |
| Near-black dark mode | Warm dark grey (`#22201d`) | Near-black is what made dark mode feel cinematic rather than comfortable. |
| Zero border radius | 8 / 12 / 16px and pills | Square corners read as mechanical. This was an explicit risk and it did not pay off. |
| UPPERCASE TRACKED labels | Sentence case | Reads as military or technical readout. |
| `80 / 8:00` in huge numerals | "Ready when you are", "8 minutes" | A clock face on the landing page is a countdown. Write durations as words. |

## Tokens

Defined once on `:root`, redefined under `prefers-color-scheme: dark`, then again
under `:root[data-theme="light"]` and `:root[data-theme="dark"]` so the manual toggle
overrides the OS preference **in both directions**. Components read tokens only; no
component is styled inside a media query.

| Token | Light | Dark | Role |
|---|---|---|---|
| `--ground` | `#f3f1ed` | `#22201d` | page background |
| `--panel` | `#ffffff` | `#2c2926` | raised surface: cards, controls |
| `--ink` | `#2b2724` | `#f2efe9` | primary text |
| `--muted` | `#7a736c` | `#a79f96` | labels, metadata, secondary text |
| `--rule` | `#e3ded7` | `#3d3833` | hairline borders |
| `--accent` | `#1f8a6d` | `#5cc9a3` | primary action, live state, progress |
| `--accent-soft` | `#ddf0e8` | `#2d463e` | selected chip fill, hover wash |
| `--warn` | `#b06a1f` | `#e0a55c` | time pressure: last 30s, slowest category |
| `--wrong` | `#b34a3a` | `#e0897a` | incorrect answers only |

Neutrals are warm on purpose, biased toward the accent rather than inherited grey.
`--warn` and `--wrong` are semantic and are **never** used as decoration.

Radii `--r-sm: 8px`, `--r-md: 12px`, `--r-lg: 16px`, `--r-pill: 999px`.
Spacing `--s1: 4px` doubling loosely to `--s8: 72px`.

## Typography

One rule does most of the work: **monospace is for digits that must line up in a
column, never for words.**

Applied: the countdown, the answer field, the results table's numeric columns, and
the `.num` helper. Not applied: headings, labels, buttons, prose, or a phrase like
"8 minutes" — a duration is a phrase, not a column.

Both faces are system stacks. The page's Content Security Policy is `default-src
'none'`, so no webfont can load; a font URL would fail silently to a fallback.

Type scale runs `--t-micro` 12px, `--t-small` 14px, `--t-body` 16px, `--t-lead` 18px,
`--t-stat` 28px, plus fluid `clamp()` for the question and the landing headline.

## Components

- **Disclosure panel** (`<details class="panel">`) — the core pattern. Native
  disclosure, so it stays keyboard-operable and screen-reader-correct with no
  JavaScript. **The summary must carry the setting's current value** — "80 questions
  in 8 minutes", "all topics", "2 of 6". This is not decoration: reviewers could not
  tell the settings were adjustable until the value appeared next to the label, and a
  collapsed filter that gives no sign it is active is worse than no filter.
- **Primary button** — pill, filled accent, white text. One per screen.
- **Ghost button** — pill, panel fill, hairline border. Secondary actions.
- **Chip** (`.cats label`) — pill, hairline. Selected state is a **filled**
  `--accent-soft` with accent text, never a one-pixel hint.
- **Switch** — a real `<input type="checkbox">` with `accent-color`. A toggle must
  look like a toggle; styling one as a button was a documented confusion source.
- **Meter** (`.catbar`) — rounded bar scaled against the largest value in its column,
  so the row needing attention reads without comparing digits.
- **Stat** — muted label above a monospace value. Labels reserve two lines
  (`min-height: 2.5em`) so values of differing label length share a baseline.

## Layout rules

- The drill screen sets `body.drilling`, which hides header and footer and gives the
  section `100dvh`. During the task, the page *is* the task.
- The primary action outranks the explanation. Reading material sits last, unfilled
  on the ground rather than on a panel, so surface treatment marks it as a different
  kind of thing before a word is read.
- Any control that only a physical keyboard can reach needs a visible equivalent.
  The numeric keypads on iOS and Android have no return key; the submit button is
  therefore always rendered and only *restyled* under `(pointer: coarse), (hover:
  none)`, never created by it. A media query must not be the only thing standing
  between a user and a working control.
- The corollary, which reads like an exception and is not: the `±` and `/` keys *are*
  created by that media query. Those keypads also omit minus and slash, both of which
  the answer parser accepts, so on a phone they are the only way to enter `-445` or
  `3/8`. A physical keyboard already has both keys, so hiding the row there removes a
  duplicate, not a path. The test is whether the control is the sole route to a
  capability — the submit button is, on touch; the assist row is, on touch; neither is
  ever the sole route on a keyboard.

## Copy

Sentence case. Say what a control does, not what the system calls it — "repeat code",
not "seed"; "Edit", not "Length", because a verb names the action a reader could not
otherwise tell was available. Explain formats in a sentence rather than listing bare
examples: a reader asked what `36, 0.375, 3/8, -12.5` meant, which is the copy
failing, not the reader.

---

# Applying this to `internship-fineprint`

**Do not copy the palette wholesale.** Fineprint already has a `DESIGN.md` and a
semantic colour system that this project does not have and must not overwrite. In
fineprint, green means *the firm stated it*, amber means *publishes nothing*, grey
means *unverified*, and its own rule is that state colours are never reused
decoratively.

Mental-math's accent is green and its warn colour is amber. Copying those across
would make green stop uniquely meaning "stated" and amber stop meaning "silent",
which breaks fineprint's stated principle that **silence never looks like an answer**.
That is a correctness problem in a database whose entire value is that it does not
overstate what firms have said.

### Transfers cleanly

- The typography rule: sans for words, monospace only for digits in columns. Fineprint
  is dense with quotes and dates and benefits most from this.
- Warm neutrals over cool. Fineprint's `--bg: #fbfbfa` / `--fg: #1a1a19` are already
  warm; they are compatible, no change needed.
- Radii and pills. Fineprint uses 7/8/10/20px; mental-math uses 8/12/16/pill. Align on
  one set — mental-math's are slightly softer and were chosen for friendliness.
- The disclosure pattern **with its current value in the summary**. Fineprint's cards
  are already `<details>`; adding the state to each summary is the single highest-value
  transfer in this document.
- Filled selected states over one-pixel hints.
- Always-rendered controls, restyled rather than created by a media query.
- Two-line label reservation so stat values share a baseline.

### Must not transfer

- **`--accent: green`.** Fineprint's accent is blue (`#1f4f82` / `#8fb8e8`) and must
  stay a colour that no record state uses.
- **`--warn: amber` as a decorative emphasis.** Amber is spoken for.
- **The copy register.** "Ready when you are" is right for a practice game and wrong
  for a reference database. Fineprint's principle 6 specifies a formal register, and
  it should keep it.
- **Uppercase labels being banned.** Removed here because they read as technical
  readouts on a game. Fineprint uses small uppercase for field labels and state pills,
  which is conventional in a dense data table and worth keeping. Judgement call, not a
  rule.

### Token mapping

| mental-math | fineprint | Note |
|---|---|---|
| `--ground` | `--bg` | compatible |
| `--panel` | `--card` | compatible |
| `--ink` | `--fg` | compatible |
| `--muted` | `--muted` | same |
| `--rule` | `--line` | same |
| `--accent` | `--accent` | **values must differ** |
| `--warn` | `--warn` | different meanings: time pressure here, caution there |
| `--wrong` | — | no equivalent; fineprint has no wrong-answer concept |
| — | `--stated` / `--silent` / `--unver` | fineprint only; do not import here either |

The right move is to merge the transferable half into fineprint's existing
`DESIGN.md` rather than replacing it. Its principles section is doing work this one
does not need to do.
