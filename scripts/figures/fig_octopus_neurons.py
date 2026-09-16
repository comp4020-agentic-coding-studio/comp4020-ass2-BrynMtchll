"""Where an octopus keeps its nervous system.

Roughly 500 million neurons in Octopus vulgaris, of which about two thirds sit
in the arms rather than the central brain -- each arm carrying a large axial
nerve cord capable of generating and completing motor programmes with the arm
severed from central control (Hochner, Current Biology 22(20), R887-R892, 2012;
Godfrey-Smith, Other Minds, 2016).

Human figures for comparison: ~86 billion neurons total, of which the enteric
nervous system -- the largest peripheral concentration -- is on the order of
half a billion. The asymmetry is the point rather than the totals.
"""
import numpy as np
import deckstyle as ds
ds.use()
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 3.8))

ax1.barh(["arms\n(8 axial nerve cords)", "central brain"], [2 / 3, 1 / 3],
         color=[ds.ACCENT, ds.MUTED], height=0.5)
ax1.text(2 / 3 + 0.02, 0, "~2/3", va="center", color=ds.FG, fontsize=14)
ax1.text(1 / 3 + 0.02, 1, "~1/3", va="center", color=ds.FG, fontsize=14)
ax1.set_xlim(0, 0.88)
ax1.invert_yaxis()
ax1.set_xlabel("share of ~500 million neurons")
ax1.set_title("Octopus vulgaris", loc="left")

ax2.barh(["periphery\n(mostly enteric)", "central nervous system"], [0.006, 0.994],
         color=[ds.ACCENT, ds.MUTED], height=0.5)
ax2.text(0.02, 0, "<1%", va="center", color=ds.FG, fontsize=14)
ax2.text(0.55, 1, ">99%", va="center", color=ds.FG, fontsize=14)
ax2.set_xlim(0, 1.15)
ax2.invert_yaxis()
ax2.set_xlabel("share of ~86 billion neurons")
ax2.set_title("Human, for contrast", loc="left")
ds.save(fig, "octopus-neurons")
