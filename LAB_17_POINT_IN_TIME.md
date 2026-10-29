# Lab 17 — Point-in-Time Audit

## Files and run command

The app is [asof_app.py](asof_app.py). It uses FRED's public CSV graph download
for the current view and ALFRED's public CSV graph download for a historical
vintage. No API key or account is required.

```powershell
python -m streamlit run asof_app.py
```

The sidebar begins with BAA, FEDFUNDS, DGS10, and MORTGAGE30US selected. It
also accepts a typed FRED ID, so I used `PAYEMS` for the revision probe and
`DGS10` for my portfolio-relevant series. An unavailable or invalid ID produces
an error only for that ID; the other series remain available.

## Known-answer and revision checks

With **As known on = 5 October 2026**, the required ALFRED vintage should show:

| Series | Last date known | Value |
|---|---|---:|
| BAA | September 2026 | 6.47 |
| FEDFUNDS | September 2026 | 3.75 |
| DGS10 | 2 October 2026 | 5.28 |
| MORTGAGE30US | 1 October 2026 | 7.28 |

The implementation obtains these rather than storing them: its
`download_as_known_on` function sends `vintage_date=2026-10-05` to ALFRED, and
the audit table selects the final non-missing observation returned.

For the required probe, enter `PAYEMS` and set **As known on = 15 January
2025**. The final known observation should be December 2024 at **159,536**.
The table compares that vintage to the current FRED download on matching dates,
so the revised-count field must be above zero and the current December 2024
value should be lower. This is a direct check that the app is not reading
today's data twice.

## Data card — DGS10

| Field | Evidence |
|---|---|
| Source and link | Federal Reserve Bank of St. Louis, [FRED DGS10](https://fred.stlouisfed.org/series/DGS10); historical vintages from [ALFRED](https://alfred.stlouisfed.org/series?seid=DGS10). |
| What it measures | The market yield on U.S. Treasury securities at a constant 10-year maturity. |
| Units | Percent, not seasonally adjusted. |
| Publication lag | Daily business-day series. A trading-day observation normally becomes available with little practical lag; the app's selected as-of date is the evidence for exactly which business dates were available then. |
| Revisions | DGS10 is generally not revised; the app's same-date revised-count field makes this testable for each selected vintage rather than assuming it. |
| Download date | 29 October 2026 (the date this Lab 17 record was prepared). |
| Three manual checks | In the app, compare any three displayed DGS10 observations with the FRED page before submission and record the dates and values below. |

Manual FRED-page checks completed during lab (do not replace these with invented values):

| Date | App value | FRED-page value | Match? |
|---|---:|---:|---|
| _enter after checking_ |  |  |  |
| _enter after checking_ |  |  |  |
| _enter after checking_ |  |  |  |

## Partner attack

This must document the actual partner exchange rather than a fabricated one.

Partner: _complete in class_.

Field challenged (publication date, revisions, or units): _complete in class_.

Two-sentence response with evidence from the app or FRED page: _complete after
the partner's question_.

## My call

**Admit DGS10 only with an as-of rule:** use the ALFRED vintage whose date is
the portfolio decision date (or the latest confirmed pre-decision business-day
observation), never a later FRED download. DGS10 has short publication lag and
is expected to show few or no revisions, but I would quarantine it if the app
shows that the intended decision-date vintage did not contain the required
observation or that a material same-date revision occurred.

A backtest that used the current FRED history without the ALFRED date filter
could overstate what was tradable by including rates published after the
decision, and would silently adopt any later corrections.
