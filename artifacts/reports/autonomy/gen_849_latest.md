# Autonomy public-indicator hunt gen 849

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T201937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1680_below_at_h` | one_head_filter_pi_star | 303 | 24.7523 | 1.5913 | 0.6436 | 3.4351 | 0.0155 | 0.3234 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1680_below_at_h` | one_head_filter_pi_star | 318 | 25.9777 | 1.5780 | 0.6447 | 3.3856 | 0.0154 | 0.3145 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1680_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.8712 | 0.6559 | 4.1169 | 0.0134 | 0.3198 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1680_below_at_h` | one_head_filter_pi_star | 278 | 22.7323 | 1.7844 | 0.6475 | 4.0885 | 0.0126 | 0.3237 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1680_above_at_h` | one_head_filter_pi_star | 84 | 6.8505 | 1.7592 | 0.6786 | 2.1599 | 0.0105 | 0.2500 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1680_above_at_h` | one_head_filter_pi_star | 51 | 4.4850 | 1.2654 | 0.6078 | 0.7407 | 0.0103 | 0.2549 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1680_above_at_h` | one_head_filter_pi_star | 93 | 7.5845 | 1.5357 | 0.6237 | 1.6484 | 0.0076 | 0.2581 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1680_above_at_h` | one_head_filter_pi_star | 45 | 3.9573 | 0.9509 | 0.5333 | -0.1455 | -0.0020 | 0.2667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1680_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1680_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
