# Autonomy public-indicator hunt gen 1596

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T173958Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema987_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.3130 | 0.6161 | 1.2277 | 0.0052 | 0.1429 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema987_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.0593 | 0.5690 | 0.2635 | 0.0011 | 0.1379 | ok | RAN |
| SOLUSDT | 8 | `ema987_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.0106 | 0.5502 | 0.0709 | 0.0002 | 0.1245 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema987_above_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 0.9895 | 0.5649 | -0.0489 | -0.0004 | 0.1221 | ok | RAN |
| ETHUSDT | 4 | `ema987_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 0.9633 | 0.5519 | -0.2442 | -0.0012 | 0.1604 | ok | RAN |
| SOLUSDT | 4 | `ema987_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9265 | 0.5312 | -0.5145 | -0.0016 | 0.1328 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema987_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 0.9361 | 0.5405 | -0.4408 | -0.0020 | 0.1532 | ok | RAN |
| ETHUSDT | 4 | `ema987_above_at_h` | one_head_filter_pi_star | 133 | 10.9763 | 0.9411 | 0.5564 | -0.2874 | -0.0025 | 0.1128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema987_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema987_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema987_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema987_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema987_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema987_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema987_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema987_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema987_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema987_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema987_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema987_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema987_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema987_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema987_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema987_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
