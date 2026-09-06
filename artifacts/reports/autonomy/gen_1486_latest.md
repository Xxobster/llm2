# Autonomy public-indicator hunt gen 1486

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T012922Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma409_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9497 | 0.6957 | 4.3184 | 0.0222 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma409_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8779 | 0.6878 | 3.9632 | 0.0216 | 0.3862 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma409_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2655 | 0.6983 | 4.5288 | 0.0177 | 0.3855 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma409_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2483 | 0.6994 | 4.4049 | 0.0173 | 0.3699 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma409_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2261 | 0.5949 | 1.1739 | 0.0078 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `wma409_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.1990 | 0.5944 | 1.0340 | 0.0070 | 0.2167 | ok | RAN |
| SOLUSDT | 4 | `wma409_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.4368 | 0.6051 | 2.1628 | 0.0069 | 0.2667 | ok | RAN |
| SOLUSDT | 8 | `wma409_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4213 | 0.6062 | 2.0907 | 0.0065 | 0.2591 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma409_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma409_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma409_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma409_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma409_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma409_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma409_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma409_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma409_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma409_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma409_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma409_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma409_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma409_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma409_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma409_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
