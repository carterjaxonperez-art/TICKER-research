# Lab 07 — Asbury Comparable-Company Policy and Implied Range

## P/E in this case

P/E equals share price divided by diluted earnings per share. It compares what investors pay for each dollar of current earnings, which can supplement a DCF by adding a market-based valuation perspective; a lower P/E alone does not mean a company is cheaper because growth, risk, capital intensity, and earnings quality can differ.

P/E is most useful when companies have comparable operations, accounting, profitability, and growth prospects. It is not meaningful with nonpositive EPS and can mislead when earnings include unusual gains or charges.

## Peer policy

Franchised vehicle retail and service/parts exposure matter more than an auto-industry label because they determine the underlying earnings model. I use AutoNation as a peer because its franchised dealership operations provide a comparable retail and service-oriented earnings base. I qualify Group 1 Automotive because it is also a franchised dealer and service/parts operator, but its geographic and operating mix needs qualification against Asbury rather than automatic inclusion; the multiple is not the reason for the decision.

## Frozen case inputs

| Company / role | 12/31/2024 closing price | FY2024 GAAP diluted EPS |
|---|---:|---:|
| Asbury Automotive (ABG), target | $243.03 | $21.50 |
| AutoNation (AN), peer | $169.84 | $16.92 |
| Group 1 Automotive (GPI), qualified peer | $421.48 | $36.81 |

## Checked outputs

| Check | Result |
|---|---:|
| AutoNation P/E | 10.037825× |
| Group 1 P/E | 11.450149× |
| Peer median P/E | 10.743987× |
| Asbury peer-implied range | $215.81–$246.18 |
| Asbury at peer median | $231.00 |
| Remove GPI: remaining AN estimate | $215.81 |
| Change from two-peer median estimate | −$15.18 |

Removing Group 1 removes the higher P/E peer, so the median implied price falls. With only AutoNation remaining, the output is a reference estimate rather than a range because there is no dispersion across multiple peers.

## Files and command

Run the calculator with:

```powershell
python lab07_asbury_comps.py
```

The calculator uses only Python's standard library and does not fetch data, add cash/debt, or install packages.
