# Autonomy public-indicator hunt gen 1094

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T221419Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma590_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0570 | 0.6995 | 4.5763 | 0.0242 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma590_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0246 | 0.6931 | 4.4588 | 0.0237 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma590_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.9267 | 0.6667 | 3.8162 | 0.0139 | 0.3590 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma590_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7953 | 0.6537 | 3.5262 | 0.0122 | 0.3512 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma590_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.6030 | 0.6230 | 2.8224 | 0.0090 | 0.2618 | ok | RAN |
| ETHUSDT | 8 | `wma590_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2608 | 0.6120 | 1.3792 | 0.0089 | 0.2186 | ok | RAN |
| SOLUSDT | 8 | `wma590_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.5305 | 0.6056 | 2.4320 | 0.0084 | 0.2667 | ok | RAN |
| ETHUSDT | 4 | `wma590_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2215 | 0.5950 | 1.1906 | 0.0079 | 0.2100 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma590_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma590_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma590_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma590_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma590_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma590_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
