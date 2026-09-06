# Autonomy public-indicator hunt gen 1032

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T143318Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2180_above_at_h` | one_head_filter_pi_star | 58 | 5.1006 | 1.5626 | 0.6207 | 1.4362 | 0.0220 | 0.2586 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2180_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5708 | 0.6366 | 3.5066 | 0.0155 | 0.3123 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2180_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5544 | 0.6377 | 3.4474 | 0.0149 | 0.3084 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2180_above_at_h` | one_head_filter_pi_star | 73 | 6.0683 | 1.8109 | 0.6712 | 2.1412 | 0.0120 | 0.3014 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2180_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 1.7874 | 0.6441 | 4.0407 | 0.0118 | 0.3119 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2180_below_at_h` | one_head_filter_pi_star | 315 | 25.6259 | 1.7758 | 0.6413 | 4.1280 | 0.0113 | 0.3206 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2180_above_at_h` | one_head_filter_pi_star | 50 | 4.3783 | 1.2588 | 0.6000 | 0.7041 | 0.0109 | 0.2400 | ok | RAN |
| SOLUSDT | 4 | `sma2180_above_at_h` | one_head_filter_pi_star | 49 | 4.0732 | 1.7305 | 0.6531 | 1.7312 | 0.0106 | 0.2857 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2180_above_at_h` | one_head_filter_pi_star | 13 | 2.3874 | 0.3214 | 0.2308 | -2.2413 | -0.0925 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2180_above_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3638 | 0.2727 | -1.8830 | -0.0964 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
