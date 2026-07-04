#!/usr/bin/env python3
"""Add GitHub-style calendar labels to a Platane/snk contribution snake SVG.

snk renders the same grid as GitHub's contribution calendar (Sunday-start
weeks, one column per week) but without any axis text. This script injects
month labels above the grid and Mon/Wed/Fri labels on the left, mirroring
github.com, and widens the viewBox to make room for the weekday column.

Usage: add_snake_labels.py <svg-file> <label-color>
The grid is anchored to today's date (UTC): the right-most column is the
current week, exactly like the calendar snk scraped moments earlier.
"""

import datetime
import re
import sys

WEEKDAY_LABELS = {1: "Mon", 3: "Wed", 5: "Fri"}
FONT = 'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10"'
LEFT_PAD = 28  # extra viewBox width for the weekday labels


def main(path: str, color: str) -> None:
    svg = open(path).read()

    cells = [
        (int(m.group(1)), int(m.group(2)))
        for m in re.finditer(r'<rect class="c[^"]*" x="(-?\d+)" y="(-?\d+)"', svg)
    ]
    if not cells:
        raise SystemExit(f"{path}: no grid cells found — snk output format changed?")

    cols = sorted({x for x, _ in cells})
    rows = sorted({y for _, y in cells})
    step = cols[1] - cols[0]
    cell = 12  # snk cell size

    # Right-most column is the week containing today; its top cell is Sunday.
    today = datetime.date.today()
    current_sunday = today - datetime.timedelta(days=(today.weekday() + 1) % 7)

    texts = []

    # Month label above every column whose Sunday starts a new month. The
    # first (partial) column is never labeled, matching github.com.
    prev_month = None
    for i, x in enumerate(cols):
        sunday = current_sunday - datetime.timedelta(weeks=len(cols) - 1 - i)
        if prev_month is not None and sunday.month != prev_month:
            texts.append(
                f'<text x="{x}" y="-8" fill="{color}" {FONT}>'
                f"{sunday.strftime('%b')}</text>"
            )
        prev_month = sunday.month

    # Mon / Wed / Fri on the left, vertically centered on their row.
    for idx, label in WEEKDAY_LABELS.items():
        if idx < len(rows):
            y = rows[idx] + cell // 2
            texts.append(
                f'<text x="{cols[0] - 8}" y="{y}" text-anchor="end" '
                f'dominant-baseline="central" fill="{color}" {FONT}>{label}</text>'
            )

    # Widen the viewBox to the left so the weekday labels are not clipped.
    def widen(m: re.Match) -> str:
        x, y, w, h = (float(v) for v in m.group(1).split())
        return f'viewBox="{x - LEFT_PAD:g} {y:g} {w + LEFT_PAD:g} {h:g}"'

    svg = re.sub(r'viewBox="([^"]+)"', widen, svg, count=1)
    svg = re.sub(
        r'width="(\d+)"', lambda m: f'width="{int(m.group(1)) + LEFT_PAD}"', svg, count=1
    )
    svg = svg.replace("</svg>", "".join(texts) + "</svg>")

    open(path, "w").write(svg)
    print(f"{path}: added {len(texts)} labels")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
