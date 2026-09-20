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

## Pass 3 — language precision and narrative flow

### Method

Mechanical audits again: wordlists for vague and pop-science register,
confidence-mismatch patterns, weak sequential transitions, sentence lengths over
34 words, term first-appearance versus first-definition, and section-divider
counts per deck.

### Language: fewer hits than expected

Only four across roughly 400 slides — "remarkable" (wk8), "kind of" (wk12), one
35-word sentence (wk12), one awkward inversion (wk8). Zero weak sequential
transitions and zero confidence-mismatch patterns.

That suggests the voice rules in `CLAUDE.md` were doing their job while the
decks were being written, which is the point of having them.

### Terminology: six terms used bare

Each now carries a one-line definition at first use.

| Term | Was | Now |
| --- | --- | --- |
| underdetermination | heading only, wk12 | defined before the diagram |
| informational cascade | heading only, wk10 | defined before the examples |
| requisite variety | table cell, wk1 | defined above the inequality |
| precision | wk6 heading | defined as inverse variance, since it differs from the ordinary sense |
| non-compensatory | wk11, in passing | defined where the simulation depends on it |
| self-model | **forward-referenced in wk5**, defined in wk7 | glossed at first use in wk5 |

The self-model case was the real defect: a term introduced two weeks before its
definition.

### Macrostructure: was invisible to students

The four-part structure existed in `docs/course-model.md` and nowhere a student
would look.

**Judgement call:** rather than a single page nobody revisits, every deck now
opens with a *"where this week sits"* slide marking its part, plus a line saying
why the third part is a control group rather than a tour. Repetition across
twelve decks is what makes a macrostructure visible.

Weeks 1, 2, 4 and 9 had one section divider between them. They now have three to
five each.

### Weeks 8–10: slides that stopped at description

Four slides described the organism and never named what it established. Now they
land the asymmetry:

- neuron counting showed our intuitions tracked the wrong quantity, and only
  from outside the lineage
- we can say what evidence would settle bee play; we cannot say what would
  settle the same question about ourselves
- the octopus gap has an outline and ours does not
- an informational cascade is invisible from inside, because every step was
  reasonable

**Judgement call:** I did not append a thesis line to all 124 slides in those
weeks. Doing so would itself be a rigid per-week template, which the brief
elsewhere asks me to avoid. Section closers and organism-introduction slides
carry it; worked detail slides do not.

### Weeks 11–12: the plant existed but did not reach

Week 11 already said the literature on human error is subject to human error. It
did not connect that to the course. It now names the site's own grades and
reading list as products of the architecture weeks 3–7 described, and cites my
failed reproduction as the instance students have already seen — then states the
question week 12 answers, so the turn arrives prepared rather than abrupt.

### Both bookends were echoing rather than sharpening

Week 1 closed "Week 12 asks this again / with no card", and week 12 closed with a
near-mirror. Both now sharpen: week 1 says what the card found and what has no
card; week 12 states the thesis in its narrower final form — the discarding is
not reportable, the checker is the checked, and the literature on that is
subject to it — closing on a track record being the only thing ever on offer.

---

## Pass 4 — benchmarked against COMP3670

Compared the decks against the real ANU **COMP3670 / COMP6670 Introduction to
Machine Learning** handouts (Sem 2 2026, Marcondes) in
`~/Downloads/comp3670 materials`.

### The measurement

| | Slides / pages |
| --- | --- |
| COMP3670 Lectures 1–4 | 69, 89, 71, 73 |
| These decks, before this pass | 29–60 |

So roughly half the length of a real 3000-level ANU lecture. But length was the
symptom; the diagnosis is what their pages contain.

### What their specificity actually consists of

Read closely, their pattern is consistent and repeatable:

1. **Definition**, in a styled box, term bolded
2. **A concrete example immediately after**, always numeric
3. **The arithmetic in full** — `0.06 + 0.14 + 0.04 + 0.06 = 0.30`
4. **A sanity check** — *"They add to 1, as a distribution must"*
5. **A collected comparison table** that makes a surprise visible
6. **A labelled moral** that names the transferable lesson

