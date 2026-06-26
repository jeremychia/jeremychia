# Job Descriptions Dataset

A corpus of European analytics engineering job postings, collected for research into whether industry survey claims (primarily dbt Labs' annual State of Analytics Engineering reports) are reflected in actual employer hiring language.

See [`state_of_analytics_engineering/report.md`](state_of_analytics_engineering/report.md) for the full analysis.

---

## Corpus

**46 records** — April to June 2026, primarily European/Berlin market.

### Role type breakdown

| role_type | n | In scope |
|---|---|---|
| analytics_engineering_bi | 34 | Yes — primary cohort |
| team_lead | 5 | Yes — governance signalling stratum |
| data_engineering | 4 | No — excluded from main analysis |
| other | 3 | No — excluded from main analysis |

**Analytical corpus: 39 records** (AE/BI + team_lead). DE and `other` roles are retained in `jd_data/` but excluded from cross-tabulations — they represent a different population and different discourse.

Team lead roles are kept because they are the most likely to contain explicit governance-mandate language ("define testing standards", "establish data culture") — the key signal for whether the 2026 report's governance anxiety has entered hiring language at the decision-making level.

### Geographic concentration

Primarily Berlin/Germany (~60%), with Nordics spillover (Stockholm, Malmö, Helsinki, Oslo, Copenhagen) and sparse representation from France, UK, Benelux, and Iberia.

**Known gap:** France is underrepresented (1 record: Decathlon, Lille). This is the priority geography to expand given the Forward Data Conference context.

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

## Key findings (n=39 analytical corpus)

| velocity_vs_rigour | All (n=46) | AE/BI (n=34) |
|---|---|---|
| rigour | 65% | 64% |
| mixed | 30% | 36% |
| velocity | 5% | 0% |

No pure AE/BI role signals velocity. This is the central empirical finding: the governance discourse identified in dbt Labs' 2026 report is already present in European employer hiring language.

---

## Scaling target

To make cross-tabulations statistically defensible for publication:

| Claim | Minimum n |
|---|---|
| Rigour dominates (±10pp CI) | ~100 |
| Rigour × domain_risk cross-tab | ~150 |
| Pattern holds across European markets | ~300 |

Priority expansion: France (+24), Nordics (+23), Germany (+23), UK (+22).
