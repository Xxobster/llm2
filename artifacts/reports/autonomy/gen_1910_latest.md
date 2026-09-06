# Autonomy public-indicator hunt gen 1910

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T001901Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma476_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1738 | 0.5968 | 0.9981 | 0.0052 | 0.1828 | ok | RAN |
| ETHUSDT | 4 | `wma476_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.1439 | 0.5855 | 0.8712 | 0.0044 | 0.1917 | ok | RAN |
| SOLUSDT | 4 | `wma476_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.0439 | 0.5655 | 0.2456 | 0.0009 | 0.1607 | ok | RAN |
| SOLUSDT | 8 | `wma476_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.0246 | 0.5367 | 0.1382 | 0.0005 | 0.0960 | ok | RAN |
| SOLUSDT | 4 | `wma476_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.0096 | 0.5361 | 0.0569 | 0.0002 | 0.1031 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma476_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9630 | 0.5519 | -0.2185 | -0.0008 | 0.1639 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma476_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8257 | 0.5365 | -1.1066 | -0.0070 | 0.0938 | ok | RAN |
| ETHUSDT | 8 | `wma476_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.7963 | 0.5405 | -1.3230 | -0.0084 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma476_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma476_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma476_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma476_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma476_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma476_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma476_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma476_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma476_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma476_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma476_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma476_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma476_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma476_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma476_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma476_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
