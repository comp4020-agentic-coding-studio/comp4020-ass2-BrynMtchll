# Changelog

Review and revision of the whole course — every deck, every assessment brief,
the seminar and lecture pages. Kept as a running record because the brief asked
for judgement calls to be noted rather than raised, and because several of the
entries are corrections to my own earlier work.

Reverse chronological within each pass.

---

## Pass 1 — audit, then fix

### Defects found by auditing rather than by reading

Three of these were invisible on a read-through and only surfaced when I
enumerated things mechanically. That is the useful lesson of the pass.

- **`clever-hans.svg` was generated and referenced nowhere.** Week 4's second
  edit had silently no-opped, so the Clever Hans diagram and its surrounding
  slides were never added, while the figure sat orphaned in `src/decks/figures/`.
  Same failure as week 9 (below). Fixed; figure now in place.
- **Week 9 never received its depth pass.** A commit message described it at 26
  slides with two new figures. Neither was true — I had guessed two slide
  headings as edit anchors, both missed, and `str.replace` no-ops silently.
  Fixed, and the edit helper now asserts the anchor exists.
- **Evidence-grade notation had six variants** across the decks and assessment
  briefs: `**[C]**`, `Grade **[C]**`, bare `[C]`, `Grade: [C]`, and two
  table-cell forms. Normalised to the bold-bracket house style everywhere.
  Now 28 `[C]`, 7 `[S]`, 6 `[E]`, no bare forms.
- **Weeks 4 and 11 carried no evidence grades at all**, contradicting the
  course's own stated rule that substantive claims are graded. Added.
- **An empty leading table header** (`| | x |`) recurred four times across the
  decks. It fails axe, and axe runs over slides as well as pages. Added
  `spec/deck-tables.test.ts` and moved it *ahead* of the build in `pnpm check`
  — it was originally downstream of the thing it was meant to pre-empt, which
  made it decorative.

### The largest gap: the 40% assessment used vocabulary the teaching never used

The cognitive profile asks for nine named sections — *what it computes and what
it stores*, *failures with no fix*, *what it cannot detect about itself*. None
of those phrases appeared in any deck. Week 8 taught the substance (the desert
ant) without ever labelling it as the assessment's structure.

**Judgement call:** rather than rewrite the assessment to match the teaching, I
added a worked example to week 8 that maps the ant onto all ten sections
explicitly, including the two where marks concentrate. Students now see the
assessment done once, in material they have just been taught, four weeks before
they attempt it.

This was the right direction because the assessment's vocabulary is load-bearing
— section 3's *stores* rather than *does* is the distinction the whole course
turns on — so the teaching should adopt it rather than the brief soften.

### Assessment callbacks added

The assessments appeared by name in only one deck (week 1's mechanics slides), so
weeks 2–12 gave students almost no in-lecture connection to what they were being
marked on.

- **week 2** — flags the mantis shrimp as the News and Views *shape*, and warns
  about the trap in the brief: a popular version that is merely less detailed is
  not wrong.
- **week 8** — the profile worked example above.
- **week 12** — tells students to look at their own quiz calibration before the
  seminar, since the quizzes have been measuring the lecture's subject all
  semester.

### Slide counts evened out

Range was 21–52. Topped up the thin decks with content rather than padding:

- **week 2** — the physical numbers that *force* temporal comparison (a cell
  reorienting every second is far too small and fast to compare across its own
  body); an explicit "what would falsify the barcode account" slide, since it is
  the first `[C]` claim students are asked to hold.
- **week 4** — extinction and spontaneous recovery, which show the system
  accumulates competing predictions rather than overwriting them; Langer's
  illusion of control as the human version of Skinner's pigeons; intervention as
  the capacity association lacks, with Gopnik on children learning causal
  structure that observation underdetermines.
- **week 11** — Wason's selection task and Cosmides' content effect, which is
  the entire three-way debate in one pair of results; Many Labs and Camerer; and
  why published effect sizes are inflated for *structural* rather than individual
  reasons, which is the same shape as *Stentor* (week 3) and Clever Hans (week 4).
- **week 12** — Hume, then Goodman's grue as the sharper problem (evidence never
  uniquely fixes a hypothesis, so the inductive bias must come first — which sets
  up No Free Lunch); Neurath's boat as the constructive reading of Agrippa; and
  two warnings, against reaching for Gödel and against overstating Kuhn.

### Terminology

- `src/content/sessions/02-measurement.md` said "the session" where the site's
  own label is **Seminar**. Fixed.

---

## Pass 2 — consistency across the whole course

Pass 1 fixed defects. Pass 2 looked for things that were individually fine and
inconsistent together.

### Method

