# Autonomy public-indicator hunt gen 1598

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T175249Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma427_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1166 | 0.5842 | 0.7111 | 0.0036 | 0.1895 | ok | RAN |
| SOLUSDT | 4 | `wma427_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.1274 | 0.5805 | 0.6969 | 0.0026 | 0.1609 | ok | RAN |
| SOLUSDT | 8 | `wma427_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.1166 | 0.5818 | 0.6093 | 0.0023 | 0.1576 | ok | RAN |
| ETHUSDT | 4 | `wma427_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.0605 | 0.5824 | 0.3730 | 0.0019 | 0.1923 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma427_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 0.9873 | 0.5412 | -0.0765 | -0.0002 | 0.1031 | ok | RAN |
| SOLUSDT | 4 | `wma427_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 0.9670 | 0.5355 | -0.1923 | -0.0006 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma427_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8454 | 0.5297 | -0.9638 | -0.0063 | 0.0973 | ok | RAN |
| ETHUSDT | 8 | `wma427_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8415 | 0.5410 | -0.9790 | -0.0063 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma427_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma427_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma427_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma427_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma427_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma427_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma427_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma427_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma427_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma427_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma427_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma427_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma427_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma427_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma427_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma427_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
