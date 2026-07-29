# What is actually known about quant firms' numerical screens

Researched 2026-07-28. Point-in-time. Every claim below carries a source and a tier.

This document exists because this repository is a practice tool for a test whose format
is not public, and pretending otherwise would make the tool dishonest. What follows is
an attempt to find out what is genuinely documented, and to be explicit about how little
that turns out to be.

---

## Headline finding

**The "80 questions in 8 minutes" format has no firm-published source at any of the six
firms examined.** It appears on no company website, in no university career-services
document, and in no source whose origin could be traced. It exists on candidate forum
posts and on test-preparation vendors, which contradict each other on every specific:
the pass mark, the scoring penalty, whether skipping is penalised, and in one case the
numbers themselves, printed as "8 in 80".

Two independent research passes disagreed about which firm the format even belongs to.
One traced it to Optiver. The other traced it, with a document trail, to **Akuna
Capital**, whose reported format matches on both numbers exactly (80 questions / 8
minutes, plus 24 sequence questions / 12 minutes), while Optiver's sequences section is
reported quite differently. That disagreement is recorded here rather than resolved,
because resolving it would require evidence neither pass found.

The practical consequence: a number that circulates as a specification is folklore of
unknown origin, and at least one firm's format appears to have been re-labelled with
other firms' names by aggregators and search engines.

---

## Method

Every claim was graded before it was believed.

**Tier 1** — the firm itself: its careers site, its own published materials, its
recruiting FAQ, or text it authored inside a job posting.
**Tier 2** — institutional secondhand: university career-services or quant-club
documents, campus recruiting materials.
**Tier 3** — aggregated candidate reports: Glassdoor, Reddit, Blind, Wall Street Oasis.
These establish only that something is *widely reported*, never that it is true, and
only where multiple genuinely independent accounts agree.

**Excluded entirely:** test-preparation vendors and coaching sites. They may be read to
find a trail back to a real source; nothing they assert is ever cited as evidence. Their
commercial incentive is to sell certainty they do not have. Also excluded: any content
appearing to be leaked live assessment questions.

**Adversarial pass.** Every firm's findings were handed to a second researcher whose only
instruction was to refute them — checking for over-generous tier assignment, staleness,
circular corroboration (many sources tracing to one origin), wrong role or region, and
misattribution between firms. Several claims did not survive. Those are marked.

---

## Optiver

The only firm here with substantial tier 1 material, and it held up completely under the
refutation pass — every quote was reproduced word for word from the live pages.

**Firm-stated and verified:**

