# Autonomy public-indicator hunt gen 470

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T155755Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma200_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9466 | 0.6904 | 4.4144 | 0.0226 | 0.3655 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma200_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9718 | 0.6898 | 4.3962 | 0.0225 | 0.3690 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma200_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2344 | 0.6936 | 4.3409 | 0.0175 | 0.3815 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma200_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1757 | 0.6941 | 4.1509 | 0.0173 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma200_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1897 | 0.6011 | 1.0014 | 0.0066 | 0.2234 | ok | RAN |
| ETHUSDT | 8 | `wma200_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.1845 | 0.5944 | 0.9328 | 0.0063 | 0.2111 | ok | RAN |
| SOLUSDT | 8 | `wma200_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3501 | 0.5972 | 1.8359 | 0.0054 | 0.2654 | ok | RAN |
| SOLUSDT | 4 | `wma200_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.2653 | 0.5813 | 1.4175 | 0.0042 | 0.2611 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma200_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma200_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
