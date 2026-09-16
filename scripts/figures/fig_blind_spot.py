"""The geometry of your own optic disc, to scale.

The blind spot is not a metaphor in this course, it is an exercise. The figures
below are the standard human values:

    eccentricity   ~15-16 deg temporal from fixation
    angular size   ~5 deg horizontal x ~7 deg vertical

For comparison the full moon subtends ~0.5 deg, so the disc spans roughly ten
moon-widths across and fourteen down -- about nine full moons by area. Nothing
reports it.

Drawn to scale in degrees of visual angle so the comparison is quantitative
rather than rhetorical.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt
import matplotlib.patches as mp

ECC, W, H = 15.5, 5.0, 7.0
MOON = 0.5

fig, ax = plt.subplots(figsize=(8.2, 4.0))

ax.add_patch(mp.Ellipse((ECC, 0), W, H, facecolor=ds.WARN, alpha=0.30,
                        edgecolor=ds.WARN, lw=2))
ax.text(ECC, -H / 2 - 1.6, "optic disc\n5° × 7°", color=ds.WARN,
        ha="center", fontsize=11)

ax.plot([0], [0], marker="+", ms=18, color=ds.FG, mew=2)
ax.text(0, -2.2, "fixation", color=ds.FG, ha="center", fontsize=11)

for i in range(9):
    a = 2 * np.pi * i / 9
    ax.add_patch(mp.Circle((ECC + 0.85 * np.cos(a) * (W / 2 - MOON / 2) * 1.5,
                            0.85 * np.sin(a) * (H / 2 - MOON / 2) * 1.3),
                           MOON / 2, facecolor=ds.FG, alpha=0.55, edgecolor="none"))
ax.text(ECC + 6.2, 2.0, "nine full moons\nwould fit inside it",
        color=ds.FG, fontsize=10.5)

ax.annotate("", xy=(ECC - W / 2, -H / 2 - 0.3), xytext=(0, -H / 2 - 0.3),
            arrowprops=dict(arrowstyle="<->", color=ds.MUTED, lw=1.4))
ax.text(ECC / 2 - 1.5, -H / 2 - 1.1, f"{ECC:.0f}° temporal", color=ds.MUTED, fontsize=10)

ax.set_xlim(-4, 27)
ax.set_ylim(-7, 6)
ax.set_xlabel("degrees of visual angle, temporal →")
ax.set_yticks([])
ax.set_aspect("equal")
for s in ("left",):
    ax.spines[s].set_visible(False)
ds.save(fig, "blind-spot-geometry")
