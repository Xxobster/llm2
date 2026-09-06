# Autonomy public-indicator hunt gen 1116

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T005835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema916_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.8351 | 0.6681 | 4.0212 | 0.0202 | 0.3489 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema916_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.7687 | 0.6651 | 3.4987 | 0.0183 | 0.3585 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema916_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.8421 | 0.6488 | 3.9494 | 0.0128 | 0.3017 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema916_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.7850 | 0.6462 | 2.7542 | 0.0111 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema916_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.6941 | 0.6411 | 3.4871 | 0.0111 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema916_above_at_h` | one_head_filter_pi_star | 134 | 11.0588 | 1.2153 | 0.5970 | 0.9862 | 0.0083 | 0.2313 | ok | RAN |
| SOLUSDT | 4 | `ema916_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.5629 | 0.6271 | 2.0231 | 0.0082 | 0.3220 | ok | RAN |
| ETHUSDT | 4 | `ema916_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 1.2046 | 0.6031 | 0.9092 | 0.0077 | 0.2137 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema916_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema916_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema916_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema916_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema916_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema916_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema916_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema916_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema916_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema916_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema916_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema916_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema916_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema916_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema916_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema916_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
