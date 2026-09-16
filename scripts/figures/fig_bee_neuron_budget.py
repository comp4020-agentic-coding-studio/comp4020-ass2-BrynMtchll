"""Where a honeybee's neurons actually go.

All counts from Chittka, L. & Niven, J. (2009), "Are Bigger Brains Better?",
Current Biology 19(21), R995-R1008, Figure 1 caption (cell counts therein
attributed to their ref. 8):

    optic lobes      lamina, medulla and lobula, ~216,000 cells EACH
    mushroom bodies  ~170,000 cells each, two of them
    protocerebrum    ~19,000 remaining neurons
    antennal lobes   ~4,500 neurons in ~160 glomeruli
    deutocerebrum    ~2,500 motor neurons

The bee brain is ~1 mm^3 and holds fewer than a million neurons, and the
striking thing once you add these up is the proportion: roughly two-thirds of
the budget is spent before any integration happens at all.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

parts = [
    ("optic lobes\n(3 × 216,000)", 3 * 216_000, ds.ACCENT),
    ("mushroom bodies\n(2 × 170,000)", 2 * 170_000, ds.FG),
    ("protocerebrum", 19_000, ds.MUTED),
    ("antennal lobes", 4_500, ds.MUTED),
    ("motor neurons", 2_500, ds.WARN),
]
total = sum(v for _, v, _ in parts)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 3.9),
                               gridspec_kw={"width_ratios": [1.25, 1]})

left = 0.0
for label, v, c in parts:
    ax1.barh([0], [v], left=left, color=c, height=0.5,
             edgecolor="none" if c != ds.FG else ds.MUTED)
    left += v
ax1.set_xlim(0, total)
ax1.set_yticks([])
ax1.set_xlabel(f"neurons  (total ≈ {total:,})")
ax1.set_title("one honeybee brain, ~1 mm³", loc="left")
for spine in ("left", "bottom"):
    ax1.spines[spine].set_visible(spine == "bottom")

names = [p[0] for p in parts]
vals = [p[1] for p in parts]
cols = [p[2] for p in parts]
ax2.barh(range(len(parts)), vals, color=cols, height=0.62)
ax2.set_yticks(range(len(parts)), names, fontsize=10)
ax2.invert_yaxis()
ax2.set_xscale("log")
ax2.set_xlabel("neurons (log scale)")
for i, v in enumerate(vals):
    ax2.text(v * 1.25, i, f"{v:,}", va="center", fontsize=10, color=ds.FG)
ax2.set_xlim(1e3, 3e6)

share = 3 * 216_000 / total * 100
print(f"  optic lobes are {share:.0f}% of the budget")
ds.save(fig, "bee-neuron-budget")
