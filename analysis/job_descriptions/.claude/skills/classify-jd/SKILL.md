---
name: classify-jd
description: Fetches a job posting URL and produces a structured Layer B classification record (JSON) and a jd.md file. No resume adaptation — classification only. JD data capture and behavioural analysis tool.
allowed-tools: WebFetch Read Write Bash
argument-hint: <job-posting-url>
---

`$ARGUMENTS` is a job posting URL. Produce a structured classification of the JD. No resume adaptation, no cover letter, no tailoring — classification only.

Work through the steps **in order**.

---

## Step 1 — Fetch and extract the JD

Fetch `$ARGUMENTS` with WebFetch. Extract:

- **Company name** (slug: lowercase, hyphens, no punctuation)
- **Job title** (slug form)
- **Location** (as stated in JD header)
- **Salary** (min, max, currency — or null)
- **Date** (today's date, YYYY-MM-DD)
- **Role type**: `analytics_engineering_bi` | `data_engineering` | `team_lead` | `other`
- **Seniority**: `junior` | `mid` | `senior` | `staff` | `lead` | `manager`

Base name: `YYYY-MM-DD_company-slug_job-title-slug`

---

## Step 2 — Layer B classification

Assign values to all seven dimensions from JD language alone — not sector assumptions.

### velocity_vs_rigour
`rigour` | `mixed` | `velocity`

- **rigour**: responsibilities emphasise correctness, quality, governance, testing, compliance, reliability. Signal phrases: "data quality", "testing", "CI/CD", "data contracts", "observability", "compliance", "meticulous", "assertion", "audit", "governance", "reliable", "accuracy".
- **velocity**: responsibilities emphasise speed, shipping, iteration as primary value. Signal phrases: "fast-paced", "move fast", "ship quickly", "MVP", "high velocity", "scrappy", "rapid delivery".
- **mixed**: at least two distinct velocity phrases alongside rigour signals. One "fast-paced" in a rigour-dominated JD → `rigour`.
- Tie-breaker: rigour signals ≥2× velocity → `rigour`. Parity → `mixed`. Velocity ≥2× → `velocity`.

Quote the single most decisive phrase in evidence.

### domain_risk
`high` | `moderate` | `low`

- **high**: errors affect financial reporting, regulatory compliance, or public-facing products at scale. Default-high sectors: fintech, banking, insurance, regulated healthcare. Override signals: "financial reporting", "compliance", "audit", "regulatory", "P&L", "revenue attribution", "mission-critical".
- **moderate**: errors affect business decisions without regulatory/financial consequence. Most e-commerce, SaaS, marketplace, media.
- **low**: limited, recoverable consequences. Education, internal tooling, non-revenue analytics.
- Tie-breaker: sector implies high but JD language is generic → `moderate`. Explicit financial/compliance/regulatory language → `high`.

### collaboration_width
Integer count of distinctly named partner teams/functions.

**Counts**: named functions (Finance, Product, Marketing, Data Science, Engineering, Operations, Legal, Customer Success, Sales, BI team, Data Platform team); named role cohorts ("analysts", "data scientists", "engineers" when a distinct group); named external parties ("clients", "customers" only when explicit collaboration partners).

**Does not count**: "various stakeholders", "the business", "cross-functional teams", "key stakeholders", "colleagues", "non-technical partners"; the role holder's own team.

List each named team verbatim in evidence, semicolon-separated.

### data_team_maturity
`early` | `mid` | `mature`

- **early**: primary mission is to establish the data function; infrastructure does not yet exist. Signals: "first data hire", "build from zero", "greenfield", "wear many hats", "you will define", "establish the foundation".
- **mid**: data function exists and is growing. Signals: named tools in responsibilities (not just requirements), multiple data roles implied, "scale existing", "improve and extend", sub-teams forming.
- **mature**: established, specialised, operating at scale. Signals: multiple named data sub-teams with distinct charters, team size 20+ implied, "join an established team", governance tooling deployed at scale.
- Tie-breaker: tools in requirements only → not a maturity signal. Tools in responsibilities ("maintain our dbt models") → push toward mid/mature.

### jd_authorship
`hiring_manager` | `mixed` | `recruiter`

Focus on the **responsibilities section only**.

- **hiring_manager**: named tools with precise application context, scale/volume numbers, specific methodology names. Reader learns what the job actually involves.
- **recruiter**: generic boilerplate ("collaborate with stakeholders", "drive data quality", "work cross-functionally"). Could apply to any data role.
- **mixed**: some technically precise bullets, some generic. Common in larger companies.
- Tie-breaker: "Could I understand what this person does on a Tuesday morning?" Yes → `hiring_manager`. Mostly specific with a few generic additions → `hiring_manager`, not `mixed`.

### stakeholder_orientation
`commercial` | `product` | `internal_data` | `finance` | `mixed`

- **commercial**: GTM, revenue, sales, customer success, marketing, partnerships. Phrases: "revenue operations", "GTM", "customer success", "pipeline", "win rate", "churn".
- **product**: product, engineering, growth, experimentation. Phrases: "product analytics", "A/B test", "funnel", "feature adoption", "user behaviour", "growth team".
- **internal_data**: data function itself — engineers, analysts, platform consumers. Phrases: "data platform", "self-serve analytics", "data consumers", "modelling layer".
- **finance**: FP&A, controllership, audit, executive reporting. Phrases: "financial reporting", "FP&A", "P&L", "board reporting", "controllership", "audit".
- **mixed**: two or more with genuinely equal weight. Cross-functional framing alone is not enough — assess where responsibilities place the emphasis.

### autonomy_level
`strategic` | `execution` | `mixed`

- **strategic**: role sets direction, defines priorities. Verbs: "define", "establish", "own", "shape", "lead", "drive", "architect". Phrases: "you will define", "shift from reactive to proactive", "set the strategy", "build the roadmap".
- **execution**: role receives scoped work and delivers it. Verbs: "support", "assist", "deliver", "help", "contribute to". Phrases: "you will support the team", "deliver against priorities".
- **mixed**: strategic ownership of a technical domain AND execution in service of a business team.
- Tie-breaker: strategic verbs only in a narrow technical sub-problem while overall framing is support-oriented → `execution`.

---

## Step 3 — Tool and stack extraction

Set `true` if mentioned anywhere in JD (required or preferred), `false` if not.

`has_dbt`, `has_spark`, `has_python`, `has_sql`, `has_airflow`, `has_dagster`, `has_prefect`, `has_snowflake`, `has_databricks`, `has_bigquery`, `has_redshift`, `has_duckdb`, `has_kafka`, `has_terraform`, `has_looker`, `has_tableau`, `has_power_bi`, `has_great_expectations`, `has_soda`

Also extract:
- **urgency**: `urgent` if JD validity ≤30 days, "immediately", "ASAP", "critical hire", or re-post signal. Otherwise `standard`.
- **greenfield_vs_fix**: `greenfield` | `fix_scale` | `mixed` — dominant verb signal across infrastructure tasks.
- **language_gate_type**: `none` | `soft` | `hard` (`hard` = "required"/"fluent"/"C1/C2"/"must speak"; `soft` = "plus"/"nice to have"/"advantage")
- **language_gate_languages**: list of non-English languages named (empty list if none)
- **interview_stages**: integer if stated, null if not
- **ats_platform**: match URL in order — `greenhouse` (greenhouse.io), `lever` (lever.co), `workday` (myworkdayjobs.com), `ashby` (ashbyhq.com), `smartrecruiters` (smartrecruiters.com), `icims` (icims.com), `jobvite` (jobvite.com), `linkedin` (linkedin.com/jobs), `welcometothejungle` (welcometothejungle.com), else `unknown`
- **ats_job_id**: platform-specific job ID from URL (greenhouse: trailing numeric; lever/ashby: UUID; workday: requisition ref after `/job/`; linkedin: numeric; others: most specific path segment or null)

---

## Step 4 — Write output files

Produce a single JSON object and pipe it to `write_jd.py`. The script writes all three output files (`jd_archive.md`, `jd.md`, `{base-name}.json`) in one shot.

```bash
python3 analysis/job_descriptions/write_jd.py <<'EOF'
{
  "jd_id": "{base-name}",
  "jd_text": "{full verbatim JD text}",
  "source_url": "{URL}",
  "company": "{Company name as in JD}",
  "role": "{Job title as in JD}",
  "job_location": "{location}",
  "seniority": "{value}",
  "role_type": "{value}",
  "salary_min": {int or null},
  "salary_max": {int or null},
  "salary_currency": "{EUR|GBP|USD|null}",
  "jd_authorship": "{value}",
  "stakeholder_orientation": "{value}",
  "autonomy_level": "{value}",
  "greenfield_vs_fix": "{value}",
  "velocity_vs_rigour": "{value}",
  "domain_risk": "{value}",
  "collaboration_width": {int},
  "data_team_maturity": "{value}",
  "urgency": "{value}",
  "language_gate_type": "{value}",
  "language_gate_languages": [],
  "interview_stages": {int or null},
  "ats_platform": "{value}",
  "ats_job_id": "{string or null}",
  "has_dbt": true,
  "has_spark": false,
  "has_python": true,
  "has_sql": true,
  "has_airflow": false,
  "has_dagster": false,
  "has_prefect": false,
  "has_snowflake": false,
  "has_databricks": false,
  "has_bigquery": false,
  "has_redshift": false,
  "has_duckdb": false,
  "has_kafka": false,
  "has_terraform": false,
  "has_looker": false,
  "has_tableau": false,
  "has_power_bi": false,
  "has_great_expectations": false,
  "has_soda": false,
  "evidence": {
    "velocity_vs_rigour": "{verbatim quote driving the classification}",
    "velocity_vs_rigour_explanation": "{one sentence explaining the classification, quoting the decisive phrase}",
    "domain_risk": "{verbatim quote driving the classification}",
    "domain_risk_explanation": "{one sentence explaining the classification, quoting the decisive phrase}",
    "collaboration_width": "{semicolon-separated named teams verbatim from JD}",
    "data_team_maturity": "{verbatim quote driving the classification}",
    "data_team_maturity_explanation": "{one sentence explaining the classification, quoting the decisive phrase}",
    "jd_authorship": "{verbatim quote from responsibilities section}",
    "jd_authorship_explanation": "{one sentence explaining the classification, quoting the decisive phrase}",
    "stakeholder_orientation": "{verbatim quote naming primary audience}",
    "stakeholder_orientation_explanation": "{one sentence naming the primary audience, quoting the decisive phrase}",
    "autonomy_level": "{verbatim verb phrase driving the classification}",
    "autonomy_level_explanation": "{one sentence explaining the classification, quoting the decisive verb phrase}",
    "greenfield_vs_fix": "{verbatim quote driving the classification}",
    "greenfield_vs_fix_explanation": "{one sentence}",
    "language_gate": "{verbatim language requirement or 'Not stated in JD'}",
    "urgency": "{verbatim urgency signal — use exact string 'No urgency signals present.' if none}",
    "loss_aversion": "{risk-reduction framing quote with context sentence, or 'No loss aversion framing detected.'}",
    "ats_keywords": ["{8–12 distinctive verbatim phrases likely used as ATS filters}"]
  }
}
EOF
```

---

## Step 5 — Run classifier and rebuild data

```bash
cd analysis/job_descriptions/state_of_analytics_engineering && python3 classify_jds.py
```

The script is incremental — skips already-processed IDs. Writes:
- `jd_traces/{base-name}.md` — 3-run LLM trace
- `llm_classifications.csv` — appended row
- `consistency_report.md` — regenerated

Then rebuild the website dataset:

```bash
cd resume/analysis && python3 build.py
```

This merges the new JSON into `data.json` (loaded by `index.html`) and regenerates `applications_dataset.csv`. If either script fails, note it and continue — the three core files from Step 4 are already written.

---

## Step 6 — Output summary

```
**{Company} — {Job Title}**
Location: {location} | Seniority: {seniority} | Role type: {role_type}

Layer B:
- velocity_vs_rigour: {value} ("{decisive quote}")
- domain_risk: {value} ("{decisive quote}")
- collaboration_width: {int} ({named teams})
- data_team_maturity: {value} ("{decisive quote}")
- jd_authorship: {value} ("{decisive quote}")
- stakeholder_orientation: {value} ("{decisive quote}")
- autonomy_level: {value} ("{decisive quote}")

Stack: {comma-separated true has_* fields}

Files written to jd_data/{base-name}/
```

---

## Notes

- Classification only — not an application tool. Use `adapt-resume` if applying.
- If the URL is inaccessible, ask for pasted JD text and proceed from Step 2.
- For non-standard roles (freelance, internship), complete the classification with best-fit mapping and note anomalies in the evidence field.
