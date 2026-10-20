# Lab 14 — Portfolio Baselines

## Files and commands

The reusable risk engine is `portfolio.py` and uses only the Python standard library.

```powershell
python portfolio.py
python mandate.py
```

## Known-answer verification

Using the course-authored inputs, `portfolio.py` calculates the following values from its editable returns, volatilities, correlations, and weights:

| Portfolio | Weights: bills / 10-year / IG / equity | Return | Volatility | Reserve-eligible | Meets 6.5%? |
|---|---:|---:|---:|---:|---|
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80% | 10.46% | 0.0% | yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20% | 5.21% | 50.0% | no |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77% | 1.05% | 90.3% | no |

The engine constructs each covariance as `correlation × volatility of sleeve i × volatility of sleeve j`. Portfolio variance sums every `weight_i × weight_j × covariance_i,j` term, and portfolio volatility is the square root of that variance.

## Validation checks

The engine rejects a correlation outside -1 to 1 and rejects a non-symmetric correlation table before computing any portfolio. Changing the IG bond fund/equity correlation from `0.25` to `0.50` in both cells changes benchmark volatility to 11.00%; the input was then restored to `0.25`.

The out-of-range test used `1.30` in both IG bond fund/equity cells. It stopped with: `Correlation for Investment-grade bond fund and Global equity index fund must be between -1 and 1; got 1.3.`

## AI check-in

**Question:** Why does `portfolio_variance()` include both the IG bond fund/equity term and the equity/IG bond fund term?

**My answer:** Portfolio variance accounts for every asset interaction. Covariance is identical in both directions, but the double sum includes both directions mathematically; together they equal `2 × weight_IG × weight_equity × covariance(IG, equity)`.

## Partner practice

**Partner question:** Why does `covariance_matrix()` multiply correlation by both sleeves' volatilities instead of using the correlation number by itself?

**Answer:** Correlation has no units; it only describes how two returns move together on a scale from -1 to +1. Multiplying it by the two volatilities converts that relationship into covariance, which is measured on the scale needed for the weighted portfolio-variance calculation. If the code used correlation alone, it would treat assets with very different volatilities as if they had the same risk scale.

In `mandate.py`, candidate E is the Lab 14 benchmark: 40% investment-grade bond fund and 60% global equity index fund. It has 0.0% reserve-eligible weight, so it fails Meridian's 3.0% reserve rule even though it meets the return objective in `portfolio.py`.

## Diversification

Diversification is the reduction of portfolio-specific risk obtained by combining assets whose returns do not move exactly together. When correlation is below +1, the covariance term is smaller than the maximum possible co-movement; gains in one sleeve can partly offset losses in another, reducing portfolio volatility.

For the benchmark, bills and the 10-year note have zero weights, so only the IG/equity terms remain:

```text
variance = (0.40² × 0.06²) + (0.60² × 0.16²)
           + 2 × 0.40 × 0.60 × 0.25 × 0.06 × 0.16
         = 0.010944
volatility = √0.010944 = 0.1046 = 10.46%
```

The inverse-volatility portfolio piles into bills because its 0.5% volatility makes `1 ÷ volatility` far larger than for the other sleeves. I would show the CIO the benchmark first because it is the stated comparison portfolio and the only baseline that reaches the 6.5% expected-return objective. I would also flag that it fails Meridian's reserve requirement, so it is not a mandate-compliant recommendation.

## Thursday preparation — fund universe

| Ticker | Fund name | Role | Source | Download date |
|---|---|---|---|---|
| BIL | SPDR Bloomberg 1-3 Month T-Bill ETF | Cash and reserve | Yahoo Finance Historical Data (monthly Adj Close) | 2026-10-20 |
| IEF | iShares 7-10 Year Treasury Bond ETF | Government bonds | Yahoo Finance Historical Data (monthly Adj Close) | 2026-10-20 |
| LQD | iShares iBoxx $ Investment Grade Corporate Bond ETF | Fixed income | Yahoo Finance Historical Data (monthly Adj Close) | 2026-10-20 |
| VT | Vanguard Total World Stock ETF | Equity | Yahoo Finance Historical Data (monthly Adj Close) | 2026-10-20 |

`prices.csv` will contain five years of monthly adjusted closing prices, with `Date` first, oldest month first, then one column for each ticker.
