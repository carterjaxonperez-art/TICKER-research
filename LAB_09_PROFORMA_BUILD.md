# Lab 09 — ABG engine build and known answer

Run `python proforma.py`. It contains the Lab 09 ABG assumptions and opening FY2025 balance sheet exactly as provided in the lab. It has no balance-sheet plug: cash is calculated last from FCFE, then revolver draw / repayment. `assert_balanced()` runs before the valuation and raises an error naming the forecast year and gap when the balance sheet is broken.

## Known-answer proof

| Line ($ millions except per-share data) | FY2026E | FY2030E |
|---|---:|---:|
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| FCFE | 211.4 | 342.3 |
| Ending cash | 101.8 | 719.8 |
| Assets − liabilities − equity | 0.0 | 0.0 |

The calculated equity value per share is **$291.75** and the share of value after 2030 is about **79.8%**.

To perform the required break test, temporarily replace the FY2026 calculated `cash` with `OPENING["cash"]` immediately before `assets = ...`. On the next run the program refuses valuation with `2026E balance sheet does not balance: gap -61.4`. Undo that change afterward.

The ABG line that must be modeled consistently is floor-plan financing: vehicle inventory and floor-plan debt move together. It cannot be treated like ordinary long-term debt or ignored while inventory grows.

## Partner explanation

The three judgments carrying a pro-forma valuation are revenue growth, operating margin, and reinvestment / terminal assumptions (capex, working capital, WACC, and terminal growth). Growth expands the revenue base; margin determines how much becomes operating profit; reinvestment determines how much of that profit is actually free cash flow. Cash is the last line because it is the accumulated result of operating, investing, and financing cash flows—not an independent operating assumption. If it is used as a plug early, a broken balance sheet can be hidden.

## Source

- [Asbury FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1144980/000114498026000051/abg-20251231.htm), consolidated balance sheet, income statement, and cash-flow statement.
