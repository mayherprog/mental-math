# Notice: what is licensed, and what this is not

## Scope of the licenses

**Code** — the Python package (`mentalmath/`), the tests (`tests/`), and the JavaScript
inside `index.html` — is licensed under the MIT License. See `LICENSE`.

**Written material** — the Markdown documents (`README.md`, `RESEARCH.md`) and the prose
content of `index.html` — is licensed under Creative Commons Attribution 4.0
International. See `LICENSE-DOCS`.

`index.html` is a single self-contained file containing both. The licenses apply to the
respective parts, not to the file as a unit.

**Quoted material in `RESEARCH.md`** is not the copyright holder's to license. Short
quotations from company recruiting pages are reproduced under fair use for the purpose of
verification and criticism, each attributed to its source with a link. Anyone
redistributing this repository is responsible for their own compliance.

## This does not replicate any firm's assessment

`RESEARCH.md` documents an attempt to find out what is publicly known about the numerical
screening assessments used by several trading firms. Its conclusion is that very little
is: the widely circulated "80 questions in 8 minutes" format has no firm-published source
at any of the six firms examined.

This tool therefore reproduces a **constraint** — mental arithmetic, under time pressure,
without a calculator — and not any firm's test. Nothing here should be read as a claim to
know what any company's assessment contains, and the default settings are not anyone's
specification.

## On the research

Every claim in `RESEARCH.md` carries a source link and a tier describing how much weight
that source can bear. Findings were checked by a separate adversarial pass whose purpose
was to refute them; several claims did not survive and were removed or marked.

It is a snapshot dated 2026-07-28. Recruiting processes change and pages get rewritten —
one page examined during the research had been completely rewritten between an archived
copy and the live version. **The firm's own current page is always the authority, not this
repository.** Where a firm publishes nothing, that is recorded as silence rather than
filled with a guess.

No content that appeared to be leaked live assessment questions was collected, cited, or
reproduced.

## Session data

The tool records your answers so improvement can be measured. That record stays on your
own machine: the command-line version writes to a gitignored `sessions/` directory, and
the web version writes to your browser's `localStorage`. Nothing is uploaded, and there is
no server. The tool is public; the performance record is not.
