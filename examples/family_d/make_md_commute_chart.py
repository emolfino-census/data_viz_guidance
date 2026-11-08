#!/usr/bin/env python3
"""Draw a part-to-whole chart of how Maryland workers got to work.

The numbers are published Census estimates. They are saved in
md_b08301_means_of_transportation.csv, next to this program, because the
Census data API asks for a key.

Source: U.S. Census Bureau
Survey: American Community Survey, 2025 1-year estimates
Table: B08301, Means of Transportation to Work
Place: Maryland (FIPS 24)
Who is counted: workers 16 years and over
Published table: https://data.census.gov/table/ACSDT1Y2025.B08301?g=040XX00US24
Saved from data.census.gov on 2026-11-08

Run from the project folder:

    python3 examples/family_d/make_md_commute_chart.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "md_b08301_means_of_transportation.csv"
OUT_PATH = HERE.parents[1] / "assets" / "family-d" / "md-means-of-transportation.png"

# These colors stay distinct for common kinds of color blindness.
# Each fill has at least a 3 to 1 contrast with the white page, and the
# black outline has at least a 3 to 1 contrast with each fill.
COLORS = {
    "car": "#0072B2",
    "home": "#D55E00",
    "transit": "#009E73",
    "other": "#AA4499",
}

GROUP_LABELS = {
    "car": "Car, truck, or van",
    "home": "Worked from home",
    "transit": "Public transportation",
    "other": "Walking, taxi or ride-hailing, bicycle, motorcycle, or other means",
}

# Same words as GROUP_LABELS, with a line break so the legend fits.
LEGEND_LABELS = {
    "car": "Car, truck, or van",
    "home": "Worked from home",
    "transit": "Public transportation",
    "other": "Walking, taxi or ride-hailing,\nbicycle, motorcycle, or other means",
}


def read_published_rows(path: Path):
    """Read the saved table, skipping the source notes at the top."""
    data_lines = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            data_lines.append(line)
    return list(csv.DictReader(data_lines))


def build_slices(rows):
    """Turn the published rows into the four slices drawn on the chart."""
    total = None
    grouped = {
        key: {"estimate": 0, "squared_margins": 0}
        for key in GROUP_LABELS
    }

    for row in rows:
        estimate = int(row["estimate"])
        margin = int(row["margin_of_error"])
        group = row["chart_group"].strip()
        if row["variable"] == "B08301_001":
            total = estimate
            continue
        if group not in grouped:
            raise SystemExit(f"Unknown chart group '{group}' in {row['variable']}.")
        grouped[group]["estimate"] += estimate
        grouped[group]["squared_margins"] += margin ** 2

    if total is None:
        raise SystemExit("The CSV is missing the published total, B08301_001.")

    slices = []
    for key, values in grouped.items():
        estimate = values["estimate"]
        # For one published row, this is that row's own margin of error.
        # For the combined slice, this is the Census formula for a sum:
        # the square root of the sum of the squared margins.
        margin = math.sqrt(values["squared_margins"])
        slices.append(
            {
                "key": key,
                "label": GROUP_LABELS[key],
                "estimate": estimate,
                "margin": margin,
                "percent": 100.0 * estimate / total,
                "color": COLORS[key],
            }
        )

    added = sum(item["estimate"] for item in slices)
    if added != total:
        raise SystemExit(
            f"The slices add to {added:,}, but the published total is {total:,}."
        )
    return total, slices


def draw_chart(total, slices, out_path: Path):
    """Save a pie chart with labels in a legend, not color alone."""
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.4, 7.0), dpi=120)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    wedges, _ = ax.pie(
        [item["estimate"] for item in slices],
        colors=[item["color"] for item in slices],
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "#1b1b1b", "linewidth": 1.8},
    )

    legend_labels = [
        f"{LEGEND_LABELS[item['key']]}\n{item['percent']:.1f}% of workers"
        for item in slices
    ]
    legend = ax.legend(
        wedges,
        legend_labels,
        loc="center left",
        bbox_to_anchor=(0.98, 0.52),
        frameon=False,
        fontsize=12,
        handlelength=1.4,
        handleheight=1.4,
        labelspacing=1.15,
        borderaxespad=0.2,
    )
    for text in legend.get_texts():
        text.set_color("#1b1b1b")

    ax.set_title(
        "How Maryland workers got to work, 2025",
        loc="left",
        fontsize=18,
        color="#1b1b1b",
        fontweight="bold",
        pad=14,
    )

    fig.text(
        0.01,
        0.075,
        f"Share of {total:,} workers age 16 and over. Percents are rounded to one decimal place.",
        fontsize=11,
        color="#1b1b1b",
        ha="left",
    )
    fig.text(
        0.01,
        0.03,
        "Source: U.S. Census Bureau. American Community Survey, 2025 1-year estimates, table B08301.",
        fontsize=11,
        color="#1b1b1b",
        ha="left",
    )

    fig.subplots_adjust(left=0.02, right=0.52, top=0.86, bottom=0.16)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, facecolor="#ffffff", bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)


def main():
    total, slices = build_slices(read_published_rows(CSV_PATH))
    draw_chart(total, slices, OUT_PATH)
    print(f"Published total: {total:,} workers")
    for item in slices:
        print(
            f"{item['label']}: {item['estimate']:,} "
            f"(±{item['margin']:,.0f}), {item['percent']:.1f}%"
        )
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
