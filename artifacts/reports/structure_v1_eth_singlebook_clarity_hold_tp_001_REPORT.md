# Gen-1 single-book clarity × hold × TP (ETHUSDT 1h direction)

**Maximum readiness:** `RESEARCH_ONLY`  
**Evidence class:** fold V2 stitched outer out-of-sample (OOS) execution grid  
**Lockbox used:** no  
**Conformance:** GREEN (tradesim 1.0.0, 62/62)

## Preregister

- `configs/preregister/structure_v1_eth_singlebook_clarity_hold_tp_001.yaml`
- sha256: `eedcafe3fdd0b0ff545c4f252f0deae3cf93cbed5e3b06299fe3aa354bb5eafa`
- Stop Loss fixed at **2%** (leverage 18×). Grid: clarity `{none, mean_strength}` × hold `{6,12}` × Take Profit `{1%, 1.5%, 2.618%}`.

## Protocol

1. Inner-select one arm on outer-fold-0 train (3 inner folds).
2. Freeze arm; walk-forward all six V2 outer folds; stitch OOS trades.
3. Compare to frozen control `none|hold6|tp1%` on the same outer stitch.
4. Do not open lockbox for selection.

## Result (20260804T064851Z)

| Arm | Stitched Profit Factor (PF) | Trades | Bootstrap pos-exp |
|-----|----------------------------|--------|-------------------|
| **Selected** `mean_strength\|hold12\|tp1%` | **3.323** | 5072 | 1.00 |
| Control `none\|hold6\|tp1%` | 1.988 | 8657 | (not gated) |

- Success vs preregister criteria: **yes** (beats control, PF≥1.20, bootstrap OK, no liquidation).
- Inner selection preferred **mean_strength + hold 12** and kept Take Profit at **1%** — not the 2.618% Fibonacci-extension target.
- Full JSON: `structure_v1_eth_singlebook_clarity_hold_tp_001_latest.json`.

## Interpretation

Transferring multitrade’s **primary-entry strength filter** and **longer hold** improved single-book stitched outer Profit Factor versus control. Raising Take Profit was not required for the winning arm.

This is **not** a replacement for the official ETH direction settle Profit Factor ≈1.77 and does **not** authorize live pack changes. Min-exchange sizing equity is not scale evidence. Probability of Backtest Overfitting (PBO) unavailable (no full candidate-by-time matrix for DSR/PBO gates).

## Forbidden next steps

- Do not re-search this candidate space after viewing this OOS.
- Do not promote from lockbox Finplot.
- Gen-2 Stop Loss grid only if explicitly preregistered as a new generation.
