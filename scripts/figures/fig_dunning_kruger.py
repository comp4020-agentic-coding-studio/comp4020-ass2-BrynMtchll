"""The Dunning-Kruger curve, reconstructed from noise.

Krueger & Mueller (2002, JPSP 82(2), 180-188) argued that the familiar chart
does not require a metacognitive deficit: regression to the mean, plus a
better-than-average effect, reproduces it. This script does exactly that and
nothing else.

Generative model, stated in full so the figure can be audited:

    true skill      ~ N(0, 1), reported as a percentile
    self-estimate    = r * true + sqrt(1 - r^2) * noise,  noise ~ N(0, 1)
    then shifted so the mean self-estimate sits at the BTA percentile

No term in that model knows anything about competence-to-judge. Nobody in the
simulation is unaware of anything. Binning by true-skill quartile and plotting
group means produces the crossing lines anyway.

This is a simulation, not their data, and the deck caption says so.
"""

import numpy as np
from scipy_free import percentile_of  # local helper, no scipy dependency

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270222)  # seeded: the figure is reproducible
N = 2000
R = 0.30  # modest correlation between ability and self-assessment
BTA = 66.0  # mean self-estimate, in percentile points

true = RNG.normal(size=N)
noise = RNG.normal(size=N)
est = R * true + np.sqrt(1 - R**2) * noise

true_pct = percentile_of(true)
est_pct = percentile_of(est)
est_pct = np.clip(est_pct - est_pct.mean() + BTA, 0, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 4.0))
fig.set_dpi(150)  # rasterised scatter only

ax1.scatter(true_pct, est_pct, s=7, color=ds.MUTED, alpha=0.45, linewidths=0,
            rasterized=True)
ax1.plot([0, 100], [0, 100], color=ds.FG, lw=1.2, ls="--", alpha=0.6)
ax1.text(6, 92, "perfect self-knowledge", color=ds.FG, fontsize=10, alpha=0.75)
ax1.set_xlabel("actual percentile")
ax1.set_ylabel("self-estimated percentile")
ax1.set_title(f"1 · noisy estimates  (r = {R}, mean = {BTA:.0f}th)", loc="left")
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)

q = np.clip((true_pct // 25).astype(int), 0, 3)
xs = np.arange(4)
actual_means = [true_pct[q == i].mean() for i in xs]
est_means = [est_pct[q == i].mean() for i in xs]

ax2.plot(xs, actual_means, color=ds.FG, lw=2.6, marker="o", label="actual")
ax2.plot(xs, est_means, color=ds.ACCENT, lw=2.6, marker="o", label="self-estimate")
ax2.set_xticks(xs, ["Q1", "Q2", "Q3", "Q4"])
ax2.set_xlabel("actual performance quartile")
ax2.set_ylabel("percentile")
ax2.set_title("2 · the same points, averaged by quartile", loc="left")
ax2.set_ylim(0, 100)
ax2.legend(loc="lower right")

gap = est_means[0] - actual_means[0]
ax2.annotate(
    f"bottom quartile\n'overrates' itself\nby {gap:.0f} points",
    xy=(0, (est_means[0] + actual_means[0]) / 2),
    xytext=(0.55, 14),
    color=ds.WARN,
    fontsize=11,
    arrowprops=dict(arrowstyle="->", color=ds.WARN, lw=1.4),
)

ds.save(fig, "dunning-kruger-artefact")
print(f"  Q1 actual {actual_means[0]:.1f} vs estimate {est_means[0]:.1f}")
print(f"  Q4 actual {actual_means[3]:.1f} vs estimate {est_means[3]:.1f}")
