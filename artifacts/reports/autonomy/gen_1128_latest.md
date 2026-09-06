# Autonomy public-indicator hunt gen 1128

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T022002Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2420_above_at_h` | one_head_filter_pi_star | 59 | 5.1885 | 1.4927 | 0.6271 | 1.3926 | 0.0189 | 0.2712 | ok | RAN |
| ETHUSDT | 4 | `sma2420_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5934 | 0.6396 | 3.5487 | 0.0158 | 0.3093 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2420_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5410 | 0.6361 | 3.3886 | 0.0148 | 0.3077 | ok | RAN |
| SOLUSDT | 4 | `sma2420_below_at_h` | one_head_filter_pi_star | 301 | 24.6130 | 1.9201 | 0.6678 | 4.7059 | 0.0133 | 0.3223 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2420_above_at_h` | one_head_filter_pi_star | 53 | 4.7943 | 1.3481 | 0.6038 | 0.9266 | 0.0129 | 0.2075 | ok | RAN |
| SOLUSDT | 8 | `sma2420_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 1.7662 | 0.6483 | 4.0813 | 0.0119 | 0.3310 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2420_above_at_h` | one_head_filter_pi_star | 64 | 5.2612 | 1.8855 | 0.6562 | 1.9446 | 0.0108 | 0.2031 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2420_above_at_h` | one_head_filter_pi_star | 75 | 6.1166 | 1.6482 | 0.6400 | 1.7762 | 0.0092 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2420_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2420_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
