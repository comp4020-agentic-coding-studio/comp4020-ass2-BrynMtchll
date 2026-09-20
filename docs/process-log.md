# Process log

Running record kept as the work happens, to draw `PROCESS.md` from later.
Prompts are **verbatim**, including typos — paraphrasing them would destroy
their value as evidence. Annotations are written at the time, not
reconstructed.

Not site content. `PROCESS.md` runs 400–600 words, so this is raw material,
not a draft of it.

Commit URLs take the form
`https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/commit/<hash>`.

---

## 1. Setup

> get setup with assignment 2

Cloned the provisioned repo, merged the harness forward, turned the published
spec into tests. Two findings worth citing:

- **The deliverables table says A2 carries a reflection (`assignment-2.md`); the
  code says it doesn't.** `scripts/check-evidence.ts:44` returns an empty list
  for assignment repos and prints "none needed — an assignment's written account
  is PROCESS.md". Settled from the code rather than the table.
- **A rule carried forward was inverted.** Every earlier repo hardcoded Astro's
  `base` in `astro.config.mjs`; this template derives it in
  `scripts/pages-base.ts`. Carrying the old rule verbatim would have been
  actively harmful. This is the clearest example of why a harness merge is a
  merge and not a copy.

Spec tests landed **3 red / 9 green** deliberately — red on what isn't built,
green on contracts the starter already meets and must keep meeting. One green
test closes a real gap: `check:evidence` greps for the `STARTER_CONTENT` marker,
so deleting the comment without replacing the prose passes it.

`c39baef` harness carry-forward · `78f832d` spec as contracts

---

## 2. Subject

> ok i've got an idea; natural intelligence - starting from the ground up with the lowest possible lifeform intelligence and building out from this and branching into various kinds of intelligence, culminating wiht the highest forms of intelligence and even speculating beyond. Write into claude.md that i want to focus on maticulousness and precision with ideas that are refined and reason about a scientific model. For cohesion i want this to work like building a model of intelligence. Prioritise (and add to claude.md) the necessity of pooling from philosophical, neuroscientific, evolutionary and psychological angles on intelligence. The first major component will be doing vast research from these fields to consolidate a unified course outline. no need to develop ideas into specifics now, just focus on core primitives so that options can be assessed before going forward.

Wrote the precision and four-lens rules. Raised two problems rather than
building past them:

- **"lowest → highest" is a ladder, and the ladder is wrong.** *Scala naturae*
  is what evolutionary biology spent a century dismantling. The fix was already
  latent in the prompt's own word "branching".
- **"Natural intelligence" isn't niche and isn't a thesis.** Comparative
  cognition is taught by real departments.

Also noted a tension I created myself: mandating four lenses per week pushes
toward a template, and a template is the failure the brief names. Recorded the
resolution in the harness — the lenses are a checklist for the argument, not a
shape for the page.

`6aeb3e4`

---

## 3. Sharpening to a thesis

> ok entertain this for a more niche angle, still building off what we already have; "how and why you're dumb" ...

Accepted, because it fixed the ladder (the summit becomes its own limits) and
gave the course a position rather than a category. Flagged the danger that
matters: **much of the "you're irrational" canon has not replicated** — ego
depletion, social priming, and the classic Dunning-Kruger curve, which is
substantially reproducible from regression to the mean. A course with this title
reciting that canon would commit its own subject.

No commit — discussion only.

---

## 4. Research and outline

> ok give me an outline with formal references

Verified 14 load-bearing citations against primary sources before writing, and
said plainly which of the 63 were carried from reading instead. Memory failed on
volume and page numbers, not authors and years — worth recording, since the
course's own rule is that no claim survives on plausibility alone.

`34642d3`

---

## 5. Voice — the most instructive reversal

> side note on voice to add to claude.md - for all writing to be done for the course content for this assignment I'd like your writing style to sound less like AI - read through my writing, namely the pdfs and md files in /Users/brynly/courses to derive rules for more normal writing style

> wait exclude comp3320 reoprt, look at [three PDFs]

