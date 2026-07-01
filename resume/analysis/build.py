#!/usr/bin/env python3
"""
Merge all records/*.json into applications_dataset.csv and data.json.

Usage:
    python3 build.py

Adding a new field:
    1. Add the field to schema.json
    2. Add it to the FIELD_ORDER list below (in the desired column position)
    3. New records include it; old records will emit an empty cell (null)
    4. Re-run build.py

The script also produces data.json — a flat array of all records with evidence
and role_type included, used by the interactive website (index.html).
"""

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "analysis/job_descriptions/state_of_analytics_engineering"))
from dimensions import DIM_NAMES

RECORDS_DIR = Path(__file__).parent / "records"
JD_DATA_DIR = Path(__file__).parent.parent.parent / "analysis/job_descriptions/jd_data"
SCHEMA_FILE = Path(__file__).parent / "schema.json"
OUTPUT_CSV  = Path(__file__).parent / "applications_dataset.csv"
OUTPUT_JSON = Path(__file__).parent / "data.json"

FIELD_ORDER = [
    "application_id", "company", "role", "job_location", "geo_region", "seniority",
    "role_type",
    "salary_min", "salary_max", "salary_currency",
    "jd_authorship", "stakeholder_orientation", "autonomy_level",
    "greenfield_vs_fix", "velocity_vs_rigour",
    "domain_risk", "collaboration_width", "data_team_maturity", "urgency",
    "language_gate_type", "language_gate_languages", "interview_stages",
    # Core stack
    "has_dbt", "has_spark", "has_python", "has_sql",
    # Orchestration
    "has_airflow", "has_dagster", "has_prefect",
    # Warehouses
    "has_snowflake", "has_databricks", "has_bigquery", "has_redshift", "has_duckdb",
    # Streaming / infra
    "has_kafka", "has_terraform",
    # BI tools
    "has_looker", "has_tableau", "has_power_bi",
    # Data quality
    "has_great_expectations", "has_soda",
]


def derive_geo_region(location: str) -> str:
    """Normalise raw job_location string to a geo_region category."""
    if not location:
        return "other"
    loc = location.lower()
    # Remote-first check before city matching
    if "remote" in loc and not any(c in loc for c in ["berlin", "hamburg", "stockholm", "copenhagen", "amsterdam"]):
        return "global_remote"
    if "berlin" in loc:
        return "berlin"
    if "hamburg" in loc:
        return "hamburg"
    if any(c in loc for c in ["stockholm", "sweden", "copenhagen", "denmark", "oslo", "norway", "helsinki", "finland"]):
        return "nordics"
    if any(c in loc for c in ["united kingdom", "uk", "london", "manchester", "edinburgh"]):
        return "uk_remote"
    if any(c in loc for c in [
        "amsterdam", "netherlands", "paris", "france", "barcelona", "spain",
        "milan", "italy", "zurich", "switzerland", "tallinn", "estonia",
        "europe", "stuttgart", "munich", "münchen", "frankfurt", "cologne",
        "köln", "düsseldorf", "verl", "billund", "lille", "budapest", "hungary",
        "singapore",
    ]):
        return "other_europe"
    return "other"


def load_records():
    records = []
    by_id = {}

    for path in sorted(RECORDS_DIR.glob("*.json")):
        with open(path) as f:
            try:
                record = json.load(f)
            except json.JSONDecodeError as e:
                print(f"ERROR: {path.name} is invalid JSON — {e}", file=sys.stderr)
                sys.exit(1)
        app_id = record.get("application_id") or path.stem
        by_id[app_id] = (path.name, record)

    n_records = len(by_id)
    n_from_jd_data = 0

    # Also load jd_data/ corpus — for IDs already in records/, backfill any
    # new fields (e.g. ai_role) that only exist in the jd_data/ copy.
    if JD_DATA_DIR.exists():
        for folder in sorted(JD_DATA_DIR.iterdir()):
            if not folder.is_dir():
                continue
            app_id = folder.name
            jd_json = folder / f"{app_id}.json"
            if not jd_json.exists():
                continue
            with open(jd_json) as f:
                try:
                    jd_record = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"ERROR: {jd_json.name} is invalid JSON — {e}", file=sys.stderr)
                    continue
            if "jd_id" in jd_record and "application_id" not in jd_record:
                jd_record["application_id"] = jd_record.pop("jd_id")

            if app_id in by_id:
                name, record = by_id[app_id]
                for dim in DIM_NAMES:
                    if dim in jd_record and dim not in record:
                        record[dim] = jd_record[dim]
                        record[f"{dim}_quote"] = jd_record.get(f"{dim}_quote")
                        record[f"{dim}_reasoning"] = jd_record.get(f"{dim}_reasoning")
                by_id[app_id] = (name, record)
            else:
                by_id[app_id] = (jd_json.name, jd_record)
                n_from_jd_data += 1

    records = list(by_id.values())
    print(f"  {n_records} from records/, {n_from_jd_data} from jd_data/")
    return records


def flatten_record(record):
    row = {}
    for field in FIELD_ORDER:
        if field == "geo_region":
            row[field] = derive_geo_region(record.get("job_location", ""))
        elif field == "language_gate_languages":
            value = record.get(field)
            if isinstance(value, list):
                row[field] = ", ".join(value)
            else:
                row[field] = value or ""
        else:
            value = record.get(field)
            row[field] = "" if value is None else value
    return row


def validate_record(name, record, schema_fields):
    valid_categoricals = {
        f["name"]: f["values"]
        for f in schema_fields
        if f["type"] == "categorical"
    }
    warnings = []
    for field, allowed in valid_categoricals.items():
        val = record.get(field)
        if val is not None and val not in allowed:
            warnings.append(f"  {field}: '{val}' not in {allowed}")
    if warnings:
        print(f"WARN {name}:", file=sys.stderr)
        for w in warnings:
            print(w, file=sys.stderr)


def main():
    with open(SCHEMA_FILE) as f:
        schema = json.load(f)
    schema_fields = schema["fields"]

    raw_records = load_records()
    print(f"Found {len(raw_records)} records")

    rows = []
    full_records = []
    for name, record in raw_records:
        validate_record(name, record, schema_fields)
        rows.append(flatten_record(record))
        record["geo_region"] = derive_geo_region(record.get("job_location", ""))
        full_records.append(record)

    # CSV — flat, for spreadsheet/pandas use
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_ORDER)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Written {len(rows)} rows to {OUTPUT_CSV.name}")

    # JSON — full fidelity, for interactive website
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(full_records, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Written {len(full_records)} records to {OUTPUT_JSON.name}")


if __name__ == "__main__":
    main()
