# Autonomy public-indicator hunt gen 2006

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T095701Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma491_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1721 | 0.5967 | 0.9762 | 0.0051 | 0.1823 | ok | RAN |
| ETHUSDT | 4 | `wma491_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1157 | 0.5870 | 0.6998 | 0.0037 | 0.2011 | ok | RAN |
| SOLUSDT | 4 | `wma491_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.1017 | 0.5789 | 0.5501 | 0.0020 | 0.1637 | ok | RAN |
| SOLUSDT | 8 | `wma491_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0397 | 0.5405 | 0.2256 | 0.0007 | 0.1027 | ok | RAN |
| SOLUSDT | 8 | `wma491_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0079 | 0.5618 | 0.0470 | 0.0002 | 0.1685 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma491_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 0.9403 | 0.5238 | -0.3635 | -0.0011 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma491_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.7976 | 0.5333 | -1.2977 | -0.0085 | 0.1000 | ok | RAN |
| ETHUSDT | 4 | `wma491_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7928 | 0.5288 | -1.3615 | -0.0086 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma491_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma491_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma491_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma491_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma491_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma491_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma491_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma491_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma491_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma491_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma491_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma491_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma491_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma491_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma491_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma491_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
