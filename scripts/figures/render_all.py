"""Regenerate every figure. Run from scripts/figures: python3 render_all.py

Outputs are committed, so CI needs no Python -- the scripts are provenance,
and each one names its source in its docstring.
"""

import runpy
import sys
from pathlib import Path

for f in sorted(Path(__file__).parent.glob("fig_*.py")):
    print(f"{f.name}:")
    sys.argv = [str(f)]
    runpy.run_path(str(f), run_name="__main__")
