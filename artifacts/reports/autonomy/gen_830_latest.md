# Autonomy public-indicator hunt gen 830

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T183018Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma425_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9557 | 0.7016 | 4.2881 | 0.0226 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma425_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8560 | 0.6837 | 4.0183 | 0.0213 | 0.3878 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma425_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2622 | 0.6988 | 4.2088 | 0.0167 | 0.3855 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma425_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1698 | 0.6971 | 4.2461 | 0.0166 | 0.3829 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma425_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2773 | 0.6053 | 1.4236 | 0.0095 | 0.2263 | ok | RAN |
| ETHUSDT | 8 | `wma425_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2660 | 0.6053 | 1.3730 | 0.0090 | 0.2158 | ok | RAN |
| SOLUSDT | 4 | `wma425_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4327 | 0.6032 | 2.1044 | 0.0067 | 0.2646 | ok | RAN |
| SOLUSDT | 8 | `wma425_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3268 | 0.6000 | 1.6986 | 0.0053 | 0.2550 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma425_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma425_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma425_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma425_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
