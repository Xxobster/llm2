# Autonomy public-indicator hunt gen 150

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T191844Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma30_cross_up` | one_head_filter_pi_star | 31 | 2.5509 | 2.0902 | 0.7097 | 1.7300 | 0.0360 | 0.3226 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma30_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma30_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma30_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma30_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1870 | 0.6928 | 4.0616 | 0.0178 | 0.4157 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma30_cross_down` | one_head_filter_pi_star | 18 | 1.5241 | 3.7247 | 0.8333 | 2.0483 | 0.0177 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma30_cross_down` | one_head_filter_pi_star | 22 | 2.3468 | 1.5643 | 0.5455 | 0.9076 | 0.0107 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma30_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2074 | 0.5938 | 0.9563 | 0.0067 | 0.2062 | ok | RAN |
| ETHUSDT | 4 | `wma30_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0066 | 0.2062 | ok | RAN |
| SOLUSDT | 8 | `wma30_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3652 | 0.5915 | 1.9785 | 0.0054 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `wma30_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3575 | 0.5935 | 1.9516 | 0.0053 | 0.2430 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma30_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma30_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma30_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma30_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
