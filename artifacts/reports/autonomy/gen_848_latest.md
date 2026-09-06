# Autonomy public-indicator hunt gen 848

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T201254Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1720_below_at_h` | one_head_filter_pi_star | 299 | 24.4256 | 1.6845 | 0.6555 | 3.8582 | 0.0171 | 0.3244 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1720_above_at_h` | one_head_filter_pi_star | 49 | 4.2591 | 2.0247 | 0.7143 | 2.2809 | 0.0155 | 0.3469 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma1720_below_at_h` | one_head_filter_pi_star | 297 | 24.2622 | 1.5663 | 0.6431 | 3.3145 | 0.0148 | 0.3266 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1720_above_at_h` | one_head_filter_pi_star | 60 | 4.9876 | 1.9499 | 0.7000 | 2.2087 | 0.0139 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1720_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.7887 | 0.6333 | 4.1289 | 0.0117 | 0.3100 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1720_below_at_h` | one_head_filter_pi_star | 310 | 25.2191 | 1.7004 | 0.6290 | 3.9170 | 0.0107 | 0.3097 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1720_above_at_h` | one_head_filter_pi_star | 64 | 5.4459 | 1.2257 | 0.5781 | 0.6875 | 0.0089 | 0.2188 | ok | RAN |
| ETHUSDT | 4 | `sma1720_above_at_h` | one_head_filter_pi_star | 55 | 4.7745 | 1.0966 | 0.5818 | 0.3049 | 0.0041 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1720_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0611 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1720_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3351 | 0.2143 | -1.4392 | -0.0737 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
