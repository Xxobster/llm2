# Autonomy public-indicator hunt gen 769

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T123721Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1480_below_at_h` | one_head_filter_pi_star | 11 | 1.3908 | 3.4002 | 0.7273 | 1.9525 | 0.1323 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1480_below_at_h` | one_head_filter_pi_star | 289 | 23.6087 | 1.7468 | 0.6574 | 4.0067 | 0.0179 | 0.3218 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1480_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6730 | 0.6554 | 3.7510 | 0.0169 | 0.3243 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1480_above_at_h` | one_head_filter_pi_star | 61 | 5.1907 | 1.3359 | 0.6066 | 0.9710 | 0.0125 | 0.2623 | ok | RAN |
| SOLUSDT | 8 | `ema1480_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 1.7077 | 0.6326 | 3.6312 | 0.0116 | 0.3295 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1480_below_at_h` | one_head_filter_pi_star | 276 | 22.5688 | 1.6709 | 0.6304 | 3.6138 | 0.0111 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1480_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.7259 | 0.6697 | 2.4370 | 0.0104 | 0.2661 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1480_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.5627 | 0.6476 | 1.9011 | 0.0081 | 0.2571 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1480_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.0041 | 0.5577 | 0.0128 | 0.0002 | 0.1923 | ok | RAN |
| BTCUSDT | 8 | `ema1480_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1480_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
