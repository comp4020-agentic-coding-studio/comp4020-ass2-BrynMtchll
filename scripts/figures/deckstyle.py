"""Shared style for every generated figure in this course's decks.

Decks are dark surfaces, so figures render light-on-transparent and inherit
the slide background rather than sitting in a white box. One module so a
colour is defined once; a colour restated per figure is how a deck starts to
disagree with itself.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Slop palette, matched to the --at-* brand tokens the deck theme uses.
FG = "#e8e4dc"  # body text and axes on a dark slide
MUTED = "#8f8a82"  # context, comparison series
ACCENT = "#f2b53b"  # the thing under discussion
WARN = "#e2664f"  # the failure, or the discarded part

BASE = {
    "figure.facecolor": "none",
    "axes.facecolor": "none",
    "savefig.facecolor": "none",
    "savefig.transparent": True,
    "text.color": FG,
    "axes.labelcolor": FG,
    "axes.edgecolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 13,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "legend.fontsize": 12,
    "legend.frameon": False,
    "figure.autolayout": True,
    "svg.fonttype": "path",  # no font dependency on the viewer's machine
}


def use():
    plt.rcParams.update(BASE)


def save(fig, name):
    """Write to src/decks/figures/<name>.svg, beside the decks that use it."""
    from pathlib import Path

    out = Path(__file__).resolve().parents[2] / "src" / "decks" / "figures" / f"{name}.svg"
    fig.savefig(out, format="svg", bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print(f"  wrote src/decks/figures/{out.name}  ({out.stat().st_size // 1024} KB)")
