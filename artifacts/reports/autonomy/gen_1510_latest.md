# Autonomy public-indicator hunt gen 1510

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T034248Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma413_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9965 | 0.6963 | 4.4174 | 0.0235 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma413_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8920 | 0.6911 | 4.1135 | 0.0218 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma413_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1927 | 0.6941 | 4.0869 | 0.0168 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma413_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.0810 | 0.6784 | 3.9631 | 0.0157 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma413_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2710 | 0.5990 | 1.3995 | 0.0091 | 0.2188 | ok | RAN |
| ETHUSDT | 8 | `wma413_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2263 | 0.6011 | 1.1668 | 0.0079 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `wma413_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3587 | 0.5961 | 1.8649 | 0.0057 | 0.2562 | ok | RAN |
| SOLUSDT | 8 | `wma413_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2998 | 0.5874 | 1.6138 | 0.0049 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma413_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma413_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma413_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma413_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma413_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma413_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma413_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma413_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma413_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma413_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma413_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma413_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma413_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma413_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma413_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma413_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
