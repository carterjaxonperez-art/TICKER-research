"""Price the Meridian Foundation Reserve's three baseline portfolios.

Run with: python portfolio.py
All returns, volatilities, correlations, and weights are decimals internally.
"""

from math import sqrt


# Editable inputs
SLEEVES = {
    "Treasury bills": {"expected_return": 0.035, "volatility": 0.005},
    "Treasury 10-year note": {"expected_return": 0.043, "volatility": 0.070},
    "Investment-grade bond fund": {"expected_return": 0.050, "volatility": 0.060},
    "Global equity index fund": {"expected_return": 0.080, "volatility": 0.160},
}

CORRELATIONS = {
    "Treasury bills": {
        "Treasury bills": 1.00, "Treasury 10-year note": 0.10,
        "Investment-grade bond fund": 0.05, "Global equity index fund": 0.00,
    },
    "Treasury 10-year note": {
        "Treasury bills": 0.10, "Treasury 10-year note": 1.00,
        "Investment-grade bond fund": 0.80, "Global equity index fund": -0.10,
    },
    "Investment-grade bond fund": {
        "Treasury bills": 0.05, "Treasury 10-year note": 0.80,
        "Investment-grade bond fund": 1.00, "Global equity index fund": 0.25,
    },
    "Global equity index fund": {
        "Treasury bills": 0.00, "Treasury 10-year note": -0.10,
        "Investment-grade bond fund": 0.25, "Global equity index fund": 1.00,
    },
}

OBJECTIVE_RETURN = 0.065  # CPI estimate (2.5%) + 4.0%
RESERVE_ELIGIBLE = {"Treasury bills", "Treasury 10-year note"}


def validate_correlations(correlations, sleeves):
    """Reject missing, out-of-range, or non-symmetric correlations."""
    names = list(sleeves)
    for first in names:
        if first not in correlations:
            raise ValueError(f"Correlation table is missing row: {first}")
        for second in names:
            if second not in correlations[first]:
                raise ValueError(f"Correlation table is missing {first}/{second}")
            value = correlations[first][second]
            if not -1.0 <= value <= 1.0:
                raise ValueError(
                    f"Correlation for {first} and {second} must be between -1 and 1; got {value}."
                )
            if value != correlations[second][first]:
                raise ValueError(
                    f"Correlation table is not symmetric for {first} and {second}."
                )


def covariance_matrix(sleeves, correlations):
    """Return covariance[first][second] = correlation * vol_first * vol_second."""
    return {
        first: {
            second: correlations[first][second]
            * sleeves[first]["volatility"]
            * sleeves[second]["volatility"]
            for second in sleeves
        }
        for first in sleeves
    }


def benchmark_weights(sleeves):
    """Return the 40% IG bond fund / 60% global equity benchmark."""
    return {
        name: 0.40 if name == "Investment-grade bond fund"
        else 0.60 if name == "Global equity index fund" else 0.0
        for name in sleeves
    }


def equal_weight_weights(sleeves):
    """Return equal weights across all sleeves."""
    return {name: 1.0 / len(sleeves) for name in sleeves}


def inverse_volatility_weights(sleeves):
    """Return 1 / volatility weights scaled to sum to 100%."""
    inverse_volatilities = {
        name: 1.0 / values["volatility"] for name, values in sleeves.items()
    }
    total = sum(inverse_volatilities.values())
    return {name: value / total for name, value in inverse_volatilities.items()}


def portfolio_return(weights, sleeves):
    """Return the weighted expected return."""
    return sum(weights[name] * sleeves[name]["expected_return"] for name in sleeves)


def portfolio_variance(weights, covariance):
    """Return w' * covariance * w, including every covariance term."""
    return sum(
        weights[first] * weights[second] * covariance[first][second]
        for first in weights for second in weights
    )


def portfolio_volatility(weights, covariance):
    """Return the square root of portfolio variance."""
    return sqrt(portfolio_variance(weights, covariance))


def reserve_eligible_weight(weights, eligible_sleeves):
    """Return the total weight assigned to reserve-eligible sleeves."""
    return sum(weights[name] for name in eligible_sleeves)


def meets_objective(expected_return, objective_return):
    """Return whether expected return reaches the objective."""
    return expected_return >= objective_return


def print_portfolio(name, weights, sleeves, covariance, objective_return):
    """Print a portfolio's requested performance and mandate information."""
    ordered_weights = " / ".join(f"{weights[sleeve] * 100:.1f}" for sleeve in sleeves)
    expected_return = portfolio_return(weights, sleeves)
    volatility = portfolio_volatility(weights, covariance)
    reserve_weight = reserve_eligible_weight(weights, RESERVE_ELIGIBLE)
    objective_result = "yes" if meets_objective(expected_return, objective_return) else "no"

    print(f"\n{name}")
    print(f"Weights (bills / 10-year / IG / equity): {ordered_weights}%")
    print(f"Expected return: {expected_return * 100:.2f}%")
    print(f"Volatility: {volatility * 100:.2f}%")
    print(f"Reserve-eligible: {reserve_weight * 100:.1f}%")
    print(f"Meets {objective_return * 100:.1f}% objective: {objective_result}")


def main():
    validate_correlations(CORRELATIONS, SLEEVES)
    covariance = covariance_matrix(SLEEVES, CORRELATIONS)
    portfolios = {
        "Benchmark": benchmark_weights(SLEEVES),
        "Equal weight": equal_weight_weights(SLEEVES),
        "Inverse volatility": inverse_volatility_weights(SLEEVES),
    }
    for name, weights in portfolios.items():
        print_portfolio(name, weights, SLEEVES, covariance, OBJECTIVE_RETURN)


if __name__ == "__main__":
    main()
