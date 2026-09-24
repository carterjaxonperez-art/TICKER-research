"""Lab 10: Tesla five-year base case (USD millions except per-share data)."""

import sys

from proforma_engine import _a, build_proforma, dcf_value, require_balanced

# FY2025 reported balance sheet, consolidated into the engine's line items.
START = {
    # Cash includes $27.546bn of highly liquid short-term investments.
    "year": 2025, "revenue": 94827, "cash": 44059, "ar": 4576,
    "inventory": 12392,
    "other_current_assets": 7615,  # prepaid expenses and other current assets
    "ppe": 40643,
    "other_noncurrent_assets": 28521,  # leases, energy systems, DTA, digital and other assets
    "ap": 13371, "employee_comp": 13279, "rebates": 3424,  # accrued liabilities and deferred revenue
    "other_current_liabilities": 0,
    "long_term_taxes": 0,
    "other_noncurrent_liabilities": 16491,  # deferred revenue + other long-term liabilities
    "debt": 8376,  # current and non-current debt/finance leases
    "paid_in_capital": 43862,  # stockholders' capital/AOCI plus NCI and redeemable NCI
    "retained_earnings": 39003,
}


def repeated(value, label, reason):
    return [_a(value, label, reason) for _ in range(5)]


A = {
    # The company-specific driver is deliveries/deployments and average selling price.
    "revenue_growth": [
        _a(0.05, "judgment", "Modest delivery/deployment recovery; Tesla gave no annual revenue guidance."),
        _a(0.08, "judgment", "Energy storage growth and vehicle volume recovery."),
        _a(0.10, "judgment", "New products and capacity contribute."),
        _a(0.10, "judgment", "Growth moderates from the new-product ramp."),
        _a(0.08, "judgment", "Mature-stage growth assumption."),
    ],
    "cogs_pct_revenue": [
        _a(0.815, "judgment", "FY2025 gross margin was 18.0%; assumes a small mix/cost recovery."),
        _a(0.81, "judgment", "Energy mix and manufacturing efficiencies."),
        _a(0.805, "judgment", "Further modest improvement."),
        _a(0.80, "judgment", "Long-run normalized gross margin."),
        _a(0.80, "judgment", "Held at normalized level."),
    ],
    "rd_pct_revenue": [
        _a(0.075, "judgment", "Above FY2025 6.8% to fund AI, autonomy and new products."),
        _a(0.075, "judgment", "Sustained AI and product investment."),
        _a(0.07, "judgment", "Some scale benefit."),
        _a(0.07, "judgment", "Held constant."),
        _a(0.07, "judgment", "Held constant."),
    ],
    "sga_pct_revenue": repeated(0.06, "history", "FY2025 SG&A / revenue, rounded; held constant."),
    "tax_rate": repeated(0.25, "judgment", "Normalizes the volatile historical effective tax rate."),
    "da_pct_revenue": repeated(6148 / 94827, "history", "FY2025 depreciation, amortization and impairment / revenue."),
    "capex_pct_revenue": [
        _a(0.211, "guidance", "FY2026 capex expected to exceed $20bn; $20bn / FY2025 revenue."),
        _a(0.12, "judgment", "AI and manufacturing build slows after 2026."),
        _a(0.09, "judgment", "Continued but moderating investment."),
        _a(0.08, "judgment", "Normalized growth capex."),
        _a(0.07, "judgment", "Further normalization."),
    ],
    "dividend_payout": repeated(0.0, "history", "Tesla paid no common dividend in FY2025."),
    "interest_pct_debt": repeated(0.04, "judgment", "Approximate financing cost; interest income is excluded from operating FCFF."),
    "debt_change": repeated(0.0, "judgment", "No net debt issuance or repayment forecast."),
    # FY2025 history ratios held constant unless specifically noted above.
    "ar_pct_revenue": repeated(4576 / 94827, "history", "FY2025 accounts receivable / revenue."),
    "inventory_pct_revenue": repeated(12392 / 94827, "history", "FY2025 inventory / revenue."),
    "oca_pct_revenue": repeated(7615 / 94827, "history", "FY2025 prepaid and other current assets / revenue."),
    "onca_pct_revenue": repeated(28521 / 94827, "history", "FY2025 other noncurrent assets / revenue."),
    "ap_pct_revenue": repeated(13371 / 94827, "history", "FY2025 accounts payable / revenue."),
    "employee_comp_pct_revenue": repeated(13279 / 94827, "history", "FY2025 accrued liabilities and other / revenue."),
    "rebates_pct_revenue": repeated(3424 / 94827, "history", "FY2025 current deferred revenue / revenue."),
    "ocl_pct_revenue": repeated(0.0, "history", "No separate revenue-linked current-liability bucket retained."),
    "lt_tax_pct_revenue": repeated(0.0, "history", "No separate long-term income-tax payable line forecast."),
    "oncl_pct_revenue": repeated(16491 / 94827, "history", "FY2025 deferred revenue and other long-term liabilities / revenue."),
}


def main():
    model = build_proforma(START, A)
    if "--break-2026-cash" in sys.argv:
        model[0]["cash"] = START["cash"]
    require_balanced(model)
    value = dcf_value(model, wacc=0.10, terminal_growth=0.03, diluted_shares=3751)
    print("Tesla base case | $ millions except per-share data")
    print("\nIncome Statement")
    print("Year  Revenue  COGS  R&D  SG&A  Operating income  Interest  Tax  Net income")
    for y in model:
        print(f"{y['year']}  {y['revenue']:8.0f}  {y['cogs']:5.0f}  {y['rd']:4.0f}  {y['sga']:5.0f}  {y['operating_income']:16.0f}  {y['interest']:8.0f}  {y['taxes']:5.0f}  {y['net_income']:10.0f}")
    print("\nBalance Sheet and Cash Flow")
    print("Year  Cash  AR  Inventory  PP&E  Other assets  Total assets  Debt  Other liabilities  Equity  CFO  Capex")
    for y in model:
        other_liabilities = y['liabilities'] - y['ap'] - y['employee_comp'] - y['rebates'] - y['debt']
        other_assets = y['assets'] - y['cash'] - y['ar'] - y['inventory'] - y['ppe']
        print(f"{y['year']}  {y['cash']:5.0f}  {y['ar']:4.0f}  {y['inventory']:9.0f}  {y['ppe']:5.0f}  {other_assets:12.0f}  {y['assets']:12.0f}  {y['debt']:4.0f}  {other_liabilities:17.0f}  {y['equity']:6.0f}  {y['cfo']:5.0f}  {y['capex']:5.0f}")
    print("\nChecks")
    for y in model:
        print(f"{y['year']}E: assets - liabilities - equity = {y['balance_check']:.2f}; cash = {y['cash']:,.1f}")
    print(f"Enterprise value: ${value['enterprise_value']:,.0f}m")
    print(f"Equity value: ${value['equity_value']:,.0f}m")
    print(f"Base-case value per share: ${value['value_per_share']:,.2f}")


if __name__ == "__main__":
    main()
