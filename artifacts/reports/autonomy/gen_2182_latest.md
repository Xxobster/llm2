# Autonomy public-indicator hunt gen 2182

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T101149Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma518_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1209 | 0.5873 | 0.7280 | 0.0038 | 0.1905 | ok | RAN |
| ETHUSDT | 4 | `wma518_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1027 | 0.5820 | 0.6171 | 0.0032 | 0.1905 | ok | RAN |
| SOLUSDT | 4 | `wma518_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.1207 | 0.5801 | 0.6760 | 0.0024 | 0.1547 | ok | RAN |
| SOLUSDT | 8 | `wma518_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.0345 | 0.5464 | 0.2042 | 0.0006 | 0.1031 | ok | RAN |
| SOLUSDT | 8 | `wma518_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0150 | 0.5574 | 0.0893 | 0.0003 | 0.1585 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma518_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 0.9440 | 0.5179 | -0.3429 | -0.0011 | 0.1026 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma518_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8074 | 0.5243 | -1.2357 | -0.0080 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `wma518_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 0.7660 | 0.5134 | -1.5419 | -0.0099 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma518_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma518_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma518_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma518_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma518_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma518_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma518_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma518_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma518_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma518_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma518_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma518_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma518_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma518_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma518_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma518_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
