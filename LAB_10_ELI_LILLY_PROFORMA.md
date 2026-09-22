# Lab 10 — Eli Lilly five-year base case

Run `py lab10_eli_lilly_proforma.py` in an environment with Python installed. The file uses $ millions, forecasts FY2026–FY2030, prints the three-statement outputs, confirms every balance check is zero (within rounding), and produces one DCF value per diluted share.

## Historical record

| $ millions except per-share data | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Revenue | 34,124 | 45,043 | 65,179 |
| Net income | 5,240 | 10,590 | 20,640 |
| Cash from operations | 4,240 | 8,818 | 16,813 |
| Capex | 3,448 | 5,058 | 7,841 |

FY2025 ending cash was $7,268m, total debt was $42,503m, and diluted shares were 899.3m. The model uses 894m shares for its FY2026 value, consistent with management’s 2026 guidance assumption.

## Assumptions and labels

All individual assumptions are coded in `A`, with a `history`, `guidance`, or `judgment` label and reason. The key base-case choices are:

| Driver | FY2026 | FY2027–30 | Label / reason |
|---|---:|---:|---|
| Revenue growth | 31.9% | 25%, 18%, 14%, 10% | 2026 is guidance midpoint of $86bn; later years are judgmental deceleration. |
| Performance margin components | COGS 14.5%, R&D 17%, SG&A 19% | COGS 15%, R&D 17%, SG&A 19% | FY2026 aligns to the company’s 49.0%–50.5% performance-margin guidance; later years are judgment. |
| Tax rate | 18.5% | 20.0% | 2026 guidance midpoint, then normalized judgment. |
| D&A / capex | 2.5% / 9.0% of revenue | same | D&A begins with FY2025 history; capex is a judgment that capacity investment moderates from FY2025. |
| WACC / terminal growth | 8.5% / 3.0% | — | valuation judgment. |

The company-specific driver is **Mounjaro/Zepbound volume and realized price**. The 2026 revenue outlook rests on that demand; price/rebate pressure is the central downside risk. The model expresses it through revenue growth and keeps working-capital ratios tied to revenue so the balance sheet and cash flow respond together.

## Base-case output

Using the stated assumptions, the base case produces an enterprise value of about **$786.2bn**, equity value of about **$758.6bn**, and **$848.57 per diluted share**. This is a model output, not a price target or investment recommendation. Its largest sensitivity is the post-2026 growth path for the incretin franchise.

## Review prompts

1. Is the 25% FY2027 revenue-growth judgment defensible after pricing/rebate pressure, international rollout, and competing therapies?
2. Does treating non-PPE noncurrent assets as revenue-linked investment overstate reinvestment after the manufacturing build-out?
3. Change one driver, rerun the model, and confirm the balance check remains zero. A value printed after a failed balance check is invalid by design.

## Sources

- [Lilly FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/59478/000005947826000013/lly-20251231.htm), statements and FY2025 balance sheet; it also contains FY2023–FY2024 comparative income and cash-flow figures.
- [Lilly FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/59478/000005947825000067/lly-20241231.htm), FY2023 comparative balance sheet.
- [Lilly FY2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/59478/000005947824000065/lly-20231231.htm), historical product and operating disclosures.
- [Lilly Q2 2026 earnings release and updated guidance](https://investor.lilly.com/static-files/1ce8d384-21b5-45a4-bafb-b981dc2d5e04), $85bn–$87bn revenue, 49.0%–50.5% performance margin, and 18%–19% tax-rate guidance.
