"""
Backfill ai_role, testing_framing, and loss_aversion_framing into existing JD records.

Design principles:
- Append-only: never rewrites existing fields in .json or trace files
- Minimal context: prompt is built from existing JSON reasoning fields (compact),
  not from the raw jd_archive.md (large)
- One subprocess per JD: context window is flushed between JDs

Writes to:
  - {jd_id}.json       — three new fields appended via json.dumps of updated dict
  - jd_traces/{jd_id}.md — new section appended at end of file

Usage:
    python3 backfill_three_dimensions.py              # all unclassified JDs
    python3 backfill_three_dimensions.py --dry-run    # preview only
    python3 backfill_three_dimensions.py --limit 5    # first N JDs only
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

JD_DATA_DIR = Path(__file__).parent.parent / "jd_data"
TRACES_DIR = Path(__file__).parent / "jd_traces"

NEW_DIMS = ["ai_role", "testing_framing", "loss_aversion_framing"]

CODEBOOK = """\
You are a structured classifier. Classify three dimensions from the JD signals below.
Output ONLY a valid JSON object — no explanation, no markdown fences, no extra text.

### ai_role
`none` | `ai_user` | `ai_enabler`

What AI skill does the *candidate* need to demonstrate? Company product context is irrelevant.

- **none**: no AI skill expected. Vague phrases ("AI-first mindset") → none. Company builds AI but AE role is standard modelling → none.
- **ai_user**: candidate uses AI coding tools to accelerate their own work. Signals: "AI-assisted coding", "GitHub Copilot", "Claude Code", "Cursor", "proven usage of AI tools in daily work".
- **ai_enabler**: candidate builds data infrastructure AI systems consume. Signals: "AI-ready data foundations", "semantic modelling for AI", "GenAI applications" in responsibilities, "text-to-SQL". If both signals present → ai_enabler.

### testing_framing
`responsibility` | `tool_listed` | `absent`

- **responsibility**: testing/quality/data contracts framed as something the candidate owns. Ownership verbs: "own", "ensure", "define", "implement", "establish" applied to quality or testing practice.
- **tool_listed**: testing tools appear in requirements/stack without ownership framing.
- **absent**: no testing or data quality signal.

### loss_aversion_framing
`none` | `moderate` | `high`

- **none**: delivery and capability framing only.
- **moderate**: operational reliability concern secondary to delivery. Fear is outages. Signals: "first to respond to incidents", "SLOs", "pipeline stability".
- **high**: risk/compliance/trust framing dominates. Fear is bad data reaching decision-makers or regulatory exposure. Signals: "regulatory", "compliance", "audit", repeated quality/trust language in first responsibilities.

Output format (JSON only):
{
  "ai_role": "<none|ai_user|ai_enabler>",
  "ai_role_quote": "<verbatim phrase from JD or 'No AI skill signal.'>",
  "ai_role_explanation": "<one sentence>",
  "testing_framing": "<responsibility|tool_listed|absent>",
  "testing_framing_quote": "<verbatim phrase from JD or 'No testing signal.'>",
  "testing_framing_explanation": "<one sentence>",
  "loss_aversion_framing": "<none|moderate|high>",
  "loss_aversion_framing_quote": "<verbatim phrase from JD or 'No loss aversion framing.'>",
  "loss_aversion_framing_explanation": "<one sentence>"
}

JD SIGNALS:
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


