---
layout: default
title: Treemap
permalink: treemap.html
tags: [Distribution, Comparison]
description: "A treemap shows parts of a whole as nested rectangles sized by value."
---

# Treemap

**Also known as:** Nested rectangle chart

## Purpose and Overview

A treemap visualizes hierarchical data as groups of nested rectangles.

A treemap shares qualities with both network and area diagrams. It gets its name from a tree diagram, which also displays hierarchical data. The key feature of a treemap is that the size of each rectangle represents the value of each category of data, making it possible to convey more information about each category of data in a smaller space.

## When to Use

Treemaps can represent data with a tree-like hierarchical relationship, such as categories of occupations, industries, or budgets. Occupations and industries are classified by a hierarchical structure, with broad groups and subgroups. Organizations spend budgets in a hierarchical structure.

Use a treemap when:

* The data has broad groups that split into smaller subgroups.
* You want to show how each part contributes to the whole and to its group.
* There are too many categories for a pie or donut chart.

## When to Use an Alternative

* Treemaps are not recommended for data types that have a natural order such as age ranges, educational outcomes, chronological data, and regional areas. Presenting these variables in a treemap makes interpretation much more cognitively taxing than if the data appeared in their natural order.
* Avoid treemaps when readers need to compare exact values. Rectangle areas are harder to compare than bar lengths.
* Avoid treemaps when values can be negative, because a rectangle cannot have a negative size.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare values precisely | Bar chart | Lengths on a shared axis are easier to compare than areas. |
| Show ordered categories, such as age ranges | Bar chart or population pyramid | Keeps the natural order of the categories. |
| Show a few parts of one whole | Pie or donut chart | Simpler to read when there are only a few categories. |
| Show change over time | Line chart or stacked area chart | Time is shown along an axis. |
| Show exact values | Table | Readers can read each number directly. |

## Data Requirements and Statistical Considerations

* The data must have a clear hierarchy, with each subgroup belonging to exactly one group.
* Values must be zero or positive, and subgroups must add up to their group total.
* State the measure, units, geographic area, and reference period.
* For survey estimates, report margins of error in a note or data table.
* Explain how missing, suppressed, or combined categories are handled.

## Visualization-Specific Considerations

In addition to the guidance provided in this section, relevant guidance can also be found in the Agency Logo, Colors, Grids, Legends, Source, Titles, and Typography sections.

* Ensure that any text displayed in each rectangle has a sufficient contrast ratio.
* Color can be used to show additional dimensions and should not represent the same information as the size of the rectangle.
* Keep a straight edge on each side of the diagram.
* Don't include patterns or images in each rectangle.
* Adding interactivity allows users to drill into each box to see its components. Interactive versions should still provide a data table.

## Census Data Example

***Example 1:*** Small Area Income and Poverty Estimates, 2022.

![Treemap from the Census Bureau's Small Area Income and Poverty Estimates (2022) showing Supplemental Nutrition Assistance Program (SNAP) participation by county in the Midwest. Each rectangle is a county, grouped by state, such as Ohio, Illinois, Michigan, and Indiana. Rectangle size shows the number of SNAP participants, and shades from light to dark green and blue show the participation rate, from less than 10 percent to more than 40 percent. Large counties such as Cook County, Illinois, and Wayne County, Michigan, have the biggest rectangles.](assets/Treemap.png)

The full visualization can be found at [https://www.census.gov/data-tools/demo/saipe_treemap/saipe_snap_treemap.html](https://www.census.gov/data-tools/demo/saipe_treemap/saipe_snap_treemap.html)

This chart is a good example of the following:

* The contrast ratio between the text and the color on the chart is sufficient. This was checked using the following contrast checker [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)
* This chart also demonstrates a straight edge on each side of the diagrams.
* Color is being used to convey additional information to the reader about participation rate.

## Developer Implementation

A reproducible Python example using U.S. Census Bureau data will be added in a later update.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Using a treemap for ordered categories | Readers lose the natural order, such as youngest to oldest. | Use a bar chart that keeps the order. |
| Color repeats the size | The second encoding adds no information. | Use color for a different measure, or one color per group. |
| Low-contrast text in rectangles | Labels are hard or impossible to read. | Check contrast is at least 4.5: 1. |
| Too many tiny rectangles | Small categories are hard to see or label. | Combine small categories or add a data table. |
| Color as the only way to identify groups | Readers with color blindness cannot match groups. | Add direct labels or a text-based legend. |

## Publication Quality Checklist

- [ ] The visualization fits the analytical question.
- [ ] Relevant alternatives were considered.
- [ ] Data source, geography, reference period, and units are documented.
- [ ] Data transformations and aggregation are appropriate.
- [ ] Missing values and relevant uncertainty are addressed.
- [ ] Existing accessibility, scaling, and axes guidance has been followed.
- [ ] Chart-specific limitations and caveats are explained.
- [ ] Code examples have been executed and verified.
- [ ] The visualization has undergone the appropriate review.

