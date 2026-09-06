# Autonomy public-indicator hunt gen 821

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T173920Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret153_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0490 | 0.6910 | 4.4807 | 0.0243 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret153_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9995 | 0.7005 | 4.5033 | 0.0234 | 0.3797 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret153_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1897 | 0.6818 | 4.2755 | 0.0164 | 0.3693 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret153_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 2.0319 | 0.6684 | 4.1006 | 0.0149 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret153_pos_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2575 | 0.6062 | 1.3291 | 0.0088 | 0.2383 | ok | RAN |
| SOLUSDT | 8 | `ret153_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4231 | 0.6011 | 2.0268 | 0.0066 | 0.2660 | ok | RAN |
| ETHUSDT | 4 | `ret153_pos_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.1684 | 0.5938 | 0.8775 | 0.0060 | 0.2188 | ok | RAN |
| SOLUSDT | 4 | `ret153_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.3620 | 0.5946 | 1.7432 | 0.0059 | 0.2703 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret153_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret153_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret153_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret153_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret153_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret153_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret153_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret153_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret153_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret153_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret153_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret153_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret153_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret153_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret153_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret153_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