def build_prompt(data: dict) -> str:
    """Build a compact prompt from existing JSON reasoning fields — not raw JD text."""
    ev = data.get("evidence", {})
    parts = [
        f"role: {data.get('role', '')} at {data.get('company', '')}",
        f"velocity_vs_rigour: {data.get('velocity_vs_rigour', '')} — {data.get('velocity_vs_rigour_reasoning', '') or ev.get('velocity_vs_rigour', '')}",
        f"domain_risk: {data.get('domain_risk', '')} — {data.get('domain_risk_reasoning', '') or ev.get('domain_risk', '')}",
        f"data_team_maturity: {data.get('data_team_maturity', '')} — {data.get('data_team_maturity_reasoning', '') or ev.get('data_team_maturity', '')}",
        f"stakeholder_orientation: {data.get('stakeholder_orientation', '')} — {data.get('stakeholder_orientation_reasoning', '') or ev.get('stakeholder_orientation', '')}",
        f"autonomy_level: {data.get('autonomy_level', '')} — {data.get('autonomy_level_reasoning', '') or ev.get('autonomy_level', '')}",
        f"loss_aversion evidence: {ev.get('loss_aversion', '')}",
        f"ats_keywords: {', '.join(ev.get('ats_keywords', []))}",
    ]
    return CODEBOOK + "\n".join(parts)


def classify_jd(data: dict) -> dict | None:
    prompt = build_prompt(data)
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", "claude-haiku-4-5-20251001"],
            capture_output=True, text=True, timeout=60,
        )
    except FileNotFoundError:
        print("ERROR: `claude` CLI not found on PATH", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.strip()
    # Strip markdown fences if present
    if output.startswith("```"):
        output = "\n".join(output.split("\n")[1:])
    if output.endswith("```"):
        output = "\n".join(output.split("\n")[:-1])

    try:
        parsed = json.loads(output)
    except json.JSONDecodeError:
        return None

    for dim, valid in VALID_VALUES.items():
        if parsed.get(dim) not in valid:
            return None

    return parsed


def append_to_json(json_path: Path, result: dict) -> None:
    """Append three new top-level fields to the JSON. All existing fields unchanged."""
    data = json.loads(json_path.read_text())
    for dim in NEW_DIMS:
        data[dim] = result[dim]
        data[f"{dim}_quote"] = result.get(f"{dim}_quote", "")
        data[f"{dim}_explanation"] = result.get(f"{dim}_explanation", "")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def append_to_trace(trace_path: Path, jd_id: str, result: dict) -> None:
    """Append a new section to the end of the trace file."""
    section = f"""
---

## New dimensions — backfill ({', '.join(NEW_DIMS)})

| Dimension | Value |
|-----------|-------|
| ai_role | {result['ai_role']} |
| testing_framing | {result['testing_framing']} |
| loss_aversion_framing | {result['loss_aversion_framing']} |

"""
    for dim in NEW_DIMS:
        quote = result.get(f"{dim}_quote", "")
        explanation = result.get(f"{dim}_explanation", "")
        section += f"### {dim}\n**Value:** `{result[dim]}`\n> {quote}\n> {explanation}\n\n"

    with open(trace_path, "a") as f:
        f.write(section)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    jd_dirs = sorted(p for p in JD_DATA_DIR.iterdir() if p.is_dir())

    todo = []
    for jd_dir in jd_dirs:
        json_path = jd_dir / f"{jd_dir.name}.json"
        if not json_path.exists():
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
        trace_path = TRACES_DIR / f"{jd_id}.md"

        data = json.loads(json_path.read_text())

        print(f"\n── {jd_id}")

        if args.dry_run:
            print(f"   [DRY RUN] would classify")
            n_ok += 1
            continue

        result = classify_jd(data)
        if result is None:
            print(f"   FAIL: invalid or timed-out response")
            n_fail += 1
            continue

        print(f"   ai_role={result['ai_role']}  testing_framing={result['testing_framing']}  loss_aversion_framing={result['loss_aversion_framing']}")

        append_to_json(json_path, result)

        if trace_path.exists():
            append_to_trace(trace_path, jd_id, result)
            print(f"   json + trace appended")
        else:
            print(f"   json appended (no trace file)")

        n_ok += 1

    print(f"\n{'═'*60}")
    mode = "DRY RUN — " if args.dry_run else ""
    print(f"  {mode}classified: {n_ok}")
    print(f"  failed:      {n_fail}")
    print(f"{'═'*60}")


if __name__ == "__main__":
    main()
