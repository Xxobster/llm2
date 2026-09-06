# Autonomy public-indicator hunt gen 338

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T124435Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret192_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0952 | 0.7022 | 4.4988 | 0.0245 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret192_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9888 | 0.6973 | 4.4866 | 0.0244 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret192_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1383 | 0.6788 | 4.0218 | 0.0165 | 0.3879 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret192_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.9976 | 0.6667 | 3.7854 | 0.0146 | 0.3729 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret192_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5839 | 0.6324 | 2.6394 | 0.0086 | 0.2811 | ok | RAN |
| SOLUSDT | 4 | `ret192_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.4959 | 0.6141 | 2.3234 | 0.0078 | 0.2772 | ok | RAN |
| ETHUSDT | 8 | `ret192_pos_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.2321 | 0.6011 | 1.2147 | 0.0076 | 0.2234 | ok | RAN |
| ETHUSDT | 4 | `ret192_pos_at_h` | one_head_filter_pi_star | 208 | 17.0973 | 1.1996 | 0.6010 | 1.0689 | 0.0071 | 0.2356 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret192_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret192_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret192_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret192_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
