"""Check the Meridian Foundation Reserve's measurable portfolio mandate."""

# Editable inputs
holdings = {
    "Cash": {
        "issuer": "none",
        "days_to_redeem": 0,
        "reserve_eligible": True,
    },
    "Treasury bills": {
        "issuer": "U.S. Treasury",
        "days_to_redeem": 1,
        "reserve_eligible": True,
    },
    "Treasury 10-year note": {
        "issuer": "U.S. Treasury",
        "days_to_redeem": 1,
        "reserve_eligible": True,
    },
    "Global equity index fund": {
        "issuer": "diversified fund",
        "days_to_redeem": 2,
        "reserve_eligible": False,
    },
    "Investment-grade bond fund": {
        "issuer": "diversified fund",
        "days_to_redeem": 3,
        "reserve_eligible": False,
    },
    "Private real estate fund": {
        "issuer": "diversified fund",
        "days_to_redeem": 90,
        "reserve_eligible": False,
    },
    "Acme Corp bonds": {
        "issuer": "Acme Corp",
        "days_to_redeem": 4,
        "reserve_eligible": False,
    },
    "Acme Corp stock": {
        "issuer": "Acme Corp",
        "days_to_redeem": 1,
        "reserve_eligible": False,
    },
}

candidates = {
    "A": {
        "Cash": 2, "Treasury bills": 2, "Treasury 10-year note": 10,
        "Global equity index fund": 60, "Investment-grade bond fund": 26,
        "Private real estate fund": 0, "Acme Corp bonds": 0, "Acme Corp stock": 0,
    },
    "B": {
        "Cash": 1, "Treasury bills": 0, "Treasury 10-year note": 0,
        "Global equity index fund": 55, "Investment-grade bond fund": 20,
        "Private real estate fund": 15, "Acme Corp bonds": 5, "Acme Corp stock": 4,
    },
    "C": {
        "Cash": 1, "Treasury bills": 1, "Treasury 10-year note": 0,
        "Global equity index fund": 70, "Investment-grade bond fund": 20,
        "Private real estate fund": 0, "Acme Corp bonds": 0, "Acme Corp stock": 8,
    },
    # Attack portfolio: passes the checker, but leaves the unmeasured loss rule open.
    "D": {
        "Cash": 3, "Treasury bills": 0, "Treasury 10-year note": 0,
        "Global equity index fund": 97, "Investment-grade bond fund": 0,
        "Private real estate fund": 0, "Acme Corp bonds": 0, "Acme Corp stock": 0,
    },
    # Lab 14 benchmark: 40% investment-grade bonds and 60% global equity.
    "E": {
        "Cash": 0, "Treasury bills": 0, "Treasury 10-year note": 0,
        "Global equity index fund": 60, "Investment-grade bond fund": 40,
        "Private real estate fund": 0, "Acme Corp bonds": 0, "Acme Corp stock": 0,
    },
}

reserve_size = 100.0  # USD millions
quarterly_distribution = 0.75  # USD millions
quarters_to_cover = 4
liquidity_window = 5  # business days
minimum_liquid_share = 90.0  # percent
issuer_limit = 8.0  # percent
issuer_exemptions = {"none", "U.S. Treasury", "diversified fund"}


def verdict(value, passes):
    return f"{value:.1f} {'pass' if passes else 'FAIL'}"


def largest_single_company(weights):
    """Aggregate all securities issued by each non-exempt company."""
    company_weights = {}
    for holding, weight in weights.items():
        issuer = holdings[holding]["issuer"]
        if issuer not in issuer_exemptions:
            company_weights[issuer] = company_weights.get(issuer, 0.0) + weight
    return max(company_weights.values(), default=0.0)


def check_candidate(name, weights, reserve_minimum):
    total_weight = sum(weights.values())
    lowest_weight = min(weights.values())
    reserve_weight = sum(
        weight for holding, weight in weights.items()
        if holdings[holding]["reserve_eligible"]
    )
    liquid_weight = sum(
        weight for holding, weight in weights.items()
        if holdings[holding]["days_to_redeem"] <= liquidity_window
    )
    company_weight = largest_single_company(weights)

    checks = [
        ("Weights sum to 100", total_weight, abs(total_weight - 100.0) < 1e-9),
        ("Long-only (lowest weight)", lowest_weight, lowest_weight >= 0.0),
        (f"Reserve >= {reserve_minimum:.1f}%", reserve_weight, reserve_weight >= reserve_minimum),
        (f"Redeemable in {liquidity_window} days >= {minimum_liquid_share:.1f}%", liquid_weight,
         liquid_weight >= minimum_liquid_share),
        (f"Largest single company <= {issuer_limit:.1f}%", company_weight,
         company_weight <= issuer_limit),
    ]

    print(f"\nCandidate {name}")
    failures = 0
    for label, value, passes in checks:
        print(f"{label}: {verdict(value, passes)}")
        failures += not passes
    print("Calendar-year loss: requires CIO clarification")
    if failures:
        print(f"Verdict: fails {failures} rule(s)")
    else:
        print("Verdict: passes every checkable rule")


def main():
    reserve_minimum = quarters_to_cover * quarterly_distribution / reserve_size * 100.0
    print(f"Reserve minimum: {reserve_minimum:.1f}% of the portfolio")
    for name, weights in candidates.items():
        check_candidate(name, weights, reserve_minimum)


if __name__ == "__main__":
    main()
