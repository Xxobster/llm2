# Autonomy public-indicator hunt gen 1966

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T053611Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma484_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1405 | 0.5860 | 0.8207 | 0.0042 | 0.1882 | ok | RAN |
| ETHUSDT | 4 | `wma484_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.0812 | 0.5789 | 0.5104 | 0.0026 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma484_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0475 | 0.5435 | 0.2670 | 0.0009 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `wma484_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0341 | 0.5698 | 0.1956 | 0.0007 | 0.1570 | ok | RAN |
| SOLUSDT | 8 | `wma484_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.0213 | 0.5598 | 0.1224 | 0.0004 | 0.1576 | ok | RAN |
| SOLUSDT | 4 | `wma484_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.0080 | 0.5431 | 0.0480 | 0.0001 | 0.1066 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma484_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.7911 | 0.5263 | -1.3732 | -0.0087 | 0.1000 | ok | RAN |
| ETHUSDT | 8 | `wma484_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7680 | 0.5269 | -1.5110 | -0.0099 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma484_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma484_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma484_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma484_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
