# Autonomy public-indicator hunt gen 2070

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T180914Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma501_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.2011 | 0.5938 | 1.1756 | 0.0059 | 0.1823 | GATE_CAND | RAN |
| ETHUSDT | 4 | `wma501_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.0871 | 0.5798 | 0.5429 | 0.0028 | 0.1968 | ok | RAN |
| SOLUSDT | 8 | `wma501_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.1284 | 0.5506 | 0.6778 | 0.0022 | 0.1011 | ok | RAN |
| SOLUSDT | 4 | `wma501_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0323 | 0.5459 | 0.1838 | 0.0006 | 0.0973 | ok | RAN |
| SOLUSDT | 8 | `wma501_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0279 | 0.5562 | 0.1632 | 0.0006 | 0.1629 | ok | RAN |
| SOLUSDT | 4 | `wma501_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0058 | 0.5618 | 0.0334 | 0.0001 | 0.1573 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma501_above_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 0.8239 | 0.5287 | -1.0933 | -0.0071 | 0.0920 | ok | RAN |
| ETHUSDT | 4 | `wma501_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.7730 | 0.5260 | -1.4986 | -0.0096 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma501_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma501_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma501_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma501_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma501_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma501_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma501_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma501_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma501_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma501_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma501_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma501_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma501_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma501_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma501_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma501_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
