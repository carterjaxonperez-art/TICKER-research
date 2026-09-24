# Lab 10 — Tesla (TSLA) five-year base case

## Question and company-specific line

**Question:** What are five years of Tesla’s statements worth, built from assumptions that can be defended?

**Company-specific line:** Tesla’s value is unusually sensitive to vehicle deliveries and average selling price, while energy-storage deployments are growing faster and with higher gross margin. The model reflects that through revenue growth and gradual gross-margin recovery; it does not apply ABG’s floor-plan debt because Tesla has no comparable manufacturer inventory-financing line.

## Filing-sourced history

All values are $ millions. FY2025’s 10-K contains the comparative 2023–2025 income statement and cash-flow statement; its FY2025/FY2024 balance sheet and the FY2024 10-K’s FY2023 balance sheet provide the balance-sheet history.

| Item | 2023 | 2024 | 2025 | Filing location |
|---|---:|---:|---:|---|
| Revenue | 96,773 | 97,690 | 94,827 | FY2025 10-K, Statements of Operations |
| Gross profit | 17,660 | 17,450 | 17,094 | FY2025 10-K, Statements of Operations |
| SG&A | 4,800 | 5,150 | 5,834 | FY2025 10-K, Statements of Operations |
| Net income | 14,974 | 7,153 | 3,855 | FY2025 10-K, Statements of Operations |
| Inventory | 13,626 | 12,017 | 12,392 | FY2024 / FY2025 10-K Balance Sheets |
| PP&E, net | 29,725 | 35,836 | 40,643 | FY2024 / FY2025 10-K Balance Sheets |
| Total equity | 63,367 | 73,617 | 82,807 | FY2025 10-K, Equity statement / Balance Sheet |
| CFO | 13,256 | 14,923 | 14,747 | FY2025 10-K, Cash Flows |
| Capital expenditures | 8,899 | 11,339 | 8,527 | FY2025 10-K, Cash Flows |

## Ratios and operating disclosure

| Ratio / disclosure | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Reported revenue growth | 3.5% | 0.9% | (2.9%) |
| Gross margin | 18.2% | 17.9% | 18.0% |
| SG&A ÷ gross profit | 27.2% | 29.5% | 34.1% |
| Inventory days (inventory ÷ cost of revenue × 365) | 62.9 | 54.7 | 58.2 |
| D&A and impairment ÷ opening PP&E | 15.7% | 18.1% | 17.2% |
| Capex ÷ revenue | 9.2% | 11.6% | 9.0% |
| Effective tax rate | (50.1%) | 20.4% | 27.0% |

Tesla does not report retail-style organic or same-store sales. Its MD&A instead says FY2025 automotive sales declined because cash deliveries fell about 8% and average selling price declined, while energy revenue rose 27% from Megapack and Powerwall deployments. Those disclosures, rather than an ABG floor-plan ratio, are the operating evidence for the forecast.

## Assumptions

The Python file labels every model input as history, guidance, or judgment and includes the reason beside it. Core assumptions are below.

| Assumption | Value | Label | Reason |
|---|---:|---|---|
| Revenue growth, 2026–30 | 5%, 8%, 10%, 10%, 8% | judgment | Modest near-term recovery, followed by energy storage and vehicle-volume growth; Tesla gives no annual revenue guidance. |
| Gross margin, 2026–30 | 18.5%, 19.0%, 19.5%, 20.0%, 20.0% | judgment | Energy mix and manufacturing efficiency offset only part of delivery/ASP pressure. |
| R&D / revenue | 7.5%, 7.5%, 7%, 7%, 7% | judgment | AI, autonomy, Optimus, and product development remain a material cost. |
| SG&A / revenue | 6.0% | history | FY2025 ratio, held constant. |
| Tax rate | 25.0% | judgment | Normalizes volatile FY2023–25 outcomes. |
| D&A / revenue | 6.48% | history | FY2025 D&A, amortization, and impairment ÷ FY2025 revenue. |
| Capex / revenue | 21.1%, 12%, 9%, 8%, 7% | guidance then judgment | Tesla expects FY2026 capex above $20bn; subsequent years assume the build moderates. |
| WACC / terminal growth | 10.0% / 3.0% | judgment | A conservative required return and mature terminal-growth rate. |
| Shares | 3,751m | fact | FY2025 year-end common shares outstanding. |

Cash includes the FY2025 $27.546bn short-term-investment balance because those investments are highly liquid. Tesla does not draw a revolver in this forecast; cash remains above zero after the modeled FY2026 AI-related capex increase.

## Valuation and check

Run:

```powershell
python lab10_tesla_proforma.py
```

The model prints five years of statements and a balance check of zero in every year. The base case produces approximately **$29.85 per share**. This is a mechanical output, not a recommendation; it is heavily affected by the FY2026 capex guidance and the assumed post-2026 margin/volume recovery.

TSLA was about **$377.33 intraday on September 24, 2026** when checked. On the same 3.751bn year-end share count, the model says about $29.85 while the market says about $377.33; the question is whether the market’s implied autonomy, AI, and future-margin expectations can be supported by future operating cash flow.

For the required refusal check, run:

```powershell
python lab10_tesla_proforma.py --break-2026-cash
```

It intentionally types the FY2025 cash balance into FY2026 and must stop before valuation with a balance-sheet error.

## Partner review — complete in class

**Attack to give a partner:** Why does revenue growth rise to 10% after FY2025 revenue fell and Tesla has not issued annual revenue guidance?

**Answer draft:** The 10% years are judgments, not guidance; they assume energy storage remains a growth contributor and vehicle volume recovers as capacity and product availability improve. I would reduce them if deliveries, average selling prices, energy deployments, or tariffs show that the assumed recovery is not occurring.



## Sources

- [Tesla FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm)
- [Tesla FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828025003063/tsla-20241231.htm)
- [Tesla FY2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm)
- [Tesla FY2026 capex outlook](https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf)
- [TSLA price history](https://stockanalysis.com/stocks/tsla/history/)
