# Autonomy public-indicator hunt gen 825

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T180045Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1620_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1620_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1620_below_at_h` | one_head_filter_pi_star | 319 | 26.0594 | 1.6579 | 0.6489 | 3.8730 | 0.0169 | 0.3166 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1620_below_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 1.6105 | 0.6446 | 3.6790 | 0.0163 | 0.3133 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1620_above_at_h` | one_head_filter_pi_star | 49 | 4.3091 | 1.3766 | 0.6122 | 0.9661 | 0.0141 | 0.2653 | ok | RAN |
| SOLUSDT | 8 | `ema1620_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.7108 | 0.6397 | 3.7542 | 0.0116 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1620_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.7282 | 0.6380 | 3.8968 | 0.0116 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1620_above_at_h` | one_head_filter_pi_star | 99 | 8.0725 | 1.5908 | 0.6364 | 1.8978 | 0.0083 | 0.2525 | ok | RAN |
| SOLUSDT | 8 | `ema1620_above_at_h` | one_head_filter_pi_star | 91 | 7.4214 | 1.5747 | 0.6374 | 1.7677 | 0.0081 | 0.2418 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1620_above_at_h` | one_head_filter_pi_star | 40 | 3.6184 | 1.0303 | 0.5500 | 0.0846 | 0.0013 | 0.2750 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1620_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0415 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1620_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
