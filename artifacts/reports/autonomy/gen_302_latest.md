# Autonomy public-indicator hunt gen 302

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T053844Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma90_cross_up` | one_head_filter_pi_star | 15 | 1.2744 | 6.4631 | 0.7333 | 2.4876 | 0.0519 | 0.2667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma90_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8582 | 0.6832 | 4.1144 | 0.0214 | 0.3713 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma90_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8033 | 0.6842 | 3.8447 | 0.0211 | 0.3828 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma90_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1813 | 0.6909 | 4.1120 | 0.0179 | 0.4121 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma90_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1408 | 0.6852 | 3.9443 | 0.0174 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma90_cross_down` | one_head_filter_pi_star | 24 | 2.3223 | 1.7761 | 0.6250 | 1.2716 | 0.0156 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma90_cross_up` | one_head_filter_pi_star | 24 | 2.0889 | 1.3053 | 0.5833 | 0.5711 | 0.0115 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma90_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.3062 | 0.6108 | 1.3929 | 0.0091 | 0.2096 | ok | RAN |
| ETHUSDT | 4 | `wma90_above_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.2987 | 0.6059 | 1.3685 | 0.0090 | 0.2176 | ok | RAN |
| SOLUSDT | 8 | `wma90_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3636 | 0.5981 | 1.9201 | 0.0053 | 0.2570 | ok | RAN |
| SOLUSDT | 4 | `wma90_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3346 | 0.5962 | 1.8255 | 0.0049 | 0.2488 | ok | RAN |
| ETHUSDT | 8 | `wma90_cross_down` | one_head_filter_pi_star | 36 | 2.9832 | 1.0627 | 0.5556 | 0.1563 | 0.0028 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma90_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma90_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma90_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma90_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
