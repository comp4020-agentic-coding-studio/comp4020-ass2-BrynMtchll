"""Why a brain would predict: the bit saving is computable.

Predictive coding's efficiency claim is usually stated qualitatively -- send
only what was not expected. It can be measured instead.

Natural signals are highly redundant: neighbouring samples are correlated, so
each one is largely predictable from the last. Transmitting the raw samples
therefore wastes capacity on information the receiver could have inferred.
Transmitting the *residual* -- what the prediction got wrong -- does not.

This generates a signal with the 1/f^2 power spectrum measured in natural
scenes,
quantises it to 256 levels, and compares the empirical Shannon entropy of the
raw samples against the entropy of first-order prediction residuals. The ratio
is the saving, in bits per sample, for a predictor of almost no sophistication.

Barlow's efficient coding hypothesis (1961) is the ancestor of this argument.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270329)
N = 1 << 15


def pink(n, rng, beta=2.0):
    """A signal whose POWER spectrum falls as 1/f^beta.

    beta = 2 is the value measured for natural scenes (Field 1987; Ruderman &
    Bialek 1994), so this is the redundancy a visual system actually faces
    rather than an arbitrary smoothness.
    """
    f = np.fft.rfftfreq(n)
    f[0] = f[1]
    spec = (f ** (-beta / 2)) * np.exp(2j * np.pi * rng.random(len(f)))
    x = np.fft.irfft(spec, n)
    return x / np.std(x)


def entropy_bits(q):
    _, counts = np.unique(q, return_counts=True)
    p = counts / counts.sum()
    return float(-(p * np.log2(p)).sum())


sig = pink(N, RNG)
raw = np.clip(np.round(sig * 40) + 128, 0, 255).astype(int)
resid = np.diff(raw, prepend=raw[0])

h_raw, h_res = entropy_bits(raw), entropy_bits(resid)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 4.0),
                               gridspec_kw={"width_ratios": [1.5, 1]})

seg = slice(0, 600)
ax1.plot(raw[seg], color=ds.MUTED, lw=1.4, label="raw samples")
ax1.plot(resid[seg] + 128, color=ds.ACCENT, lw=1.2, label="prediction residual")
ax1.axhline(128, color=ds.FG, lw=0.8, alpha=0.4)
ax1.set_xlabel("sample")
ax1.set_yticks([])
ax1.legend(loc="upper right", fontsize=10)
ax1.set_title("the residual is almost flat — that is the point", loc="left")

bars = ax2.bar(["raw", "residual"], [h_raw, h_res],
               color=[ds.MUTED, ds.ACCENT], width=0.55)
for b, v in zip(bars, [h_raw, h_res]):
    ax2.text(b.get_x() + b.get_width() / 2, v + 0.12, f"{v:.2f}",
             ha="center", fontsize=13, color=ds.FG)
ax2.set_ylabel("entropy (bits/sample)")
ax2.set_ylim(0, max(h_raw, h_res) * 1.25)
ax2.set_title(f"{h_raw - h_res:.2f} bits saved per sample", loc="left")

print(f"  raw {h_raw:.3f} bits   residual {h_res:.3f} bits")
print(f"  saving {h_raw - h_res:.3f} bits/sample  ({(1 - h_res / h_raw) * 100:.0f}%)")
ds.save(fig, "predictive-coding-bits")
