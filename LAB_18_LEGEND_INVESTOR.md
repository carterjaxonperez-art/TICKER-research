# Lab 18 — Legend Investor as Skill

## Deliverables

- [Skill instructions](skills/buffett-10k-investor/SKILL.md)
- [EDGAR extractor](skills/buffett-10k-investor/scripts/edgar_buffett.py)
- [Streamlit app](buffett_app.py)
- [COST memo](memos/COST_buffett_memo.md)

The skill keeps the numerical work in deterministic code: SEC ticker-to-CIK and
company-facts downloads, 10-K-only selection, annual-flow filtering, latest
filing for duplicate periods, required XBRL-tag fallbacks, derived ROE and
owner earnings, and the three Buffett checks. The memo performs only the
business-quality judgment and cannot introduce an unprinted number without the
app flagging it.

## Run

Do not save a personal email address in the repository. In PowerShell, set a
truthful contact for the current terminal session, then run:

```powershell
$env:SEC_USER_AGENT = "Your Name your.email@example.edu"
python skills/buffett-10k-investor/scripts/edgar_buffett.py COST
python -m streamlit run buffett_app.py
```

The app asks for the same contact in its password-style sidebar field and never
writes it to disk. It displays owner earnings and net income over the five
years, the tagged table, all three checks, the memo, and any number in the memo
that did not come from the script output.

## Required verification

For `COST`, compare the live script output to the instructor's known-answer
table: FY2022 through FY2026 should match, and all three checks should pass.
The saved memo uses only values in that table and makes no price claim.

For `JPM`, run the same command. The extractor must leave unavailable capital
spending and owner earnings as `not found`; therefore the two owner-earnings
checks must remain `not known`. This is intentional—no substitution or estimate
is permitted.

To perform the hand-number probe, add `40.0%` to the COST memo text in the app.
It should appear under “Numbers not printed by the script.” Remove it afterward.

## Decision

I trust the COST business-quality verdict as a repeatable first screen because
its quantities are constrained to tagged SEC 10-K facts and code-derived
checks. I would not treat it as a decision to buy: price and valuation are
outside this lab and deliberately absent from the memo.

## Live partner work

Partner explanation and the partner's question must be completed in class. They
are not claimed here because they require the actual exchange.
