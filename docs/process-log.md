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

## Still open

- Title wording, and the risk the blunt title licenses the deficiency reading
- Week 1 adds only framing — merge into week 2?
- Whether artificial systems appear at all
- Assessment scheme, per §7
- `spec/assignment-2.test.ts` has a test named for the teaching period that only
  checks date format. The range is covered by the shipped
  `data-integrity.test.ts`, but the name overclaims.
