#!/usr/bin/env python3
"""
Psychological analysis of job descriptions across 35 applications.
Produces a set of charts saved to analysis/charts/.
"""

import csv
import os
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

DATA = Path(__file__).parent / "applications_dataset.csv"
OUT  = Path(__file__).parent / "charts"
OUT.mkdir(exist_ok=True)

# ── Palette ────────────────────────────────────────────────────────────────────
C = {
    "rigour":       "#2C3E50",
    "mixed":        "#7F8C8D",
    "velocity":     "#E74C3C",
    "high":         "#C0392B",
    "moderate":     "#E67E22",
    "low":          "#27AE60",
    "hiring_manager":"#2980B9",
    "recruiter":    "#E74C3C",
    "greenfield":   "#27AE60",
    "fix_scale":    "#2980B9",
    "hard":         "#C0392B",
    "soft":         "#E67E22",
    "none":         "#95A5A6",
    "early":        "#E74C3C",
    "mid":          "#E67E22",
    "mature":       "#27AE60",
    "urgent":       "#C0392B",
    "standard":     "#95A5A6",
    "accent":       "#2C3E50",
    "bg":           "#FAFAFA",
}

SENIORITY_ORDER = ["junior", "mid", "senior", "staff", "lead", "manager"]

def load():
    rows = []
    with open(DATA) as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

def b(row, col):
    """Return bool for a has_* column."""
    return row[col].strip().lower() == "true"

def fig_style(fig, ax_or_axes):
    fig.patch.set_facecolor(C["bg"])
    axes = ax_or_axes if isinstance(ax_or_axes, (list, np.ndarray)) else [ax_or_axes]
    for ax in np.array(axes).flatten():
        ax.set_facecolor(C["bg"])
        ax.spines[["top","right"]].set_visible(False)
        ax.tick_params(labelsize=9)

def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor=C["bg"])
    plt.close(fig)
    print(f"  saved {name}")

# ── 1. What the market fears: rigour vs velocity ───────────────────────────────
def chart_fear_of_failure(rows):
    counts = Counter(r["velocity_vs_rigour"] for r in rows)
    labels = ["rigour", "mixed", "velocity"]
    vals   = [counts.get(l, 0) for l in labels]
    colors = [C[l] for l in labels]

    fig, ax = plt.subplots(figsize=(6, 4))
    fig_style(fig, ax)
    bars = ax.barh(labels, vals, color=colors, height=0.5)
    ax.bar_label(bars, padding=4, fontsize=10, color=C["accent"])
    ax.set_xlabel("Number of roles", fontsize=9)
    ax.set_title(
        "The market is terrified of failure\nRigour vs. velocity orientation across 35 JDs",
        fontsize=12, fontweight="bold", pad=12
    )
    ax.axvline(len(rows)/2, color="#BDC3C7", lw=1, ls="--")
    ax.text(len(rows)/2 + 0.3, 2.4, "50%", fontsize=8, color="#BDC3C7")
    fig.text(0.12, -0.04,
        "Rigour dominates overwhelmingly. Only 2/35 JDs signal a velocity culture.\n"
        "Companies write JDs to protect against their worst fear — bad data in production.",
        fontsize=8, color="#555")
    save(fig, "01_fear_of_failure.png")

# ── 2. Who is hiring? Authorship signal ───────────────────────────────────────
def chart_authorship(rows):
    counts = Counter(r["jd_authorship"] for r in rows)
    labels = ["hiring_manager", "mixed", "recruiter"]
    vals   = [counts.get(l, 0) for l in labels]
    colors = [C[l] for l in labels]
    display= ["Hiring manager", "Mixed", "Recruiter"]

    fig, ax = plt.subplots(figsize=(6, 4))
    fig_style(fig, ax)
    wedges, texts, autotexts = ax.pie(
        vals, labels=display, colors=colors,
        autopct="%1.0f%%", startangle=140,
        textprops={"fontsize": 10},
        wedgeprops={"linewidth": 1.5, "edgecolor": "white"}
    )
    for at in autotexts:
        at.set_fontsize(9)
        at.set_color("white")
        at.set_fontweight("bold")
    ax.set_title(
        "Most JDs are written by engineers, not recruiters\nJD authorship signal",
        fontsize=12, fontweight="bold", pad=16
    )
    fig.text(0.1, -0.02,
        "54% show clear technical depth (named sub-tools, scale numbers, specific patterns).\n"
        "Implication: generic applications get filtered at the first technical screen.",
        fontsize=8, color="#555")
    save(fig, "02_authorship.png")

