---
name: filter-where-the-data-is-read
description: in a dbt model, put each row filter in the import cte that reads the table, name that cte for the rows it keeps, and leave renames and joins to the cte below
metadata:
  type: feedback
---

Filter rows in the import CTE that reads the table, not in a later CTE. An import stays a plain select of raw columns (or `select *`) with a `where` clause. Name it for the rows it keeps: `euro_balances`, `interest_bearing_accounts`, `euro_short_term_rates`, not `balance_report` or `<table>_source`. Renames, joins and calculations go in the derived CTE below, because an alias or a join in an import breaks the bare-import lint rule. Select only the columns used further down, and drop a column that only the import's own `where` reads.

**Why:** asked on an interest-accrual pr: "can the filter not be earlier?" Three filters sat downstream, one in a CTE of its own and two in a join's `where`. That hid what each input was for, and it made the reader check every later CTE to learn which rows survive. With the filters moved up, one CTE disappeared, the join lost its `where`, and each import's name said what it holds.

**How to apply:** when writing or reviewing a model, check every `where` below the imports. If it reads only one import's columns, move it into that import and rename the import for the rows it keeps. Keep in the derived CTE only what can't sit in a bare import: aliases, joins, aggregates and conditions across two inputs. Rerun the linter and the unit tests, and compare the output with the old version on real data. Related: [[pass-only-what-the-code-reads]], [[filter-then-act]], [[full-word-names-in-code]].