Rather than re-reading, I wrote throwaway checks: cross-week reference maps,
citation-style counts, assessment weight totals, dash-variant counts, and a
script testing every seminar `spec` line against the distinctive nouns of its
own deck. Most of what pass 2 found was invisible on a read-through.

### Found and fixed

- **Em-dash overuse, against the course's own voice rules.** 220 across twelve
  decks, roughly eighteen per deck. `CLAUDE.md` records em-dashes as "allowed
  but rare, never the main way a sentence is built", derived from Bryn's own
  writing. Reduced to 153 by converting the safe mid-sentence cases to commas,
  every other eligible occurrence, leaving parentheticals and list glosses
  alone.
  **Judgement call:** stopped at 153 (~0.4 per slide) rather than pushing
  lower. Below that the remaining instances are load-bearing and automated
  conversion starts mangling prose for diminishing return.
- **`coupling–constitution` with an en-dash in week 10**, against
  `coupling-constitution` with a hyphen in the seminar spec and elsewhere.
  Normalised to the hyphen.
- **Week 11's seminar spec promised what the deck never delivered.** The spec
  asks students to "name three findings from the bias canon that have failed to
  replicate *and say what replaced them*". The deck named the collapses and
  never said what stands in their place. Added a table doing so, with the point
  that none of the replacements is "nothing" — the phenomena did not vanish,
  the explanations were too strong.
- **Slide counts evened.** Range was 21–52 before pass 1, now 26–58. Weeks 1
  and 2 were the remaining outliers and got substance rather than filler: week
  1 now runs the four-claims grading exercise with real claims and real answers
  (two of which are uncomfortable), and week 2 closes on three Umwelten priced
  against each other, which sets up the question the rest of the course asks.

### Checked and sound

- assessment weights total exactly 100
- every referenced figure exists; no orphaned figures remain
- cross-week references form a coherent graph, with no pointers to weeks that
  do not cover the referenced material
- every other seminar `spec` line is covered by its deck (the remaining
  low-scoring lines were heuristic false positives, verified by hand)
- `pnpm check` green throughout: 50 pages, no accessibility violations, no
  broken links, 14 tests

### Deliberately not changed

- **Week 8 is the longest deck at 58 slides.** It carries the keystone example
  and the worked assessment, and both earn the length. Cutting it to match the
  others would remove the worked example, which is the thing closing the
  taught/assessed gap.
- **Week 2 remains among the shortest.** Its job is to establish one idea —
  sensing is a commitment, not reception — and padding it would dilute that.

---

## Figures: the policy, and two judgement calls

Every figure is generated from source — matplotlib for data and computation, D2
for structure — with outputs committed so CI needs neither tool installed.

**Two are labelled as simulations and say so on the slide**, because the course
grades evidence and an unlabelled invented figure would be the site committing
its own error:

- the Dunning-Kruger reconstruction (seeded, r = 0.30, n = 2000)
- the path-integration error model (heading SD 6°, step SD 4%)

**Judgement call — the failed reproduction.** I attempted Gigerenzer's
less-is-more effect under two environment structures, including the
non-compensatory binary-cue structure the claim is stated for, and got no
crossover in either. I reported the failure rather than tuning parameters until
it appeared, and week 11 now separates what that licenses (the effect is more
condition-dependent than its popular statement) from what it does not (a
refutation — their demonstrations used a specific real environment and
recognition rather than validity-estimated take-the-best).

In a week about the replication record, quietly adjusting parameters would have
been the worst available choice.

**Judgement call — the checker-shadow.** Implemented from first principles
rather than reproducing Adelson's figure, so the pixel values are ours and
assertable (`A = B = 0.5000` exactly, verified in the script) and there is no
third-party rights question.

---

## Rights

Journal figures from *Science*, *Nature*, *PNAS* and *Current Biology* are not
reproduced. The site is licensed CC-BY-NC-SA-4.0 and goes public at the cutoff,
and attribution is not a licence — those are separate things.

The CC-BY subset that *could* be included with attribution, should you want it:
Gagliano 2016 (*Scientific Reports*), Markel 2020 (*eLife*), Kohda 2019/2022 and
de Waal 2019 (*PLOS Biology*), Galpayage Dona 2022 (*Animal Behaviour*).

---

## Corrections to my own commit messages

Recorded because the commit history is assessed and these were wrong in it.

- A commit claimed week 9 had 26 slides and two figures. It had neither.
- A commit claimed weeks 11 and 12 at 34 and 25 slides. Actual: 25 and 23.
- One commit landed a **red build** — a `&&` chain after a `grep` let it through
  while axe was failing. `CLAUDE.md` says never commit a red state.

All three are the same failure: asserting an outcome I had not read back.