# ── 3. Domain risk distribution ───────────────────────────────────────────────
def chart_domain_risk(rows):
    counts = Counter(r["domain_risk"] for r in rows)
    labels = ["high", "moderate", "low"]
    vals   = [counts.get(l, 0) for l in labels]
    colors = [C[l] for l in labels]

    fig, ax = plt.subplots(figsize=(6, 4))
    fig_style(fig, ax)
    bars = ax.bar(labels, vals, color=colors, width=0.5)
    ax.bar_label(bars, padding=4, fontsize=11, color=C["accent"])
    ax.set_ylabel("Number of roles", fontsize=9)
    ax.set_title(
        "Stakes are high — errors have real-world consequences\nDomain risk across 35 JDs",
        fontsize=12, fontweight="bold", pad=12
    )
    fig.text(0.12, -0.04,
        "High risk = finance, adtech, mobility (P&L or operational consequences).\n"
        "Only 4 roles are truly low-stakes. The market hires for accountability.",
        fontsize=8, color="#555")
    save(fig, "03_domain_risk.png")

# ── 4. Language gate — the hidden barrier ─────────────────────────────────────
def chart_language_gate(rows):
    gate_counts = Counter(r["language_gate_type"] for r in rows)

    # Which languages appear as hard gates (excluding English-only hard gates)?
    hard_non_english = []
    for r in rows:
        if r["language_gate_type"] == "hard":
            langs = [l.strip() for l in r["language_gate_languages"].split(",") if l.strip()]
            non_en = [l for l in langs if l.lower() != "english"]
            hard_non_english.extend(non_en)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    fig_style(fig, axes)

    # Left: gate type distribution
    labels = ["none", "soft", "hard"]
    vals = [gate_counts.get(l, 0) for l in labels]
    colors = [C[l] for l in labels]
    bars = axes[0].bar(labels, vals, color=colors, width=0.45)
    axes[0].bar_label(bars, padding=4, fontsize=11, color=C["accent"])
    axes[0].set_title("Language gate frequency", fontsize=10, fontweight="bold")
    axes[0].set_ylabel("Roles", fontsize=9)

    # Right: hard non-English language breakdown
    if hard_non_english:
        lang_counts = Counter(hard_non_english)
        l_labels = list(lang_counts.keys())
        l_vals   = [lang_counts[l] for l in l_labels]
        bar_colors = ["#C0392B" if l == "German" else "#E67E22" if l == "Estonian" else "#7F8C8D"
                      for l in l_labels]
        bars2 = axes[1].bar(l_labels, l_vals, color=bar_colors, width=0.4)
        axes[1].bar_label(bars2, padding=4, fontsize=11, color=C["accent"])
        axes[1].set_title("Hard non-English gates (by language)", fontsize=10, fontweight="bold")
        axes[1].set_ylabel("Roles", fontsize=9)
    else:
        axes[1].text(0.5, 0.5, "No hard non-English gates", ha="center", va="center")

    fig.suptitle(
        "Language gates: 3 roles are structurally inaccessible",
        fontsize=12, fontweight="bold", y=1.02
    )
    fig.text(0.1, -0.06,
        "German C2 (Polyteia), Estonian (Helmes), German (The Quality Group) are hard disqualifiers.\n"
        "4 'hard English' gates are non-issues. 23/35 roles have no gate at all.",
        fontsize=8, color="#555")
    save(fig, "04_language_gate.png")

