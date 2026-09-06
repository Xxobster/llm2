# Autonomy public-indicator hunt gen 274

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T033834Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret128_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9564 | 0.6845 | 4.2048 | 0.0234 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret128_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9064 | 0.6757 | 4.1231 | 0.0223 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret128_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1862 | 0.6902 | 4.3706 | 0.0164 | 0.3696 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret128_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.0862 | 0.6648 | 3.9846 | 0.0148 | 0.3575 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret128_pos_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.3264 | 0.6133 | 1.5859 | 0.0108 | 0.2320 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret128_pos_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2650 | 0.6141 | 1.3666 | 0.0095 | 0.2283 | ok | RAN |
| SOLUSDT | 8 | `ret128_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3962 | 0.6099 | 1.9504 | 0.0063 | 0.2473 | ok | RAN |
| SOLUSDT | 4 | `ret128_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3869 | 0.5970 | 1.9543 | 0.0063 | 0.2687 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret128_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret128_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret128_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret128_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
