# Autonomy public-indicator hunt gen 1798

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T141353Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma458_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1435 | 0.5882 | 0.8450 | 0.0044 | 0.1925 | ok | RAN |
| ETHUSDT | 4 | `wma458_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.0899 | 0.5789 | 0.5614 | 0.0028 | 0.1947 | ok | RAN |
| SOLUSDT | 8 | `wma458_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0992 | 0.5771 | 0.5513 | 0.0021 | 0.1657 | ok | RAN |
| SOLUSDT | 4 | `wma458_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0898 | 0.5747 | 0.5000 | 0.0018 | 0.1609 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma458_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 0.9856 | 0.5424 | -0.0837 | -0.0003 | 0.1017 | ok | RAN |
| SOLUSDT | 4 | `wma458_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 0.9820 | 0.5412 | -0.1073 | -0.0003 | 0.1031 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma458_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8360 | 0.5393 | -1.0275 | -0.0065 | 0.0942 | ok | RAN |
| ETHUSDT | 8 | `wma458_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8148 | 0.5410 | -1.1395 | -0.0075 | 0.0874 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma458_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma458_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma458_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma458_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma458_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma458_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma458_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma458_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma458_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma458_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma458_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma458_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma458_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma458_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma458_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma458_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
