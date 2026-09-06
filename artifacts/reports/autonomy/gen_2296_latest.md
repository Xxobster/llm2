# Autonomy public-indicator hunt gen 2296

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T001328Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5340_above_at_h` | one_head_filter_pi_star | 58 | 4.9388 | 1.7833 | 0.6379 | 1.6336 | 0.0117 | 0.1034 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5340_above_at_h` | one_head_filter_pi_star | 63 | 5.3646 | 1.5826 | 0.6032 | 1.4708 | 0.0091 | 0.1270 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5340_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.0043 | 0.5634 | 0.0337 | 0.0001 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5340_below_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 0.9682 | 0.5344 | -0.2481 | -0.0006 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `sma5340_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9691 | 0.5533 | -0.2490 | -0.0010 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma5340_below_at_h` | one_head_filter_pi_star | 307 | 25.1037 | 0.9147 | 0.5277 | -0.6612 | -0.0018 | 0.1336 | ok | RAN |
| ETHUSDT | 8 | `sma5340_above_at_h` | one_head_filter_pi_star | 28 | 8.4494 | 0.9120 | 0.5000 | -0.3632 | -0.0038 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `sma5340_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.8337 | 0.5000 | -0.8421 | -0.0090 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
