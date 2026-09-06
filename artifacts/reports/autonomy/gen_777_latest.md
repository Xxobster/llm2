# Autonomy public-indicator hunt gen 777

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T132351Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1500_below_at_h` | one_head_filter_pi_star | 303 | 24.7523 | 1.7232 | 0.6601 | 3.9371 | 0.0180 | 0.3168 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1500_below_at_h` | one_head_filter_pi_star | 301 | 24.5889 | 1.6203 | 0.6478 | 3.5472 | 0.0159 | 0.3256 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1500_below_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.7587 | 0.6431 | 4.0000 | 0.0121 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1500_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.7078 | 0.6400 | 3.7279 | 0.0114 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1500_above_at_h` | one_head_filter_pi_star | 85 | 6.9321 | 1.7620 | 0.6824 | 2.2101 | 0.0107 | 0.2588 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema1500_above_at_h` | one_head_filter_pi_star | 56 | 4.6216 | 1.2547 | 0.5893 | 0.6973 | 0.0094 | 0.2321 | ok | RAN |
| ETHUSDT | 4 | `ema1500_above_at_h` | one_head_filter_pi_star | 53 | 4.5099 | 1.2048 | 0.5849 | 0.5941 | 0.0075 | 0.2264 | ok | RAN |
| SOLUSDT | 4 | `ema1500_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.4557 | 0.6455 | 1.6407 | 0.0070 | 0.2818 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1500_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1500_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