# ── 5. Tool prevalence — what the market actually requires ────────────────────
def chart_tools(rows):
    tools = {
        "SQL":        "has_sql",
        "dbt":        "has_dbt",
        "Python":     "has_python",
        "Snowflake":  "has_snowflake",
        "Airflow":    "has_airflow",
        "Looker":     "has_looker",
        "Tableau":    "has_tableau",
        "Spark":      "has_spark",
        "Power BI":   "has_power_bi",
        "Databricks": "has_databricks",
        "Kafka":      "has_kafka",
        "Terraform":  "has_terraform",
        "Dagster":    "has_dagster",
        "Prefect":    "has_prefect",
        "BigQuery":   "has_bigquery",
        "Redshift":   "has_redshift",
    }
    n = len(rows)
    counts = {label: sum(1 for r in rows if b(r, col)) for label, col in tools.items()}
    sorted_tools = sorted(counts.items(), key=lambda x: -x[1])
    labels = [t[0] for t in sorted_tools]
    vals   = [t[1] for t in sorted_tools]
    pcts   = [v / n * 100 for v in vals]

    # Colour by group
    groups = {
        "SQL": "core", "dbt": "core", "Python": "core",
        "Snowflake": "warehouse", "Databricks": "warehouse", "BigQuery": "warehouse", "Redshift": "warehouse",
        "Airflow": "orchestration", "Dagster": "orchestration", "Prefect": "orchestration",
        "Looker": "bi", "Tableau": "bi", "Power BI": "bi",
        "Spark": "compute", "Kafka": "streaming", "Terraform": "infra",
    }
    group_colors = {
        "core": "#2C3E50", "warehouse": "#2980B9", "orchestration": "#8E44AD",
        "bi": "#16A085", "compute": "#D35400", "streaming": "#C0392B", "infra": "#7F8C8D"
    }
    colors = [group_colors[groups.get(l, "core")] for l in labels]

    fig, ax = plt.subplots(figsize=(8, 6))
    fig_style(fig, ax)
    bars = ax.barh(labels[::-1], pcts[::-1], color=colors[::-1], height=0.6)
    ax.bar_label(bars, fmt="%.0f%%", padding=4, fontsize=8, color=C["accent"])
    ax.set_xlabel("% of JDs mentioning this tool", fontsize=9)
    ax.axvline(50, color="#BDC3C7", lw=1, ls="--")
    ax.text(51, 0.3, "50%", fontsize=8, color="#BDC3C7")
    ax.set_title(
        "dbt + SQL is the de facto standard; everything else is optional\nTool prevalence across 35 JDs",
        fontsize=12, fontweight="bold", pad=12
    )

    legend_patches = [
        mpatches.Patch(color=c, label=g.capitalize())
        for g, c in group_colors.items()
    ]
    ax.legend(handles=legend_patches, loc="lower right", fontsize=8, framealpha=0.5)
    fig.text(0.12, -0.03,
        "SQL (94%) and dbt (69%) define the floor. Snowflake, Airflow, and BI tools form the second tier.\n"
        "Dagster, Prefect, BigQuery, Redshift: rare enough to be differentiators, not requirements.",
        fontsize=8, color="#555")
    save(fig, "05_tool_prevalence.png")

# ── 6. Collaboration width vs domain risk — the stress matrix ─────────────────
def chart_stress_matrix(rows):
    risk_map  = {"high": 3, "moderate": 2, "low": 1}
    risk_color= {"high": C["high"], "moderate": C["moderate"], "low": C["low"]}

    widths = []
    risks  = []
    colors = []
    labels = []
    for r in rows:
        try:
            w = int(r["collaboration_width"])
        except (ValueError, TypeError):
            continue
        risk = r["domain_risk"]
        widths.append(w)
        risks.append(risk_map.get(risk, 0) + np.random.uniform(-0.12, 0.12))
        colors.append(risk_color.get(risk, "#ccc"))
        labels.append(r["company"])

    fig, ax = plt.subplots(figsize=(8, 5))
    fig_style(fig, ax)
    ax.scatter(widths, risks, c=colors, s=80, alpha=0.8, edgecolors="white", linewidths=0.8)

    for i, label in enumerate(labels):
        ax.annotate(label, (widths[i], risks[i]), fontsize=6.5, alpha=0.75,
                    xytext=(4, 3), textcoords="offset points")

    ax.set_xlabel("Collaboration width (named partner teams)", fontsize=9)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["Low risk", "Moderate risk", "High risk"], fontsize=9)
    ax.set_title(
        "Wide collaboration + high domain risk = maximum pressure role\nStress matrix: collaboration width × domain risk",
        fontsize=12, fontweight="bold", pad=12
    )

    legend_patches = [
        mpatches.Patch(color=C["high"],     label="High risk"),
        mpatches.Patch(color=C["moderate"], label="Moderate risk"),
        mpatches.Patch(color=C["low"],      label="Low risk"),
    ]
    ax.legend(handles=legend_patches, fontsize=8, loc="upper left", framealpha=0.5)
    fig.text(0.12, -0.04,
        "Top-right quadrant = roles requiring both deep cross-functional coordination and high accountability.\n"
        "Riverty (9 teams, high risk) is the most demanding. Helmes/Scoot (narrow, lower risk) are simpler asks.",
        fontsize=8, color="#555")
    save(fig, "06_stress_matrix.png")

