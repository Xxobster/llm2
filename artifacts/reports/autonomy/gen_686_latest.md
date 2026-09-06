# Autonomy public-indicator hunt gen 686

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T061041Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma335_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0919 | 0.7049 | 4.6795 | 0.0250 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma335_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0342 | 0.7011 | 4.4947 | 0.0239 | 0.3804 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma335_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2980 | 0.7011 | 4.4704 | 0.0181 | 0.3908 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma335_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2583 | 0.6951 | 4.2000 | 0.0174 | 0.3841 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma335_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2757 | 0.5979 | 1.4063 | 0.0093 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `wma335_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2051 | 0.5939 | 1.1003 | 0.0071 | 0.2081 | ok | RAN |
| SOLUSDT | 8 | `wma335_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3382 | 0.6031 | 1.7521 | 0.0054 | 0.2629 | ok | RAN |
| SOLUSDT | 4 | `wma335_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.3154 | 0.5882 | 1.6678 | 0.0051 | 0.2598 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma335_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma335_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma335_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma335_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
