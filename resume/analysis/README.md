# Job Market Analysis

Structured dataset and interactive visualisation of job descriptions, extracted from the `applications/` folder.

---

## Viewing the site

The site reads `data.json` via `fetch()` and must be served over HTTP — opening `index.html` directly from the filesystem will fail.

```bash
cd resume/analysis
python3 -m http.server 8765
open http://localhost:8765

# to stop the server:
lsof -ti :8765 | xargs kill -9
```

---

## Adding a new application to the dataset

When you run `adapt-resume` on a new JD, the skill automatically writes `analysis/records/<application-id>.json` and rebuilds `data.json`. If you need to add a record manually, follow these steps:

### Step 1 — Run adapt-resume as normal

The skill (Step 11b) will write `analysis/records/<base-name>.json` automatically. Skip to Step 3.

### Step 2 — If adding manually: create the record file

Copy an existing record from `records/` as a template:

```bash
cp records/2026-04-08_lego_senior-analytics-engineer.json \
   records/YYYY-MM-DD_company_role.json
```

Fill in every field. Use `null` for fields you cannot determine. The `evidence` object should contain verbatim quotes from the JD — these appear as tooltips on the scatter plot.

Key fields to get right:

| Field | Values | Notes |
|---|---|---|
| `role_type` | `analytics_engineering_bi` / `data_engineering` / `team_lead` / `other` | Drives the filter on the site |
| `velocity_vs_rigour` | `rigour` / `velocity` / `mixed` | Read repeated language: "TDD", "production-grade" = rigour; "bias for action", "iterate" = velocity |
| `domain_risk` | `high` / `moderate` / `low` | High = finance/adtech/regulated; Moderate = product/ops; Low = internal tooling |
| `jd_authorship` | `hiring_manager` / `recruiter` / `mixed` | Named sub-tools, scale numbers, specific patterns = hiring manager |
| `collaboration_width` | integer | Count distinct named teams/functions |
| `data_team_maturity` | `early` / `mid` / `mature` | Solo hire with no team described = early; "lead a team of N" = mature |
| `language_gate_type` | `none` / `soft` / `hard` | Hard = C2/required/fluent; soft = "a plus"/"preferred" |
| `language_gate_languages` | JSON array e.g. `["German"]` | Extract language names; `[]` if none |

### Step 3 — Rebuild the dataset

```bash
cd resume/analysis
python3 build.py
```

This regenerates both `applications_dataset.csv` and `data.json`. The site picks up the new record immediately on next page load.

---

## Updating the schema (adding new fields)

1. Add the field definition to `schema.json` under `"fields"`
2. Add the field key to the `FIELD_ORDER` list in `build.py` (in the correct column position)
3. If it's a tool flag, add it to the `TOOLS` array in `index.html`
4. Re-run `python3 build.py` — old records emit empty/null for the new field automatically
5. Update the `adapt-resume` SKILL.md (Step 11b) so future runs include the new field

---

## Updating the adapt-resume skill

The skill file lives at:

```
resume/.claude/skills/adapt-resume/SKILL.md
```

**To add a new Layer B dimension** (a new psychological lens to read JDs through):

1. Add the dimension to the `### Layer B — Behavioural and cognitive reading` section in Step 1 — describe what to look for and what it signals
2. Add the corresponding output placeholder to the `jd.md` template in Step 3
3. Decide whether to add it as a structured field in the dataset (Step 11b) or keep it prose-only in jd.md

**To add a new structured field to the analysis record** (Step 11b):

1. Add the field to the JSON template in Step 11b of SKILL.md
2. Follow the schema update steps above

**To change the cover letter or resume adaptation logic:**

Steps 5–10 of SKILL.md control the resume adaptation, self-critique, gap probing, and cover letter generation. Each step is self-contained — edit the relevant step directly.

---

## File structure

```
analysis/
  index.html              ← interactive website (serve via HTTP)
  data.json               ← full records with evidence, used by the site
  applications_dataset.csv← flat CSV for pandas/spreadsheet analysis
  build.py                ← merges records/ → data.json + CSV
  schema.json             ← field definitions and valid categorical values
  analyse.py              ← generates static PNG charts (run: python3 analyse.py)
  charts/                 ← static PNG outputs from analyse.py
  records/                ← one JSON file per application
    2026-04-08_lego_senior-analytics-engineer.json
    ...
  evidence/               ← intermediate batch files from evidence extraction agents
    batch1.json ... batch6.json
```

`data.json` and `applications_dataset.csv` are derived outputs — both are safe to regenerate at any time by running `python3 build.py`.