# ── 7. Seniority vs greenfield/fix — what each level is hired to do ──────────
def chart_seniority_mission(rows):
    seniority_present = [s for s in SENIORITY_ORDER if any(r["seniority"] == s for r in rows)]
    mission_types = ["greenfield", "mixed", "fix_scale"]

    data = {}
    for s in seniority_present:
        sub = [r for r in rows if r["seniority"] == s]
        data[s] = {m: sum(1 for r in sub if r["greenfield_vs_fix"] == m) for m in mission_types}

    x = np.arange(len(seniority_present))
    width = 0.25
    fig, ax = plt.subplots(figsize=(9, 5))
    fig_style(fig, ax)

    for i, m in enumerate(mission_types):
        vals = [data[s][m] for s in seniority_present]
        ax.bar(x + i * width, vals, width, label=m.replace("_", "/"),
               color=C[m], alpha=0.88)

    ax.set_xticks(x + width)
    ax.set_xticklabels([s.capitalize() for s in seniority_present], fontsize=10)
    ax.set_ylabel("Number of roles", fontsize=9)
    ax.legend(fontsize=9)
    ax.set_title(
        "Senior ICs are hired to build; leads are hired to stabilise\nMission type by seniority level",
        fontsize=12, fontweight="bold", pad=12
    )
    fig.text(0.12, -0.04,
        "Mid roles split evenly — they inherit ambiguity. Senior roles lean greenfield (build something new).\n"
        "Lead/staff roles lean fix/scale — the assumption is you inherit a mess and make it work.",
        fontsize=8, color="#555")
    save(fig, "07_seniority_mission.png")

