"""
Backfill ai_role, testing_framing, and loss_aversion_framing into existing JD records.

Each JD is classified in a fresh subprocess (one `claude -p` call per JD) so that
the main process context window is never loaded with JD text. Results are written
back to the .json and jd.md files.

Usage:
    python3 backfill_three_dimensions.py              # classify all unclassified JDs
    python3 backfill_three_dimensions.py --dry-run    # print what would run, no writes
    python3 backfill_three_dimensions.py --limit 5    # process at most 5 JDs

Requires:
    - `claude` CLI on PATH (Anthropic Claude Code)
    - JD data under analysis/job_descriptions/jd_data/
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

JD_DATA_DIR = Path(__file__).parent.parent / "jd_data"

NEW_DIMS = ["ai_role", "testing_framing", "loss_aversion_framing"]

CODEBOOK = """
You are a structured classifier. Read the job description below and classify three dimensions.
Output ONLY a valid JSON object — no explanation, no markdown fences, no extra text.

---

### ai_role
`none` | `ai_user` | `ai_enabler`

The question is what AI skill the *candidate* is expected to demonstrate. Company product context is irrelevant.

- **none**: no AI skill expected of the candidate. Vague phrases ("AI-first mindset", "interest in AI") → none. Company builds AI but AE role is standard modelling → none.
- **ai_user**: candidate expected to use AI coding tools to accelerate their own work. Signals: "AI-assisted coding", "GitHub Copilot", "Claude Code", "Cursor", "coding agents", "proven usage of AI tools in daily work".
- **ai_enabler**: candidate expected to build data infrastructure that AI systems consume. Signals: "AI-ready data foundations", "data for AI/ML pipelines", "text-to-SQL", "semantic modelling for AI", "GenAI applications" in responsibilities. If both ai_user and ai_enabler signals present → ai_enabler.

### testing_framing
`responsibility` | `tool_listed` | `absent`

- **responsibility**: testing/quality/data contracts framed as something the candidate *owns or defines*. Ownership verbs: "own", "ensure", "define", "implement", "establish". Example: "own the quality of data", "define testing standards", "data contracts" as a named responsibility.
- **tool_listed**: testing tools appear in requirements/stack without ownership framing. "Experience with dbt tests" in a skill list → tool_listed.
- **absent**: no testing or data quality signal.

### loss_aversion_framing
`none` | `moderate` | `high`

- **none**: delivery and capability framing only, no risk register.
- **moderate**: operational reliability concern, secondary to delivery. Fear is outages or data failures. Signals: "first to respond to incidents", "SLOs", "pipeline stability", "production reliability".
- **high**: risk/compliance/trust framing dominates. Fear is bad data reaching decision-makers or regulatory exposure. Signals: "regulatory", "compliance", "audit", "data accuracy has direct business impact", "trustworthiness" as primary role framing, repeated quality/reliability language in first responsibilities.

---

Output format (JSON only, no markdown):
{
  "ai_role": "<none|ai_user|ai_enabler>",
  "ai_role_quote": "<verbatim phrase from JD that drove classification, or 'No AI skill signal.'>",
  "ai_role_explanation": "<one sentence>",
  "testing_framing": "<responsibility|tool_listed|absent>",
  "testing_framing_quote": "<verbatim phrase from JD, or 'No testing signal.'>",
  "testing_framing_explanation": "<one sentence>",
  "loss_aversion_framing": "<none|moderate|high>",
  "loss_aversion_framing_quote": "<verbatim phrase from JD, or 'No loss aversion framing.'>",
  "loss_aversion_framing_explanation": "<one sentence>"
}

---