Plus a *"Recall the end of Lecture 1"* opener carrying an explicit open question,
a *"Why we cannot answer it yet"* slide that maps each vague word in the question
to the concept that will formalise it, and named confusion-anticipation slides
(*"a random variable is neither random nor a variable"*).

### Adopted

- **Worked numeric examples with visible arithmetic and a sanity check.** The
  most valuable is the quiz scoring, which was a genuine taught/assessed gap:
  the deck asserted that certainty-based marking is a *proper* scoring rule and
  never demonstrated it, while assessing students with it at 15%. Now derived —
  expected score is linear in `p` for each declaration, setting the lines equal
  gives `p = 2/3` and `p = 4/5`, and those are the published 67% and 80%
  thresholds recovered from the payoff table. New figure plots the envelope.
- The **bee neuron budget** now shows the addition and the division rather than
  stating "64%", with a sanity check that the parts sum to the published total,
  so we know we have the whole budget and not a subset.
- **Ashby's law worked on a thermostat** with real numbers, including the check
  that repertoire beyond the disturbance variety buys nothing.
- **"Recall the end of week N" + a highlighted open question**, on every deck
  from week 2. Their strongest device, and the one this course needed most: it
  claimed to be cumulative and was only asserting it. The eleven carried
  questions now form a visible chain from the card in week 1 to the
  self-application in week 12.
- **"The moral."** as a labelled device where a slide's lesson generalises past
  its example.

### Deliberately not adopted

**Judgement call: no definition/example box formalism.** That register is right
for measure theory, where a definition is stipulative and an example is a
verification. It is wrong here. Boxing contested empirical claims as
*Definitions* would manufacture exactly the false precision this course is
about — and the course already has a notation for epistemic status, which is
`[E]`/`[C]`/`[S]`.

### Still short of the benchmark

Decks now run 30–62 slides against COMP3670's 69–89. Closing that fully would
need a worked example per conceptual move, and the honest constraint is that a
conceptual course has fewer things that *can* be worked than a mathematical one.
Where a derivation exists, it is now shown.

---

## Pass 5 — worked examples throughout

Went through every deck for abstract claims with no concrete instance, and added
a worked example in the COMP3670 register: numbers, the arithmetic visible, a
sanity check, then a labelled moral.

Nine added. The three that were genuine absences rather than improvements:

- **Week 11 had no base-rate calculation at all.** The single most-cited worked
  example in the heuristics literature was missing from the week about that
  literature. Now worked twice on the same screening problem — once as
  probabilities (`P(D|+) = 0.0090/0.0981 ≈ 9%`, against a modal intuition of
  80–90%) and once in natural frequencies (`9 / 98`). The second version is
  Gigerenzer's argument made operational rather than asserted: identical
  arithmetic, no formula, and much of the deficit disappears with the format.
- **Week 2's barcode hypothesis never committed to a number.** It does now:
  `420 nm / 12 bins = 35 nm` predicted threshold against `25–30 nm` measured and
  `1–4 nm` in the comparison animals. The prediction lands, which is why the
  claim is `[C]` rather than `[S]`, and the moral generalises — a story becomes
  a scientific claim when it commits to a number it could be wrong about.
- **Week 10 asserted that averaging helps without ever showing why.** Now
  `SE = 21/√60 = 2.7`, then the shared-versus-private error decomposition that
  explains the Lorenz result exactly: influence converts private noise into
  shared content, so spread falls 21 → 1.6 and collective error stays at 6.7.

The other six:

| Week | Worked |
| --- | --- |
| 3 | the U-trap as a rule with no exit, then the one extra bit that opens one |
| 4 | Rescorla–Wagner over four trials, then blocking as arithmetic (0.30 → 0.015 per trial) |
| 5 | route inflation on two 400 m pairs, and why directional error is not noise |
| 6 | a precision-weighted update twice, same error moving the estimate 1.2 then 4.8 |
| 7 | the compression ratio, ~10¹⁴ synaptic states against ~5×10³ bits of report |
| 8 | the stilts arithmetic — 1,000 strides at 13 mm gives a 3 m overshoot |
| 9 | 42 million neurons per octopus arm against 71 million in a whole mouse |
| 12 | two Brier scores on identical accuracy, 0.272 against 0.210 |

