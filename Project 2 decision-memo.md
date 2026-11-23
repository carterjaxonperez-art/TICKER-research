# Decision Memo — Meridian Foundation Reserve

**AI use:** I used OpenAI Codex to help write and review code, organize documentation, and create reproducibility checks. **The analysis and decision are mine. This is for education only, not investment advice.**

## Recommendation

**Pilot a 0%–10% allocation** to the app's constrained portfolio rather than adopt the process for the full reserve. The range limits implementation while the committee observes whether the return estimate, reserve buffer, risk signal, and turnover rule remain stable.

## Mandate

The Reserve seeks CPI + 4% net of costs, using a 6.5% estimated annual-return proxy. It may use BIL, IEF, LQD, and VT; compares results to a 60% VT / 40% LQD benchmark; uses annualized volatility as the risk measure; and must be long-only, hold ≥3% in reserve-eligible Treasury sleeves, retain ≥90% five-business-day liquidity, stay below 8% in a non-exempt single issuer, and limit annual turnover to 25% absent approval.

## Process and decision rule

The constrained portfolio searches 5%-increment, long-only allocations and selects the feasible mix with the lowest estimated volatility after the selected implementation cost. The app places it beside Equal Weight and the 60/40 benchmark, each with the same mandate verdict and failed-rule list. The return objective is part of the verdict: a liquid portfolio that misses the net 6.5% objective is not a mandate pass.

The point-in-time signal is VT's trailing 12-month adjusted-price return using observations available through 2026-10-01. A positive signal is risk-on; a non-positive signal is risk-off. The process stops new risk allocations if the signal is risk-off, no feasible allocation remains, a hard mandate limit fails, or rebalancing would require more than 25% turnover without approval.

## Stress and monitoring

The app displays separate stresses for a 1 percentage-point lower VT return estimate, a last-36-month window, a 50-basis-point cost, and a 10% reserve minimum. I would monitor net estimated return versus 6.5%, volatility, reserve-eligible weight, turnover, the signal, and any material allocation change between the full-history and 36-month windows. A stop condition reverses the pilot recommendation until committee review.

## Limits

The model uses historical adjusted prices and annualized arithmetic-average return estimates; neither is a forecast. The 6.5% proxy and the mandate's unresolved calendar-loss rule are limitations, not silently solved assumptions.
