# COMP4020 — Slop University course site (A2)

This repo is a **course website for Slop University**, built on a fixed Astro
platform. The **deployed site is what gets marked** — not this repo, and not "it
works on my machine". It's read live in Chrome at 1920×1080 and 390×844, both in
full, for about ten minutes: home page, a few non-adjacent weeks, an assessment,
the deck, the policies page.

The platform is fixed and documented in `README.md` — Slop branding, the four
content collections, the build pipeline, the generated API. **There is no stack
choice in this repo.** Read `README.md` for the platform; this file is only the
rules I hold the agent to and the things it keeps getting wrong.

The brief and spec are on the
[course website](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/assessments/assignment-2/).
Read both before planning or building.

## My rules

- Be terse, skip long explanations unless asked
- Flag trade-offs briefly rather than writing essays
- Tell me directly if a request conflicts with an earlier constraint
- Don't ask for permissions for standard commands and testing
- When asked to come up with ideas, think deeply and explore a wide array of
  inspirations in order to come up with novel and interesting ideas
- **Content is the deliverable here, not just the code.** Twelve weeks that
  repeat one another fails the brief however green the checks are. Never
  generate a week's content by pattern-filling the week before it.
- **No AI slop prose.** One voice, held all semester. If a paragraph could sit
  in any course on any topic, it's wrong. Read it back before accepting it.

## How to work in here

- Keep the dev server running (`pnpm dev`) so you see changes as you make them.
  It serves under the base path — `http://localhost:4321/comp4020-ass2-BrynMtchll/`.
  The bare `http://localhost:4321` Astro prints is a 404; don't report that as
  a broken build.
- Before you push, run `pnpm check` (typecheck → build → spec). CI runs the same
  thing plus the secret scan and the deploy, and CI is skipped entirely while
  the repo is private — so local `pnpm check` is the only feedback loop until
  ship day, and it's the faster one anyway.
