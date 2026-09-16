"""Choice blindness: predicted detection against measured detection.

Johansson, Hall, Sikstrom & Olsson (2005), "Failure to Detect Mismatches
Between Intention and Outcome in a Simple Decision Task", Science 310(5745),
116-119. doi:10.1126/science.1111709

Values as reported in that paper:
  - fewer than 1 in 10 manipulations were easily spotted  -> 10 (upper bound)
  - no more than 20% of manipulations were exposed by the end of a session
  - 84% of participants, asked hypothetically afterwards, said they would
    have noticed if their chosen face had been swapped

The first two are reported as bounds, so they are drawn as bounds.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

labels = ["said they\nwould notice", "detected by\nend of session", "easily\nspotted"]
values = [84, 20, 10]
colours = [ds.ACCENT, ds.MUTED, ds.MUTED]
bounds = [False, True, True]

fig, ax = plt.subplots(figsize=(7.0, 3.5))
bars = ax.barh(labels, values, color=colours, height=0.58)
for bar, v, is_bound in zip(bars, values, bounds):
    ax.text(v + 2, bar.get_y() + bar.get_height() / 2,
            f"{'≤' if is_bound else ''}{v}%", color=ds.FG, va="center", fontsize=13)

ax.set_xlim(0, 100)
ax.set_xlabel("percentage")
ax.invert_yaxis()
ax.annotate("", xy=(84, 0.42), xytext=(20, 0.42),
            arrowprops=dict(arrowstyle="<->", color=ds.WARN, lw=1.6))
ax.text(52, 0.26, "the gap is the finding", color=ds.WARN, ha="center", fontsize=12)
ds.save(fig, "choice-blindness")
