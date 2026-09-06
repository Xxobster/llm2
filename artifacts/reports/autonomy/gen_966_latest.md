# Autonomy public-indicator hunt gen 966

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T184532Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma510_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0406 | 0.6995 | 4.4688 | 0.0243 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma510_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8972 | 0.6891 | 4.1572 | 0.0216 | 0.3886 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma510_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1317 | 0.6813 | 4.2795 | 0.0158 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma510_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.9688 | 0.6649 | 3.8954 | 0.0142 | 0.3617 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma510_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2358 | 0.6010 | 1.2427 | 0.0081 | 0.2176 | ok | RAN |
| ETHUSDT | 8 | `wma510_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2278 | 0.5978 | 1.1993 | 0.0080 | 0.2179 | ok | RAN |
| SOLUSDT | 8 | `wma510_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4764 | 0.6075 | 2.2520 | 0.0074 | 0.2581 | ok | RAN |
| SOLUSDT | 4 | `wma510_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4382 | 0.6091 | 2.1506 | 0.0068 | 0.2589 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma510_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma510_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma510_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma510_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma510_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma510_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma510_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma510_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma510_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma510_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma510_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma510_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma510_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma510_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma510_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma510_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
