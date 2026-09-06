# Autonomy public-indicator hunt gen 609

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T010609Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1080_below_at_h` | one_head_filter_pi_star | 248 | 20.2593 | 1.7929 | 0.6613 | 3.9763 | 0.0193 | 0.3427 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1080_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 1.7293 | 0.6571 | 3.7198 | 0.0183 | 0.3469 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1080_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.7367 | 0.6377 | 3.7912 | 0.0115 | 0.3132 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1080_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.5981 | 0.6310 | 3.2801 | 0.0100 | 0.3063 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1080_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.5720 | 0.6356 | 2.1176 | 0.0088 | 0.2797 | ok | RAN |
| SOLUSDT | 4 | `ema1080_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.5003 | 0.6321 | 1.7599 | 0.0077 | 0.2925 | ok | RAN |
| ETHUSDT | 4 | `ema1080_above_at_h` | one_head_filter_pi_star | 130 | 10.7278 | 1.1001 | 0.5769 | 0.4543 | 0.0040 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `ema1080_above_at_h` | one_head_filter_pi_star | 115 | 9.4529 | 1.0710 | 0.5652 | 0.3096 | 0.0030 | 0.2261 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1080_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1080_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
