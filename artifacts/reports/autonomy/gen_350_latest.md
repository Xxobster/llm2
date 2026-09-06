# Autonomy public-indicator hunt gen 350

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T150758Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma125_cross_up` | one_head_filter_pi_star | 15 | 1.4626 | 32.0219 | 0.8667 | 3.4013 | 0.0511 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma125_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8790 | 0.6884 | 4.1442 | 0.0219 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma125_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.7460 | 0.6732 | 3.6739 | 0.0196 | 0.3659 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma125_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2863 | 0.6946 | 4.3609 | 0.0189 | 0.4072 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma125_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2600 | 0.6928 | 4.3146 | 0.0184 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma125_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.3216 | 0.6111 | 1.5224 | 0.0099 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `wma125_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2567 | 0.6033 | 1.2313 | 0.0083 | 0.2283 | ok | RAN |
| SOLUSDT | 8 | `wma125_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3186 | 0.5924 | 1.6925 | 0.0048 | 0.2559 | ok | RAN |
| SOLUSDT | 4 | `wma125_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.2925 | 0.5905 | 1.5881 | 0.0044 | 0.2476 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma125_cross_up` | one_head_filter_pi_star | 21 | 1.8223 | 0.6183 | 0.4286 | -0.9564 | -0.0177 | 0.2857 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma125_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma125_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma125_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma125_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
