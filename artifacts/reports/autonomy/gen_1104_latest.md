# Autonomy public-indicator hunt gen 1104

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T233439Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2360_above_at_h` | one_head_filter_pi_star | 52 | 4.7039 | 1.4171 | 0.5962 | 1.1178 | 0.0168 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `sma2360_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5809 | 0.6388 | 3.5180 | 0.0155 | 0.3075 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2360_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5339 | 0.6328 | 3.3444 | 0.0147 | 0.3075 | ok | RAN |
| ETHUSDT | 8 | `sma2360_above_at_h` | one_head_filter_pi_star | 51 | 4.6908 | 1.3380 | 0.5882 | 0.9248 | 0.0132 | 0.2353 | ok | RAN |
| SOLUSDT | 4 | `sma2360_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.8078 | 0.6457 | 4.2124 | 0.0120 | 0.3245 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2360_below_at_h` | one_head_filter_pi_star | 292 | 23.8771 | 1.7867 | 0.6473 | 4.1284 | 0.0118 | 0.3288 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma2360_above_at_h` | one_head_filter_pi_star | 69 | 5.6722 | 1.6008 | 0.6377 | 1.6275 | 0.0090 | 0.2754 | ok | RAN |
| SOLUSDT | 8 | `sma2360_above_at_h` | one_head_filter_pi_star | 70 | 5.7088 | 1.5661 | 0.6286 | 1.5488 | 0.0088 | 0.2714 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2360_above_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3638 | 0.2727 | -1.8830 | -0.0964 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
