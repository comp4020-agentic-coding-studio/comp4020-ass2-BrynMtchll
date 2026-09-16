"""Ashby's law of requisite variety, as the inequality it actually is.

Ashby (1956), An Introduction to Cybernetics, ch. 11. In information-theoretic
form the law states a floor on the variety a regulator cannot remove:

    H(outcome) >= H(disturbance) - H(regulator)

So residual variety falls one-for-one with regulator variety and no faster, and
it cannot go below zero. A regulator with fewer distinguishable responses than
the world has distinguishable disturbances leaves the remainder standing --
however cleverly it is organised.

This plots the bound for several disturbance varieties, in bits. It is a
computed inequality, not a schematic: the kink at H_r = H_d is where the
regulator first has enough repertoire to absorb everything, and the slope is
exactly -1 by construction.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.4, 4.2))

h_r = np.linspace(0, 10, 400)
for h_d, colour, style in [(8.0, ds.ACCENT, "-"), (5.0, ds.FG, "-"), (3.0, ds.MUTED, "-")]:
    residual = np.maximum(h_d - h_r, 0.0)
    ax.plot(h_r, residual, color=colour, lw=2.6, ls=style,
            label=f"disturbance variety = {h_d:.0f} bits")
    ax.plot([h_d], [0], marker="o", color=colour, ms=7)

ax.axvspan(0, 3, color=ds.WARN, alpha=0.08)
ax.text(1.5, 7.4, "under-matched\nregulator", color=ds.WARN, fontsize=11, ha="center")
ax.annotate("slope is exactly −1:\none bit of repertoire\nremoves one bit of variety",
            xy=(3.0, 5.0), xytext=(4.6, 6.4), color=ds.FG, fontsize=10,
            arrowprops=dict(arrowstyle="->", color=ds.MUTED, lw=1.3))

ax.set_xlabel("regulator variety, $H_r$  (bits)")
ax.set_ylabel("variety it cannot remove  (bits)")
ax.set_xlim(0, 10)
ax.set_ylim(0, 8.6)
ax.legend(loc="upper right", fontsize=10)
ds.save(fig, "requisite-variety")
