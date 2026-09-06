# Autonomy public-indicator hunt gen 817

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T171547Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1600_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1600_below_at_h` | one_head_filter_pi_star | 306 | 24.9974 | 1.6283 | 0.6471 | 3.5544 | 0.0160 | 0.3170 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1600_below_at_h` | one_head_filter_pi_star | 310 | 25.3242 | 1.5881 | 0.6452 | 3.4467 | 0.0155 | 0.3194 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1600_below_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.7666 | 0.6466 | 3.9723 | 0.0122 | 0.3322 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1600_below_at_h` | one_head_filter_pi_star | 294 | 24.0406 | 1.6861 | 0.6361 | 3.8050 | 0.0111 | 0.3197 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema1600_above_at_h` | one_head_filter_pi_star | 46 | 4.0453 | 1.2572 | 0.6087 | 0.6659 | 0.0097 | 0.2826 | ok | RAN |
| SOLUSDT | 4 | `ema1600_above_at_h` | one_head_filter_pi_star | 89 | 7.2571 | 1.6059 | 0.6629 | 1.9337 | 0.0090 | 0.2472 | ok | RAN |
| SOLUSDT | 8 | `ema1600_above_at_h` | one_head_filter_pi_star | 89 | 7.2583 | 1.6511 | 0.6404 | 1.9820 | 0.0088 | 0.2360 | ok | RAN |
| ETHUSDT | 8 | `ema1600_above_at_h` | one_head_filter_pi_star | 47 | 4.1332 | 1.1998 | 0.5957 | 0.5367 | 0.0078 | 0.2340 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1600_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1600_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0655 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
