# Autonomy public-indicator hunt gen 2310

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T015214Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma538_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1856 | 0.5955 | 1.0484 | 0.0055 | 0.1854 | ok | RAN |
| ETHUSDT | 4 | `wma538_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1400 | 0.5932 | 0.8150 | 0.0044 | 0.1977 | ok | RAN |
| SOLUSDT | 8 | `wma538_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.1453 | 0.5531 | 0.7747 | 0.0026 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `wma538_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0471 | 0.5683 | 0.2750 | 0.0010 | 0.1530 | ok | RAN |
| SOLUSDT | 4 | `wma538_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0213 | 0.5304 | 0.1225 | 0.0004 | 0.0994 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma538_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.0037 | 0.5580 | 0.0218 | 0.0001 | 0.1492 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma538_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8124 | 0.5368 | -1.2215 | -0.0079 | 0.0947 | ok | RAN |
| ETHUSDT | 8 | `wma538_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7860 | 0.5236 | -1.3970 | -0.0089 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma538_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma538_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma538_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma538_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma538_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma538_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma538_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma538_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma538_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma538_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma538_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma538_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma538_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma538_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma538_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma538_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
