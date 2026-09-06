# Autonomy public-indicator hunt gen 878

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T231234Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma455_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0002 | 0.6947 | 4.4643 | 0.0233 | 0.3895 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma455_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9442 | 0.6907 | 4.2483 | 0.0228 | 0.3814 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma455_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2697 | 0.6994 | 4.3590 | 0.0172 | 0.3815 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma455_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.0458 | 0.6809 | 4.1203 | 0.0154 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma455_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2456 | 0.5989 | 1.2599 | 0.0084 | 0.2246 | ok | RAN |
| ETHUSDT | 8 | `wma455_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1902 | 0.6021 | 1.0152 | 0.0069 | 0.2147 | ok | RAN |
| SOLUSDT | 8 | `wma455_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4138 | 0.6041 | 2.0799 | 0.0064 | 0.2589 | ok | RAN |
| SOLUSDT | 4 | `wma455_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3470 | 0.5950 | 1.7905 | 0.0055 | 0.2600 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma455_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma455_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma455_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma455_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
