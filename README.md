# Tesla FIN 43900 Project 1

Reproducible Tesla corporate-finance application for a point-in-time valuation dated October 19, 2026. Dollars are USD millions except per-share amounts. The project uses FY2025 reported results, Q2 2026 actual interim financials, and Q3 2026 operating disclosures only. Q3 financial results were scheduled after the valuation date and are not treated as actuals.

## Status

The core model and validation suite are source-complete and dependency-free. This workstation currently has no Python interpreter available (`python` and `py` are not recognized), so execution-generated outputs, the Excel workbook, Word memo, and PowerPoint deck remain pending a local Python installation. No result is represented as executed until that blocker is removed.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts\build_all.py
python -m pytest -q
streamlit run app.py
```

The core model itself needs only the Python standard library: `python scripts\build_all.py --core-only`.

## Design

`model/engine.py` forecasts automotive vehicle sales, regulatory credits, leasing, energy, and services separately. It then builds linked income statement, balance sheet, cash flow, FCFF, DCF, scenario, sensitivity, and reverse-DCF outputs. The forecast is deliberately conservative about Robotaxi, FSD, and Optimus: base-case contribution is zero until evidence supports a separately measurable cash-flow stream.

## Important limitations

- No dated October 19, 2026 market close is included yet. The model therefore does not claim a completed upside/downside conclusion or a final investment action.
- Peer financial data has not yet been frozen from same-date filings and pricing sources. Relative valuation is documented as pending rather than estimated.
- `outputs/` is created by the build script. Excel, DOCX, and PPTX exports require optional packages listed in `requirements.txt`.
- Human-required course actions, including partner review and recorded videos, remain templates only.

## Sources

Primary sources and exact uses are listed in `data/source_register.csv`. Key sources include Tesla's [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm), [Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm), and [Q3 2026 operating release](https://ir.tesla.com/press-release/tesla-third-quarter-2026-production-deliveries-and-deployments).
