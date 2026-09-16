"""A million-fold difference in brain mass buys two to three times the
behavioural repertoire.

Repertoire counts from Chittka & Niven (2009), Current Biology 19(21),
R995-R1008, drawing on Changizi's compilation (their ref. 48) plus their own
literature survey for the honeybee:

    honeybee            59   (their Box 1, enumerated)
    North American moose 22
    De Brazza's monkey  44
    bottlenose dolphin  123
    typical range across several dozen species: 15-42

Brain masses are order-of-magnitude values for the comparison only, so the
x-axis is labelled as such. The point is the y-axis: the range is narrow.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

pts = [
    ("honeybee", 1e-6, 59, ds.ACCENT),
    ("moose", 0.5, 22, ds.MUTED),
    ("De Brazza's monkey", 0.08, 44, ds.MUTED),
    ("bottlenose dolphin", 1.6, 123, ds.MUTED),
]

fig, ax = plt.subplots(figsize=(7.6, 4.0))
ax.axhspan(15, 42, color=ds.MUTED, alpha=0.14)
ax.text(2e-6, 28, "typical range across\nseveral dozen species", fontsize=10,
        color=ds.MUTED, va="center")

for name, mass, rep, c in pts:
    ax.scatter([mass], [rep], s=120, color=c, zorder=3, linewidths=0)
    ax.annotate(f"{name}\n{rep} behaviours", (mass, rep),
                textcoords="offset points", xytext=(12, 8),
                fontsize=11, color=ds.FG if c == ds.MUTED else ds.ACCENT)

ax.set_xscale("log")
ax.set_xlim(2e-7, 2e1)
ax.set_ylim(0, 150)
ax.set_xlabel("brain mass, kg  (order of magnitude)")
ax.set_ylabel("distinct behaviour types")
ax.annotate("", xy=(1.6, 8), xytext=(1e-6, 8),
            arrowprops=dict(arrowstyle="<->", color=ds.WARN, lw=1.6))
ax.text(1e-3, 14, "~10⁶× brain mass", color=ds.WARN, ha="center", fontsize=11)
ds.save(fig, "repertoire-vs-brain")
