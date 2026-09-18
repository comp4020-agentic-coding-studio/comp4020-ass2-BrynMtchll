"""Why certainty-based marking cannot be gamed: the thresholds are derivable.

Gardner-Medwin's scheme, as used in the quizzes:

    declared certainty     correct     wrong
    low                       +1          0
    mid                       +2         -2
    high                      +3         -6

If your true probability of being correct is p, expected score is linear in p:

    E[low]  = 1p + 0(1-p) =     p
    E[mid]  = 2p - 2(1-p) = 4p - 2
    E[high] = 3p - 6(1-p) = 9p - 6

The best declaration is whichever line is highest at your actual p, and the
crossings are exactly where the advice changes:

    low = mid   ->  p = 4p - 2   ->  p = 2/3  ~ 0.667
    mid = high  ->  4p - 2 = 9p - 6  ->  p = 4/5 = 0.800

Those are the published 67% and 80% thresholds, recovered from the payoff table
in two lines of algebra. Because the maximum is attained by declaring your
genuine p, no misreport does better: the rule is proper.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

p = np.linspace(0, 1, 400)
low, mid, high = p, 4 * p - 2, 9 * p - 6

fig, ax = plt.subplots(figsize=(7.8, 4.3))
ax.plot(p, low, color=ds.MUTED, lw=2.6, label="declare low   ($p$)")
ax.plot(p, mid, color=ds.FG, lw=2.6, label="declare mid   ($4p-2$)")
ax.plot(p, high, color=ds.ACCENT, lw=2.6, label="declare high  ($9p-6$)")

best = np.maximum.reduce([low, mid, high])
ax.plot(p, best, color=ds.ACCENT, lw=6, alpha=0.18)

for x, lab in [(2 / 3, "2/3"), (0.8, "4/5")]:
    ax.axvline(x, color=ds.WARN, lw=1.5, ls="--")
    ax.plot([x], [x if x < 0.7 else 4 * x - 2], marker="o", ms=8, color=ds.WARN)
    ax.text(x, -2.55, lab, color=ds.WARN, ha="center", fontsize=12)

ax.axhline(0, color=ds.MUTED, lw=1)
ax.set_xlabel("your true probability of being correct, $p$")
ax.set_ylabel("expected score")
ax.set_xlim(0, 1)
ax.set_ylim(-2.8, 3.2)
ax.legend(loc="upper left", fontsize=10)
ax.set_title("the upper envelope is the honest declaration", loc="left")
print(f"  crossings at p = {2/3:.4f} and {0.8:.4f}")
ds.save(fig, "cbm-proper-rule")
