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

RECORDS_DIR = Path(__file__).parent / "records"
SCHEMA_FILE = Path(__file__).parent / "schema.json"
OUTPUT_CSV  = Path(__file__).parent / "applications_dataset.csv"
OUTPUT_JSON = Path(__file__).parent / "data.json"

FIELD_ORDER = [
    "application_id", "company", "role", "job_location", "seniority",
    "role_type",
    "salary_min", "salary_max", "salary_currency",
    "jd_authorship", "greenfield_vs_fix", "velocity_vs_rigour",
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


def load_records():
    records = []
    for path in sorted(RECORDS_DIR.glob("*.json")):
        with open(path) as f:
            try:
                record = json.load(f)
            except json.JSONDecodeError as e:
                print(f"ERROR: {path.name} is invalid JSON — {e}", file=sys.stderr)
                sys.exit(1)
        records.append((path.name, record))
    return records


def flatten_record(record):
    row = {}
    for field in FIELD_ORDER:
        value = record.get(field)
        if field == "language_gate_languages":
            if isinstance(value, list):
                row[field] = ", ".join(value)
            else:
                row[field] = value or ""
        elif value is None:
            row[field] = ""
        else:
            row[field] = value
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
        full_records.append(record)  # keep nested fields (evidence, language_gate_languages) intact

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
