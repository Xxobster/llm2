# Autonomy public-indicator hunt gen 235

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T005717Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma58_cross_up` | one_head_filter_pi_star | 21 | 1.7498 | 4.5249 | 0.6667 | 2.5303 | 0.0372 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma58_cross_down` | one_head_filter_pi_star | 27 | 2.2374 | 2.1533 | 0.6296 | 1.6715 | 0.0268 | 0.2963 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma58_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8037 | 0.6776 | 3.8312 | 0.0213 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma58_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.7043 | 0.6667 | 3.5118 | 0.0193 | 0.3667 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma58_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1986 | 0.6914 | 4.1853 | 0.0183 | 0.4074 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma58_below_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.1602 | 0.6855 | 3.9904 | 0.0179 | 0.4151 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma58_cross_down` | one_head_filter_pi_star | 30 | 2.5605 | 1.4147 | 0.6333 | 0.7668 | 0.0083 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma58_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2600 | 0.6038 | 1.1721 | 0.0079 | 0.2138 | ok | RAN |
| ETHUSDT | 8 | `sma58_above_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.2257 | 0.6024 | 1.0532 | 0.0070 | 0.2169 | ok | RAN |
| SOLUSDT | 4 | `sma58_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.4104 | 0.6103 | 2.1004 | 0.0059 | 0.2535 | ok | RAN |
| SOLUSDT | 8 | `sma58_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3591 | 0.5991 | 1.9045 | 0.0053 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma58_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma58_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `sma58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma58_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma58_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