JOB DESCRIPTION:
"""

VALID_VALUES = {
    "ai_role": {"none", "ai_user", "ai_enabler"},
    "testing_framing": {"responsibility", "tool_listed", "absent"},
    "loss_aversion_framing": {"none", "moderate", "high"},
}


def already_classified(json_path: Path) -> bool:
    try:
        data = json.loads(json_path.read_text())
        return all(dim in data for dim in NEW_DIMS)
    except Exception:
        return False


def classify_jd(jd_text: str) -> dict | None:
    prompt = CODEBOOK + jd_text
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", "claude-haiku-4-5-20251001"],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except FileNotFoundError:
        print("ERROR: `claude` CLI not found on PATH", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.strip()
    # Strip markdown fences if present
    output = re.sub(r"^```(?:json)?\n?", "", output)
    output = re.sub(r"\n?```$", "", output)

    try:
        parsed = json.loads(output)
    except json.JSONDecodeError:
        return None

    # Validate values
    for dim, valid in VALID_VALUES.items():
        if parsed.get(dim) not in valid:
            return None

    return parsed


def patch_json(json_path: Path, result: dict) -> None:
    data = json.loads(json_path.read_text())

    # Insert new dimensions after autonomy_level in top-level object
    new_data = {}
    for k, v in data.items():
        new_data[k] = v
        if k == "autonomy_level":
            for dim in NEW_DIMS:
                new_data[dim] = result[dim]

    # Insert quotes/explanations into evidence
    if "evidence" in new_data and isinstance(new_data["evidence"], dict):
        ev = dict(new_data["evidence"])
        # Append after autonomy_level entries in evidence
        insert_after = "autonomy_level_explanation" if "autonomy_level_explanation" in ev else "autonomy_level"
        new_ev = {}
        for k, v in ev.items():
            new_ev[k] = v
            if k == insert_after:
                for dim in NEW_DIMS:
                    new_ev[dim] = result.get(f"{dim}_quote", "")
                    new_ev[f"{dim}_explanation"] = result.get(f"{dim}_explanation", "")
        new_data["evidence"] = new_ev

    json_path.write_text(json.dumps(new_data, indent=2, ensure_ascii=False) + "\n")


def patch_jd_md(jd_md_path: Path, result: dict) -> None:
    text = jd_md_path.read_text()
    if "**ai_role:**" in text:
        return

    lines = []
    for dim in NEW_DIMS:
        val = result[dim]
        explanation = result.get(f"{dim}_explanation", "")
        lines.append(f"\n**{dim}:** {val} — {explanation}")

    # Insert after **autonomy_level:** block
    pattern = r"(\*\*autonomy_level:\*\*[^\n]*(?:\n(?!\*\*)[^\n]*)*)"
    match = re.search(pattern, text)
    if not match:
        return
    new_text = text[: match.end()] + "".join(lines) + text[match.end() :]
    jd_md_path.write_text(new_text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    jd_dirs = sorted(p for p in JD_DATA_DIR.iterdir() if p.is_dir())

    todo = []
    for jd_dir in jd_dirs:
        json_path = jd_dir / f"{jd_dir.name}.json"
        archive_path = jd_dir / "jd_archive.md"
        if not json_path.exists() or not archive_path.exists():
            continue
        if already_classified(json_path):
            continue
        todo.append(jd_dir)

    print(f"JDs to classify: {len(todo)}")
    if args.limit:
        todo = todo[: args.limit]
        print(f"Limiting to {args.limit}")

    n_ok = 0
    n_fail = 0

    for jd_dir in todo:
        jd_id = jd_dir.name
        json_path = jd_dir / f"{jd_id}.json"
        archive_path = jd_dir / "jd_archive.md"
        jd_md_path = jd_dir / "jd.md"

        jd_text = archive_path.read_text()

        print(f"\n── {jd_id}")

        if args.dry_run:
            print(f"   [DRY RUN] would classify")
            n_ok += 1
            continue

        result = classify_jd(jd_text)
        if result is None:
            print(f"   FAIL: invalid or timed-out response")
            n_fail += 1
            continue

        print(f"   ai_role={result['ai_role']}  testing_framing={result['testing_framing']}  loss_aversion_framing={result['loss_aversion_framing']}")

        patch_json(json_path, result)
        if jd_md_path.exists():
            patch_jd_md(jd_md_path, result)
        print(f"   written")
        n_ok += 1

    print(f"\n{'═'*60}")
    mode = "DRY RUN — " if args.dry_run else ""
    print(f"  {mode}classified: {n_ok}")
    print(f"  failed:      {n_fail}")
    print(f"{'═'*60}")


if __name__ == "__main__":
    main()
