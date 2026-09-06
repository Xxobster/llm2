# Autonomy public-indicator hunt gen 1160

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T061442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2500_above_at_h` | one_head_filter_pi_star | 48 | 4.3420 | 1.4689 | 0.6250 | 1.1210 | 0.0168 | 0.2708 | ok | RAN |
| ETHUSDT | 8 | `sma2500_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5968 | 0.6422 | 3.6802 | 0.0160 | 0.3109 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2500_below_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 1.5844 | 0.6366 | 3.4701 | 0.0155 | 0.3168 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2500_above_at_h` | one_head_filter_pi_star | 49 | 4.4325 | 1.3361 | 0.5918 | 0.8979 | 0.0133 | 0.3061 | ok | RAN |
| SOLUSDT | 4 | `sma2500_below_at_h` | one_head_filter_pi_star | 305 | 24.9401 | 1.7100 | 0.6361 | 3.9122 | 0.0113 | 0.3311 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2500_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 1.6946 | 0.6367 | 3.8551 | 0.0109 | 0.3312 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma2500_above_at_h` | one_head_filter_pi_star | 66 | 5.4256 | 1.7094 | 0.6364 | 1.8769 | 0.0098 | 0.2273 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2500_above_at_h` | one_head_filter_pi_star | 54 | 4.4394 | 1.5722 | 0.6296 | 1.3681 | 0.0075 | 0.2037 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2500_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2500_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