**The first pass was wrong, and wrong in a way that would have made the problem
worse.** Rules derived from the comp3320 report — bolded claim-sentences,
one-word paragraph fragments, an em-dash ban, a British-spelling rule — turned
out to describe agent-written prose, not mine. Four rules were backwards.

Rebuilt from the RIN paper and both COMP4620 assignments. What's actually
distinctive: connective-first sentence openers, "that is," to sharpen a claim
just made, contractions kept in formal prose, bold marking a defined term rather
than an assertion, and anomalies stated without being explained away — *"I was
unable to determine a cause of error."*

Also recorded the one off-voice passage in my own corpus (the RIN reflection
section) as a negative example, since ethics-and-implications prose is where
padding appears — which on this site means the philosophical weeks.

**Both commits kept deliberately.** The history shows the wrong derivation and
the correction, which is more honest than a clean line.

`a60b742` wrong derivation · `7169948` rebuilt

---

## 6. Dropping my own framing

> i dont get your framing of capacity approximation and gap

> i dont want the framing at all

I had required every week to declare a capacity, the shortcut buying it, and the
resulting blind spot. Under questioning it didn't hold: it fitted weeks 2–7 and
11, and failed on weeks 1, 8–10 and 12 — a rule that fails a third of its cases
isn't a rule. Removed entirely rather than renamed.

**What it cost:** the two `spec/` tests built on it (a dependency graph, and
no-capacity-without-a-cost) went with it. Those were my invention, not anything
the published spec asks for. Cohesion is now a judgement rather than a check,
which is a real trade.

`785fbb1`

---

## 7. Assessment

> I don't like these assignments - I would like to explore more creative/practical options ... Explore these possibilities on principles rather than getting too concerned with specifics

My first three tasks were *descriptions* of the thesis. The principle that
emerged: this course's subject is only learnable first-person — nobody can be
told what their own model excludes — so assessment should engineer an encounter
with a limit rather than ask for an essay about one. Working principles: vary
the object but fix the obligations; open-endedness needs a commitment device
fixed in advance; failure must be creditable.

Open at time of writing.

---

## 8. Research participation — explored and rejected

> what are some common assignment formats (look at the ANU) for biology, neuroscience, psychology and philosophy

> explore the research participation feasiblity

Pulled real assessment tables off ANU Programs and Courses (PHIL2061, PHIL3075,
PHIL1008, PHIL2057, BIOL3109, BIOL6142, BIOL8700, NEUR8701, NEUR6102, PSYC1003/4).
Useful format vocabulary: annotated bibliography, journal club presentation,
"news and views" short review article, peer review as its own graded item,
research proposal you never run, reading response journal, seen exam, hurdle,
and the Honours Pathway Option — which is branching paths solved
institutionally, with weights redistributed rather than a free-for-all.

ANU's psychology **research participation requirement** (5 hours as an
experimental subject, or read an article and summarise it in lieu) looked
thematically perfect: a course arguing you can't see your own bounds from
inside, assessed by making you the subject.

**It doesn't survive feasibility, and not for the reason I expected.** The
blocker isn't ethics paperwork, it's that ANU can only do this because the
Research School of Psychology runs a continuous research programme with SONA
managing sign-ups. A single niche course has no lab and no stream of approved
studies to fill 150 participant-hours.

Ethics findings worth keeping anyway:

