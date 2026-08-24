# 🌍 Understanding Pro-Environmental Behaviour Among the Youth — Delhi Study

A complete, reproducible data project that studies **what drives young people to
act pro-environmentally** by combining **open-source environmental data** (Layer A)
with a **behaviour survey** (Layer B) of **35 students living in Delhi** — 20
Delhi natives and 15 students who moved from other Indian states to study there.

> 📄 Full write-up: [`PROJECT_REPORT.md`](PROJECT_REPORT.md)

---

## The idea

```
Layer A   Pollution & emissions (OPEN WORLD BANK API — no key needed)   ─┐
                                                                         ├─ JOIN
Layer B   Behaviour survey — 35 Delhi students (Theory of Planned Behavior) ─┘
                 └─> concern · intention · action · intention–behaviour gap
```

**Research question:** Does the environmental pollution a young person lives with
relate to how strongly they *care* — and how much they *actually act* — on the
environment? Do interstate migrants differ from Delhi natives?

---

## Key findings

- **Concern predicts action** — `r ≈ 0.34, p ≈ 0.05` (statistically significant).
- **Intention–behaviour gap** — students intend to act more than they report doing
  (positive gap in both groups, larger for migrants).
- **No significant difference** between Delhi natives and interstate migrants
  (all t-tests `p > 0.05`) → shared city experience matters more than home state.
- **Regression** (`action ~ concern + intention`): concern coefficient ≈ **+0.65**, R² ≈ 0.11.

---

## Project structure

```
pro-environmental-behaviour-youth/
├── README.md               ← this file
├── LICENSE                 ← MIT licence
├── requirements.txt        ← Python dependencies
├── .gitignore              ← files to exclude from git
├── .github/workflows/      ← CI: runs the pipeline automatically
├── PROJECT_REPORT.md       ← the full academic report
├── analysis.py             ← pipeline: open data + survey + statistics + charts
├── generate_survey.py      ← builds the demo survey → data/survey_data.csv
├── survey_template.md      ← questionnaire template for real data collection
├── data/
│   ├── survey_data.csv     ← 35-respondent behaviour survey
│   └── data_layerA_india.csv ← India pollution/emissions time-series (1990–2024)
└── outputs/                ← figures + results tables (generated)
```

---

## How to run it

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/pro-environmental-behaviour-youth.git
cd pro-environmental-behaviour-youth
```

### 2. Set up a Python environment (recommended)
Requires **Python 3.9+**. Create an environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate          # Linux/macOS  (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### 3. (Re)generate the demo survey data
```bash
python3 generate_survey.py
```
This writes `data/survey_data.csv` (35 respondents: 20 natives + 15 migrants).

### 4. Run the full analysis
```bash
python3 analysis.py
```
This:
- pulls **live World Bank open data** for India (needs internet),
- joins it with the survey,
- runs t-tests, correlations, and a regression,
- writes figures + result tables into `outputs/`.

### 5. View the results
Open the files in `outputs/` — or the report in `PROJECT_REPORT.md`.

> **To use your own real survey:** export your Google Form responses to CSV,
> replace `data/survey_data.csv`, and re-run `python3 analysis.py`.
> See `survey_template.md` for the questionnaire.

---

## Results files (in `outputs/`)

| File | What it is |
|---|---|
| `fig1_concern_vs_action.png` | Concern vs action, coloured by native/migrant |
| `fig2_intention_gap.png` | Intention–behaviour gap per respondent |
| `fig3_pollution_vs_concern.png` | Home-state PM2.5 vs concern |
| `fig_A_india_trends.png` | India PM2.5 & CO₂ per capita over time (open data) |
| `results_group_means.csv` | Native vs migrant group averages |
| `results_ttest.csv` | Welch's t-test results |
| `results_correlations.csv` | Pearson correlations |
| `results_regression.csv` | OLS regression coefficients |

---

## Data sources & honesty notes

| Layer | Source | Access |
|---|---|---|
| A — India time-series | **World Bank API** | Free, **no key** |
| A — home-state PM2.5 | Indicative annual means (CPCB / State of Global Air) | linked, illustrative |
| B — behaviour survey | This demo dataset (synthetic) | replace with real data |

**Important:** the India pollution time-series is verified, live open data. The
**home-state PM2.5 values are indicative** (demonstrating the join) and the
**survey is synthetic demo data** — swap in **CPCB/NAAQS station data** and your
**real Google Form responses** for a submitted study.

---

## References

- Ajzen, I. (1991). *The Theory of Planned Behavior.* Organizational Behavior
  & Human Decision Processes, 50(2), 179–211.
- Stern, P. C. (2000). *Toward a coherent theory of environmentally significant
  behavior.* Journal of Social Issues, 56(3), 407–424.
- World Bank Open Data (pollution indicators); CPCB / State of Global Air (PM2.5).

---

## License

MIT — see [LICENSE](LICENSE).
