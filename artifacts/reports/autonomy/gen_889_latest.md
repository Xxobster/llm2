# Autonomy public-indicator hunt gen 889

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T001838Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1780_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1780_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.5708 | 0.6372 | 3.5314 | 0.0155 | 0.3097 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1780_below_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.5763 | 0.6411 | 3.4765 | 0.0154 | 0.3098 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1780_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.8326 | 0.6545 | 4.1866 | 0.0132 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1780_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.8079 | 0.6460 | 4.0924 | 0.0129 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1780_above_at_h` | one_head_filter_pi_star | 89 | 7.2583 | 1.3865 | 0.6292 | 1.2256 | 0.0058 | 0.2472 | ok | RAN |
| ETHUSDT | 4 | `ema1780_above_at_h` | one_head_filter_pi_star | 61 | 5.2220 | 1.1363 | 0.5902 | 0.4422 | 0.0056 | 0.2295 | ok | RAN |
| SOLUSDT | 8 | `ema1780_above_at_h` | one_head_filter_pi_star | 95 | 7.7468 | 1.3935 | 0.6211 | 1.3344 | 0.0056 | 0.2421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1780_above_at_h` | one_head_filter_pi_star | 43 | 3.7814 | 1.0183 | 0.5581 | 0.0514 | 0.0008 | 0.2558 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1780_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1780_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0827 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
