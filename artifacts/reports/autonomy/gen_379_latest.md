# Autonomy public-indicator hunt gen 379

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T213000Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma154_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8642 | 0.6806 | 4.0627 | 0.0212 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma154_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8112 | 0.6769 | 3.8305 | 0.0204 | 0.3744 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma154_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2821 | 0.6971 | 4.3954 | 0.0176 | 0.3771 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma154_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2810 | 0.6927 | 4.4961 | 0.0174 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma154_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.3233 | 0.6108 | 1.5196 | 0.0106 | 0.2270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma154_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.3030 | 0.6126 | 1.4577 | 0.0100 | 0.2304 | ok | RAN |
| SOLUSDT | 8 | `sma154_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3361 | 0.5950 | 1.7515 | 0.0053 | 0.2550 | ok | RAN |
| SOLUSDT | 4 | `sma154_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.2871 | 0.5911 | 1.5365 | 0.0046 | 0.2611 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma154_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma154_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma154_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma154_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma154_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma154_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma154_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma154_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma154_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma154_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma154_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma154_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma154_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma154_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma154_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma154_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
