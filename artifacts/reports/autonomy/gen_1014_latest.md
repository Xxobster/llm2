# Autonomy public-indicator hunt gen 1014

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T121054Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma540_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9641 | 0.6902 | 4.2284 | 0.0234 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma540_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9104 | 0.6907 | 4.1529 | 0.0218 | 0.3814 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma540_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 2.1053 | 0.6788 | 4.2564 | 0.0156 | 0.3575 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma540_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8866 | 0.6667 | 3.7354 | 0.0134 | 0.3590 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma540_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2490 | 0.6054 | 1.2864 | 0.0085 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `wma540_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4592 | 0.6099 | 2.2111 | 0.0072 | 0.2637 | ok | RAN |
| ETHUSDT | 4 | `wma540_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2027 | 0.5889 | 1.0780 | 0.0072 | 0.2167 | ok | RAN |
| SOLUSDT | 4 | `wma540_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4467 | 0.6114 | 2.1928 | 0.0071 | 0.2591 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma540_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma540_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
