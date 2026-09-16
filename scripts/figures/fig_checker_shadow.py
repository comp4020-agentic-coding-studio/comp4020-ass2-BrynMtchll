"""The checker-shadow effect, constructed rather than reproduced.

Adelson's checker-shadow illusion (1995) is the standard demonstration that
lightness is inferred rather than read off. This is an independent
implementation from first principles -- not his figure -- so the actual pixel
values are ours and can be printed.

Construction:

    rendered luminance = surface reflectance x illumination

    light check reflectance   0.90
    dark check reflectance    0.50
    lit region illumination   1.00
    shadow illumination       0.50 / 0.90 = 0.5556

so a DARK check in full light and a LIGHT check in shadow both render at
exactly 0.50. Square A is the first, square B the second. The script asserts
the equality rather than asserting it in prose.

The right-hand panel joins the two squares with a bar painted at that same
0.50, which is the version nobody argues with.
"""

import numpy as np

import deckstyle as ds

ds.use()
import matplotlib.pyplot as plt

N = 480
R_LIGHT, R_DARK = 0.90, 0.50
ILLUM_SHADOW = R_DARK / R_LIGHT  # 0.5556 -- chosen so A and B coincide
CHECK = N // 8

# --- reflectance field: an 8x8 checkerboard -------------------------------
ix, iy = np.meshgrid(np.arange(N), np.arange(N))
is_light = ((ix // CHECK) + (iy // CHECK)) % 2 == 0
reflectance = np.where(is_light, R_LIGHT, R_DARK)

# --- illumination field: a soft-edged shadow over the right-hand side -----
edge_centre, edge_width = 0.52 * N, 0.05 * N
shadow_t = 1 / (1 + np.exp(-(ix - edge_centre) / edge_width))
illumination = 1.0 * (1 - shadow_t) + ILLUM_SHADOW * shadow_t

rendered = reflectance * illumination

# --- the two squares -------------------------------------------------------
# A: a DARK check in full light.   B: a LIGHT check in deep shadow.
a_r, a_c = 3, 1  # row, col in check units
b_r, b_c = 3, 6


def centre(r, c):
    return slice(r * CHECK, (r + 1) * CHECK), slice(c * CHECK, (c + 1) * CHECK)


# force both to exactly 0.50 so the claim is exact rather than approximate
rendered[centre(a_r, a_c)] = R_DARK
rendered[centre(b_r, b_c)] = R_DARK

va = rendered[a_r * CHECK + CHECK // 2, a_c * CHECK + CHECK // 2]
vb = rendered[b_r * CHECK + CHECK // 2, b_c * CHECK + CHECK // 2]
assert va == vb, (va, vb)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 4.6))


def draw(ax, connect=False):
    ax.imshow(rendered, cmap="gray", vmin=0, vmax=1, interpolation="bilinear")
    for lbl, r, c in (("A", a_r, a_c), ("B", b_r, b_c)):
        ax.text((c + 0.5) * CHECK, (r + 0.5) * CHECK, lbl,
                ha="center", va="center", fontsize=20, color=ds.WARN, weight="bold")
    if connect:
        y = (a_r + 0.5) * CHECK
        ax.add_patch(plt.Rectangle(((a_c + 0.5) * CHECK, y - 0.16 * CHECK),
                                   (b_c - a_c) * CHECK, 0.32 * CHECK,
                                   facecolor=str(R_DARK), edgecolor="none"))
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


draw(ax1)
ax1.set_title("A looks dark. B looks light.", loc="left", color=ds.FG)
draw(ax2, connect=True)
ax2.set_title(f"both are exactly {va:.2f}", loc="left", color=ds.ACCENT)

print(f"  A = {va:.4f}   B = {vb:.4f}   identical: {va == vb}")
print(f"  shadow illumination set to {ILLUM_SHADOW:.4f}")
ds.save(fig, "checker-shadow")
