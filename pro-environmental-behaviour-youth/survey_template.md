# Youth Pro-Environmental Behaviour — Survey Template
### Layer B of the "Understanding Pro-Environmental Behaviour Among the Youth" project
*(Copy/adapt the questions into Google Forms, Qualtrics, or a paper form. Keep this as-part-of a two-layer design: Layer A pollution data ▸ Layer B behaviour data.)*

**Target respondents:** students / young adults, ~15–30 years old.
**Goal:** measure **awareness**, **concern**, **intention**, and **self-reported action** so
you can (a) score each respondent and (b) compare across cities/states/regions that
have different pollution levels (from Layer A).

> Tip: add one field at the top — **City / State** — so you can join Layer B to the
> Layer A pollution values for that location.

---

## Section 1 — Demographics (3 quick items)
1. Age (years): ____
2. Gender: ☐ Male ☐ Female ☐ Other
3. City / State you currently live in: ____

## Section 2 — Awareness & Concern (1–5 scale: 1 = Not at all, 5 = Extremely)
4. How aware are you about air pollution in your city? `1 2 3 4 5`
5. How concerned are you about environmental problems (pollution, climate change, waste)? `1 2 3 4 5`
6. Would you describe climate change as an urgent problem? `1 2 3 4 5`

## Section 3 — Intention (Theory of Planned Behavior, Ajzen 1991)
*This is the heart of the theory. Rate each 1–5 (1 = Strongly disagree, 5 = Strongly agree).*

7. **Attitude:** "I believe acting pro-environmentally is important and worthwhile." `1–5`
8. **Subjective norm:** "People whose opinions matter to me (friends/family) expect me to act environmentally." `1–5`
9. **Perceived behavioural control:** "It is easy for me to make environment-friendly choices in my daily life." `1–5`
10. **Intention:** "I intend to take concrete pro-environmental actions in the next few months." `1–5`

## Section 4 — Self-reported behaviour (Yes / Sometimes / No)
11. Do you segregate (separate) your waste at home?
12. Do you carry a reusable bag / bottle to reduce single-use plastic?
13. Do you prefer public transport, cycling, or walking over private vehicles?
14. Do you recycle or responsibly dispose of e-waste (old phones, batteries, chargers)?
15. Have you participated in any environmental activity (clean-up drive, tree planting, awareness campaign)?

## Section 5 — Open (optional)
16. In 1–2 sentences: what makes it *hard* or *easy* for you to act environment-friendly?

---

## How to score (after you collect the data)
- **Concern score** = mean of items 4–6.
- **TPB intention score** = mean of items 7–10.
- **Action score** = count of "Yes" in items 11–15 (each = 1 point, max 5).
- **Intention–behaviour gap** = intention score − action score (a *big* positive gap =
  they say they care but don't act — a classic finding from the literature!).

Then in Python:
```python
# join to Layer A (pollution) by city, and compare:
#   does concern/intention track city PM2.5?
#   linear regression: Action ~ Concern + Intention + Pollution
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
survey = pd.read_csv("my_survey.csv")     # your data
pollution = pd.read_csv("data_panel.csv") # from analysis.py

merged = survey.merge(pollution, left_on="city", right_on="country")
sns.scatterplot(data=merged, x="PM25", y="concern").set_title("Pollution vs concern")
plt.savefig("concern_vs_pollution.png")
```
