# Autonomy public-indicator hunt gen 1822

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T162358Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma462_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1754 | 0.5968 | 1.0131 | 0.0052 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `wma462_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1190 | 0.5856 | 0.7135 | 0.0037 | 0.1989 | ok | RAN |
| SOLUSDT | 8 | `wma462_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0892 | 0.5714 | 0.4975 | 0.0018 | 0.1657 | ok | RAN |
| SOLUSDT | 4 | `wma462_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0262 | 0.5405 | 0.1502 | 0.0005 | 0.1027 | ok | RAN |
| SOLUSDT | 4 | `wma462_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.0208 | 0.5697 | 0.1163 | 0.0004 | 0.1515 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma462_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 0.9749 | 0.5355 | -0.1464 | -0.0005 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma462_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 0.8079 | 0.5323 | -1.2349 | -0.0079 | 0.0914 | ok | RAN |
| ETHUSDT | 8 | `wma462_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.7881 | 0.5251 | -1.3304 | -0.0090 | 0.0950 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma462_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma462_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma462_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma462_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma462_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma462_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma462_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma462_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma462_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma462_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma462_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma462_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma462_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma462_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma462_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma462_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
