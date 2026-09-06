# Autonomy public-indicator hunt gen 1112

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T003103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2380_above_at_h` | one_head_filter_pi_star | 60 | 5.2540 | 1.6232 | 0.6500 | 1.5987 | 0.0220 | 0.2333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2380_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.5833 | 0.6358 | 3.4649 | 0.0156 | 0.3086 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2380_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.5780 | 0.6364 | 3.4869 | 0.0155 | 0.3152 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2380_above_at_h` | one_head_filter_pi_star | 58 | 5.2466 | 1.3725 | 0.6207 | 1.0597 | 0.0148 | 0.2586 | ok | RAN |
| SOLUSDT | 4 | `sma2380_below_at_h` | one_head_filter_pi_star | 298 | 24.2429 | 1.8716 | 0.6611 | 4.4322 | 0.0130 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2380_below_at_h` | one_head_filter_pi_star | 303 | 24.7766 | 1.8062 | 0.6436 | 4.2081 | 0.0120 | 0.3267 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2380_above_at_h` | one_head_filter_pi_star | 56 | 4.6035 | 1.8061 | 0.6429 | 1.7996 | 0.0112 | 0.2857 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2380_above_at_h` | one_head_filter_pi_star | 60 | 4.9876 | 1.5617 | 0.6167 | 1.4273 | 0.0083 | 0.2833 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2380_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2380_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
