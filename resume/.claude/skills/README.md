# Skills

This directory holds the [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills) that power the job-search workflow in `resume/`. Each subfolder is one skill: a `SKILL.md` written in plain instructions that Claude Code discovers automatically and runs as a slash command (e.g. `/adapt-resume`) when invoked from inside the `resume/` directory.

A skill is not a script — it's a structured prompt. Each `SKILL.md` breaks a task into ordered steps, some of which block for user input, and encodes the judgment calls (tone, framing, what counts as a genuine skill gap) that a plain template can't. Reading any file below both documents the workflow and doubles as a worked example of how to write a skill: frontmatter for name/description/tools, then numbered steps with self-critique checklists before anything gets written to disk.

## Skills in this folder

| Skill | Command | Purpose |
|---|---|---|
| [`adapt-resume`](adapt-resume/SKILL.md) | `/adapt-resume <job-posting-url>` | Fetches a JD, tailors the resume and cover letter to it, outputs a full application package under `applications/` |
| [`render-resume`](render-resume/SKILL.md) | `/render-resume <name>` | Renders the untailored `resume-base.json` into HTML + PDF |
| [`prep-recruiter-call`](prep-recruiter-call/SKILL.md) | `/prep-recruiter-call <application-folder>` | Builds a recruiter-call prep doc: company research, STAR prompts, opening hook |
| [`prep-hiring-manager`](prep-hiring-manager/SKILL.md) | `/prep-hiring-manager <application-folder> <name-or-linkedin>` | Researches the hiring manager and builds a calibrated interview prep doc |
| [`review-applications`](review-applications/SKILL.md) | `/review-applications` | Synthesises patterns across all past applications — what's working, what's failing |

See the top-level [`resume/README.md`](../../README.md) for the full workflow (base resume, profile files, analysis dashboard) these skills operate on.

## How a skill is structured

Every `SKILL.md` here follows the same shape:

```
---
name: skill-name
description: One line — what it does and when it produces output
allowed-tools: <tools this skill is permitted to use>
argument-hint: <what $ARGUMENTS should look like, if any>
---

`$ARGUMENTS` is ... Work through these steps in order.

## Step 1 — ...
## Step 2 — ...
...
## Step Nb — Self-critique pass (MANDATORY before proceeding)
...
## Step N — Report
```

Two conventions worth copying if you're writing a new skill in this style:

- **`[BLOCKING]` steps** — a step that must stop and wait for the user (e.g. `adapt-resume` Step 6, probing for genuine skill gaps before writing anything false to the resume). Mark it explicitly so the agent doesn't barrel through.
- **Self-critique checklists** — a step where the agent re-reads its own draft against a checklist of failure modes (clichés, unsupported claims, tone violations) and fixes them before the file is written. See `adapt-resume` Step 5b or `prep-hiring-manager` Step 5b for the pattern.

## Example: reading a skill end to end

[`prep-recruiter-call/SKILL.md`](prep-recruiter-call/SKILL.md) is a good first one to read — it's self-contained (no dependency on other skills' output), and shows the full arc: locate input → read source files → do sourced web research → analyse → write output → self-critique → report back to the user. `adapt-resume/SKILL.md` is the most complex example, showing how skills can read each other's output (it pulls the opening hook from `recruiter-prep.md` if that skill already ran) and maintain a running "lessons learned" log at the bottom of the file that gets updated after real runs — see its Step 12.

For the broader idea of Claude Code skills beyond this project, see [Anthropic's skills documentation](https://docs.claude.com/en/docs/claude-code/skills) and the [anthropics/skills](https://github.com/anthropics/skills) repository on GitHub for more examples.