- Calculators are not permitted. *"To effectively evaluate your skills, the use of
  calculators is not permitted during our assessment."*
  — [Sydney campus recruiting FAQs](https://www.optiver.com/join-us/stories/optiver-sydney-campus-recruiting-faqs/)
  **Caveat:** this page is scoped in its own text to Australia and New Zealand. The US
  and Europe FAQs do not contain the word "calculator" at all. For a US application this
  is a strong inference, not a firm statement.

- **One assessment attempt every 8 months, across all offices and all roles.** *"We only
  allow candidates to attempt an assessment at Optiver every 8 months, across all offices
  and roles."* Scores carry over automatically within that window.
  — [Sydney campus recruiting FAQs](https://www.optiver.com/join-us/stories/optiver-sydney-campus-recruiting-faqs/)

- No resets or retakes once an attempt has started, and a **separate 8-month cooling
  period before reapplying** after an unsuccessful application.
  — [Europe recruitment FAQ](https://www.optiver.com/join-us/stories/optiver-europe-recruitment-faq/)

- The campus process begins with an online assessment, and stage sequences differ by
  role.
  — [US campus recruiting Q&A](https://optiver.com/working-at-optiver/career-hub/us-campus-recruiting-faqs-2/)

- Preparation advice, in full: *"it may be helpful to practice activities that involve
  quick problem-solving skills, such as mental math and strategy games."* No question
  count, no time limit, no arithmetic breakdown.
  — [US campus recruiting Q&A](https://optiver.com/working-at-optiver/career-hub/us-campus-recruiting-faqs-2/)

- Real preparation guidance is emailed privately: *"Please refer to the Interview tips
  and tricks document that was sent to you in your confirmation email."* Not published.

- Optiver declines to ratify circulating descriptions of its process. Asked how a
  candidate should know what is true, the published answer is to ask a recruiter.

- *"Being good at mental math is necessary but insufficient to thrive as a Trader at
  Optiver."*

**Negative findings.** `numericaltest.optiver.com` appears in search indexes with
descriptive test text attached, but refused all connections when tested on 2026-07-28 and
has no archive snapshot. The Wayback Machine does hold 2016 pages under
`/numerical-test-register/`, indicating a decommissioned legacy system — which explains
the stale index entry. The "Brain Circuit" public quiz is also gone. **There is no
currently live Optiver-published practice test.**

**Not established:** question count, time limit, pass mark, scoring penalty, or whether a
speed-arithmetic section appears in a Quantitative Research intern's assessment at all.

---

## Jane Street

**No evidence of a timed mental-arithmetic screen exists, and Jane Street's own writing
cuts against one.**

- The trading interviews page states the interview *will feel more like a conversation
  than a quiz* and *will not involve complicated math*.
  — [Trading interviews](https://www.janestreet.com/trading-interviews/)

- The 2020 process blog states the firm does not ask math or probability questions for
  general software engineering roles.
  — [Interview process (2020)](https://blog.janestreet.com/jane-street-interview-process-2020/)
  *Tier 1 for 2020; the post disclaims its own durability.*

- The only online assessment Jane Street documents is for **Strategy and Product**:
  multiple-choice and short answer, taking about an hour.
  — [Strategy and Product interviewing](https://www.janestreet.com/join-jane-street/sp/interviewing)
  Candidate reports describe roughly ten questions in sixty minutes — about six minutes
  per question, which is structurally the opposite of a speed drill.

- The only quantitative preparation material the firm publishes is a
  [Probability and Markets Guide](https://www.janestreet.com/probability-markets/).

**The circulating "60 questions in 8 minutes, 70–80% pass bar" figure should be treated
as unsourced and probably fabricated.** The traceable origin carries no citation, no
byline, and no methodology; its pass-bar figure drifts between its own pages; and it
additionally claims Jane Street screens software engineers with a timed mental math test,
which Jane Street's own words directly contradict. A source demonstrably false on a
checkable claim does not get believed on an uncheckable one. The number also closely
mirrors the Optiver figure, which is the expected signature of a claim migrating between
firms.

---

## Five Rings

**No tier 1 or tier 2 source documents the screen.** All seven firm-controlled pages and
both live Greenhouse postings were re-fetched independently and contain nothing about
assessments — including the live
[Summer Intern 2027 Quantitative Trader posting](https://job-boards.greenhouse.io/fiveringsllc/jobs/5139668008).

What tier 3 accounts converge on: an early, heavily time-pressured quantitative screen,
probably delivered on HackerRank, weighted toward estimation and bounding, expected
value, geometry, logs and deliberately non-routine problems — plus a separate rapid-fire
recruiter screen built on Fermi estimation.

**Dropped outright:** the sequences section. The only numbers ever attached to it are
another firm's (see the Akuna attribution above). No question count and no time limit
survived scrutiny; every precise figure in circulation traces to downstream aggregation
of a handful of anonymous posts.

---

## Susquehanna International Group

**Publishes nothing about test format.** The only firm statement about how candidates are
evaluated is about puzzles: *"We use puzzles to emulate the trading environment."*
— [Trading careers](https://sig.com/careers/trading/)

Candidate reports do converge that a timed online assessment exists early in the trading
process. What those candidates describe is **counting, logic, conditional probability,
expectation and word problems** — probability and logic, not rapid mental arithmetic.
That conflicts with the vendor framing and agrees with SIG's own language.

The circulating specifics are worthless: vendors state at least five mutually
incompatible formats across four different testing platforms (HackerEarth, CodeSignal,
Codility, Mercer Mettl).

---

## Citadel / Citadel Securities

**Nothing reliable is publicly known.** No documented question count, no time limit, no
calculator policy.

The only concrete format in circulation — "50 questions in 12 minutes" — is the
off-the-shelf **Wonderlic Cognitive Ability Test** specification, publicly documented and
identical for every employer that has ever used it, resold by vendors with the employer
name swapped in. It is also not an arithmetic-speed test, so it would not justify a
"Citadel mental math" module even if true.

Citadel's published interview-process pages
([Quantitative Research](https://www.citadelsecurities.com/careers/career-perspectives/our-quantitative-research-interview-process/),
[Engineering](https://www.citadelsecurities.com/careers/career-perspectives/our-engineering-interview-process/))
describe funnels beginning with a live video interview, with no online assessment step.

**Important scope caveat.** Those pages address quantitative research and engineering,
largely the experienced funnel. Citadel Securities publishes **no interview-process page
for Markets & Trading at all**. So the firm's silence is silence about the wrong
population. The defensible statement is not "Citadel does not use a numerical screen" but
"Citadel documents nothing about the track where one would most plausibly sit."

---

## Point72 / Cubist Systematic Strategies

**Nothing reliable is known.** Point72's own current postings for the Academy
investment-analyst track state that an unspecified *"online assessment"* follows the case
study. That is the entire firm-published record; it never says what the assessment
contains. Cubist postings, checked across two separate requisitions, describe **no
assessment stage at all** —
[Cubist Quantitative Researcher Intern](https://job-boards.greenhouse.io/point72/jobs/7297611002).

Point72 also states that *"actual dates and interview processes vary by program and
region"* — the firm itself denying that one pipeline generalises.

The same Wonderlic pattern appears here, and collapses for the same reason. The vendors
cannot even agree on which instrument they are selling answers to, which is what
disagreement among fabricators looks like.

---

## What this tool therefore claims

It reproduces **a constraint, not an assessment**: mental arithmetic, under time
pressure, without a calculator. That constraint is firm-stated at Optiver and consistent
with what candidates report elsewhere.

It does **not** claim to reproduce any firm's assessment, and it does not offer per-firm
question mixes, because for five of these six firms there is no public basis for one, and
for Jane Street building one would require contradicting the firm's own published words.

The default 80-question, 480-second setting is adjustable and is **not** presented as any
firm's specification. It is a round number that produces the right kind of pressure.

---

## Limitations

- This is a snapshot of 2026-07-28. Recruiting processes change and pages get rewritten;
  one Citadel page was found to have been completely rewritten between an archived copy
  and the live version during this research.
- Glassdoor and Wall Street Oasis blocked direct fetches, so some tier 3 material was
  read at search-summary level rather than from the primary page. Those claims are weaker
  than the tier alone suggests.
- Absence of a published policy is not proof that no policy exists. Several findings here
  are "the firm says nothing," which is a fact about the public record, not about the
  firm's internal practice.
- Six firms is not the industry.
