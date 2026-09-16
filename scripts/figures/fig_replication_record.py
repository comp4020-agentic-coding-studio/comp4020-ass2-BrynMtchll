"""The replication record that week 11 has to be read against.

Open Science Collaboration (2015), "Estimating the reproducibility of
psychological science", Science 349(6251), aac4716. One hundred replications of
studies from three high-profile journals, conducted with the original authors'
input on protocols.

    97 of 100 original studies reported a statistically significant result
    36 of 100 replications reached statistical significance
    replication effect sizes averaged roughly half the originals

Plus the two specific collapses this week deals with:

    ego depletion -- Hagger et al. (2016), Perspectives on Psychological
    Science 11(4), 546-573. Registered Replication Report, 23 laboratories,
    N = 2,141. No effect.

    Carter et al. (2015), J. Exp. Psychol. General 144, 796-815, had already
    challenged the resource account meta-analytically.
"""

import numpy as np

import sys
sys.path.insert(0, "scripts/figures")
import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 3.8),
                               gridspec_kw={"width_ratios": [1, 1]})

ax1.barh(["original studies", "replications"], [97, 36],
         color=[ds.MUTED, ds.WARN], height=0.55)
for y, v in enumerate([97, 36]):
    ax1.text(v + 2, y, f"{v}/100", va="center", color=ds.FG, fontsize=13)
ax1.invert_yaxis()
ax1.set_xlim(0, 112)
ax1.set_xlabel("reported a statistically significant result")
ax1.set_title("Open Science Collaboration, 2015", loc="left")

labs = np.arange(1, 24)
RNG = np.random.default_rng(20270506)
eff = RNG.normal(0.0, 0.16, len(labs))  # null-centred, as reported
ax2.errorbar(eff, labs, xerr=0.30, fmt="o", color=ds.MUTED,
             ecolor=ds.MUTED, elinewidth=1, capsize=0, ms=4, alpha=0.75)
ax2.axvline(0, color=ds.FG, lw=1.6)
ax2.plot([eff.mean()], [12], marker="D", ms=11, color=ds.WARN)
ax2.errorbar([eff.mean()], [12], xerr=0.07, color=ds.WARN, elinewidth=3, capsize=0)
ax2.text(0.42, 12, "pooled\nestimate", color=ds.WARN, fontsize=11, va="center")
ax2.set_yticks([])
ax2.set_xlim(-0.75, 0.95)
ax2.set_xlabel("effect size")
ax2.set_title("ego depletion: 23 labs, N = 2,141", loc="left")
ax2.text(-0.72, 23.5, "individual lab estimates are illustrative;\nthe pooled null is the reported finding",
         color=ds.MUTED, fontsize=9.5, va="top")

ds.save(fig, "replication-record")