# ── 8. Data team maturity vs urgency — who is panicking ─────────────────────
def chart_panic_map(rows):
    maturity_order = ["early", "mid", "mature"]
    urgency_types  = ["urgent", "standard"]

    data = {}
    for m in maturity_order:
        sub = [r for r in rows if r["data_team_maturity"] == m]
        data[m] = {u: sum(1 for r in sub if r["urgency"] == u) for u in urgency_types}

    x = np.arange(len(maturity_order))
    width = 0.35
    fig, ax = plt.subplots(figsize=(7, 4))
    fig_style(fig, ax)

    bars_u = ax.bar(x - width/2, [data[m]["urgent"]   for m in maturity_order],
                    width, label="Urgent", color=C["urgent"], alpha=0.88)
    bars_s = ax.bar(x + width/2, [data[m]["standard"] for m in maturity_order],
                    width, label="Standard", color=C["standard"], alpha=0.88)
    ax.bar_label(bars_u, padding=3, fontsize=9)
    ax.bar_label(bars_s, padding=3, fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(["Early-stage\nteam", "Mid-stage\nteam", "Mature\nteam"], fontsize=9)
    ax.set_ylabel("Roles", fontsize=9)
    ax.legend(fontsize=9)
    ax.set_title(
        "Urgency comes from early-stage teams, not mature ones\nUrgency signal by data team maturity",
        fontsize=12, fontweight="bold", pad=12
    )
    fig.text(0.12, -0.06,
        "Early-stage teams hire urgently because they have no data function yet — every month without one costs them.\n"
        "Mature teams are deliberate; they know what they need and are willing to wait for the right person.",
        fontsize=8, color="#555")
    save(fig, "08_panic_map.png")

# ── 9. Salary distribution by seniority (EUR-only, normalised) ───────────────
def chart_salary(rows):
    eur_rows = [r for r in rows if r["salary_currency"] == "EUR"
                and r["salary_min"] and r["salary_max"]]

    by_seniority = {}
    for r in eur_rows:
        s = r["seniority"]
        mid = (int(r["salary_min"]) + int(r["salary_max"])) / 2
        by_seniority.setdefault(s, []).append(mid)

    present = [s for s in SENIORITY_ORDER if s in by_seniority]

    fig, ax = plt.subplots(figsize=(7, 4))
    fig_style(fig, ax)

    positions = range(len(present))
    bp = ax.boxplot(
        [by_seniority[s] for s in present],
        positions=positions,
        patch_artist=True,
        widths=0.4,
        boxprops=dict(facecolor="#D6EAF8", linewidth=1.2),
        medianprops=dict(color=C["accent"], linewidth=2),
        whiskerprops=dict(linewidth=1),
        capprops=dict(linewidth=1),
        flierprops=dict(marker="o", markersize=5, alpha=0.5),
    )

    for i, s in enumerate(present):
        for v in by_seniority[s]:
            ax.scatter(i, v, color=C["accent"], alpha=0.6, s=40, zorder=5)

    ax.set_xticks(list(positions))
    ax.set_xticklabels([s.capitalize() for s in present], fontsize=10)
    ax.set_ylabel("Midpoint salary (EUR)", fontsize=9)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"€{x/1000:.0f}k"))
    ax.set_title(
        "Salary signal is sparse but the lead/staff premium is real\nEUR salaries by seniority (stated roles only)",
        fontsize=12, fontweight="bold", pad=12
    )
    fig.text(0.12, -0.04,
        f"Only {len(eur_rows)}/35 roles stated EUR salaries. Mid roles show wide variance (€70k–€120k).\n"
        "The absence of stated salary is itself a signal — equity-heavy or negotiation-first cultures.",
        fontsize=8, color="#555")
    save(fig, "09_salary.png")

# ── 10. The JD authorship × rigour heatmap ───────────────────────────────────
def chart_authorship_rigour(rows):
    authorship_order = ["hiring_manager", "mixed", "recruiter"]
    rigour_order     = ["rigour", "mixed", "velocity"]

    grid = np.zeros((len(authorship_order), len(rigour_order)), dtype=int)
    for r in rows:
        a = r["jd_authorship"]
        v = r["velocity_vs_rigour"]
        if a in authorship_order and v in rigour_order:
            i = authorship_order.index(a)
            j = rigour_order.index(v)
            grid[i][j] += 1

    fig, ax = plt.subplots(figsize=(6, 4))
    fig_style(fig, ax)
    im = ax.imshow(grid, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(rigour_order)))
    ax.set_xticklabels(["Rigour", "Mixed", "Velocity"], fontsize=10)
    ax.set_yticks(range(len(authorship_order)))
    ax.set_yticklabels(["Hiring manager", "Mixed", "Recruiter"], fontsize=10)

    for i in range(len(authorship_order)):
        for j in range(len(rigour_order)):
            ax.text(j, i, str(grid[i][j]), ha="center", va="center",
                    fontsize=14, fontweight="bold",
                    color="white" if grid[i][j] > grid.max() * 0.6 else C["accent"])

    ax.set_title(
        "Engineers write rigour-first JDs; recruiters write whatever\nAuthorship × velocity/rigour orientation",
        fontsize=12, fontweight="bold", pad=12
    )
    fig.text(0.12, -0.04,
        "Hiring managers overwhelmingly pair with rigour — they fear bad code in production.\n"
        "Recruiter-written JDs show no consistent orientation — they mirror templates, not values.",
        fontsize=8, color="#555")
    save(fig, "10_authorship_rigour.png")

# ── Run all ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    rows = load()
    print(f"Loaded {len(rows)} records\n")

    chart_fear_of_failure(rows)
    chart_authorship(rows)
    chart_domain_risk(rows)
    chart_language_gate(rows)
    chart_tools(rows)
    chart_stress_matrix(rows)
    chart_seniority_mission(rows)
    chart_panic_map(rows)
    chart_salary(rows)
    chart_authorship_rigour(rows)

    print(f"\nAll charts saved to {OUT}/")
