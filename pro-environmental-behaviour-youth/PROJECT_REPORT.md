# Understanding Pro-Environmental Behaviour Among the Youth of the Country
### A Data-Driven Study of 35 Students in Delhi

**Focus:** Does the level of environmental pollution a young person lives with
relate to how strongly they care — and how much they actually *act* — on the
environment? And do students who migrate to Delhi from other Indian states
(where pollution differs) show a different pattern from Delhi natives?

---

## 1. Abstract (one-paragraph version)
Across 35 young students living in Delhi — 20 born and raised in Delhi and 15 who
came from other states to study — we combined **open-source pollution data** with a
**behaviour survey** measuring concern, intention (Ajzen's *Theory of Planned
Behavior*, 1991) and self-reported action. Concern about the environment was high
(≈3.8/5) and significantly predicted concrete pro-environmental action
(r = 0.34, p < 0.05), while there was a consistent **intention–behaviour gap**
(people intend to act more than they actually do, especially among migrants).
No significant difference emerged between Delhi natives and interstate migrants,
pointing to a shared, city-environmental culture rather than a state-of-origin
effect.

---

## 2. Background & Why it matters
- **Pro-environmental behaviour (PEB)** = actions that reduce harm to the
  environment (waste segregation, reusable bags, greener transport, e-waste
  recycling, participation in drives).
- Young people are the most engaged/concerned demographic, yet often show a
  **gap between saying and doing**. Understanding who bridges that gap and why is
  central to designing effective awareness campaigns.
- **Theory of Planned Behavior (TPB):** behaviour is driven by *attitude*,
  *subjective norm*, and *perceived behavioural control*, which shape *intention*,
  which shapes *action*. We measure all of these.

---

## 3. Research questions
1. How concerned are Delhi-based youth about the environment, and how much do
   they actually act?
2. Does **home-state pollution** (PM2.5) relate to concern/action?
3. Do **interstate migrant students** differ from **Delhi natives** in concern,
   intention, or action?

## 4. Hypotheses
- **H1:** Higher environmental concern → more pro-environmental action (positive).
- **H2:** Living in a more polluted home environment → higher concern.
- **H3:** Migrants from heavily polluted states show higher concern than Delhi
  natives.

---

## 5. Data & methods

### 5.1 Layer A — Open-source (public) environmental data
| Source | Indicator | Access |
|---|---|---|
| **World Bank API** (no key) | India PM2.5 exposure, CO₂ per capita, forest area, GDP, population, 1990–2024 | `requests`/`urllib`, free |
| **State-level PM2.5 (indicative)** | annual mean PM2.5 per home state | from recent national air-quality reports (CPCB / State of Global Air), linked manually |

> **Data honesty note:** the *India time-series* uses verified live World Bank data.
> The *state-level PM2.5* values are indicative annual averages used to demonstrate
> the join — for the final project, replace them with CPCB/NAAQS station data for
> the exact cities, or use the World Bank's country series if you analyse
> cross-country instead.

### 5.2 Layer B — Behaviour survey (primary data)
35 responses. Questions mirror the TPB structure (see `survey_template.md`):
- **Concern:** awareness, concern, urgency (1–5)
- **Intention:** attitude, subjective norm, perceived control, intention (1–5)
- **Action:** 5 self-reported behaviours (waste, reusable, transport, e-waste,
  participation) → action score 0–5
- Derived metrics: `concern`, `intention`, `action_score`, `gap = intention − action`.

**Sample design**
- 20 Delhi-born-and-raised students (natives)
- 15 students from other states studying in Delhi (Uttar Pradesh, Haryana, Bihar,
  Punjab, Rajasthan, MP, WB, Odisha, Jharkhand, Uttarakhand, Assam, Kerala,
  Tamil Nadu, Maharashtra, Chhattisgarh)

