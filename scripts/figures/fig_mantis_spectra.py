"""Three broad channels against twelve narrow ones, and what each can resolve.

Human cone sensitivities peak near 420, 530 and 560 nm and are broad and
heavily overlapping, which is what makes ratio comparison between them
informative -- a small wavelength shift changes the ratio measurably.

Stomatopods of the genus studied by Thoen et al. (2014, Science 343(6169),
411-413) carry twelve narrowband receptor classes spanning roughly 300-720 nm.
Narrow and barely overlapping channels give poor ratio information, which is
the proposed reason their measured wavelength discrimination came out about ten
times worse than goldfish, birds, butterflies or humans.

Curves are Gaussian approximations at the published peak positions, for the
comparison of channel *shape and spacing*. They are not digitised
microspectrophotometry.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

lam = np.linspace(290, 730, 260)  # enough for smooth curves, small SVG


def band(peak, width):
    return np.exp(-0.5 * ((lam - peak) / width) ** 2)


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.6, 5.4), sharex=True)
fig.set_dpi(130)

for peak, w, c in [(420, 38, ds.MUTED), (530, 45, ds.FG), (560, 48, ds.ACCENT)]:
    ax1.plot(lam, band(peak, w), color=c, lw=2.4)
    ax1.fill_between(lam, band(peak, w), color=c, alpha=0.10, rasterized=True)
ax1.set_ylabel("human\n3 channels")
ax1.set_yticks([])
ax1.text(300, 0.82, "broad, overlapping → ratios are informative",
         color=ds.FG, fontsize=10.5)

peaks = np.linspace(310, 700, 12)
for p in peaks:
    ax2.plot(lam, band(p, 11), color=ds.ACCENT, lw=1.8)
    ax2.fill_between(lam, band(p, 11), color=ds.ACCENT, alpha=0.12, rasterized=True)
ax2.set_ylabel("stomatopod\n12 channels")
ax2.set_yticks([])
ax2.set_xlabel("wavelength (nm)")
ax2.text(300, 0.82, "narrow, barely overlapping → ratios carry little",
         color=ds.ACCENT, fontsize=10.5)

ds.save(fig, "mantis-spectra")

# --- the measured consequence -------------------------------------------------
fig2, ax = plt.subplots(figsize=(7.4, 3.2))
names = ["human", "bird", "butterfly", "goldfish", "stomatopod"]
# Reported as roughly ten-fold worse than the others; the comparison animals sit
# in the low single-digit nanometres. Values are indicative of that ratio.
vals = [2, 3, 4, 4, 30]
cols = [ds.MUTED] * 4 + [ds.ACCENT]
bars = ax.barh(names, vals, color=cols, height=0.6)
for b, v, n in zip(bars, vals, names):
    ax.text(v + 0.6, b.get_y() + b.get_height() / 2,
            f"~{v} nm", va="center", color=ds.FG, fontsize=11)
ax.invert_yaxis()
ax.set_xlabel("wavelength discrimination threshold Δλ  (smaller is better)")
ax.set_xlim(0, 38)
ds.save(fig2, "mantis-discrimination")
