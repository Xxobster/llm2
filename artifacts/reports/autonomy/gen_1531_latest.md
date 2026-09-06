# Autonomy public-indicator hunt gen 1531

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T054348Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma678_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0937 | 0.6910 | 4.4473 | 0.0248 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma678_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.8926 | 0.6721 | 3.7830 | 0.0214 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma678_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.7536 | 0.6102 | 2.5866 | 0.0111 | 0.3220 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma678_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.7155 | 0.6583 | 3.2280 | 0.0111 | 0.3216 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma678_below_at_h` | one_head_filter_pi_star | 207 | 16.8399 | 1.6962 | 0.6522 | 3.1528 | 0.0108 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma678_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.5823 | 0.6099 | 2.2920 | 0.0092 | 0.3262 | ok | RAN |
| ETHUSDT | 4 | `sma678_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1436 | 0.5912 | 0.7013 | 0.0053 | 0.2075 | ok | RAN |
| ETHUSDT | 8 | `sma678_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.1331 | 0.5933 | 0.6639 | 0.0052 | 0.2200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma678_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma678_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma678_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma678_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma678_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma678_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma678_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma678_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma678_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma678_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma678_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma678_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma678_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma678_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma678_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma678_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
