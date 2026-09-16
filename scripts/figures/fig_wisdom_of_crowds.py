"""Why social influence can undermine a group estimate without improving it.

Lorenz, Rauhut, Schweitzer & Helbing (2011), PNAS 108(22), 9020-9025, report
that mild social influence reduced the *diversity* of estimates without
reducing the *collective error* -- so groups converged and became more
confident while getting no closer to the truth.

This simulates the mechanism rather than their data. Estimators start with
independent beliefs that are unbiased but noisy; the crowd mean is therefore
close to the truth. Under influence, each estimator moves partway toward the
group mean each round. Averaging is a variance-reduction trick, so shrinking
the spread cannot improve the mean -- but it does shrink the visible
disagreement, which is what people read confidence off.

Becker, Brackbill & Centola (2017, PNAS) show decentralised network structures
where influence *does* improve accuracy. The disagreement in the literature is
about topology, not about people.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20270426)
TRUTH, N, ROUNDS, PULL = 100.0, 60, 6, 0.35
BIAS = 6.0  # a small shared bias, as real estimation tasks have

est = TRUTH + BIAS + RNG.normal(0, 22, N)
spread, error = [est.std()], [abs(est.mean() - TRUTH)]
history = [est.copy()]

for _ in range(ROUNDS):
    est = est + PULL * (est.mean() - est)
    history.append(est.copy())
    spread.append(est.std())
    error.append(abs(est.mean() - TRUTH))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 4.1))

for r, e in enumerate(history):
    ax1.scatter(np.full(N, r), e, s=10, color=ds.MUTED, alpha=0.5, linewidths=0)
ax1.axhline(TRUTH, color=ds.FG, lw=1.6, ls="--", label="truth")
ax1.plot(range(len(history)), [h.mean() for h in history],
         color=ds.ACCENT, lw=2.6, marker="o", label="group mean")
ax1.set_xlabel("round of social influence")
ax1.set_ylabel("estimate")
ax1.legend(loc="upper right", fontsize=10)
ax1.set_title("the crowd converges", loc="left")

ax2.plot(spread, color=ds.WARN, lw=2.6, marker="o", label="spread (SD of estimates)")
ax2.plot(error, color=ds.ACCENT, lw=2.6, marker="o", label="collective error")
ax2.set_xlabel("round of social influence")
ax2.set_ylabel("value")
ax2.legend(loc="center right", fontsize=10)
ax2.set_title("on what it converges, and what it doesn't", loc="left")

print(f"  spread {spread[0]:.1f} -> {spread[-1]:.1f}   error {error[0]:.1f} -> {error[-1]:.1f}")
ds.save(fig, "wisdom-of-crowds")
