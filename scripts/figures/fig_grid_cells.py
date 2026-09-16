"""A grid cell's firing field, and the same code applied to a space that is not
space at all.

The standard model of a grid field is the thresholded sum of three cosine plane
waves whose wave vectors sit 60 degrees apart. That construction produces a
hexagonal lattice necessarily -- it is a fact about interference, not a drawing
decision -- which is why hexagonal symmetry is the signature the fMRI work
looks for.

Panel 1: three plane waves, summed, thresholded. A hexagonal firing field.
Panel 2: the same field, with the axes relabelled as two continuous conceptual
dimensions rather than metres.

That relabelling is the whole of Constantinescu, O'Reilly & Behrens (2016,
Science 352(6292), 1464-1468): people navigating a two-dimensional space of
concepts showed the same hexagonally symmetric signal, in entorhinal cortex and
vmPFC, stable across sessions a week apart.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

GRID_CM = LinearSegmentedColormap.from_list(
    "grid", ["#00000000", "#2b2823", "#8f6a20", ds.ACCENT]
)

n, extent = 420, 3.0
x = np.linspace(-extent, extent, n)
X, Y = np.meshgrid(x, x)

SCALE = 2.6  # spatial frequency
field = np.zeros_like(X)
for angle in (0, 60, 120):
    th = np.deg2rad(angle)
    k = SCALE * np.array([np.cos(th), np.sin(th)])
    field += np.cos(k[0] * X + k[1] * Y)

field = (field - field.min()) / (field.max() - field.min())
field = np.clip((field - 0.55) / 0.45, 0, 1)  # threshold: only peaks fire

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 4.7))

for ax in (ax1, ax2):
    ax.imshow(field, cmap=GRID_CM, extent=[-extent, extent, -extent, extent],
              origin="lower", interpolation="bilinear")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(ds.MUTED)

ax1.set_xlabel("position, x (m)")
ax1.set_ylabel("position, y (m)")
ax1.set_title("a grid cell in an open arena", loc="left")

ax2.set_xlabel("stimulus dimension 1  (e.g. neck length)")
ax2.set_ylabel("dimension 2  (e.g. leg length)")
ax2.set_title("the same code, over concepts", loc="left", color=ds.ACCENT)

# mark the hexagon that the interference guarantees
import matplotlib.patches as mp

hexagon = mp.RegularPolygon((0, 0), numVertices=6, radius=2.79,
                            orientation=np.deg2rad(30), fill=False,
                            edgecolor=ds.WARN, lw=2, ls="--")
ax1.add_patch(hexagon)
ax1.text(0, -2.55, "60° symmetry is forced by the construction",
         color=ds.WARN, ha="center", fontsize=10)

ds.save(fig, "grid-cells")
print(f"  field peaks: {(field > 0.9).sum()} pixels above 0.9")
