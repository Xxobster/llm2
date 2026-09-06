# Autonomy public-indicator hunt gen 2166

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T072750Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma516_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1533 | 0.6000 | 0.9184 | 0.0047 | 0.1947 | ok | RAN |
| ETHUSDT | 8 | `wma516_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1031 | 0.5829 | 0.6117 | 0.0032 | 0.1872 | ok | RAN |
| SOLUSDT | 4 | `wma516_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0597 | 0.5763 | 0.3435 | 0.0012 | 0.1582 | ok | RAN |
| SOLUSDT | 4 | `wma516_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0547 | 0.5464 | 0.3112 | 0.0010 | 0.0984 | ok | RAN |
| SOLUSDT | 8 | `wma516_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.0477 | 0.5487 | 0.2793 | 0.0009 | 0.1026 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma516_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9890 | 0.5519 | -0.0665 | -0.0002 | 0.1639 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma516_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 0.8324 | 0.5389 | -1.0467 | -0.0068 | 0.0889 | ok | RAN |
| ETHUSDT | 4 | `wma516_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8105 | 0.5312 | -1.2449 | -0.0077 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma516_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma516_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma516_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma516_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma516_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma516_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma516_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma516_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma516_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma516_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma516_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma516_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma516_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma516_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma516_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma516_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
