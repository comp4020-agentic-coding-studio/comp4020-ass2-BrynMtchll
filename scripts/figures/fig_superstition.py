"""Superstition as a prediction of the mechanism, not a malfunction of it.

Skinner (1948), 'Superstition in the pigeon', J. Exp. Psychol. 38, 168-172:
birds on a fixed-interval food schedule acquired elaborate stereotyped
routines. The hopper was on a timer. Nothing the bird did affected it.

This simulates why that happens to any system that has access to co-occurrence
and no access to causal structure. The agent emits one of several actions per
step, food arrives on a fixed interval regardless, and the agent tracks how
often each action was followed by food. Whichever action happens to be in
progress when the timer fires gains strength, is emitted more often, and is
therefore more likely to be in progress next time.

Positive feedback on a coincidence. The true contingency is zero for every
action, and the agent ends up committed to one of them anyway.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270318)
N_ACTIONS, STEPS, INTERVAL = 6, 4000, 15
LR = 0.06

strength = np.ones(N_ACTIONS)
history = np.zeros((STEPS, N_ACTIONS))

for t in range(STEPS):
    p = strength / strength.sum()
    a = RNG.choice(N_ACTIONS, p=p)
    fed = (t % INTERVAL) == 0  # nothing the agent does affects this
    if fed:
        strength[a] += LR * strength[a] * 10
    strength *= 1 - LR * 0.02  # slow decay
    strength = np.clip(strength, 0.05, None)
    history[t] = strength / strength.sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 4.0),
                               gridspec_kw={"width_ratios": [1.45, 1]})

cols = [ds.ACCENT, ds.FG, ds.MUTED, ds.MUTED, ds.MUTED, ds.MUTED]
order = np.argsort(-history[-1])
for rank, i in enumerate(order):
    ax1.plot(history[:, i], color=cols[min(rank, 5)],
             lw=2.4 if rank == 0 else 1.3,
             label=f"action {i + 1}" if rank < 2 else None)
ax1.axhline(1 / N_ACTIONS, color=ds.WARN, lw=1.6, ls="--")
ax1.text(STEPS * 0.02, 1 / N_ACTIONS + 0.012, "chance (1/6)", color=ds.WARN, fontsize=10)
ax1.set_xlabel("time step")
ax1.set_ylabel("probability of emission")
ax1.legend(loc="upper left", fontsize=10)
ax1.set_title("one run: the agent commits to an action", loc="left")

ax2.bar(["true\ncontingency", "learned\nstrength"], [0.0, history[-1].max()],
        color=[ds.MUTED, ds.ACCENT], width=0.55)
ax2.text(0, 0.03, "0.00", ha="center", color=ds.FG, fontsize=13)
ax2.text(1, history[-1].max() + 0.03, f"{history[-1].max():.2f}",
         ha="center", color=ds.FG, fontsize=13)
ax2.set_ylim(0, max(0.5, history[-1].max() * 1.3))
ax2.set_title("for the winning action", loc="left")

print(f"  winner reaches p = {history[-1].max():.3f}, true contingency 0.000")
ds.save(fig, "superstition")
