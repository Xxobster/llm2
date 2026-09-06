# Autonomy public-indicator hunt gen 1004

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T105531Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1590_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1590_below_at_h` | one_head_filter_pi_star | 314 | 25.6509 | 1.6533 | 0.6497 | 3.8092 | 0.0166 | 0.3185 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1590_below_at_h` | one_head_filter_pi_star | 303 | 24.7523 | 1.5950 | 0.6436 | 3.3766 | 0.0154 | 0.3168 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1590_below_at_h` | one_head_filter_pi_star | 288 | 23.5500 | 1.7701 | 0.6458 | 4.1489 | 0.0120 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1590_below_at_h` | one_head_filter_pi_star | 284 | 23.2229 | 1.7522 | 0.6444 | 3.9156 | 0.0118 | 0.3345 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1590_above_at_h` | one_head_filter_pi_star | 102 | 8.3171 | 1.5589 | 0.6275 | 1.8910 | 0.0088 | 0.2451 | ok | RAN |
| SOLUSDT | 4 | `ema1590_above_at_h` | one_head_filter_pi_star | 90 | 7.3399 | 1.5958 | 0.6556 | 1.8082 | 0.0084 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `ema1590_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.1954 | 0.5769 | 0.5726 | 0.0082 | 0.2885 | ok | RAN |
| ETHUSDT | 4 | `ema1590_above_at_h` | one_head_filter_pi_star | 43 | 3.7814 | 1.0427 | 0.5581 | 0.1191 | 0.0017 | 0.2791 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1590_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0454 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1590_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1590_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
