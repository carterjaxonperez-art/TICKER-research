# Eli Lilly DCF Analysis — Lab 04

**Company:** Eli Lilly and Company (NYSE: LLY)  
**Valuation date:** September 10, 2026  
**Most recent confirmed regular-market close:** **$1,124.21 on September 9, 2026, 4:00 p.m. EDT**

## Inputs

All amounts are USD millions except per-share data.

| Input | Value | Status / source |
|---|---:|---|
| Starting FCFF | 18,190.0 | TTM through 6/30/2026: FY2025 FCFF of 8,972.0, less H1 2025 FCFF of 1,546.0, plus H1 2026 FCFF of 10,764.0. FCFF is operating cash flow less capex. |
| Growth, Year 1 | 31.9% | 2026 revenue-guidance midpoint of $86.0B versus FY2025 revenue of $65.179B. |
| Growth, Year 2 | 6.0% | Placeholder: training value retained. |
| Growth, Year 3 | 5.0% | Placeholder: training value retained. |
| Growth, Year 4 | 4.0% | Placeholder: training value retained. |
| Growth, Year 5 | 3.0% | Placeholder: training value retained. |
| WACC | 10.0% | Placeholder: training value retained. |
| Terminal growth | 3.0% | Placeholder: training value retained. |
| Non-operating cash | 8,950.0 | Cash and cash equivalents at 6/30/2026. |
| Debt | 54,908.0 | Short-term borrowings plus long-term debt at 6/30/2026. |
| Diluted shares | 893.7 | Six-month weighted-average diluted shares at 6/30/2026. |

## Base DCF

| Output | Value |
|---|---:|
| Present value of explicit FCFF | $99,622.83 |
| Terminal value at Year 5 | $420,903.37 |
| Present value of terminal value | $261,347.88 |
| Enterprise value | $360,970.71 |
| Equity value | $315,012.71 |
| **Value per diluted share** | **$352.48** |
| Terminal value as a share of enterprise value | 72.40% |

The September 9 close of $1,124.21 is **3.19×** the base DCF value of $352.48, outside the 0.5×–2× reasonableness range. I would distrust the long-run growth path most because Years 2–5 are training placeholders rather than sourced forecasts; I did not adjust them to force a closer valuation.

## Sensitivity Analysis — Value per Diluted Share

| WACC \ terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| 9% | $366.17 | $420.16 | $495.74 |
| 10% | $313.44 | $352.48 | $404.53 |
| 11% | $272.45 | $301.73 | $339.38 |

The base case is the center cell. Value falls as WACC rises and rises as terminal growth rises. The grid’s low and high corners are $272.45 and $495.74, respectively.

## Reverse DCF

Target price: **$1,124.21**. The reverse DCF searches for one uniform shift to all five explicit growth rates, using the prescribed bracket from −5.00 to +10.00 percentage points and holding starting FCFF, the base growth-rate pattern, WACC, terminal growth, cash, debt, and diluted shares fixed.

**Result: no solution in the selected bracket.** A −5.00-point shift produces $277.81 per share and a +10.00-point shift produces $545.74 per share, both below the $1,124.21 target. This is not proof of mispricing; it shows that the stated inputs and allowed reverse-DCF range do not reproduce the market price.

## Conditional Recommendation

**Watch-defer. Initiate if the market price falls below about $704.96, which is 2× my current base DCF value, or if sourced forecasts replace the placeholder Years 2–5 growth path and raise the valuation. Monitor operating cash flow less capital expenditures next quarter, because Lilly expects manufacturing investment and capex to remain meaningfully elevated in the near term.**

## Sources

- [Eli Lilly Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/59478/000005947826000081/lly-20260630.htm)
- [Lilly Q2 2026 guidance](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-second-quarter-2026-financial-results-raises-full)
- [Lilly historic stock lookup](https://investor.lilly.com/node/5921)
