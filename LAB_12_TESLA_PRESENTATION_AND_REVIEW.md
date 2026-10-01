# Lab 12 — Tesla: Presentation and Review Notes

## Current conclusion (start here)

**Conditional conclusion:** The five-year FCFE base case estimates Tesla at **$22.88 per share**, versus a saved **$377.94 TSLA regular-session closing price on September 24, 2026 (4:00 p.m. EDT)**. Both values are in USD per common share and use **3,751 million FY2025 year-end shares**. I therefore cannot support the observed price from the base operating-cash-flow assumptions alone. The conclusion is conditional: Tesla may justify a higher value only if future growth, margins, autonomy/AI economics, or other valuation assumptions are materially stronger than this model assumes.

This is a model-based conclusion, not an instruction to buy, sell, or hold securities.

## Presentation route (15 minutes)

### 1. Target selection — about 2 minutes

I selected Tesla because it has a public, comparable five-year financial history, a full SEC filing record, and a clear operating question: can vehicle-demand recovery and fast-growing Energy storage translate into cash flows sufficient to support its valuation? Tesla is suitable because the business combines a mature, large automotive operation with material uncertainty around new products, AI/autonomy, and energy storage. My initial view was that the company’s market valuation depended on operating outcomes well beyond a simple steady-state auto forecast.

### 2. Company and evidence — about 2 minutes

Tesla earns revenue primarily from automotive sales, energy generation and storage, and services/other activities. All historical financial-statement facts below are in USD millions and cover fiscal years ending December 31.

| Evidence | FY2023 | FY2024 | FY2025 | Why it matters |
|---|---:|---:|---:|---|
| Revenue | 96,773 | 97,690 | 94,827 | Revenue declined 2.9% in 2025, making the model’s recovery path a judgment. |
| Gross profit | 17,660 | 17,450 | 17,094 | Gross margin remained about 18%, making margin recovery a key assumption. |
| Net income | 14,974 | 7,153 | 3,855 | Profit declined sharply, so earnings alone do not explain a high valuation. |
| CFO / capex | 13,256 / 8,899 | 14,923 / 11,339 | 14,747 / 8,527 | Cash conversion and reinvestment matter for FCFE. |

The FY2025 10-K reports that automotive sales declined as cash deliveries fell about 8% and average selling price declined, while energy revenue rose 27% due to Megapack and Powerwall deployments. These are the company-specific facts behind the revenue-growth and margin assumptions.

