# Applications

One folder per job application, created automatically by `/adapt-resume`. Nothing in here is meant to be created by hand — every file is either skill output or a note added during the process.

## Folder naming

`YYYY-MM-DD_company_job-title` — the date is when `/adapt-resume` ran, not when you applied. Company and job title are lowercase, hyphenated slugs derived from the job posting.

## What's inside a folder

Not every file exists in every folder — most only appear once the relevant skill has been run against that application.

| File | Written by | When it appears |
|---|---|---|
| `jd.md` | `/adapt-resume` (Step 3) | Always — the job posting saved verbatim, plus a Layer B behavioural analysis section |
| `{base-name}.json` | `/adapt-resume` (Step 5) | Always — the tailored resume content, source of truth for the HTML/PDF |
| `{base-name}.html` / `.pdf` | `/adapt-resume` (Step 8) | Always — rendered from the JSON, what actually gets sent |
| `{base-name}-cover-letter.md` | `/adapt-resume` (Step 10) | Always |
| `{base-name}-gaps.md` | `/adapt-resume` (Step 6) | Always — genuine skill/experience gaps identified against the JD, and whether the user closed or left each one open |
| `recruiter-prep.md` | `/prep-recruiter-call` | Only if a recruiter call happened |
| `hiring-manager-prep.md` | `/prep-hiring-manager` | Only if a hiring-manager interview happened |
| `notes.md` | You, by hand | Only if you took your own notes during the process (team size, interviewer names, impressions) |
| `rejection_feedback.md` | You, by hand | Only if the company gave explicit rejection feedback — paste it verbatim |

Later-stage prep docs sometimes appear under other names for further interview rounds (e.g. `case-study-2-prep.md`, `vp-engineering-prep.md`, `meet-the-team-prep.md`) — there's no fixed skill for these yet, they're written ad hoc following the same structure as `hiring-manager-prep.md`.

## `notes.md` and `rejection_feedback.md` are the highest-leverage files here

Everything else in a folder is generated. These two are the only inputs that carry real signal about what actually happened in the process — and they're what `/review-applications` and `profile/interview-feedback.md` depend on to find patterns across applications. Add them as soon as you have something to record; a rejection with no feedback captured is a data point lost.

## Cross-application files

| File | Written by | Purpose |
|---|---|---|
| `review-{YYYY-MM-DD}.md` | `/review-applications` | Synthesis across every folder here — systemic rejection themes, stage distribution, what's working, evidence-graded recommendations |

Run `/review-applications` periodically (after a batch of rejections, or every few weeks) rather than after every single one — patterns need 3+ data points to be more than noise.

## Related

- [`../profile/README.md`](../profile/README.md) — the personal source material (`narrative.md`, `values.md`, `star-stories.md`, etc.) that `/adapt-resume` and the prep skills read from
- [`../.claude/skills/README.md`](../.claude/skills/README.md) — how the skills that populate this folder work
- [`../analysis/`](../analysis/) — structured dataset (one record per application, written by `/adapt-resume` Step 11b) feeding the job-market analysis dashboard; this is the quantitative counterpart to the qualitative synthesis in `review-{date}.md`
