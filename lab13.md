# Lab 13 — Portfolio Mandate Defense

## Files and command

The checker is `mandate.py` (standard library only). Run it from this folder with:

```powershell
python mandate.py
```

## Sort before building: S1–S10

| Statement | Type | Reason |
|---|---|---|
| S1 | Hard constraint | A seven-year horizon and annual rebalancing set the investment time frame and operating cadence. |
| S2 | Objective | CPI + 4% net of costs over rolling five-year periods is the required investment outcome. |
| S3 | Hard constraint | The stated payout reserve is a measurable liquidity requirement. |
| S4 | Preference | The 60/40 benchmark is a comparison reference, not a stated allocation limit or optimization objective. |
| S5 | Hard constraint | Long-only, no borrowing, no short sales, and no derivatives are prohibitions. |
| S6 | Hard constraint | The 8% maximum single-issuer exposure is a measurable concentration cap. |
| S7 | Hard constraint | Turnover is capped at 25% annually unless the committee approves an exception. |
| S8 | Hard constraint | At least 90% must be redeemable within five business days. |
| S9 | Unverifiable promise | It expresses a loss limit, but gives no return measure, valuation point, or breach response. |
| S10 | Missing | It explicitly leaves the pilot's optimization target unspecified and supplies no sector, ESG, tax, or home-bias preference. |

## Known-answer check

`python mandate.py` computes the 3.0% reserve minimum. The expected measured results are:

| Rule | A | B | C |
|---|---|---|---|
| Weights sum to 100 | 100.0 pass | 100.0 pass | 100.0 pass |
| Long-only (lowest weight) | 0.0 pass | 0.0 pass | 0.0 pass |
| Reserve >= 3.0% | 14.0 pass | 1.0 FAIL | 2.0 FAIL |
| Redeemable in 5 days >= 90.0% | 100.0 pass | 85.0 FAIL | 100.0 pass |
| Largest single company <= 8.0% | 0.0 pass | 9.0 FAIL | 8.0 pass |
| Calendar-year loss | requires CIO clarification | requires CIO clarification | requires CIO clarification |
| Verdict | passes every checkable rule | fails 3 rule(s) | fails 1 rule(s) |

The Acme result is 9.0% in B because the 5% bonds and 4% stock are both Acme securities. Candidate D is the attack described below.

### Long-only probe

For the required probe, I temporarily changed candidate A's Cash from `2` to `-2` and its Global equity index fund from `60` to `64`, ran the file, and restored both values. A still summed to 100.0; its lowest weight was -2.0 and failed long-only; its reserve-eligible weight was 10.0 and passed; no other check failed.

### AI check-in

The line I least understood was the issuer aggregation. The AI asked: “Why does candidate B fail the issuer limit when neither Acme position exceeds 8% by itself?” My answer: “The mandate says one company’s securities count together, so 5% Acme bonds plus 4% Acme stock equals 9%, which exceeds 8%.”

## Attack: candidate D

Candidate D is 3% Cash and 97% Global equity index fund (all other holdings are 0%). It passes every check in `mandate.py`: it is fully liquid within five days, has the 3.0% payout reserve, and the diversified fund is exempt from the single-company cap.

The CIO could reasonably reject it under S9. A nearly all-equity reserve can experience a calendar-year loss well beyond 10%, and S9 has not said how that loss is measured or what happens after a breach. The objection holds: S9 is the statement that decides it, even though it cannot yet be tested by the program.

As the sceptical colleague, I proposed a different passing portfolio: 100% Treasury 10-year note. It is reserve-eligible, liquid in one day, long-only, and issuer-exempt, but I would reject it under S2 because it may not be a credible way to achieve CPI + 4% net over rolling five-year periods. Against that colleague portfolio, I cite S2.

## One question for the CIO before optimization

**What criterion should the pilot optimize—expected return, probability of meeting CPI + 4%, tracking error to the 60/40 benchmark, or downside/shortfall risk?**

For example, an answer of “minimize the probability of missing CPI + 4% while respecting a defined calendar-loss limit” would justify a more diversified, bond-and-cash-buffered portfolio than an answer of “maximize expected return subject to the hard constraints.” This is the missing decision in S10; S9 must also be defined before its stated loss limit can become a checkable constraint.

## Investment policy statement (IPS)

An IPS is the governing document that turns a client's purpose, return goal, risk tolerance, liquidity needs, and implementation limits into portfolio directions and a way to monitor them. It works by distinguishing objectives (what success means) from constraints (what is permitted) and preferences or unresolved choices (what needs a client decision before construction).

For Meridian, S1 supplies horizon and operating cadence; S2 supplies the return objective; S3, S5, S6, S7, and S8 are measurable implementation and risk constraints; S4 is the benchmark for comparison; S9 is a risk-intent statement that lacks a test; and S10 records preferences that are absent plus the missing optimization decision. These are the components of an IPS, but S9 and S10 show that Meridian's version is incomplete for portfolio optimization.

## Reflection

A portfolio can pass every checkable rule and still be unsuitable because the code only tests rules that have a precise measure and threshold. Candidate D proves this: its 97% equity exposure passes the coded liquidity, reserve, and issuer rules, but may conflict with the client’s intended 10% loss tolerance. The type I was least sure of was S4: I classified the benchmark as a preference/reference because it does not say that the portfolio must track it or stay within a tracking-error range.
