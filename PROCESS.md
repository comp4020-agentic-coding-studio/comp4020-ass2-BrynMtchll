# Process overview

## What I built

**SLOP3233 — *How and Why You're Dumb***: a twelve-week course arguing that
intelligence is lossy compression of a world too large to represent, and that
every compression has a shape you cannot see from inside it. Twelve seminars,
twelve lectures, twelve decks, four assessments. The curricular judgement is
mine. Most of the words were written by an agent working to rules I wrote
first, which is the part worth accounting for.

## How I got here

I settled three things about what a good course is before drafting any of it.
Coherence has to come from one model rather than from coverage — if a week could
be moved anywhere in the order without loss, it isn't carrying its part of the
argument. A subject this full of failed replications has to grade its own
evidence out loud. And no single discipline settles a question about
intelligence, so four have to be pooled rather than surveyed.

Then I wrote those into the harness instead of applying them by hand:

> Write into claude.md that i want to focus on maticulousness and precision
> [...] Prioritise (and add to claude.md) the necessity of pooling from
> philosophical, neuroscientific, evolutionary and psychological angles on
> intelligence.

That is [`6aeb3e4`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/commit/6aeb3e4).
The obvious alternative was to hold the standard in my head and correct the
output when it drifted. Rules scale and corrections don't: across twelve weeks
and twelve decks I'd have re-derived the same judgement dozens of times.

The rule immediately created a problem of my own making. Four lenses per week,
run in the same order, produces twelve pages with one shape, and a template is
the failure this brief names explicitly. I could have dropped the rule or
enforced it weekly. Instead I recorded the distinction: the lenses are a
checklist for the argument, not a shape for the page, and each week leads with
whichever one carries the weight. Hence week 3 leading on a ninety-year
replication failure and week 9 on whether a famous question is malformed.

The intervention that mattered most was aimed at my own inputs rather than at
the output. Having asked for voice rules derived from my writing, I stopped it:

> wait exclude comp3320 reoprt

That report was itself heavily agent-written, and four rules derived from it had
come out backwards — including an em-dash ban and a spelling rule my actual
writing doesn't follow
([`a60b742...7169948`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/compare/a60b742...7169948)).
Reviewing output would never have caught this: the output was faithfully obeying
rules that were wrong. I checked the rewrite against the three source documents
rather than against how the prose felt.

What went into `spec/` is what had to stay true and could be checked: that every
week after the first declares a dependency on an earlier one, so the chain the
course claims is a thing the build tests rather than a sentence in `CLAUDE.md`;
that no public page addresses the builder instead of the reader; that each week
carries at least three resolvable sources, which failed honestly and got
satisfied rather than lowered
([`5051fcc`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/commit/5051fcc)).

The rules I trust least are the ones that have never fired. A `max-height` in the
deck stylesheet, commented as the important one, had quietly stopped matching
anything when the figures moved from inline SVG to generated images — five slides
were clipping their own concluding line behind a green build. So I negative-tested
the sensor I wrote for it before believing it
([`5b47230`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-BrynMtchll/commit/5b47230)).

What I deliberately left out of the harness: whether the course is genuinely
niche, whether twelve weeks cohere into one idea, and whether the prose has a
voice. Those belong to the crit. A test asserting them would only have measured
my ability to write the test.
