# Lab 19 — Legend Panel

## Deliverables

- [Panel app](buffett_app.py)
- [Shared SEC 10-K extractor](skills/buffett-10k-investor/scripts/edgar_buffett.py)
- [Graham skill](skills/graham-10k-investor/SKILL.md)
- [Burry skill](skills/burry-10k-investor/SKILL.md)

The app retains the Lab 18 Buffett screen and adds Graham and Burry on the same five annual SEC 10-K facts. It prints the raw selected values, XBRL tags, derived ratios, code-only panel checks, three side-by-side memos, and one unprinted-number audit across all three memos. Missing values are never estimated: `not found` stays visible and a dependent check is `not known`.

## Run

Do not save a personal email address in the repository. In PowerShell, set a truthful contact only for the current terminal session, then run:

```powershell
$env:SEC_USER_AGENT = "Your Name your.email@example.edu"
py skills/buffett-10k-investor/scripts/edgar_buffett.py COST
py -m streamlit run buffett_app.py
```

Enter the same contact in the app sidebar. It is used only for the SEC request and is not written to disk.

## Required COST verification

With Graham's default 2.0 current-ratio threshold, the completed live COST table must show:

| Investor | Expected result |
|---|---|
| Buffett | 3 of 3 pass |
| Graham | 2 of 3 pass; current ratio fails at 1.06 |
| Burry | 2 of 2 pass; latest liabilities/equity is 1.49 |

For the required probe, change the sidebar's Graham threshold to `1.0`; Graham should then pass COST. Restore `2.0` and retain the displayed reason for keeping the conservative threshold.

## Your-company run and decision

My Lab 14 fund list includes BIL, IEF, LQD, and VT. The largest company inside a fund is not stored in this repository, so the company must be selected from the fund's current published holdings before the final in-class run. Run that SEC filer in the app, retain every gap, then record the panel table, three verdicts, three memos, a two-sentence bull case and bear case, and this one-line decision:

> I would use the panel only as a first screen, conditioned on checking the issuer's current filing coverage and completing valuation and fundamental due diligence outside these limited rules.

## Notes for checkout

The published app URL and GitHub file links should be added after deployment. Partner explanations and the individual Brightspace quiz must be completed personally in class.