- To see what the page actually looks like rather than what you assume it looks
  like, open it in a browser (the `agent-browser` CLI, documented on
  [the course site](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/topics/backpressure/#agent-browser-the-rendered-page-as-ground-truth)).
  The rendered page is the truth; your mental model of it isn't. This matters
  more here than on a one-page prototype: twenty-odd pages means the one you
  broke is rarely the one you're looking at.
- When a check fails, read its output before changing anything. The failure
  message is the instruction: it names the file, the line, or the contract.
  Treat a red check as authoritative — the page is wrong until the check is
  green, not until you decide it should be.
- Commit when the checks pass. Never commit a red state.

## The checks (my sensors)

`pnpm check` = `astro check` (types) → `pnpm build` → `vitest run spec`. An early
failure stops the rest, so a broken build hides every spec result behind it.

- **build is itself several checks.** `pnpm build` runs axe over every rendered
  page, verifies internal links respect the base path, **fails on a dangling
  content ref**, compiles every deck, and emits the versioned API. A green build
  is a much stronger signal here than on the earlier prototypes — treat a build
  failure as the first thing to fix, always.
- **spec** — `spec/data-integrity.test.ts` ships with the platform and checks the
  one cross-page fact the build can't: dated material stays inside the teaching
  period. My own contract tests live alongside it (any `spec/*.test.ts`).
- **evidence** (`pnpm check:evidence`) — the submission gate. Citations in
  `PROCESS.md` must resolve to real commits; **every `STARTER_CONTENT` marker
  must be gone**; starter imagery must be replaced. See below.
- **secrets** — CI runs trufflehog twice (verified secrets, then the course-key
  shape). The local pre-commit hook in `.githooks/` is the one that matters —
  by the time CI sees a key it's already pushed.
- **deploy** — deliberately *not* gated on `check`. A red spec test of mine is a
  finding about my course, not a reason to take the live site down. But the
  deploy runs its own `pnpm build`, so a site that can't build still can't ship.

Nothing here measures **performance**, and axe is not the whole of
accessibility — it catches machine-checkable violations, not whether the site is
usable. Neither is a mark; both are mine to wire up if I want them.

## Platform traps (the rest is in README.md)

- **Never hardcode `base`.** It's derived at config time from
  `GITHUB_REPOSITORY` or the git origin, in `scripts/pages-base.ts`. This is a
  change from every earlier repo in this course, where `base` was set by hand in
  `astro.config.mjs` — do not port that pattern in.
- **A root-absolute link in an `.astro` file skips Astro's base handling.**
  `href="/sessions/"` works on localhost and 404s live. Markdown links and theme
  components are rewritten automatically; the build's link checker catches the
  rest.
- **The collection key is the whole address.** `sessions/getting-started` is the
  file, the page, the API endpoint and the ref other pages link by. Renaming one
  means renaming all four.
- **`related:` is bidirectional** — declare it on whichever side is convenient,
  it renders on both. A ref that doesn't resolve fails the build.
- **`src/course-config.ts` is the single source for the course record.** Don't
  restate its facts in page content; they'll drift. Keep the last three digits
  of the SLOP code — they're allocated to this repo.
- **`published: false` hides an entry from production but keeps it in `pnpm dev`.**
  So "it's on the dev server" is not evidence it ships.
- Commit `pnpm-lock.yaml`: CI installs with `--frozen-lockfile`.

## What I've learned (carried forward)

- **A green test suite is not evidence the artefact works.** Tests hold
  contracts. Whether a human can actually use the thing is found by using it,
  and only by using it. On a course site that means reading it as a prospective
  student would, at both viewports.
- **Instrument, don't squint at screenshots.** A dev-only probe reporting real
  values beats "does that look right?" every time.
- **A probe must report page coordinates, not component-relative ones.** Off-by-a-header
  is the classic, and it only surfaces once targets get small.
- **`agent-browser console` returns accumulated history across page loads.** A
  warning from deleted code still reads as current. Restart the dev server and
  clear `node_modules/.vite` before believing it.
- **A probe cannot see what a person cannot see.** Scripted checks aim at
  coordinates, so they never notice that a human has no way to tell what they're
  about to click. Instrumentation proves the mechanism works, not that anyone
  can reach it.
- **Sizes belong in relative units, not pixels.** Anything written as a pixel
  constant looks right at one marking viewport and wrong at the other.
- **`every()` on an empty array is `true`.** Guard the empty case before reading
  a verdict off a fold.
- **When a spec test greps built output, don't quote-match narrowly.** The
  production minifier rewrites string literals as template literals, so a
  `["']` character class reads a working page as broken.

## Process is part of the mark

Process is the **largest criterion (45%)**. The checks can't see any of it; a
person reads it directly.

- **Commit as you go.** Small, frequent commits are the record. A trail that grew
  alongside the work is the strongest evidence; a dump the night before is the
  weakest.
- **`PROCESS.md` runs 400–600 words**, written by me, as one narrative — not a
  run of fixes with a hash apiece. Its spine for A2: what I decided a good
  university course looks like, which of those decisions I encoded in the harness
  (a rule here, or a check in `spec/`), and which I deliberately left out. Cite
  commits as you go; an uncited claim isn't evidence, and `check:evidence` fails
  a `PROCESS.md` with no citations.
- **There is no reflection file for this assignment.** `reflections/` stays empty
  — `check:evidence` expects none for an assignment repo, and warns on any file
  that isn't `crit-N.md`. The week 7 retro presents from `PROCESS.md`.
- **`spec/` is read as process evidence**, not just backpressure: my checks are
  the record of what I decided had to stay true about my course.
- **This file is process evidence too.** Keep it honest and current.

## This file is yours

Carried forward from `comp4020-crit5-BrynMtchll`, merged with
`comp4020-ass1-BrynMtchll`, and corrected against this repo's actual platform.
Rules about Three.js and simulation timing were dropped as dead; the `base`
hardcoding rule was **inverted**, because this platform derives it.

As I learn what this site needs — a convention to hold the agent to, a sensor
that keeps catching me out, a fact the agent keeps getting wrong — it goes here.
