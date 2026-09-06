# Autonomy public-indicator hunt gen 697

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T065650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1300_below_at_h` | one_head_filter_pi_star | 280 | 22.8734 | 1.7661 | 0.6607 | 4.0251 | 0.0184 | 0.3286 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1300_below_at_h` | one_head_filter_pi_star | 255 | 20.8312 | 1.7454 | 0.6471 | 3.8068 | 0.0178 | 0.3412 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1300_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.6988 | 0.6316 | 3.7329 | 0.0114 | 0.3228 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1300_below_at_h` | one_head_filter_pi_star | 291 | 23.7953 | 1.6400 | 0.6289 | 3.5572 | 0.0104 | 0.3162 | ok | RAN |
| SOLUSDT | 8 | `ema1300_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.7547 | 0.6698 | 2.4446 | 0.0102 | 0.2642 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema1300_above_at_h` | one_head_filter_pi_star | 83 | 6.8499 | 1.2257 | 0.5904 | 0.7773 | 0.0084 | 0.2410 | ok | RAN |
| SOLUSDT | 4 | `ema1300_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.5543 | 0.6296 | 1.8765 | 0.0079 | 0.2778 | ok | RAN |
| ETHUSDT | 8 | `ema1300_above_at_h` | one_head_filter_pi_star | 77 | 6.3547 | 1.1509 | 0.5714 | 0.5320 | 0.0063 | 0.2208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1300_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1300_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
