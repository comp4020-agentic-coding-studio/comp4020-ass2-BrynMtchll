"""E. coli chemotaxis: gradient climbing from a purely local comparison.

The bacterium has no spatial sense of the gradient and no representation of a
target. It has a receptor occupancy now, a memory of occupancy a few seconds
ago, and two motor states -- run and tumble (Berg, 'E. coli in Motion', 2004;
Macnab & Koshland, PNAS 69(9), 1972).

The rule simulated here is the whole mechanism:

    if things are improving, extend the current run
    otherwise, tumble to a random new heading

That is a biased random walk. It has no direction-finding in it at all, and it
climbs anyway. The right panel shows the population drifting up-gradient over
time, which is the only sense in which the bacterium 'goes' anywhere.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270304)
STEPS, N_CELLS = 900, 300
P_TUMBLE_BAD, P_TUMBLE_GOOD = 0.35, 0.06  # the entire decision rule


def run_and_tumble(rng, steps=STEPS):
    pos = np.zeros(2)
    heading = rng.uniform(0, 2 * np.pi)
    last_c = pos[0]
    track = [pos.copy()]
    for _ in range(steps):
        pos = pos + 0.35 * np.array([np.cos(heading), np.sin(heading)])
        c = pos[0]  # concentration increases with x
        improving = c > last_c
        last_c = c
        if rng.random() < (P_TUMBLE_GOOD if improving else P_TUMBLE_BAD):
            heading = rng.uniform(0, 2 * np.pi)
        track.append(pos.copy())
    return np.array(track)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 4.2),
                               gridspec_kw={"width_ratios": [1.3, 1]})

grad = np.linspace(0, 1, 256).reshape(1, -1)
ax1.imshow(grad, extent=[-8, 60, -22, 22], aspect="auto", origin="lower",
           cmap="gray", alpha=0.16)
for _ in range(6):
    t = run_and_tumble(RNG)
    ax1.plot(t[:, 0], t[:, 1], color=ds.MUTED, lw=1.0, alpha=0.8)
t = run_and_tumble(RNG)
ax1.plot(t[:, 0], t[:, 1], color=ds.ACCENT, lw=1.8)
ax1.scatter([0], [0], s=60, color=ds.FG, zorder=4, linewidths=0)
ax1.set_xlim(-8, 60)
ax1.set_ylim(-22, 22)
ax1.set_yticks([])
ax1.set_xlabel("attractant concentration increases →")
ax1.set_title("seven cells, same rule, no direction sensing", loc="left")

finals = np.array([run_and_tumble(RNG)[:, 0] for _ in range(N_CELLS)])
mean_x = finals.mean(axis=0)
ax2.plot(mean_x, color=ds.ACCENT, lw=2.6)
ax2.fill_between(range(len(mean_x)),
                 np.percentile(finals, 25, axis=0),
                 np.percentile(finals, 75, axis=0),
                 color=ds.ACCENT, alpha=0.15)
ax2.set_xlabel("time step")
ax2.set_ylabel("mean position up-gradient")
ax2.set_title(f"{N_CELLS} cells: the population climbs", loc="left")

print(f"  mean displacement after {STEPS} steps: {mean_x[-1]:.1f} units")
ds.save(fig, "chemotaxis")
