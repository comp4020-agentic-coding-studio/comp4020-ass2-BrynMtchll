"""No Free Lunch, computed rather than asserted.

Wolpert & Macready (1997). Averaged over all possible target functions, every
learner performs identically off the training set.

This is small enough to verify exhaustively rather than sample. Take 8 binary
input points and enumerate all 2^8 = 256 possible target labellings. Train on
the first 4 points (so every learner sees identical evidence), predict the
remaining 4, and score. No sampling, no seed, no approximation: the bars below
are the complete population.

Three learners with genuinely different biases are compared. Each wins on some
target functions and loses on others, and all three average to exactly 0.5.
"""

import itertools

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

N_POINTS, N_TRAIN = 8, 4
targets = np.array(list(itertools.product([0, 1], repeat=N_POINTS)))


def majority(train_y):
    """Predict whatever was most common in training."""
    return int(train_y.sum() * 2 >= len(train_y))


def learners(train_y):
    m = majority(train_y)
    return {
        "follow the majority": [m] * (N_POINTS - N_TRAIN),
        "oppose the majority": [1 - m] * (N_POINTS - N_TRAIN),
        "alternate": [(i % 2) for i in range(N_POINTS - N_TRAIN)],
    }


scores = {k: [] for k in learners(targets[0][:N_TRAIN])}
for t in targets:
    train_y, test_y = t[:N_TRAIN], t[N_TRAIN:]
    for name, pred in learners(train_y).items():
        scores[name].append(float(np.mean(np.array(pred) == test_y)))

fig, ax = plt.subplots(figsize=(7.4, 3.9))
colours = [ds.ACCENT, ds.WARN, ds.MUTED]
for (name, s), c in zip(scores.items(), colours):
    vals, counts = np.unique(s, return_counts=True)
    ax.plot(vals, counts, marker="o", lw=2.4, color=c,
            label=f"{name}  (mean {np.mean(s):.3f})")

ax.axvline(0.5, color=ds.FG, lw=1.2, ls="--", alpha=0.6)
ax.text(0.505, ax.get_ylim()[1] * 0.92, "0.5", color=ds.FG, fontsize=11, alpha=0.8)
ax.set_xlabel("off-training accuracy on one target function")
ax.set_ylabel("number of target functions")
ax.legend(loc="upper left")
ds.save(fig, "no-free-lunch")
for name, s in scores.items():
    print(f"  {name:22s} mean = {np.mean(s):.6f}")
