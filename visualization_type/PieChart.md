---
layout: default
title: Pie Chart
permalink: piechart.html
tags: [Distribution]
description: "Short Description of Pie Chart"
---

<style>
  .custom-sidebar h3,
  .main-content h3 { color: #137e55; }
  .tag-link { background: #137e55; }
  .main-content .highlight,
  .main-content .highlight pre,
  .main-content pre,
  .main-content code {
    color: #1b1b1b;
    background: #f6f8fa;
    max-width: 100%;
    box-sizing: border-box;
  }
  .main-content .highlight span { color: #1b1b1b !important; }
  .main-content .highlight,
  .main-content .highlight pre,
  .main-content pre,
  .main-content code,
  .main-content .highlight span {
    overflow: visible !important;
    white-space: pre-wrap !important;
    overflow-wrap: anywhere;
  }
</style>

# Pie Chart

Also known as: circle chart

A pie chart is a circular graph that presents values as proportionate wedges or slices of a circle.

It is strongly suggested not to use a pie chart to depict data. Before using a pie chart, consider using a [bar chart](https://xdgov.github.io/data-design-standards/visualizations/bar-chart), stacked bar chart, a table, donut chart or displaying numeric values directly for improved usability.

Pie charts are one of the most commonly used data visualizations but are often not the most effective way to compare data values. This failure in effectiveness is mainly due to problems interpreting the size of each wedge and the number of data categories being represented. Pie charts can also be represented as a doughnut chart, which is generally better for users to compare the size of each wedge or arc.

## Guidance
In addition to the guidance provided in this section, relevant guidance can also be found in the [Agency Logo](https://xdgov.github.io/data-design-standards/components/agency-logo), [Axes](https://xdgov.github.io/data-design-standards/components/axes), [Colors](https://xdgov.github.io/data-design-standards/components/colors), [Grids](https://xdgov.github.io/data-design-standards/components/grids), [Legends](https://xdgov.github.io/data-design-standards/components/legends), [Source](https://xdgov.github.io/data-design-standards/components/source), [Titles](https://xdgov.github.io/data-design-standards/components/titles), [Typography](https://xdgov.github.io/data-design-standards/components/typography) sections.

## Best Practices

### Essential

* Include a legend or label wedges directly.
* Ensure that the values of the wedges total to 100%.
* When appropriate, display measures of uncertainty and indicate the measure being used within the chart, please see the section Showing Uncertainty. 

### Avoid

* Never use three-dimensional (3D) graphics as they distort the visual calculation of volume.

## Additional Recommendations

### Recommended

* Use contrasting color to ensure the wedges stand out. Consider using contrasting outlines to make each wedge stands out.
* Consider not using more than 3-4 wedge pieces. With more wedges, it becomes harder to discern differences. If more are needed, consider using a bar chart.
* Use hash marks or different colors to signify statistical significance.

### Not recommended

* Don’t include large gaps between each wedge, such as in an exploded pie chart. This distorts the perceived sizes of the pie wedges.
* Don’t use multi-level pie charts as they are difficult to decipher. (like those that use consecutive rings, nested doughnut charts)
* Don’t use two or more pie charts to compare against each other. An alternative is to use bar charts.

## Examples

***Example 1.*** Management in U.S. Manufacturing

<img src="{{ '/visualization_type/assets/PieChart1.png' | relative_url }}" alt="Pie chart of key performance indicators in U.S. manufacturing. The slices are 3 to 9 indicators at 47.97 percent, 10 or more indicators at 34.65 percent, no indicators at 9.43 percent, and 1 to 2 indicators at 7.95 percent.">

Source: U.S. Census Bureau, Massachusetts Institute of Technology, National Bureau of Economic Research, and Stanford University; 2015 Management and Organizational Practices Survey (MOPS). Accessed in March 2019.

Notice the following characteristics with this pie chart:

* High contrast colors are used as well as outlines to distinguish the wedges of the pie chart.
* The values being represented in the visualization are written out on top of each wedge, helping the user interpret the differences in the sizes of each wedge.
* An appropriate number of wedges are being displayed for the user to interpret easily.
* A legend is used to define each wedge.

***Example 2:*** Ownership Share of All Businesses By Sex: 2021

<img src="{{ '/visualization_type/assets/PieChart2.png' | relative_url }}" alt="Small pie charts for U.S. states showing the ownership share of all businesses by sex in 2021. Colors stand for female, equally male and female, male, and unclassifiable ownership.">

The interactive chart is <a href="https://www.census.gov/library/visualizations/interactive/ownership-share-of-businesses-by-demographics.html">Ownership Share of All Businesses by Demographics on census.gov</a>.

Take note of the following characteristics of these pie charts:
* A legend is used to define all the wedges of the pie charts.
* On hover of each wedge slice, the value represented by the wedge is displayed along with margins of error which helps to communicate the uncertainty with the estimates being displayed. 

## An accessible example

This example is a part-to-whole chart for Family D. It uses four slices, because this page recommends staying near three or four. The smallest published ways of getting to work are added together in the last slice. The table under the chart lists each of those published numbers on its own.

The picture description states the result. The caption names the chart. The source line starts with "Source: U.S. Census Bureau." The same numbers are in a table that opens from the keyboard.

{% include accessible-figure.html
   id="md-commute"
   src="assets/family-d/md-means-of-transportation.png"
   alt="Pie chart of how workers in Maryland got to work in 2025. 76.4 percent used a car, truck, or van. 13.7 percent worked from home. 5.5 percent used public transportation. 4.4 percent walked, biked, used a taxi or ride-hailing service, rode a motorcycle, or used another means."
   caption="How Maryland workers got to work in 2025. Each slice is a share of workers age 16 and over."
   source_detail="American Community Survey, 2025 1-year estimates, table B08301, Maryland. Workers 16 years and over."
   source_url="https://data.census.gov/table/ACSDT1Y2025.B08301?g=040XX00US24"
   summary="Show the data table"
   table_caption="Means of transportation to work, Maryland, 2025"
   headers="Means of transportation|Workers|Margin of error|Percent of workers"
   rows="Car, truck, or van|2,429,541|±23,333|76.4%||Worked from home|435,692|±12,713|13.7%||Public transportation|174,860|±10,198|5.5%||Walking, taxi or ride-hailing, bicycle, motorcycle, or other means|139,844|±9,931 (calculated)|4.4%||All workers|3,179,937|±21,959|100%"
   note="The four modes add up to all workers. The last mode is the sum of five published estimates, which are listed in the next table. Its margin of error is calculated from those five published margins with the Census Bureau formula for a sum: the square root of the sum of the squared margins. Percents are rounded to one decimal place and add to 100.0. Estimates were saved from data.census.gov on November 8, 2026."
   table_caption_2="Published estimates added together in the last slice"
   headers_2="Means of transportation|Workers|Margin of error|Percent of workers"
   rows_2="Walked|63,419|±5,896|2.0%||Taxi or ride-hailing services|32,438|±6,036|1.0%||Other means|31,032|±4,358|1.0%||Bicycle|8,938|±2,054|0.3%||Motorcycle|4,017|±2,056|0.1%"
%}

## Make this chart again

The program below is saved at `examples/family_d/make_md_commute_chart.py`. It saves the picture used above. It needs Python 3 and the matplotlib package.

To download the live 2025 estimates, request a free Census Data API key at https://api.census.gov/data/key_signup.html and set it in your terminal. Leave the key out of the program, this page, and the saved table:

```
export CENSUS_API_KEY=your_key_here
python3 examples/family_d/make_md_commute_chart.py
```

If `CENSUS_API_KEY` is not set, the program uses the saved file `examples/family_d/md_b08301_means_of_transportation.csv`. Those numbers were copied from the published table on November 8, 2026. The live 2025 values for Maryland match that file: 3,179,937 workers in total, 2,429,541 by car, truck, or van, 174,860 by public transportation, and 435,692 who worked from home.

```python
#!/usr/bin/env python3
"""Draw a part-to-whole chart of how Maryland workers got to work.

The numbers are published Census estimates for American Community Survey
2025 1-year table B08301, Maryland (FIPS 24), workers 16 years and over.
Published table: https://data.census.gov/table/ACSDT1Y2025.B08301?g=040XX00US24

To download the live estimates, set a Census Data API key in the environment.
Do not paste the key into this file:

    export CENSUS_API_KEY=your_key_here
    python3 examples/family_d/make_md_commute_chart.py

If CENSUS_API_KEY is not set, the program uses the saved estimates in
md_b08301_means_of_transportation.csv. Those saved numbers were copied from
the published table on 2026-11-08. The live API values for the total,
car/truck/van, public transportation, and worked from home matched this
file exactly.
"""

from __future__ import annotations

import csv
import json
import math
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "md_b08301_means_of_transportation.csv"
OUT_PATH = HERE.parents[1] / "assets" / "family-d" / "md-means-of-transportation.png"
API_URL = "https://api.census.gov/data/2025/acs/acs1"
STATE_FIPS = "24"

# variable, label, chart group. The total is not given a group.
PUBLISHED_LINES = (
    ("B08301_001", "Total", ""),
    ("B08301_002", "Car, truck, or van", "car"),
    ("B08301_021", "Worked from home", "home"),
    ("B08301_010", "Public transportation", "transit"),
    ("B08301_019", "Walked", "other"),
    ("B08301_016", "Taxi or ride-hailing services", "other"),
    ("B08301_020", "Other means", "other"),
    ("B08301_018", "Bicycle", "other"),
    ("B08301_017", "Motorcycle", "other"),
)

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


def rows_from_api_payload(raw: str):
    """Turn a Census Data API JSON table into the same rows as the CSV."""
    try:
        table = json.loads(raw)
    except json.JSONDecodeError:
        raise SystemExit(
            "The Census Data API did not return a data table. "
            "Check that CENSUS_API_KEY is valid."
        )
    if (
        not isinstance(table, list)
        or len(table) < 2
        or not isinstance(table[0], list)
        or not isinstance(table[1], list)
    ):
        raise SystemExit(
            "The Census Data API returned an unexpected table. "
            "Check that CENSUS_API_KEY is valid."
        )

    by_name = dict(zip(table[0], table[1]))
    if by_name.get("state") != STATE_FIPS:
        raise SystemExit(
            "The Census Data API response did not include Maryland. "
            "Check that CENSUS_API_KEY is valid."
        )

    rows = []
    for code, label, group in PUBLISHED_LINES:
        estimate_name = f"{code}E"
        margin_name = f"{code}M"
        if estimate_name not in by_name or margin_name not in by_name:
            raise SystemExit(f"The Census Data API response is missing {code}.")
        try:
            estimate = str(int(by_name[estimate_name]))
            margin = str(int(by_name[margin_name]))
        except (TypeError, ValueError):
            raise SystemExit(
                f"The Census Data API returned a non-numeric value for {code}."
            )
        rows.append(
            {
                "variable": code,
                "label": label,
                "estimate": estimate,
                "margin_of_error": margin,
                "chart_group": group,
            }
        )
    return rows


def fetch_live_rows(api_key: str):
    """Download B08301 for Maryland. The key is not printed or saved."""
    fields = ["NAME"]
    for code, _label, _group in PUBLISHED_LINES:
        fields.extend((f"{code}E", f"{code}M"))
    params = urllib.parse.urlencode(
        {
            "get": ",".join(fields),
            "for": f"state:{STATE_FIPS}",
            "key": api_key,
        }
    )
    request = urllib.request.Request(
        f"{API_URL}?{params}",
        headers={"User-Agent": "data-viz-guidance family-d example"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise SystemExit(
            f"The Census Data API returned status {error.code}. "
            "Check that CENSUS_API_KEY is valid."
        )
    except urllib.error.URLError:
        raise SystemExit(
            "The Census Data API could not be reached. "
            "Check your network connection."
        )
    return rows_from_api_payload(raw)


def load_rows():
    """Use the live API when a key is set, and the saved CSV otherwise."""
    api_key = os.environ.get("CENSUS_API_KEY", "").strip()
    if not api_key:
        print("No CENSUS_API_KEY set. Using the saved CSV.")
        return read_published_rows(CSV_PATH)
    print(
        "Using live 2025 ACS 1-year estimates for Maryland "
        "from the Census Data API."
    )
    return fetch_live_rows(api_key)


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
        raise SystemExit("The estimates are missing the published total, B08301_001.")

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
    total, slices = build_slices(load_rows())
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
```

## Accessibility checklist

Use this list before publishing a pie chart. More requirements are on the [508 compliance](508.html) page.

* Say what the chart means in the picture description, and include the main numbers.
* Give the chart a caption that says what it is about.
* Start the source line with "Source: U.S. Census Bureau," then name the survey, the year, and the table.
* Put the same numbers in a table with a title and column headings. A reader should be able to open that table with the keyboard.
* Write the name and percent for every slice. Color can help, but it cannot be the only way to tell the slices apart.
* Choose colors that people with color blindness can tell apart, and give text a contrast of at least 4.5 to 1.
* Stay near four slices. In this example the smallest modes are added together, and each published number is still listed in the table.
* Do not use 3D effects or exploded slices. They make the sizes harder to judge.