**Sources to open with my partner:** [Tesla FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm), [Tesla FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828025003063/tsla-20241231.htm), and the saved [TSLA price-history page](https://stockanalysis.com/stocks/tsla/history/). Reporting periods, currency, and source locations are documented in [Lab 10](LAB_10_TESLA_PROFORMA.md).

### 3. Pro-forma — about 3 minutes

The linked 2026–30 statements begin with the FY2025 balance sheet. Revenue growth is 5%, 8%, 10%, 10%, and 8%; gross margin rises gradually from 18.5% to 20.0%. These are judgment assumptions reflecting delivery/ASP uncertainty, Energy-storage growth, and modest cost/mix recovery—not company guidance. R&D stays elevated at 7.5%, 7.5%, then 7.0% of revenue for AI, autonomy, Optimus, and product investment.

FY2026 capex is 21.1% of revenue because Tesla stated 2026 capex should exceed $20bn; it then declines to 7.0% by 2030 as a judgmental normalization. Revenue-linked operating assets and liabilities recalculate each year; cash is calculated last. The model’s accounting check is assets − liabilities − equity, and every base forecast year is zero within the stated $0.5m tolerance. FY2026 FCFE is negative because of the capital-spending assumption; I retain that signed cash flow rather than discard it.

Open: [Lab 10 report](LAB_10_TESLA_PROFORMA.md) and [Tesla pro-forma code](lab10_tesla_proforma.py).

### 4. Valuation — about 3 minutes

The primary valuation is an **FCFE DCF**, not an enterprise-value DCF. It discounts annual FCFE at a 10.0% required return and applies a 3.0% terminal-growth rate to positive FY2030 FCFE. The result is directly an equity value, so it does **not** require an enterprise-to-equity bridge. Debt is held constant; cash is already captured through FCFE and the balance-sheet forecast. The model also prints an FCFF cross-check of $29.85 per share. The $6.97 difference reflects different cash-flow conventions and terminal calculations, so I do not average them.

The valuation date is **September 24, 2026** for the saved market-price comparison; the market observation is the **NASDAQ regular-session close of $377.94 at 4:00 p.m. EDT**, rather than an intraday indication. The valuation uses FY2025 actuals and a FY2026–30 forecast. The market-price comparison is limited because the valuation does not separately model autonomy, robotaxi, Optimus, or a full segment-level Energy-storage forecast.

**Reverse DCF:** Holding COGS, R&D, SG&A, tax, D&A, capex, working-capital ratios, debt change, WACC (10%), terminal growth (3%), and shares fixed, matching the **$377.94 regular-session close** requires a parallel percentage-point increase to every annual revenue-growth assumption. Run the saved [reverse-DCF code](lab12_tesla_reverse_dcf.py) to reproduce the precise bisection result; it holds the stated operating, reinvestment, discount-rate, terminal-growth, and share-count inputs fixed. This is not a literal market forecast; it shows that revenue growth alone cannot reasonably reconcile the price under the held-fixed base assumptions.

**Peer-comparison limitation:** No Tesla peer-multiple analysis or dated peer-market inputs are saved in this workspace. I will not invent a peer target or average it with the DCF. A proper next step is a same-date, same-currency comparison with BYD, GM, Ford, and an Energy-storage-relevant group, using a metric appropriate to each business and explaining why capital structure, segment mix, and earnings quality make multiples differ. This unresolved item limits triangulation but does not invalidate the disclosed FCFE DCF.

### 5. Sensitivity and drivers — about 3 minutes

I changed only one independent input at a time and restored all other assumptions to base. Both paths use parallel ±2.0-percentage-point shifts across 2026–30. Over these stated ranges, gross margin is the largest driver:

| 2030 output span | Revenue growth | Gross margin | Larger driver over these ranges |
|---|---:|---:|---|
| Operating income | $1,820m | $5,621m | Gross margin |
| FCFE | $2,797m | $4,216m | Gross margin |
| FCFE value per share | $8.27 | $13.82 | Gross margin |

For the higher-margin case, COGS falls from 80% to 78% of unchanged 2030 revenue. Operating income rises from $9,837m to $12,647m; FCFE rises from $8,813m to $10,921m; value rises from $22.88 to $29.79 per share. The ranking is conditional on the ranges and is not a forecast probability. Open [Lab 11 sensitivity report](LAB_11_TESLA_SENSITIVITY.md) and [sensitivity code](lab11_tesla_sensitivity.py).

### 6. Interpretation and next evidence — about 2 minutes

I keep the conditional conclusion: the base DCF does not support the saved market price. I would revise it if evidence supports a sustained margin improvement, materially stronger deliveries/ASP and Energy-storage growth, or separately modeled autonomy/AI cash flows. My next research priority is Tesla’s gross-margin path—vehicle pricing, mix, tariffs, manufacturing efficiency, and Energy-storage mix/margin—because gross margin is the largest driver in the stated sensitivity ranges. The peer analysis is the second priority because it is currently unresolved.

## Matthew discussion record — prepare before class; complete during the real discussion

Matthew is the assigned learning partner. The prompts below prepare the required discussion, but the bracketed fields must be replaced with Matthew's real company, answer, source/calculation check, and feedback during class. They are intentionally not fabricated as completed participation.

### Questions I asked my partner

- **Selection and evidence:** [Why this company, and which specific source supports your most important operating claim?]
- **Model and valuation:** [How does your key assumption reach cash flow and value, or why do your valuation methods differ?]
- **Sensitivity and interpretation:** [Does your driver ranking depend on the selected range, and what evidence would change your conclusion?]
- **Follow-up and answer:** [Record the actual follow-up, answer, or unresolved gap.]


### My explanation back and feedback to my partner

- Their valuation conclusion: ** Its auto, Energy, and AI expectations make it a good valuation case. The FY2025 10-K supports the delivery, ASP, and Energy trends.**
- Their main driver and biggest limitation: **Main driver is research and development and biggest limitation is capturing more of the martket. *
- Evidence-backed strength: ****
- Specific improvement: **Sell more model X**

## Matthew's review of my TSLA presentation — complete during the real discussion

- Matthew's question received: **Why use $22.88 instead of $29.85?**
- My answer or a specifically scoped gap: **$22.88 is my FCFE DCF; $29.85 is an FCFF cross-check. They use different cash-flow methods, so I do not average them.**
- What I will keep, revise, or investigate: **Keep the FCFE conclusion and investigate gross-margin evidence and a dated peer comparison.**
- Does the review change my conclusion or research priority? **No change before new evidence: the base model remains below the saved price; gross-margin evidence remains the first priority because it has the largest tested value span.**





## Submission links

- [Source register with page and section citations](TSLA_LAB_12_SOURCE_REGISTER.md)
- [Lab 10 pro-forma report](LAB_10_TESLA_PROFORMA.md)
- [Lab 10 code](lab10_tesla_proforma.py)
- [Lab 11 sensitivity report](LAB_11_TESLA_SENSITIVITY.md)
- [Lab 11 sensitivity code](lab11_tesla_sensitivity.py)
- [Lab 12 reverse DCF](lab12_tesla_reverse_dcf.py)
