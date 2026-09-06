# Autonomy public-indicator hunt gen 1048

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T162033Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2220_above_at_h` | one_head_filter_pi_star | 46 | 4.5162 | 1.5836 | 0.6304 | 1.4520 | 0.0209 | 0.2609 | ok | RAN |
| ETHUSDT | 4 | `sma2220_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.5798 | 0.6389 | 3.4541 | 0.0154 | 0.3148 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2220_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5374 | 0.6393 | 3.4067 | 0.0146 | 0.3050 | ok | RAN |
| SOLUSDT | 4 | `sma2220_below_at_h` | one_head_filter_pi_star | 301 | 24.4869 | 1.7957 | 0.6412 | 4.1585 | 0.0116 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2220_below_at_h` | one_head_filter_pi_star | 296 | 24.0802 | 1.7439 | 0.6385 | 3.8943 | 0.0114 | 0.3176 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2220_above_at_h` | one_head_filter_pi_star | 59 | 4.9045 | 1.8009 | 0.6780 | 1.8120 | 0.0110 | 0.2881 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2220_above_at_h` | one_head_filter_pi_star | 72 | 5.9851 | 1.7668 | 0.6806 | 2.1285 | 0.0107 | 0.2778 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma2220_above_at_h` | one_head_filter_pi_star | 35 | 3.4363 | 1.1463 | 0.5714 | 0.3751 | 0.0060 | 0.2286 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
