#!/usr/bin/env python3
"""Compile every .d2 source to src/decks/figures/<name>.svg.

    python3 scripts/diagrams/render_all.py

Two things this does beyond calling d2:

1. Strips the theme background. D2 paints an opaque rect behind the diagram,
   and because a deck references the file as <img src="...">, external CSS
   cannot reach inside it -- so transparency has to be baked in here. We inject
   a style override rather than deleting the rect, which survives d2 changing
   its markup.

2. Makes the root SVG scale. D2 emits a fixed width/height; dropping those and
   keeping the viewBox lets the deck's .fig rules size it at both marking
   viewports.

Outputs are committed, so CI never needs d2 installed. The .d2 sources are the
provenance: each names its subject and its week.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "scripts" / "diagrams"
OUT = ROOT / "src" / "decks" / "figures"
THEME = "200"  # Dark Mauve; every colour is overridden in _style.d2 anyway

OVERRIDE = (
    "<style type=\"text/css\"><![CDATA["
    ".d2-svg>rect:first-of-type,rect.fill-N7{fill:transparent!important}"
    "]]></style>"
)


def render(src: Path) -> None:
    dst = OUT / f"{src.stem}.svg"
    r = subprocess.run(
        ["d2", "--theme", THEME, "--dark-theme", THEME, str(src), str(dst)],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(f"  FAIL {src.name}\n{r.stderr.strip()}")
        return 1

    svg = dst.read_text()
    # bake transparency
    svg = svg.replace("</svg>", OVERRIDE + "</svg>", 1) if "fill-N7" in svg else svg
    # let the slide size it
    svg = re.sub(r'(<svg[^>]*?)\swidth="\d+"\sheight="\d+"', r"\1", svg, count=1)
    dst.write_text(svg)
    print(f"  {src.name:34s} -> src/decks/figures/{dst.name}  ({dst.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sources = sorted(p for p in SRC.glob("*.d2") if not p.name.startswith("_"))
    if not sources:
        sys.exit("no .d2 sources found")
    fails = sum(render(s) or 0 for s in sources)
    print(f"{len(sources) - fails}/{len(sources)} diagrams rendered")
    sys.exit(1 if fails else 0)
