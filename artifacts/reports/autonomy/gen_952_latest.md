# Autonomy public-indicator hunt gen 952

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T071354Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `sma1980_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1160 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1980_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5831 | 0.6396 | 3.5136 | 0.0156 | 0.3123 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma1980_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.5355 | 0.6375 | 3.2759 | 0.0147 | 0.3112 | ok | RAN |
| SOLUSDT | 8 | `sma1980_below_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 1.8644 | 0.6459 | 4.4464 | 0.0126 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1980_below_at_h` | one_head_filter_pi_star | 287 | 23.3480 | 1.8451 | 0.6446 | 4.2839 | 0.0122 | 0.3171 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1980_above_at_h` | one_head_filter_pi_star | 37 | 3.5692 | 1.2632 | 0.5946 | 0.6565 | 0.0109 | 0.2703 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma1980_above_at_h` | one_head_filter_pi_star | 65 | 5.4033 | 1.7175 | 0.6615 | 1.8099 | 0.0106 | 0.2923 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1980_above_at_h` | one_head_filter_pi_star | 44 | 3.8529 | 1.2567 | 0.5682 | 0.6680 | 0.0102 | 0.1818 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1980_above_at_h` | one_head_filter_pi_star | 77 | 6.4008 | 1.4875 | 0.6364 | 1.4678 | 0.0077 | 0.3117 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1980_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0611 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1980_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0910 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
