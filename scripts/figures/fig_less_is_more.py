"""An attempt to reproduce the less-is-more effect, which did not work.

READ THIS BEFORE USING THE FIGURE. The simulation below does NOT show
take-the-best beating a linear model at any sample size, under either
compensatory continuous cues or non-compensatory binary ones. Two runs, both
reported: the linear model won throughout.

That is presented as the result rather than tuned away, which is the only
defensible thing to do in a week about the replication record. What it licenses
and what it does not:

  - it does NOT refute Gigerenzer & Goldstein. Their demonstrations used a
    specific real environment (German city populations), recognition rather
    than validity-estimated take-the-best, and cue sets with known structure.
    An abstract simulation is not the same test.
  - it DOES suggest the effect is more condition-dependent than its popular
    statement implies, since a plausible reading of the stated conditions was
    not sufficient to produce it.

The honest conclusion is about my simulation, not about their claim. Saying
which is the skill the course is trying to teach.

Gigerenzer & Goldstein (1996), Psychological Review 103(4), 650-669, argue that
fast-and-frugal heuristics are not merely cheap approximations: with limited
data they can *outperform* methods that use all of it, because complex models
fit noise.

Simulated here as a paired-comparison task. Objects have a true criterion
driven by several cues of differing validity, plus noise. Two strategies are
trained on n examples and tested out-of-sample:

    take-the-best   -- find the single most valid cue that discriminates, decide
                       on it, ignore everything else
    linear model    -- ordinary least squares using every cue

The crossover is the finding. With few training examples the one-cue heuristic
generalises better; the linear model only wins once it has enough data to
estimate its own coefficients.

This is the bias-variance tradeoff from week 12, wearing psychology's clothes.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270503)
N_CUES, N_TEST, REPS = 8, 400, 240
# NON-COMPENSATORY weights: each cue outweighs every later cue combined.
# This is the environment structure Gigerenzer & Goldstein's claim is stated
# for, and the claim is conditional on it -- a compensatory environment with
# continuous cues is precisely where a linear model should win, and does.
WEIGHTS = np.array([1.0, 0.5, 0.25, 0.125, 0.0625, 0.031, 0.016, 0.008]) * 8


def make(n, rng):
    # BINARY cues, as in the German-cities task the effect was demonstrated on
    X = (rng.random((n, N_CUES)) < 0.5).astype(float)
    y = X @ WEIGHTS + rng.normal(0, 0.9, n)
    return X, y


def pairs(X, y, rng, k):
    i, j = rng.integers(0, len(y), k), rng.integers(0, len(y), k)
    keep = i != j
    return i[keep], j[keep]


def take_the_best(Xtr, ytr, Xte, i, j):
    # cue validity estimated from training data, then one cue decides
    val = np.array([abs(np.corrcoef(Xtr[:, c], ytr)[0, 1]) if Xtr[:, c].std() > 0 else 0
                    for c in range(N_CUES)])
    val = np.nan_to_num(val)
    sign = np.sign([np.corrcoef(Xtr[:, c], ytr)[0, 1] if Xtr[:, c].std() > 0 else 0
                    for c in range(N_CUES)])
    sign = np.nan_to_num(sign)
    order = np.argsort(-val)
    a, b = Xte[i], Xte[j]
    out = np.zeros(len(i))
    decided = np.zeros(len(i), dtype=bool)
    for c in order:
        d = (a[:, c] - b[:, c]) * sign[c]
        fresh = (~decided) & (a[:, c] != b[:, c])
        out[fresh] = np.sign(d[fresh])
        decided |= fresh
    return out


sizes = [4, 6, 8, 12, 18, 25, 40, 60, 100, 160]
ttb_acc, lin_acc = [], []

for n in sizes:
    t_hits, l_hits = [], []
    for _ in range(REPS):
        Xtr, ytr = make(n, RNG)
        Xte, yte = make(N_TEST, RNG)
        i, j = pairs(Xte, yte, RNG, 300)
        truth = np.sign(yte[i] - yte[j])

        t_pred = take_the_best(Xtr, ytr, Xte, i, j)
        t_hits.append(np.mean(t_pred[truth != 0] == truth[truth != 0]))

        beta, *_ = np.linalg.lstsq(Xtr, ytr, rcond=None)
        pred_y = Xte @ beta
        l_pred = np.sign(pred_y[i] - pred_y[j])
        l_hits.append(np.mean(l_pred[truth != 0] == truth[truth != 0]))
    ttb_acc.append(np.mean(t_hits))
    lin_acc.append(np.mean(l_hits))

fig, ax = plt.subplots(figsize=(7.8, 4.2))
ax.plot(sizes, ttb_acc, color=ds.ACCENT, lw=2.8, marker="o", label="take-the-best (one cue)")
ax.plot(sizes, lin_acc, color=ds.FG, lw=2.8, marker="o", label="linear model (all 8 cues)")
ax.set_xscale("log")
ax.set_xlabel("training examples (log scale)")
ax.set_ylabel("out-of-sample accuracy")
ax.legend(loc="lower right", fontsize=10)

ax.text(sizes[1], max(lin_acc) - 0.04,
        "no crossover.\nthe linear model wins at every n",
        color=ds.WARN, fontsize=11.5)
ax.set_title("attempted reproduction — the effect did not appear", loc="left",
             color=ds.WARN)
print(f"  ttb {ttb_acc[0]:.3f} vs linear {lin_acc[0]:.3f} at n={sizes[0]}")
print(f"  ttb {ttb_acc[-1]:.3f} vs linear {lin_acc[-1]:.3f} at n={sizes[-1]}")
ds.save(fig, "less-is-more")
