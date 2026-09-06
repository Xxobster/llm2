# Autonomy public-indicator hunt gen 1942

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T032253Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma481_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1440 | 0.5864 | 0.8556 | 0.0044 | 0.1885 | ok | RAN |
| ETHUSDT | 4 | `wma481_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1317 | 0.5812 | 0.8065 | 0.0041 | 0.1937 | ok | RAN |
| SOLUSDT | 4 | `wma481_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.0631 | 0.5661 | 0.3630 | 0.0013 | 0.1481 | ok | RAN |
| SOLUSDT | 8 | `wma481_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0481 | 0.5604 | 0.2805 | 0.0010 | 0.1593 | ok | RAN |
| SOLUSDT | 8 | `wma481_above_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.0329 | 0.5439 | 0.1801 | 0.0006 | 0.0994 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma481_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 0.9768 | 0.5361 | -0.1390 | -0.0004 | 0.1082 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma481_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8394 | 0.5405 | -0.9975 | -0.0065 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `wma481_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8123 | 0.5319 | -1.2000 | -0.0077 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma481_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5135 | 0.2941 | -1.0520 | -0.0487 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma481_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma481_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma481_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma481_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma481_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma481_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma481_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma481_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma481_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma481_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma481_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma481_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma481_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma481_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma481_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
