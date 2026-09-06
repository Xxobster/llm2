# Autonomy public-indicator hunt gen 597

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T002101Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret97_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.7980 | 0.6585 | 3.9143 | 0.0206 | 0.3659 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret97_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7251 | 0.6566 | 3.5562 | 0.0187 | 0.3586 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret97_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2255 | 0.6780 | 4.3118 | 0.0170 | 0.3729 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret97_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.0962 | 0.6667 | 3.9560 | 0.0158 | 0.3563 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret97_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.3407 | 0.6307 | 1.6625 | 0.0114 | 0.2273 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret97_pos_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2813 | 0.6162 | 1.3688 | 0.0094 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `ret97_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4050 | 0.6000 | 2.0426 | 0.0064 | 0.2684 | ok | RAN |
| SOLUSDT | 4 | `ret97_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3283 | 0.5990 | 1.7131 | 0.0053 | 0.2552 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret97_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret97_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret97_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret97_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret97_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret97_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret97_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret97_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret97_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret97_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret97_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret97_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret97_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret97_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret97_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret97_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
