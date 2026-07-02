# Job Descriptions Dataset

A corpus of European analytics engineering job postings, collected for research into whether industry survey claims (primarily dbt Labs' annual State of Analytics Engineering reports) are reflected in actual employer hiring language.

See [`state_of_analytics_engineering/report.md`](state_of_analytics_engineering/report.md) for the full analysis.

---

## Corpus

**132 records** — April to June 2026, primarily European/Berlin market.

### Role type breakdown

| role_type | n | In scope |
|---|---|---|
| analytics_engineering_bi | 116 | Yes — primary cohort |
| team_lead | 7 | Yes — governance signalling stratum |
| data_engineering | 6 | No — excluded from main analysis |
| other | 3 | No — excluded from main analysis |

**Analytical corpus: 123 records** (AE/BI + team_lead). DE and `other` roles are retained in `jd_data/` but excluded from cross-tabulations — they represent a different population and different discourse.

Team lead roles are kept because they are the most likely to contain explicit governance-mandate language ("define testing standards", "establish data culture") — the key signal for whether the 2026 report's governance anxiety has entered hiring language at the decision-making level.

### Geographic concentration

Primarily Berlin/Germany (~27% Berlin specifically, higher including wider DACH), with meaningful Nordics (15 records: Stockholm, Malmö, Helsinki, Oslo, Copenhagen) and UK (14 records) representation, and a smaller France cluster (7 records).

**Known gap:** France remains underrepresented relative to Germany/Nordics/UK. This is the priority geography to expand given the Forward Data Conference context.

> **Note on geographic bucketing:** the `geo_region` field used elsewhere (e.g. the resume-site dashboard) is derived from keyword-matching the free-text `job_location` string — it reflects what got scraped and how that string parses, not real market concentration. Treat regional counts as corpus-coverage information, not a labour-market claim.

---

## Directory structure

```
job_descriptions/
├── jd_data/                          # One subdirectory per JD record
│   └── YYYY-MM-DD_company_role/
│       ├── YYYY-MM-DD_company_role.json   # Structured Layer B classification
│       └── jd.md                          # Full JD text + behavioural analysis
├── state_of_analytics_engineering/
│   └── report.md                     # Cross-reference analysis vs dbt Labs reports
└── README.md
```

---

## Classification schema

Each JSON record captures:

- **Metadata:** `jd_id`, `company`, `role`, `job_location`, `seniority`, `role_type`, `salary_*`, `source_url`
- **Layer B dimensions:**
  - `velocity_vs_rigour` — `rigour` | `mixed` | `velocity`
  - `domain_risk` — `high` | `moderate` | `low`
  - `collaboration_width` — integer (named partner teams)
  - `data_team_maturity` — `early` | `mid` | `mature`
  - `jd_authorship` — `hiring_manager` | `mixed` | `recruiter`
- **Tool flags:** `has_dbt`, `has_spark`, `has_python`, `has_sql`, `has_airflow`, `has_snowflake`, `has_databricks`, `has_bigquery`, `has_looker`, `has_tableau`, `has_power_bi`, `has_soda`, `has_great_expectations`, etc.
- **Evidence:** quoted signal phrases supporting each classification

Classification is performed by `/classify-jd` skill (see `.claude/skills/classify-jd/SKILL.md`).

---

## Key findings (n=123 analytical corpus)

| velocity_vs_rigour | All (n=131) | AE/BI (n=116) |
|---|---|---|
| rigour | 87% | 89% |
| mixed | 12% | 11% |
| velocity | 1% | 0% |

Pure velocity is effectively absent from AE/BI roles. This is the central empirical finding: the governance discourse identified in dbt Labs' 2026 report is already present in European employer hiring language.

> **Note:** [`state_of_analytics_engineering/report.md`](state_of_analytics_engineering/report.md) currently cites n=93 and 84% rigour — it was written against an earlier snapshot and hasn't been re-run against the full 132-record corpus. Treat the numbers above as current; re-run the report's analysis before citing its specific percentages externally (e.g. conference submissions).

---

## Scaling target

To make cross-tabulations statistically defensible for publication:

| Claim | Minimum n |
|---|---|
| Rigour dominates (±10pp CI) | ~100 |
| Rigour × domain_risk cross-tab | ~150 |
| Pattern holds across European markets | ~300 |

Priority expansion: France (+24), Nordics (+23), Germany (+23), UK (+22).
