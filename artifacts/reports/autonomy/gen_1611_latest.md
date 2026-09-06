# Autonomy public-indicator hunt gen 1611

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T191120Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma689_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1284 | 0.5789 | 0.7294 | 0.0039 | 0.1930 | ok | RAN |
| ETHUSDT | 8 | `sma689_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1160 | 0.5699 | 0.7038 | 0.0036 | 0.1774 | ok | RAN |
| SOLUSDT | 8 | `sma689_above_at_h` | one_head_filter_pi_star | 109 | 8.9385 | 1.2046 | 0.5688 | 0.8289 | 0.0035 | 0.1193 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma689_above_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.0586 | 0.5352 | 0.2885 | 0.0011 | 0.1268 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma689_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 0.9495 | 0.5545 | -0.3104 | -0.0011 | 0.1436 | ok | RAN |
| SOLUSDT | 8 | `sma689_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 0.9269 | 0.5495 | -0.4548 | -0.0015 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma689_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.9032 | 0.5649 | -0.5284 | -0.0040 | 0.1104 | ok | RAN |
| ETHUSDT | 4 | `sma689_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8596 | 0.5533 | -0.7546 | -0.0059 | 0.1133 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma689_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma689_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma689_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma689_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma689_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma689_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma689_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma689_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma689_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma689_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma689_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma689_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma689_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma689_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma689_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma689_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
