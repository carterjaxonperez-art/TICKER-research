# Lab 11 — Tesla Pro-Forma Sensitivity

## Question

Which assumptions drive Tesla's forecast and value, and what explains their effects?

All dollar figures below are **USD millions**, except value per share. The model's cash-flow measure is **FCFE = CFO − capex**. Debt change is zero in every forecast year, so no financing adjustment is needed.

## Inputs, ranges, and locked prediction

**Locked Changed-Input Record — 2026-09-29 13:56:06 -04:00 (before runs)**

| Driver | Base 2026–30 | Lower / higher case | Units and affected years | Range basis | Prediction |
|---|---|---|---|---|---|
| Revenue growth | 5%, 8%, 10%, 10%, 8% | Base minus / plus 2.0 percentage points in every year: 3%, 6%, 8%, 8%, 6% / 7%, 10%, 12%, 12%, 10% | % of prior-year revenue; 2026–30 | Labelled judgment sensitivity range around the Lab 10 recovery path. It represents uncertainty in deliveries, ASP, and energy-storage deployment growth. | Higher growth should raise revenue and operating income. It should also raise FCFE and value, although working-capital and capex needs will make the FCFE change smaller than the operating-profit change. |
| Gross margin, implemented through COGS / revenue | Gross margin: 18.5%, 19.0%, 19.5%, 20.0%, 20.0% | Gross margin minus / plus 2.0 percentage points in every year: 16.5%, 17.0%, 17.5%, 18.0%, 18.0% / 20.5%, 21.0%, 21.5%, 22.0%, 22.0% | % of revenue; 2026–30. The code changes COGS / revenue in the opposite direction. | Labelled judgment sensitivity range around the Lab 10 margin-recovery path. It represents pricing, mix, tariffs, and manufacturing-efficiency uncertainty. | Higher gross margin should raise operating income almost dollar-for-dollar on revenue, then raise FCFE and value. I expect it to be the larger driver over these equal-width ranges. |

The percentage-point shifts are additive; they are not 2% multiplicative changes. For every case, all other independent assumptions are restored to base and the linked statements recalculate.

## Results

| Driver and case | Actual 2026–30 input path | 2030 operating income | Change from base | 2030 FCFE | Change from base | FCFE value/share | Change from base | Accounting checks |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Revenue growth — Lower | 3%, 6%, 8%, 8%, 6% | 8,960 | (876) | 7,487 | (1,326) | $18.94 | ($3.93) | Pass |
| Revenue growth — Base | 5%, 8%, 10%, 10%, 8% | 9,837 | — | 8,813 | — | $22.88 | — | Pass |
| Revenue growth — Higher | 7%, 10%, 12%, 12%, 10% | 10,780 | 944 | 10,284 | 1,471 | $27.21 | $4.34 | Pass |
| Gross margin — Lower | 16.5%, 17.0%, 17.5%, 18.0%, 18.0% | 7,026 | (2,811) | 6,705 | (2,108) | $15.97 | ($6.91) | Pass |
| Gross margin — Base | 18.5%, 19.0%, 19.5%, 20.0%, 20.0% | 9,837 | — | 8,813 | — | $22.88 | — | Pass |
| Gross margin — Higher | 20.5%, 21.0%, 21.5%, 22.0%, 22.0% | 12,647 | 2,811 | 10,921 | 2,108 | $29.79 | $6.91 | Pass |

Signed changes equal changed-case output minus base-case output. The 2030 FCFE figures retain their signs; no negative years were dropped from the valuation calculation.

## Driver ranking over these ranges

| Output | Revenue-growth span | Gross-margin span | Larger driver over these ranges |
|---|---:|---:|---|
| 2030 operating income | $1,820m | $5,621m | Gross margin |
| 2030 FCFE | $2,797m | $4,216m | Gross margin |
| FCFE value per share | $8.27 | $13.82 | Gross margin |

Gross margin is the larger driver **over these ranges**. A margin change affects the profitability of every dollar of revenue directly: lower COGS lifts gross profit, operating income, net income, CFO, FCFE, and then the terminal value. Revenue growth increases sales but also increases revenue-linked working capital, other operating assets, and capex; that is why its FCFE effect is not simply the revenue effect times the base margin.

The ranking is not a claim that margin is inherently more important than demand. It partly reflects the selected ranges: both cases use a 2.0-percentage-point parallel shift, but a wider or narrower range could change the spans and the ranking. A one-at-a-time sensitivity table is also not a forecast probability: it does not attach likelihoods to the inputs or capture drivers moving together.

## Validation and interpretation

The prediction was directionally correct. Gross margin produced the largest span for operating income, FCFE, and value per share, as expected. The notable result is that revenue growth still has a material value range ($18.94 to $27.21 per share) even though growth also pulls cash into linked operating assets and capital spending.

There was no directional prediction error: both cases moved the outputs in the predicted direction, and gross margin was the larger driver as predicted. The magnitude was a model result rather than a pre-run claim; the gross-margin range created a $13.82 per-share span versus $8.27 for revenue growth.

The base case was rerun after all scenarios. It returned 2030 operating income of $9,837m, 2030 FCFE of $8,813m, and FCFE value per share of $22.88—the same as the saved Lab 10 base within rounding. All forecast-year balance checks are zero within the model's $0.5m tolerance.

The sensitivity result does not close the gap between the model's $22.88 base FCFE value and the Lab 10 observed TSLA market price. My next research priority is therefore the gross-margin path: Tesla's automotive pricing, mix, and tariffs, plus the mix and margin of Energy storage. That evidence would most directly test the model's largest driver over the stated ranges.

## Trace of a selected result

In the higher gross-margin case, 2030 gross margin rises from 20.0% to 22.0% because COGS / revenue falls from 80.0% to 78.0%. At the unchanged 2030 base revenue level, that adds about $2,811m to operating income. After tax and linked cash-flow effects, 2030 FCFE increases by $2,108m; the higher explicit FCFE and terminal FCFE increase FCFE value per share from $22.88 to $29.79.

| Selected higher-margin 2030 statement line | Amount ($m) |
|---|---:|
| Revenue | 140,525 |
| COGS | 109,610 |
| R&D / SG&A | 9,837 / 8,432 |
| Operating income | 12,647 |
| Net income / CFO | 9,234 / 20,758 |
| Capex / FCFE | 9,837 / 10,921 |
| Ending cash / balance-sheet check | 50,575 / 0.00 |

## Partner exchange notes — complete in class

- My partner's question about my analysis: **[add exact question]**
- My response or correction: **[add exact response]**
- Check I performed on my partner's analysis: **[add the recomputed difference, independent-input check, and statement trace]**
- Partner check of my analysis: **[add their recomputed difference and any correction]**

Suggested evidence check for my partner: recompute the higher gross-margin value change as $29.79 − $22.88 = **+$6.91 per share**, confirm revenue growth remains 5%, 8%, 10%, 10%, 8%, and trace lower COGS to operating income, FCFE, and value.

## Files and run command

- `lab11_tesla_sensitivity.py` adds the one-at-a-time analysis without modifying the Lab 10 model.
- `lab10_tesla_proforma.py` remains the original base model.

Run this after Python is available on the computer:

```powershell
python lab11_tesla_sensitivity.py
```

If the Windows Python launcher is used instead:

```powershell
py lab11_tesla_sensitivity.py
```
