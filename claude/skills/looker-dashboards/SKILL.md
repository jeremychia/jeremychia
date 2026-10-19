---
name: looker-dashboards
description: Build or change a LookML dashboard so its tiles read as one consistent page. Use when adding, moving or restyling tiles in a .dashboard.lookml file, adding headline single-value tiles, or opening a dashboard pull request that depends on a new measure.
---

# Looker dashboards

## 1. Render headline numbers at one size

- **Never rely on a font-size setting for a single-value tile.** There is none. Looker scales the value to fill its tile, so a shorter number renders larger.
- **Give every headline tile in a row the same width and height.**
- **Give every headline value in a row the same format.** Prefer a compact one, such as millions with one decimal (`value_format: '0.0,,"M"'`), so the values sit close in length.
- **Use one table tile instead when the sizes must match exactly**: a single row, one column per number, with `rows_font_size` and `header_font_size` set.

## 2. Fit every title in its tile

- **Keep a single-value title short enough to fit the tile's width.** A longer title is cut off with an ellipsis.
- **Move the qualifier into the tile note** ("in the selected period", "excluding suspicious users") when the title does not fit.

## 3. Keep the grid consistent

- **Shift every tile below an inserted tile down by the new tile's height.**
- **List each tile's row, col, width and height after any move**, and check that no two tiles overlap and no row exceeds 24 columns.
- **Match the file's existing whitespace.** One blank line between tiles, never two.

## 4. Land the measure before the dashboard

- **Open the dashboard pull request as a draft** while any measure it uses is not yet in the view.
- **Expect LookML validation to fail with "Unknown field"** until the view change merges. A second warning about unpivoted dimensions on the same tiles comes from the unknown field, and clears with it.
- **Update the dashboard branch from main after the view change merges.** That re-runs validation. A pull request that is behind main does not re-run on its own.

## Worked case

Three headline tiles, 4 columns wide each, showed a 9-digit, a 7-digit and a 9-digit count. The 7-digit value rendered visibly larger. The third title, the longest, was cut off with an ellipsis. The fix gave all three tiles `value_format: '0.0,,"M"'`, so they read like 120.4M, 5.9M and 126.3M. A table tile would have matched the sizes exactly.
