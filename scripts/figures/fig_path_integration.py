"""Why a desert ant ends its homeward run with a spiral.

Cataglyphis fortis navigates by path integration: bearing from the polarised
skylight pattern, distance from a stride integrator (Wittlinger, Wehner & Wolf,
2006, Science 312, 1965-1967). What it holds is a running home vector, not the
route it took.

An accumulator with no independent reference cannot correct itself, so per-step
error compounds. This simulates that directly: at each step the ant's internal
estimate of its own heading and step length carries small Gaussian error, and
the home vector is integrated from the erroneous estimates rather than the true
ones.

The consequence falls out rather than being asserted, and it is not what you
would guess. The integrator is *good*: errors partly cancel on a wandering
path, so the miss grows only as roughly the square root of path length and
stays within a few body lengths.

It is still not good enough, because the target is a hole. Once the expected
miss exceeds the width of the nest entrance, arriving at the right place is no
longer the same as finding it -- so the systematic search at the end of the run
is not a failure of the system, it is the only available remedy.

Simulation, not their data. Noise parameters are stated on the figure.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270415)
HEAD_SD = np.deg2rad(6.0)  # per-step heading misestimate
STEP_SD = 0.04  # per-step length misestimate, proportional


def forage(n_steps, rng):
    """Return true path and the ant's integrated estimate of its displacement."""
    true_pos = np.zeros(2)
    est_disp = np.zeros(2)
    path = [true_pos.copy()]
    heading = rng.uniform(0, 2 * np.pi)
    for _ in range(n_steps):
        heading += rng.normal(0, 0.5)  # real wandering
        step = 1.0
        true_pos = true_pos + step * np.array([np.cos(heading), np.sin(heading)])
        path.append(true_pos.copy())
        # what the ant thinks it just did
        h_est = heading + rng.normal(0, HEAD_SD)
        s_est = step * (1 + rng.normal(0, STEP_SD))
        est_disp = est_disp + s_est * np.array([np.cos(h_est), np.sin(h_est)])
    return np.array(path), true_pos, est_disp


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 4.3))

path, true_end, est_disp = forage(220, RNG)
ax1.plot(path[:, 0], path[:, 1], color=ds.MUTED, lw=1.3, label="outbound (wandering)")
ax1.scatter([0], [0], s=110, color=ds.ACCENT, zorder=4, linewidths=0)
ax1.annotate("nest", (0, 0), textcoords="offset points", xytext=(10, 8),
             color=ds.ACCENT, fontsize=11)
ax1.scatter([true_end[0]], [true_end[1]], s=70, color=ds.FG, zorder=4, linewidths=0)
believed_home = true_end - est_disp
ax1.plot([true_end[0], believed_home[0]], [true_end[1], believed_home[1]],
         color=ds.WARN, lw=2.4, ls="--", label="homeward vector it runs")
ax1.plot([true_end[0], 0], [true_end[1], 0], color=ds.FG, lw=1.6, alpha=0.6,
         label="true direction home")
ax1.scatter([believed_home[0]], [believed_home[1]], s=70, color=ds.WARN,
            zorder=4, linewidths=0)
miss = np.hypot(*believed_home)
ax1.annotate(f"misses by {miss:.0f} body-lengths", believed_home,
             textcoords="offset points", xytext=(8, -16), color=ds.WARN, fontsize=11)
ax1.set_aspect("equal")
ax1.set_xticks([])
ax1.set_yticks([])
for s in ax1.spines.values():
    s.set_visible(False)
ax1.legend(loc="upper left", fontsize=10)
ax1.set_title("one foraging run", loc="left")

lengths = np.arange(25, 601, 25)
means, p90 = [], []
for n in lengths:
    misses = []
    for _ in range(300):
        _, te, ed = forage(int(n), RNG)
        misses.append(np.hypot(*(te - ed)))
    means.append(np.mean(misses))
    p90.append(np.percentile(misses, 90))

NEST = 0.5  # nest entrance, in body lengths -- an inconspicuous hole
ax2.plot(lengths, means, color=ds.ACCENT, lw=2.6, label="mean miss distance")
ax2.fill_between(lengths, 0, p90, color=ds.ACCENT, alpha=0.13,
                 label="up to 90th percentile")
ax2.axhline(NEST, color=ds.WARN, lw=2, ls="--")
ax2.text(lengths[-1], NEST + 0.06, "width of the nest entrance",
         color=ds.WARN, ha="right", fontsize=11)
crossing = next(l for l, m in zip(lengths, means) if m > NEST)
ax2.annotate(f"beyond ~{crossing} steps the error\nexceeds the target",
             xy=(crossing, NEST), xytext=(crossing + 90, NEST + 0.75),
             color=ds.WARN, fontsize=11,
             arrowprops=dict(arrowstyle="->", color=ds.WARN, lw=1.4))
ax2.set_xlabel("outbound path length (steps)")
ax2.set_ylabel("miss distance (body lengths)")
ax2.legend(loc="upper left", fontsize=10)
ax2.set_title(f"good, and not good enough  (heading SD {np.rad2deg(HEAD_SD):.0f}°, step SD {STEP_SD:.0%})",
              loc="left")
print(f"  error exceeds nest entrance beyond ~{crossing} steps")
print(f"  miss at 100 steps: {means[3]:.1f}   at 600 steps: {means[-1]:.1f}")
ds.save(fig, "path-integration-error")