**Judgement call on week 7.** The synapse and speech-rate figures are
order-of-magnitude, so the slide says the exact numbers do not matter and the
conclusion survives four orders of magnitude either way. Stating a ratio that
loose without flagging it would be the false precision this course objects to.

Decks now 33–65 slides, against COMP3670's 69–89.

---

## Pass 6 — the site as a reader meets it

The first five passes read the course. This one read the *site*, on the route a
prospective student actually takes: home page, a couple of non-adjacent weeks,
an assessment, a deck. Different route, different defects.

### Defects

- **Four listing pages were still addressing the builder.** `/assessments/`
  said "Weights should sum to 100"; `/sessions/` said "Set the visible singular
  and plural names once in `src/site-config.ts`"; `/lectures/` explained how
  `related:` works; `/people/` had no prose at all. All four are on the only
  route to a week page. None carried a `STARTER_CONTENT` marker, so
  `check:evidence` was blind to them. Rewritten, and a spec test now asserts
  that no public page contains builder-facing text.
- **The policies page claimed something false.** It says "the individual briefs
  link back to this page rather than restating it". None of the four did. Each
  brief now closes with that link.
- **No definition of the evidence-grading scheme existed outside week 1's
  seminar body.** The notation appears on a dozen pages and the policies page
  makes students accountable for grades they assign. `/evidence/` is now the
  canonical definition, with the standing contested set as a table.
- **No schedule.** Lectures and seminars were two parallel lists with no page
  joining them. `/schedule/` is the twelve weeks in one table, grouped by the
  four parts of the argument.
- **No readings anywhere on the site**, in a course whose method is reading
  primary literature. Seventy-four sources now, across twelve weeks, annotated.
- **The dependency chain was absent from the graph.** 22 edges, none of them
  session-to-session. Eighteen session-to-session edges added, each one a
  dependency the week's prose already carried.

### Judgement calls

- **Readings live in the body, not in `links:` frontmatter.** `links:` is the
  idiomatic field and `RelatedContent` renders it for free, but its shape is
  `{label, url}` and the annotation is most of the value — which paper the
  seminar turns on, which one is the objection you are expected to arrive with.
  A bare link list would have been tidier and worth less.
- **No evidence grades on the readings.** A grade belongs to a claim, not to a
  paper, and several of these papers contain claims at two different grades.
  Saying so on every week page is a small piece of teaching that a graded
  bibliography would have quietly contradicted.
- **Every DOI resolved against Crossref, none recalled.** About a third of the
  first-pass search hits were wrong in ways that looked right: reprints in
  edited collections for Shannon and for Nisbett & Wilson, the author response
  rather than the article for Markel, the preprint rather than the *Cell* paper
  for Whittington.
- **A failing test was satisfied rather than relaxed.** The reading test
  requires three resolvable sources per week; weeks 1 and 4 came in at two.
  Added Ramachandran & Gregory (1991) on perceptual filling-in of induced
  scotomas to week 1, which makes the blind-spot demonstration citable, and
  Rescorla (1988) to week 4.
- **Six figures moved from the decks onto the week pages.** The site is
  otherwise image-free by design and stays so; these six are arguments rather
  than decoration, and two of them are computations rather than depictions.

### Closed decisions

- **The title stays, and the home page grades it [S].** The tension between a
  deficiency-sounding title and a course that rejects the deficiency reading is
  real. Resolving it by applying the course's own notation to its own title is
  better than softening either.
- **Artificial systems stay out, and the home page says why.** They are not an
  independent lineage — built by one of the systems under study, out of data
  produced by it — so they are a case the model should predict, which is where
  the cognitive profile's optional speculative close already puts them.

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
