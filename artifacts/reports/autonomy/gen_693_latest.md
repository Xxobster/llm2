# Autonomy public-indicator hunt gen 693

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T064031Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret121_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.9523 | 0.6949 | 4.1486 | 0.0236 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret121_neg_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.6758 | 0.6553 | 3.4501 | 0.0178 | 0.3544 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret121_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2009 | 0.6872 | 4.2574 | 0.0163 | 0.3799 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret121_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.0918 | 0.6721 | 4.0406 | 0.0155 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret121_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.4498 | 0.6325 | 2.0229 | 0.0139 | 0.2410 | ok | RAN |
| ETHUSDT | 4 | `ret121_pos_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.3675 | 0.6237 | 1.7823 | 0.0119 | 0.2258 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret121_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.4337 | 0.6047 | 2.0622 | 0.0069 | 0.2616 | ok | RAN |
| SOLUSDT | 4 | `ret121_pos_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3846 | 0.6010 | 1.9429 | 0.0062 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret121_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret121_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret121_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret121_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret121_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret121_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret121_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret121_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret121_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret121_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret121_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret121_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret121_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret121_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret121_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret121_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
