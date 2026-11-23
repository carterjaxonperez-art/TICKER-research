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

### Pre-run lock — student completes before running and commits/pushes

- Date/time: **[student enters]**
- AI-off prediction: state the old and new input with units, expected direction of portfolio return/volatility/weights, and expected decision effect: **[student enters]**
- Chosen load-bearing input (choose one: estimate, window, cost, or constraint): **[student enters]**
- Prediction commit SHA and GitHub URL: **[student enters before rerun]**

### Post-run record — complete after the committed prediction run

- Command or app control change used: **[student enters]**
- Before result: **[student enters]**
- After result: **[student enters]**
- What happened and whether the decision changed: **[student enters]**
- Why actual matched or differed from the prediction: **[student enters]**

## AI verification boundary

AI assistance did not substitute for the student-authored prediction, Git commit, changed-input reasoning, decision, or videos. Before final submission, independently verify the price-data source, run the app from the README, inspect every app verdict, and ensure all written claims match the displayed results.
