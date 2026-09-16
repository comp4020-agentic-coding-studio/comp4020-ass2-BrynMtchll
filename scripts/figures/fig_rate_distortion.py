"""Rate-distortion function for a memoryless Gaussian source.

This is not a schematic. For a Gaussian source of variance sigma^2 under
squared-error distortion, the rate-distortion function has a closed form
(Shannon 1948; see Cover & Thomas, *Elements of Information Theory*, 2nd ed.,
Theorem 10.3.2):

    R(D) = 0.5 * log2(sigma^2 / D)   for 0 < D <= sigma^2
    R(D) = 0                          for D > sigma^2

So the curve below is computed, not drawn, and the knee at D = sigma^2 is a
real feature: once you are allowed distortion equal to the source variance,
you can transmit nothing at all and simply guess the mean.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4, 3.6))

for sigma2, colour, label in [(1.0, ds.ACCENT, r"$\sigma^2 = 1$"), (0.5, ds.MUTED, r"$\sigma^2 = 0.5$")]:
    D = np.linspace(1e-3, sigma2, 600)
    R = 0.5 * np.log2(sigma2 / D)
    ax.plot(D, R, color=colour, lw=2.6, label=label)
    ax.plot([sigma2, 1.15], [0, 0], color=colour, lw=2.6, ls=":")

ax.annotate(
    "no information sent:\nguess the mean",
    xy=(1.0, 0.0),
    xytext=(0.66, 1.15),
    color=ds.WARN,
    fontsize=11,
    arrowprops=dict(arrowstyle="->", color=ds.WARN, lw=1.4),
)
ax.set_xlabel("distortion $D$  (mean squared error)")
ax.set_ylabel("rate $R(D)$  (bits/sample)")
ax.set_xlim(0, 1.15)
ax.set_ylim(0, 4.2)
ax.legend(loc="upper right")
ds.save(fig, "rate-distortion")
