# Lab 16 — Provenance Gate

Run:

```powershell
python asof.py
```

`asof.py` uses only the Python standard library. Its editable inputs are the
training-table CSV and the decision date at the top of the file. It applies the
rules in the prescribed order: quarantine missing tickers, remove exact
duplicates, exclude post-decision-date publications, then retain the latest
available vintage for each ticker/month.

## Verification

With decision date `2026-03-31`, the row funnel is:

| Step | Removed rows |
|---|---|
| Quarantined: no ticker | 11 |
| Exact duplicate | 7 |
| Published after 31 March | 3, 8, 10 |
| Older vintage replaced by a revision | 2 |
| As-of panel | 1, 4, 5, 6, 9, 12 |

| Ticker | As-of signal | Naive signal |
|---|---:|---:|
| AAA | +1.98% (February) | +5.83% (March) |
| BBB | -1.02% (February) | -5.15% (March) |
| CCC | +0.91% (February) | +1.82% (February, revised) |

Changing `DECISION_DATE` to `2026-04-15` makes the as-of signals equal the
naive signals for every ticker, because every publication in the training table
is then available.

## Point-in-time explanation

Look-ahead bias occurs when an analysis uses information that was not available
on its decision date. Here, a month is the period measured, while the
publication date determines when the observation could have been known. A
revision is a second publication for the same ticker and measured month; the
gate retains only the latest revision published by the decision date. For AAA,
the naive +5.83% March result uses the 10 April March publication, so it could
not have supported a 31 March trade. The decision-date-safe result was +1.98%
using the 25 March February revision.
