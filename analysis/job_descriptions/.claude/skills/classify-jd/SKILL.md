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

- **Company name** (slug form: lowercase, hyphens, no punctuation)
- **Job title** (slug form)
- **Location** (as stated in the JD header)
- **Salary** (min, max, currency — or null if not stated)
- **Date** (today's date in YYYY-MM-DD)
- **Role type** — assign one of: `analytics_engineering_bi`, `data_engineering`, `team_lead`, `other`
- **Seniority** — assign one of: `junior`, `mid`, `senior`, `staff`, `lead`, `manager`

Derive the base name: `YYYY-MM-DD_company-slug_job-title-slug`

---

## Step 2 — Layer B classification

Read the JD and assign values to all five structured dimensions. Use the exact decision rules below. Do not use sector assumptions as the sole basis for a classification — derive from JD language.

### velocity_vs_rigour

Values: `rigour` | `mixed` | `velocity`

- **rigour**: The JD's responsibilities section emphasises correctness, quality, governance, testing, compliance, reliability, or data accuracy as core expectations. Signal phrases (quote one verbatim): "data quality", "testing", "CI/CD", "data contracts", "observability", "compliance", "thorough", "meticulous", "assertion", "audit", "governance", "data trust", "reliable", "accuracy", "high-quality data".
- **velocity**: The JD's responsibilities section emphasises speed, shipping, iteration, or delivery pace as its primary value. Signal phrases: "fast-paced", "move fast", "ship quickly", "MVP", "iteration speed", "high velocity", "scrappy", "startup pace", "rapid delivery".
- **mixed**: Assign `mixed` only when velocity signals are genuinely present and substantial — at least two distinct velocity phrases in the responsibilities section alongside rigour signals. A single "fast-paced environment" in a JD otherwise dominated by quality language is not enough for `mixed`. One velocity signal + several rigour signals → `rigour`.
- **Tie-breaker**: Count the rigour signals and velocity signals in the responsibilities section. If rigour signals outnumber velocity signals 2:1 or more → `rigour`. Rough parity → `mixed`. Velocity signals outnumber rigour 2:1 or more → `velocity`.

Quote the single most decisive phrase in the evidence field.

### domain_risk

Values: `high` | `moderate` | `low`

- **high**: Data errors would directly affect financial reporting, regulatory compliance, or public-facing products at scale. Sectors that default to high: fintech, banking, insurance, regulated healthcare. JD override signals: "financial reporting", "compliance", "audit", "regulatory", "P&L", "revenue attribution", "mission-critical".
- **moderate**: Data errors affect business decisions but without immediate regulatory or financial consequences. Most e-commerce, marketplace, SaaS, and media roles. JD signals: "business intelligence", "operational reporting", "stakeholder decisions".
- **low**: Limited, recoverable consequences. Education, internal tooling, non-revenue analytics.
- **Tie-breaker**: Sector implies high risk but JD language is generic → `moderate`. JD explicitly uses financial/compliance/regulatory language → `high`.

Quote the single most decisive phrase in the evidence field.

### collaboration_width

Value: integer (count of distinctly named partner teams/functions)

Count each named team or function that appears in the JD text as a specific, identifiable entity. The test: could a reader identify exactly which team is meant? If yes, count it.

**Counts as 1** (specific, identifiable):
- A named function: "Finance", "Product", "Marketing", "Data Science", "Engineering", "Operations", "Commercial", "Legal", "Customer Success", "Sales", "Analytics", "BI team", "Data Platform team", "Data Engineering team"
- A named role cohort that implies a team: "analysts", "data scientists", "engineers" (when clearly referring to a distinct group, not the role holder themselves)
- A named external party: "clients", "customers" (only if explicitly named as a collaboration partner, not just end users)

**Does NOT count** (too vague to identify):
- "various stakeholders", "the business", "cross-functional teams", "internal teams", "key stakeholders", "relevant teams", "colleagues", "the wider team"
- Vague role descriptions: "non-technical partners", "business users", "decision makers" (no specific team identified)
- The role holder's own team (e.g. "the analytics engineering team" when that is the team being hired into)

**When in doubt**: If you cannot name the specific team from the JD text, do not count it.

In the evidence field, list each named team you counted with the verbatim quote that identifies it, separated by semicolons.

### data_team_maturity

Values: `early` | `mid` | `mature`

- **early**: The primary mission of the role is to establish or build the data function. The data infrastructure does not yet exist in usable form. Signals: "first data hire", "build from zero", "greenfield", "no existing infrastructure", "wear many hats", "you will define", "establish the foundation". Named tools in requirements do NOT override this — a JD can require dbt and still be `early` if the task is to introduce it. The question is: does this role exist because there is no data function yet?
- **mid**: The data function exists and has produced something, but is growing or maturing significantly. Signals: existing named tools already deployed and in use (not just required), multiple data roles implied, "scale existing", "improve and extend", "we've built X, now we need to grow it", sub-teams beginning to form. The question is: does this role exist to grow something that already works?
- **mature**: The data function is established, specialised, and operating at scale. Signals: multiple named data sub-teams each with distinct charters, team size 20+ implied, "join an established team", governance and platform tooling already deployed at scale, role is a specialist within a larger structure. The question is: does this role exist to deepen specialisation within an already-functioning organisation?
- **Tie-breaker**: Named tools in the requirements list signal what the company wants, not what exists. Named tools in the responsibilities section ("you will maintain our dbt models", "you will extend the existing pipeline") signal what already exists → push toward `mid`/`mature`. Named tools only in requirements → do not use as maturity signal.

Quote the single most decisive phrase in the evidence field.

### jd_authorship

Values: `hiring_manager` | `mixed` | `recruiter`

Focus exclusively on the **responsibilities section** (not the requirements list, not the benefits, not the company description). The responsibilities section is where authorship is most diagnostic — it describes what the person will actually do day-to-day.

- **hiring_manager**: The responsibilities section contains technical specificity that could only come from someone who has done this job: named tools with precise application context (e.g. "Unity Catalog governance (schemas, access, metadata tagging)", "optimise dbt incremental models for 1B+ row tables"), specific methodology names, scale/volume numbers, or language that reveals deep knowledge of the role's daily work. The reader learns something specific about what the job actually involves.
- **recruiter**: The responsibilities section is generic — uses boilerplate action verbs ("collaborate with stakeholders", "drive data quality", "work cross-functionally") that could apply to any data role. Tools may be listed but without specific application context. A reader learns very little about what this job actually involves day-to-day.
- **mixed**: The responsibilities section has a mix — some bullets are technically precise (hiring manager input) and others are generic boilerplate (recruiter additions). Common in larger companies where the HM contributes the technical bullets and HR adds standard language around them.
- **Tie-breaker**: Read only the responsibilities section. Ask: "Could I understand what this person will actually do on a Tuesday morning?" If yes → `hiring_manager`. If the responsibilities could apply to any data role → `recruiter`. If some bullets are specific and some are generic → `mixed`. When the responsibilities are mostly specific but have a few generic additions → `hiring_manager` not `mixed`.

**Examples of the hiring_manager/mixed boundary:**
- `hiring_manager`: "Drive Unity Catalog governance (schemas, access, metadata tagging)" + "Build incremental dbt models for terabyte-scale MySQL transfers" + one generic bullet like "collaborate with stakeholders" → `hiring_manager`. The generic bullet doesn't override the specificity of the rest.
- `mixed`: Three technically precise bullets + three generic bullets of roughly equal weight → `mixed`. Neither clearly dominates.
- `recruiter`: "Work with data to drive business decisions", "Collaborate cross-functionally to deliver insights", "Own data quality initiatives" → `recruiter`. Action verbs without any specific technical content.

Quote the single most decisive phrase from the responsibilities section in the evidence field.

---

## Step 3 — Tool and stack extraction

Scan the JD for each of the following. Set `true` if mentioned (required or preferred), `false` if not mentioned. Do not infer from sector or role type.

```
has_dbt, has_spark, has_python, has_sql, has_airflow, has_dagster, has_prefect,
has_snowflake, has_databricks, has_bigquery, has_redshift, has_duckdb,
has_kafka, has_terraform, has_looker, has_tableau, has_power_bi,
has_great_expectations, has_soda
```

Also extract:
- **urgency**: `urgent` if JD validity window ≤30 days, "immediately", "ASAP", "critical hire", or re-post signal. Otherwise `standard`.
- **greenfield_vs_fix**: `greenfield` if primary verbs are build/establish/create applied to infrastructure. `fix_scale` if primary verbs are improve/scale/maintain. `mixed` if both.
- **language_gate_type**: `none` | `soft` | `hard`
  - `hard`: "required", "fluent", "C1/C2", "must speak"
  - `soft`: "plus", "nice to have", "advantage", "preferred"
  - `none`: English only or not mentioned
- **language_gate_languages**: list of non-English languages named in the gate (empty list if none)
- **interview_stages**: integer if stated in JD, null if not
- **ats_platform**: identify the ATS or job board from the URL. Use these rules (match in order):
  - `greenhouse` — URL contains `greenhouse.io` or `boards.greenhouse.io`
  - `lever` — URL contains `lever.co` or `jobs.lever.co`
  - `workday` — URL contains `myworkdayjobs.com` or `wd1.myworkday.com` / `wd3.myworkday.com` etc.
  - `ashby` — URL contains `ashbyhq.com` or `jobs.ashbyhq.com`
  - `smartrecruiters` — URL contains `smartrecruiters.com`
  - `icims` — URL contains `icims.com`
  - `jobvite` — URL contains `jobvite.com`
  - `linkedin` — URL contains `linkedin.com/jobs`
  - `welcometothejungle` — URL contains `welcometothejungle.com`
  - `unknown` — none of the above match
- **ats_job_id**: extract the platform-specific job identifier from the URL so the posting can be retrieved via API later. Rules by platform:
  - `greenhouse`: the numeric ID at the end of the path, e.g. `boards.greenhouse.io/company/jobs/12345678` → `"12345678"`
  - `lever`: the UUID segment, e.g. `jobs.lever.co/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` → `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`
  - `workday`: the job-requisition slug after `/job/`, e.g. `.../job/London/Data-Engineer_R12345` → `"R12345"` (take the trailing alphanumeric ref if present, otherwise the full slug)
  - `ashby`: the UUID segment, e.g. `jobs.ashbyhq.com/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` → `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`
  - `smartrecruiters`: the job ID after `/job/`, e.g. `.../job/COMPANYNAME/123456789` → `"123456789"`
  - `linkedin`: the numeric job ID, e.g. `linkedin.com/jobs/view/1234567890` → `"1234567890"`
  - `welcometothejungle`: the slug after `/jobs/`, e.g. `.../jobs/en-GB/companies/company/roles/job-title_XXXXX` → full slug
  - All others: extract the most specific path segment that looks like a job identifier (numeric ID or UUID), or set `null` if none is identifiable

---

## Step 4 — Create output folder and files

### 4a — Create folder

```bash
mkdir -p "jd_data/{base-name}"
```

### 4b — Write jd_archive.md

Write `jd_data/{base-name}/jd_archive.md` containing the full verbatim JD text as fetched — no analysis, no headers added. This is a raw archive in case the original URL goes down.

### 4c — Write jd.md

Write `jd_data/{base-name}/jd.md` with:

```
# {Job Title} — {Company}

**URL:** {source URL}
**Location:** {location}
**Date Posted:** {date from JD or today}
{**Salary:** min–max currency — only if stated}

---

{Full verbatim JD text — all sections, no summarising or paraphrasing}

---

## Layer B — Behavioural Analysis

**velocity_vs_rigour:** {rigour|mixed|velocity} — {one sentence explaining the classification, quoting the decisive phrase}

**domain_risk:** {high|moderate|low} — {one sentence explaining the classification, quoting the decisive phrase}

**collaboration_width:** {integer} — named teams: {semicolon-separated list, or "none identified"}

**data_team_maturity:** {early|mid|mature} — {one sentence explaining the classification, quoting the decisive phrase}

**jd_authorship:** {hiring_manager|mixed|recruiter} — {one sentence explaining the classification, quoting the decisive phrase}

**greenfield_vs_fix:** {greenfield|fix_scale|mixed} — {one sentence}

**urgency:** {urgent|standard} — {one sentence}

**language_gate:** {none|soft|hard} — {quote exact language requirement phrase, or "Not stated in JD"}

**interview_stages:** {integer or "Not stated in JD"}

**ats_platform:** {greenhouse|lever|workday|ashby|smartrecruiters|icims|jobvite|linkedin|welcometothejungle|unknown}

**ats_job_id:** {extracted job ID or "Not identifiable"}

**loss_aversion:** {Does the JD frame the role in risk-reduction or reliability terms? Quote any specific framing. If absent, say "No loss aversion framing detected."}

**ATS keywords:**
- {verbatim phrase 1}
- {verbatim phrase 2}
- {8–12 distinctive phrases likely used as ATS filters — not generics like "SQL"}
```

### 4d — Write classification JSON

Write `jd_data/{base-name}/{base-name}.json` with this exact structure:

```json
{
  "jd_id": "{base-name}",
  "company": "{Company name as it appears in JD}",
  "role": "{Job title as it appears in JD}",
  "job_location": "{Location as stated in JD}",
  "seniority": "{junior|mid|senior|staff|lead|manager}",
  "role_type": "{analytics_engineering_bi|data_engineering|team_lead|other}",
  "salary_min": {integer or null},
  "salary_max": {integer or null},
  "salary_currency": "{EUR|GBP|USD|etc. or null}",
  "jd_authorship": "{hiring_manager|mixed|recruiter}",
  "greenfield_vs_fix": "{greenfield|fix_scale|mixed}",
  "velocity_vs_rigour": "{velocity|rigour|mixed}",
  "domain_risk": "{high|moderate|low}",
  "collaboration_width": {integer},
  "data_team_maturity": "{early|mid|mature}",
  "urgency": "{standard|urgent}",
  "language_gate_type": "{none|soft|hard}",
  "language_gate_languages": [],
  "interview_stages": {integer or null},
  "ats_platform": "{greenhouse|lever|workday|ashby|smartrecruiters|icims|jobvite|linkedin|welcometothejungle|unknown}",
  "ats_job_id": "{extracted job ID string or null}",
  "has_dbt": {true|false},
  "has_spark": {true|false},
  "has_python": {true|false},
  "has_sql": {true|false},
  "has_airflow": {true|false},
  "has_dagster": {true|false},
  "has_prefect": {true|false},
  "has_snowflake": {true|false},
  "has_databricks": {true|false},
  "has_bigquery": {true|false},
  "has_redshift": {true|false},
  "has_duckdb": {true|false},
  "has_kafka": {true|false},
  "has_terraform": {true|false},
  "has_looker": {true|false},
  "has_tableau": {true|false},
  "has_power_bi": {true|false},
  "has_great_expectations": {true|false},
  "has_soda": {true|false},
  "evidence": {
    "velocity_vs_rigour": "{verbatim quote driving the classification}",
    "domain_risk": "{verbatim quote driving the classification}",
    "collaboration_width": "{semicolon-separated list of named teams counted}",
    "data_team_maturity": "{verbatim quote driving the classification}",
    "jd_authorship": "{verbatim quote driving the classification}",
    "greenfield_vs_fix": "{verbatim quote driving the classification}",
    "language_gate": "{verbatim language requirement quote, or 'Not stated in JD'}",
    "urgency": "{verbatim urgency signal, or 'No urgency signals present'}"
  }
}
```

---

## Step 5 — Output summary to user

Print a short summary:

```
**{Company} — {Job Title}**
Location: {location} | Seniority: {seniority} | Role type: {role_type}

Layer B classification:
- velocity_vs_rigour: {value} ("{decisive quote}")
- domain_risk: {value} ("{decisive quote}")
- collaboration_width: {integer} ({named teams})
- data_team_maturity: {value} ("{decisive quote}")
- jd_authorship: {value} ("{decisive quote}")

Stack: {comma-separated list of has_* fields that are true}

Files written:
- jd_data/{base-name}/jd_archive.md
- jd_data/{base-name}/jd.md
- jd_data/{base-name}/{base-name}.json

Files written to jd_data/{base-name}/
```

---

## Notes

- This skill classifies only — it is a JD data capture and behavioural analysis tool, not an application tracker. It does not adapt a resume, write a cover letter, or produce application output. Use `adapt-resume` for the full application pipeline if you decide to apply.
- JSON records are stored in `jd_data/{base-name}/{base-name}.json` and can be queried directly or loaded into analysis scripts in `state_of_analytics_engineering/`.
- If the JD URL is inaccessible (paywall, login required, 404), ask the user to paste the JD text directly and proceed from Step 2 using the pasted text.
- For roles that don't fit the primary schema well (e.g. freelance, internship, non-data roles), still complete the classification with the best available mapping and note the anomaly in the evidence field.
