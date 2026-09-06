# Autonomy public-indicator hunt gen 694

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T064440Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma340_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9541 | 0.6898 | 4.2748 | 0.0224 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma340_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9357 | 0.6895 | 4.3234 | 0.0224 | 0.3842 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma340_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2655 | 0.7018 | 4.3172 | 0.0177 | 0.3918 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma340_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1515 | 0.6886 | 4.0810 | 0.0166 | 0.3832 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma340_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2633 | 0.5979 | 1.3688 | 0.0090 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `wma340_above_at_h` | one_head_filter_pi_star | 197 | 16.2567 | 1.2444 | 0.5990 | 1.2841 | 0.0084 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `wma340_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3940 | 0.5961 | 2.0134 | 0.0062 | 0.2611 | ok | RAN |
| SOLUSDT | 8 | `wma340_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3145 | 0.5920 | 1.6678 | 0.0050 | 0.2537 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma340_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma340_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
