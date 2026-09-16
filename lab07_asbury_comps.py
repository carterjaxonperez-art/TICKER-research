"""Lab 07 comparable-company P/E calculator. No external packages required."""

from statistics import median

# Editable case inputs
TARGET = {
    "ticker": "ABG",
    "name": "Asbury Automotive",
    "price": 243.03,
    "diluted_eps": 21.50,
}

PEERS = [
    {
        "ticker": "AN",
        "name": "AutoNation",
        "price": 169.84,
        "diluted_eps": 16.92,
    },
    {
        "ticker": "GPI",
        "name": "Group 1 Automotive",
        "price": 421.48,
        "diluted_eps": 36.81,
    },
]


def has_positive_number(company, key):
    """Return True only for a present, positive numeric input."""
    value = company.get(key)
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def meaningful_pe(company):
    """Return a P/E only when both price and diluted EPS are positive."""
    if not has_positive_number(company, "price") or not has_positive_number(
        company, "diluted_eps"
    ):
        return None
    return company["price"] / company["diluted_eps"]


def unique_non_target_peers(target, peers):
    """Deduplicate by ticker and exclude the target from the peer set."""
    target_ticker = target.get("ticker")
    seen_tickers = {target_ticker}
    selected_peers = []

    for peer in peers:
        ticker = peer.get("ticker")
        if not ticker:
            print("Unnamed peer: excluded (missing ticker).")
        elif ticker in seen_tickers:
            print(f"{ticker}: excluded (duplicate or target).")
        else:
            seen_tickers.add(ticker)
            selected_peers.append(peer)

    return selected_peers


def implied_price(pe_multiple, target_eps):
    """Return the implied target price, or None if target EPS is not meaningful."""
    if not isinstance(target_eps, (int, float)) or isinstance(target_eps, bool):
        return None
    if target_eps <= 0:
        return None
    return pe_multiple * target_eps


def print_leave_one_out(valid_peers, target_eps, full_peer_estimate):
    """Print each peer-removal result using unrounded calculation values."""
    print("\nLeave-One-Out Results")
    for removed_peer, _ in valid_peers:
        remaining_multiples = [
            pe_multiple
            for peer, pe_multiple in valid_peers
            if peer["ticker"] != removed_peer["ticker"]
        ]
        if not remaining_multiples:
            print(f"Remove {removed_peer['ticker']}: no estimate (no peers remain).")
            continue

        remaining_median = median(remaining_multiples)
        remaining_estimate = implied_price(remaining_median, target_eps)
        change = remaining_estimate - full_peer_estimate
        print(
            f"Remove {removed_peer['ticker']}: remaining median-implied price "
            f"${remaining_estimate:.2f}; change from full-peer estimate ${change:.2f}"
        )


def main():
    target_eps = TARGET.get("diluted_eps")
    selected_peers = unique_non_target_peers(TARGET, PEERS)
    valid_peers = []

    print(f"Target: {TARGET['name']} ({TARGET['ticker']})")
    if not has_positive_number(TARGET, "price"):
        print("Target price: not meaningful (price must be positive).")
    else:
        print(f"Target closing price: ${TARGET['price']:.2f}")
    if not has_positive_number(TARGET, "diluted_eps"):
        print("Target diluted EPS: not meaningful (EPS must be positive).")
    else:
        print(f"Target diluted EPS: ${TARGET['diluted_eps']:.2f}")

    print("\nPeer P/E Multiples")
    for peer in selected_peers:
        pe_multiple = meaningful_pe(peer)
        if pe_multiple is None:
            print(
                f"{peer['name']} ({peer['ticker']}) P/E: not meaningful "
                "(price and diluted EPS must be positive)."
            )
        else:
            valid_peers.append((peer, pe_multiple))
            print(f"{peer['name']} ({peer['ticker']}) P/E: {pe_multiple:.6f}x")

    if not valid_peers:
        print("\nImplied Valuation: no usable peers.")
        return
    if not has_positive_number(TARGET, "diluted_eps"):
        print("\nImplied Valuation: not meaningful (target diluted EPS must be positive).")
        return

    peer_multiples = [pe_multiple for _, pe_multiple in valid_peers]
    minimum_multiple = min(peer_multiples)
    median_multiple = median(peer_multiples)
    maximum_multiple = max(peer_multiples)
    full_peer_estimate = implied_price(median_multiple, target_eps)

    print("\nImplied Valuation")
    print(f"Peer median P/E: {median_multiple:.6f}x")
    if len(valid_peers) == 1:
        print(f"Reference estimate (one valid peer): ${full_peer_estimate:.2f}")
    else:
        minimum_price = implied_price(minimum_multiple, target_eps)
        maximum_price = implied_price(maximum_multiple, target_eps)
        print(f"Asbury peer-implied range: ${minimum_price:.2f}-${maximum_price:.2f}")
        print(f"Asbury at peer median: ${full_peer_estimate:.2f}")

    print_leave_one_out(valid_peers, target_eps, full_peer_estimate)


if __name__ == "__main__":
    main()
