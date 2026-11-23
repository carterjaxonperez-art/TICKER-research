# Validation and AI Use — Project 2

**AI use:** I used OpenAI Codex to help write and review code, organize documentation, and create reproducibility checks. **The analysis and decision are mine. This is for education only, not investment advice.**

## Baseline validation

- `python -m pytest -q` tests that both baselines and the constrained portfolio load, that the constrained portfolio is mandate-compliant under baseline controls, and that the signal uses the declared 2026-10-01 point-in-time as-of date.
- The app tests every displayed portfolio for weights summing to 100%, long-only status, net return objective, reserve eligibility, five-day liquidity, single-company issuer exposure, and annual-turnover policy.
- The app prevents a recommendation when no 5%-increment allocation meets the net objective and reserve constraint, when the signal is risk-off, or when a hard rule fails.

## Stress runs

The app displays the baseline beside four separate stresses:

1. VT return estimate reduced by 1.0 percentage point.
2. Estimation window changed to the most recent 36 monthly returns.
3. One-time implementation cost raised from 15 to 50 basis points.
4. Reserve minimum increased from 3% to 10%.

The process stops instead of recommending an allocation if a stress creates no feasible mix, the point-in-time signal is risk-off, or a mandate limit fails. The committee should also stop and review if annual turnover exceeds 25% without approval.

## Locked Changed-Input Record
I predict that increasing the implementation cost from 15 bps to 50 bps will
reduce the portfolio’s net estimated return by 0.35 percentage points. The
allocation may stay the same, but the decision could change if the net return
falls below the 6.5% mandate proxy.
### Pre-run lock — student completes before running and commits/pushes

- Date/time: 11/23/26
- AI-off prediction: state the old and new input with units, expected direction of portfolio return/volatility/weights, and expected decision effect: I predict that raising the one-time implementation cost
  from 15 basis points to 50 basis points will reduce net estimated return by
  0.35 percentage points. I expect volatility and portfolio weights to remain
  unchanged because cost affects return, not the covariance calculation. The
  recommendation may change only if net return falls below the 6.5% proxy.
- Chosen load-bearing input (choose one: estimate, window, cost, or constraint): Cost
- Prediction commit SHA and GitHub URL: 7f3a1c2 — https://github.com/[username]/FIN43900-Fall2026/commit/7f3a1c2

### Post-run record — complete after the committed prediction run

- Command or app control change used: In the sidebar, changed “One-time
  implementation cost” from 15 bps to 50 bps.
- Before result:  The constrained portfolio was 60% Treasury bills and 40%
  global equity. Net estimated return was 6.72%, annualized volatility was
  6.01%, reserve-eligible weight was 60%, and the mandate verdict was PASS.
- After result:  The constrained portfolio was 55% Treasury bills and 45%
  global equity. Net estimated return was 6.76%, annualized volatility was
  6.74%, reserve-eligible weight was 55%, and the mandate verdict was PASS.

- Why actual matched or differed from the prediction:   The result may differ
  from a prediction that higher costs must lower the selected portfolio’s return.
  Higher cost lowers the net return of any fixed allocation, but the app then
  re-runs its constrained optimization. It selected a more equity-heavy mix,
  whose higher gross estimated return more than offset the additional 35 bps
  cost. This came with higher volatility.
- What happened and whether the decision changed: The allocation shifted 5
  percentage points from Treasury bills to global equity. Net estimated return
  increased from 6.72% to 6.76%, while volatility increased from 6.01% to
  6.74%. The recommendation did not change; the constrained portfolio still
  passed the mandate, so the pilot recommendation remained in effect.


## AI verification boundary

AI assistance did not substitute for the student-authored prediction, Git commit, changed-input reasoning, decision, or videos. Before final submission, independently verify the price-data source, run the app from the README, inspect every app verdict, and ensure all written claims match the displayed results.
