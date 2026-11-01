#!/usr/bin/env python3
"""Keep the contribution calendar readable while the snake moves over it.

Platane/snk normally animates contribution cells to the empty color when they
are eaten. For a portfolio README we want to retain the real activity grid
throughout the animation, including its low-activity cells.
"""

from pathlib import Path

FILES = (
    Path("dist/github-contribution-grid-snake.svg"),
    Path("dist/github-contribution-grid-snake-dark.svg"),
)

ORIGINAL_VIEW = 'viewBox="-16 -32 880 192" width="880" height="192"'
COMPACT_VIEW = 'viewBox="-16 -20 880 152" width="880" height="152"'
# The snake uses .s and its own keyframes; only the cell-eating animations
# and extra bottom progress strip are disabled.
PRESERVE_GRID = (
    ".c{animation:none!important}"
    ".u{display:none!important}"
)

for path in FILES:
    svg = path.read_text(encoding="utf-8")
    if svg.count("</style>") != 1 or ORIGINAL_VIEW not in svg:
        raise SystemExit(f"Unexpected SVG format in {path}; refusing silent changes")
    if 'class="c ' not in svg or 'class="s ' not in svg:
        raise SystemExit(f"Missing contribution cells or animated snake in {path}")

    svg = svg.replace("</style>", PRESERVE_GRID + "</style>", 1)
    svg = svg.replace(ORIGINAL_VIEW, COMPACT_VIEW, 1)

    # Preserve the data and the snake keyframes. Only change presentation.
    assert "@keyframes s0" in svg
    assert 'class="c ' in svg
    assert "animation:none!important" in svg

    path.write_text(svg, encoding="utf-8")
    print(f"Preserved contribution grid in {path}")