- the alternative task is **mandatory**, not a courtesy (45 CFR 46.116 / OHRP,
  and Canada's TCPS) — ANU's Option 2 exists for that reason
- Walker (2020, *Science and Engineering Ethics*) argues for abolishing
  compulsory pools outright: an alternative task doesn't make a compulsory pool
  voluntary, since the student still faces a forced choice between two unchosen
  options
- so the real risk was looking **dated** — designing a 2027 course around a
  mechanism a live literature calls coercive is exactly the failure this course
  is about

**What replaced it.** Predict-then-measure: commit to predicting your own result
before taking a known instrument, then take it, and the graded object is the
gap — scoreable, no pool, and it connects to Tetlock's calibration work.

**The by-product worth more than the assessment.** Self-administration has a
methodological limit that is itself course content: perceptual effects survive
knowing about them, judgement effects mostly don't. You can know the Adelson
checker-shadow and still see it wrong; you cannot self-administer an anchoring
study. So the blind spots that survive self-knowledge are the structural ones,
which is the category the course actually cares about. Mapping your own retinal
blind spot with a card is mechanism and metaphor in five minutes.

**Structural constraint found:** participation can never be a graded
percentage. ANU treats it as a requirement, not a weighted item, because
"having had an experience" doesn't scale-grade. Participation is a hurdle; the
graded item is derived from it.

No commit to the site yet — assessment scheme still open.

---

## 9. Building the site

> ok yep and get underway with expanding out all content and drafting up the entire course including all lecture decks etc.

Built in four staged commits, checking after each rather than generating
everything and hoping.

Two decisions taken without asking, both flagged as cheap to reverse: the title
**How and Why You're Dumb** and code **SLOP3233** (keeping the allocated 233),
and an **image-free treatment** — the README sanctions it, `socialImage` is
optional in the theme, and I can't produce course-specific artwork. All four
starter images deleted rather than deferred.

Structural decisions worth citing:

- **Lectures Monday, seminars Thursday**, with a division of labour that stops
  the two page types repeating: a lecture page says what the argument is, a
  seminar page says what you do with it. Nothing is explained twice.
- **No per-week template**, per the harness rule. Week 3 is built around a
  replication failure, week 6 ends with the lecturer arguing against their own
  lecture, week 12 adds no mechanism at all.
- **Three staff, one per discipline** the four-lens rule requires, which puts
  the rule in the staffing rather than only in the prose.
- **The position statement is a 0% hurdle folded into the revision entry**,
  because the schema requires a positive weight. It can't be extended past week
  3, since a statement written in week 8 has already been contaminated by the
  thing it is meant to predate.

**Problem found on the way.** The build runs axe over the *slides* as well as
the pages, and an empty table header in the week 3 deck failed it. Worth
knowing: a deck is not exempt from the accessibility check.

**Where the research sweep changed the outline rather than filling it.** The
mantis shrimp carries week 2 because the popular claim inverts the finding.
*Stentor* carries week 3 because a correct result was discarded for ninety years
over a species mismatch with nobody behaving badly — a better failure case than
fraud or statistics. Constantinescu reframed week 5 from space to relational
structure. Olkowicz and Herculano-Houzel dissolve the small-brain puzzle in week
8 rather than marvelling at it.

**State:** 42 pages, 32 API nodes, 22 graph edges, four decks, no accessibility
violations, no broken links, 12/12 spec tests green. `check:evidence` passes on
starter content and imagery; only `PROCESS.md` remains, and that one is mine to
write.

`f065b88` frame · `00d00e6` seminars, lectures, decks · assessments commit
following

---

## 10. The eight missing decks

> why not decks for the rest of the weeks

Fair, and the honest answer is that I stopped at the spec minimum ("at least one
lecture carries a real deck") and then presented it as a design choice. It
wasn't. It was effort.

The rationalisation doesn't survive scrutiny either: **the inconsistency is the
tell.** Four weeks with decks and eight without, with no stated reason, reads as
ran out of time rather than as designed, and a marker reading the site as a
prospective student can't tell those apart. The course is presented as fully
specified for Semester 1 2027, so it should be.

Wrote the remaining eight. Twelve lectures now each carry a deck, 12 decks
compile, 50 pages.

Worth recording as a general lesson rather than a one-off: **a spec minimum is
not a design target.** The published spec says what must be true to pass, not
what a finished thing looks like, and I treated the two as the same.

---

## 11. Figures from data, and week 8 as the depth template

> i dont like the inline svgs i want you to use (properly cited) figures and images from the literature, or use matplotlib or other programming to create actual graphs using sourced data

> yes i want diagrams too, but properly made diagrams using diagram tools ... and lots more examples with imagery (pull images from the internet) ... i won't be publishing the figures from journals as my own, just credit the journals/papers

> each lecture deck needs to be much longer and cover a lot more content in greater depth and detail

Replaced hand-drawn inline SVG with two generators, both committing their
outputs so CI needs neither: **matplotlib** for anything with data or a
computation, and **D2** (a real layout engine, installed via brew) for
structure with no data to plot.

**Two figures are computations rather than depictions.** No Free Lunch is
exhaustive — all 256 target labellings of eight binary points, three learners
with different biases, all averaging exactly 0.500000. Rate-distortion is the
exact closed form for a Gaussian source. And the Dunning-Kruger figure is a
seeded simulation in which Q1 "overrates" itself by 44 percentile points from a
model containing no metacognitive deficit at all.

**A finding I did not expect, from the path integration simulation.** I built it
assuming the point would be that error compounds badly. It doesn't — errors
partly cancel on a wandering path, so the miss stays within a few body lengths.
The integrator is *good*. It is still not good enough, because the target is a
hole: past roughly fifty steps the expected error exceeds the nest entrance. So
the ant's terminal spiral is not a failure of the mechanism, it is the only
available remedy. The figure was reframed around target size rather than error
magnitude, and it makes a better argument than the one I set out to make.

**What I cannot do.** Pull images from the internet. I have no tool that fetches
binary files and could not verify an image if I had the bytes. Saying otherwise
would be inventing a capability. What did emerge is that WebFetch saves binary
responses locally, so I can *read* PDFs — which is how the Chittka & Niven
numbers below were obtained rather than recalled.

**On journal figures.** Crediting them settles plagiarism, which is the half
that gets marked. It does not settle copyright, which is a different thing —
attribution is not a licence. The genuinely reusable subset is CC-BY: Gagliano
2016, Markel 2020, Kohda 2019/2022, de Waal 2019, Galpayage Dona 2022.

**Week 8 rebuilt as the depth template: 52 slides**, from real numbers read out
of Chittka & Niven (2009) rather than paraphrased — the bee's neuron budget
(optic lobes are 64% of it), glomeruli and V1 scaling, skeletal muscle counts
putting a locust inside the mammalian range, the 59-behaviour repertoire against
a million-fold brain mass difference, and the Dujardin/Pandazis mushroom-body
episode where the largest ones turn out to belong to horseshoe crabs.

**Recurring trap, third time now:** an empty leading table header (`| | units |`)
fails axe, and axe runs over decks. Worth a pre-commit grep rather than
discovering it at build time.

---

## 12. The audit, and what the listing pages were still saying

> ok i need you to assess how things are looking and what are possible directions fore imporvement

> can we do another iteration on design and development of the course, lets return to the drawing board and examine whats there and whats not there

> do all of it

Read the site the way a marker does — home, a few non-adjacent weeks, an
assessment, a deck — rather than the way I had been reading it, which was
file by file in the order I wrote them.

**The finding that mattered: four listing pages were still addressing me.**
`/assessments/` said "Weights should sum to 100". `/sessions/` said "Set the
visible singular and plural names once in `src/site-config.ts`". These are
instructions to the person building the site, published as course prose, on
the only route a reader has to reach a week.

What makes this worth recording rather than just fixing: **it is the same gap
I had already identified and written a test for, one level up in the page
tree.** In section 1 I noted that `check:evidence` greps for the
`STARTER_CONTENT` marker, so deleting the comment without replacing the prose
passes the gate, and I wrote an assertion against the course record to close
it. The listing pages carried no marker at all, so neither the gate nor my
test could see them. I had generalised the lesson to exactly one collection
and stopped. The new test is deliberately about the reader rather than about
any one phrase.

**Readings — the gap between what the site promised and what it showed.** The
home page says "you will read primary literature every week"; every assessment
requires reaching a primary source; the `links:` key was used zero times, and
the bibliography lived only in this file, which is explicitly not site content.
Seventy-four sources now sit on the twelve week pages, annotated, with the
paper each seminar turns on named.

**Every DOI was resolved against Crossref rather than recalled.** This is not
diligence for its own sake. A course whose subject is the gap between a claim
and its source cannot ship a fabricated DOI, and roughly a third of my first
search hits were wrong in ways that looked right — reprints in edited
collections for Shannon and Nisbett & Wilson, the *author response* rather than
the article for Markel, the bioRxiv preprint rather than the *Cell* paper for
Whittington. Every one of those would have rendered as a plausible link.

Decided against `links:` frontmatter for the reading lists despite it being the
idiomatic field, because the annotation is the point — which paper the seminar
turns on, and why a particular one is the objection you are expected to arrive
with — and `{label, url}` cannot carry that.

**A test failed honestly and I did not relax it.** The reading test asserts
three resolvable sources per week; weeks 1 and 4 came in at two, because both
lean on books. The available moves were lowering the bar to two or finding the
papers. Ramachandran and Gregory (1991) on perceptual filling-in of induced
scotomas is now week 1's reading and it turns the blind-spot demonstration into
a citable finding; Rescorla's 1988 "it's not what you think it is" is now week
4's. The bar found real thinness rather than being wrong about it.

**The dependency chain was not in the graph.** The API had 22 edges, all
lecture-to-session and assessment-to-session, and not one session-to-session.
The harness rule says a week that could be moved anywhere in the order isn't
carrying its part of the argument, and the one machine-readable structure the
site emits had no record of any week depending on any other. Eighteen edges
now, each one a dependency the week's own prose already carried, and a test
asserting week 12 still reaches back to week 1.

**Two open decisions closed, on the site rather than here.** The title is now
graded on the home page — **[S]**, a reasoned extension stated provocatively,
not a finding — which resolves the tension between a deficiency-sounding title
and a course that rejects the deficiency reading by applying the course's own
method to itself. And artificial systems stay out, with the reason stated: they
are not an independent lineage, having been built by one of the systems under
study out of data produced by it, so they belong in the profile's optional
speculative close as a case the model should *predict*, not as a week of
content.

[`5051fcc`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/commit/5051fcc)

---

## 13. The phone viewport, and the trap that nearly hid it

> ive still got time and budget, what more work can i put in

The assessment page fixes two marking viewports, 1920x1080 and 390x844, and
says both are full marking environments. Nothing on this site had ever been
looked at on a phone.

**Seven figures overflowed at 390px.** Every generated figure added in pass 6 —
on weeks 1, 2, 3, 8, 10 and 12 — rendered at 417px inside a 390px viewport,
making the whole page scroll sideways. Desktop was clean.

**The cause is a theme behaviour I was the first to exercise.** The theme runs
content images full-bleed on purpose: it cancels `max-width`, sets
`width: calc(100% + ...)` and pulls the image outward with negative inline
margins. At 1920 the page gutters absorb that and it looks good. At 390 there
are no gutters to absorb it. The starter shipped images only as hero artwork,
so nothing had put an image in `.at-main` prose until I did. Fixed in
`src/styles/figures.css`, which cancels the full-bleed below 48rem and keeps it
above — the treatment is right where it works.

**The trap, which is the part worth recording.** My first measurement was a
Chrome screenshot at `--window-size=390,844`, and it showed *every* page
clipping text mid-word, home page included. That looks exactly like a
catastrophic site-wide layout bug. It isn't one. Chrome enforces a minimum
window width, so the page had been laid out at a wider viewport and the PNG was
simply cropped to 390. I was one step away from "fixing" a bug that did not
exist, on evidence that looked conclusive.

What distinguished them was measuring instead of looking: an iframe set to a
true 390px, reporting `documentElement.scrollWidth` against `innerWidth`. That
returned 390 for the home page — no overflow — and 399 for the six seminar
pages, each naming the `<img>` responsible. The instrument that looked more
direct was the one that lied.

This is the same failure as *Stentor* in week 3, which is uncomfortable. A
result was produced by an apparatus that wasn't measuring what it appeared to
be measuring, and nothing inside the result said so.

**What I could not do: turn this into a committed check.** I wrote one, twice.
Chrome headless can be driven without any new dependency by reading
measurements back out of `--dump-dom`, and it works for a handful of pages —
that is how the real figures above were obtained. Over forty pages at two
viewports it stalls on its own virtual clock, batching included, and I could not
make it finish reliably. A check that hangs is worse than no check, so there
isn't one in `scripts/`, and deck legibility at both viewports remains a human
job. The honest state is that this pass was verified by hand.

[`5051fcc...HEAD`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/compare/5051fcc...main)

---

## 14. Restyle, and the title that had quietly disappeared

> we can go further with restyle and imrpovement

The platform fixes the Slop identity, so the palette, type scale and spacing
stay as they arrived. What was available was the visual vocabulary this
particular course needs, and the obvious candidate was its own notation.

**The grades were the site's least visible load-bearing element.** [E], [C] and
[S] sit on every substantive claim, the policies page makes students
accountable for the ones they assign, and they rendered as bold text —
indistinguishable from ordinary emphasis. They are now badges, coloured from
the theme's own semantic tokens.

They are *also* differentiated by border style: solid, heavy solid, dashed. A
course whose argument is that no single channel is sufficient should not encode
its own notation in one channel, and the three stay tellable apart in greyscale
or to a colour-blind reader. That is the rare case where the content dictated
the CSS.

**Two defects surfaced, both consequences of a decision made weeks earlier.**

Four pages had no `<h1>` at all: `/evidence/`, `/lectures/`, `/assessments/`
and `/people/`. The cause is two template layers away from the decision that
produced it. `BaseLayout` renders its heading only inside the hero
(`{heroTitle && resolvedHeroImage && ...}`), and the hero only renders when a
hero image resolves. Emptying `src/assets/images/` for the image-free treatment
therefore deleted the page title from every page that relied on `heroTitle`,
silently, with the build green and axe clean throughout. `PageLayout` now takes
over the lead paragraph and renders the title above it, which restores the
title-then-lead order the detail routes already had.

The same decision left `src/pages/404.md` pointing at
`hero-home.avif`, deleted weeks ago and never noticed because a missing hero
image renders as no hero rather than as an error.

This is the third time in this project that a correct-looking green build
concealed something, and the pattern is consistent: **the failures are all in
the gap between a decision and its consequence somewhere I wasn't looking.**
That is, uncomfortably, the thesis of the course.

The spec test I wrote for it — exactly one `<h1>` per page — earned itself
immediately by catching a duplicate on `/policies/`, a page I had not touched,
where the starter's own body heading now collided with the one the layout
supplies.

**A judgement call recorded rather than hidden.** The decks keep the bold-
bracket form, so the site and the decks now differ. Forty-two occurrences
across twelve decks would each add a border and some padding to a slide whose
fit I have no way to verify automatically, and bold already reads well at
projection size. Consistency was worth less than not breaking something I
cannot see.

[`03f9f69`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/commit/03f9f69)

---

## Still open

- `PROCESS.md` — mine, 400-600 words, drawn from this log. Not started.
- Ship: the repo is still private, Pages is off, and every CI run to date is
  `skipped`. The first public push is the first time `check` and `deploy`
  actually execute.
- The SLOP level digit (currently 3; one character to change)
- No automated viewport check. Pages were verified by hand at 1920x1080 and
  390x844; deck slide fit and legibility have still only been eyeballed on
  desktop.

## Closed since

- **Title wording** — kept, and graded **[S]** on the home page. The provocation
  earns its place if the site says what it is, and grading our own title is the
  course's method applied to itself.
- **Whether artificial systems appear** — no, and the home page now says why
  rather than being silent about it.
- **The overclaiming test name.** `spec/assignment-2.test.ts` had a test called
  "gives every assessment a due date inside the teaching period" that only
  checked the date format. Renamed to what it asserts, with a comment pointing
  at `data-integrity.test.ts`, which owns the range claim for every dated node
  rather than for assessments alone.
