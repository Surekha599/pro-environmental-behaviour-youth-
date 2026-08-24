"""
Generate a demo survey dataset: 35 youth students living in Delhi,
of whom 15 are from other states (studying in Delhi) and 20 are Delhi natives.

The survey mirrors survey_template.md (awareness / concern / TPB intention / action).
This is DEMO/dummy data for illustrating the project; replace with real responses
from your Google Form when you collect them.

Run:  python3 generate_survey.py
Outputs: survey_data.csv  +  survey_data_codebook.csv
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)  # seed -> reproducible demo

# ---- Respondent design ---------------------------------------------------
# 20 Delhi natives + 15 from other states studying in Delhi
OTHER_STATES = [
    ("Uttar Pradesh", "UP"), ("Haryana", "HR"), ("Bihar", "BR"),
    ("Punjab", "PB"), ("Rajasthan", "RJ"), ("Madhya Pradesh", "MP"),
    ("West Bengal", "WB"), ("Odisha", "OD"), ("Jharkhand", "JH"),
    ("Uttarakhand", "UK"), ("Assam", "AS"), ("Kerala", "KL"),
    ("Tamil Nadu", "TN"), ("Maharashtra", "MH"), ("Chhattisgarh", "CG"),
]

# Indicative annual average PM2.5 (ug/m3) per state — APPROXIMATE figures from
# recent national reports (CPCB / State of Global Air). Used for the demo join.
STATE_PM25 = {
    "Delhi": 98, "Uttar Pradesh": 88, "Haryana": 82, "Bihar": 80,
    "Punjab": 78, "Rajasthan": 66, "Madhya Pradesh": 58,
    "West Bengal": 60, "Odisha": 54, "Jharkhand": 57, "Uttarakhand": 52,
    "Assam": 45, "Kerala": 38, "Tamil Nadu": 40, "Maharashtra": 46,
    "Chhattisgarh": 62,
}


def pick(scale=5, lo=1, hi=5):
    """Integer response 1..5, slightly left-skewed (people rate high on concern)."""
    v = int(round(rng.normal(3.9, 0.9)))
    return int(min(hi, max(lo, v)))


def action_option(concern, base_p):
    """Action likelihood rises with concern (the real-world signal we want the
    demo to reveal). base_p is the 'Sometimes-or-Yes' tendency at concern=3."""
    p_yes = np.clip(base_p + 0.06 * (concern - 3) + rng.normal(0, 0.05), 0.05, 0.95)
    return "Yes" if rng.random() < p_yes else ("Sometimes" if rng.random() < 0.5 else "No")


rows = []
# ---- Delhi natives -------------------------------------------------------
for i in range(20):
    nid = f"D{i+1:02d}"
    aware, con, urg = pick(), pick(), pick()
    concern = (aware + con + urg) / 3.0
    rows.append(dict(
        respondent_id=nid, age=rng.integers(19, 24), gender=rng.choice(["F", "M"]),
        is_migrant=0, origin_state="Delhi", years_in_delhi="since birth",
        state_pm25=STATE_PM25["Delhi"],
        aware=aware, concern=con, urgent=urg,
        attitude=pick(), norm=pick(), control=pick(), intention=pick(),
        waste=action_option(concern, 0.55), reusable=action_option(concern, 0.5),
        transport=action_option(concern, 0.6), ewaste=action_option(concern, 0.25),
        activity=action_option(concern, 0.45),
    ))

# ---- Migrants from other states studying in Delhi ------------------------
for j, (state, code) in enumerate(OTHER_STATES):
    nid = f"M{j+1:02d}"
    yrs = int(rng.integers(1, 4))
    base = STATE_PM25[state]
    # migrants from higher-pollution home states report slightly higher concern
    boost = 0.2 if base >= 75 else (0.05 if base >= 55 else 0.0)
    aware, con, urg = pick(), pick(), pick()
    concern = np.clip(((aware + con + urg) / 3.0) + boost, 1, 5)
    rows.append(dict(
        respondent_id=nid, age=rng.integers(20, 25), gender=rng.choice(["F", "M"]),
        is_migrant=1, origin_state=state, years_in_delhi=f"{yrs} year(s)",
        state_pm25=base,
        aware=aware, concern=min(5, round(con)), urgent=urg,
        attitude=pick(), norm=pick(), control=pick(), intention=pick(),
        waste=action_option(concern, 0.55), reusable=action_option(concern, 0.5),
        transport=action_option(concern, 0.5), ewaste=action_option(concern, 0.22),
        activity=action_option(concern, 0.4),
    ))

df = pd.DataFrame(rows)

# ---- Derived scores -------------------------------------------------------
def _action_score(row, cols):
    vals = [row[c] for c in cols]
    return sum(1 for v in vals if v == "Yes") + 0.5 * sum(1 for v in vals if v == "Sometimes")

action_cols = ["waste", "reusable", "transport", "ewaste", "activity"]
df["concern"] = df[["aware", "concern", "urgent"]].mean(axis=1).round(2)
df["intention"] = df[["attitude", "norm", "control", "intention"]].mean(axis=1).round(2)
df["action_score"] = df.apply(lambda r: _action_score(r, action_cols), axis=1).round(1)
df["gap"] = (df["intention"] - df["action_score"]).round(2)  # intention-behaviour gap

import os
os.makedirs("data", exist_ok=True)
df.to_csv("data/survey_data.csv", index=False)
print(f"Saved data/survey_data.csv with {len(df)} respondents "
      f"({df.is_migrant.sum()} migrants, {20} Delhi natives)\n")

# ---- Quick summary -------------------------------------------------------
print("=== Group means ===")
print(df.groupby("is_migrant")[["concern", "intention", "action_score", "gap"]].mean().round(2).rename(
    index={0: "Delhi natives (20)", 1: "Migrants from other states (15)"}))
print("\n=== Migrants' origin states ===")
print(df[df.is_migrant == 1][["respondent_id", "origin_state", "years_in_delhi", "state_pm25"]].to_string(index=False))