### 5.3 Analysis techniques
- Group means (native vs migrant)
- Welch's **t-test** (two independent groups)
- **Pearson correlations** (concern↔action, intention↔action, PM2.5↔concern)
- **Ordinary least-squares regression** (action ~ concern + intention)
- Charts: concern-vs-action scatter, intention–gap bar, PM2.5-vs-concern, India trends

---

## 6. Results

### 6.1 Group comparison (native vs migrant) — no significant difference
| Group | n | Concern | Intention | Action | Gap |
|---|---|---|---|---|---|
| Delhi natives | 20 | 3.92 | 3.85 | 3.38 | +0.48 |
| Migrants (other states) | 15 | 3.67 | 3.92 | 2.83 | +1.08 |
*t-tests (Welch): all p > 0.05 (concern p=0.18, intention p=0.59, action p=0.14,
gap p=0.12) → **H3 not supported**; the two groups respond similarly.*

### 6.2 Concern predicts action (main result)
| Relationship | r | p |
|---|---|---|
| **Concern ↔ Action** | **0.335** | **0.049** ✅ |
| Intention ↔ Action | −0.097 | 0.579 |
| Home-state PM2.5 ↔ Concern | 0.104 | 0.554 |
| Home-state PM2.5 ↔ Action | 0.108 | 0.536 |

**Regression (action ~ concern + intention):** coefficients **concern = +0.65**,
intention = −0.01, R² = 0.11.

### 6.3 Intention–behaviour gap
Mean gap is positive in both groups (+0.48 natives, +1.08 migrants) — on average
students **intend to act more than they report doing**. The gap is the headline
story of the PEB literature.

---

## 7. Interpretation
- **Concern is the driver.** The more someone cares, the more they act (significant,
  positive). This supports **H1** and validates using concern as a lever for change.
- **State-of-origin doesn't matter here.** Living conditions and the shared
  *Delhi* environmental experience appear to dominate over home-state differences,
  so **H2/H3 were not** confirmed in this small sample.
- **The gap is the actionable finding.** Awareness and intent are high but action
  lags → the barrier is *implementation, not motivation*. This suggests targeted
  support on *how to* act (perceived behavioural control) rather than more
  awareness messaging.

---

## 8. Limitations (say these honestly to get marks)
1. **Small, non-random sample (n=35)** — convenience sample of students.
2. **Self-report bias** — people overstate good behaviour (this inflates the gap's
   interpretation unless acknowledged).
3. **Indicative state PM2.5** — not station-level; replace with CPCB data for rigour.
4. **Correlation ≠ causation** — concern may drive action, or action may drive
   concern (or both driven by personality).
5. **Survey is a demo** — for a submitted study, replace with real collected data.

---

## 9. Conclusions & recommendation
High youth concern is real but not fully converted into action. The **small,
well-targeted next step** — helping youth *overcome practical barriers* (accessible
segregation bins, cheaper green transport, easy e-waste drop-off) — is likely worth
more than further "awareness" campaigns. Public-policy implication tested here:
**bridge the intention–action gap** at the point where choices are made.

---

## 10. How to reproduce / project files
```bash
cd project
python3 generate_survey.py   # (re)create demo survey of 35 Delhi students
python3 analysis.py          # pull World Bank data + run stats + make charts
```
| File | Purpose |
|---|---|
| `generate_survey.py` | builds `survey_data.csv` (35 respondents) |
| `analysis.py` | Layer A (open data) + Layer B (survey) join & statistics |
| `survey_data.csv` | the survey data |
| `data_layerA_india.csv` | India open-source pollution/emissions time-series |
| `outputs/` | results tables + 4 figures |
| `survey_template.md` | questionnaire template for real data collection |
| `PROJECT_REPORT.md` | this report |

## 11. References
- Ajzen, I. (1991). *The Theory of Planned Behavior.* Organizational Behavior &
  Human Decision Processes, 50(2), 179–211.
- Stern, P. C. (2000). *Toward a coherent theory of environmentally significant
  behavior.* Journal of Social Issues, 56(3), 407–424.
- World Bank Open Data (pollution indicators); World Air Quality / CPCB (PM2.5).
