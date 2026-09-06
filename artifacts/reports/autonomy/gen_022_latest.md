# Autonomy public-indicator hunt gen 022

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T094632Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `mass_cross_up_27` | one_head_filter_pi_star | 90 | 7.4577 | 2.0051 | 0.6778 | 3.0538 | 0.0308 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `mass_high_at_h` | one_head_filter_pi_star | 134 | 10.9640 | 2.0406 | 0.7015 | 3.9143 | 0.0307 | 0.4179 | EBR>35% | RAN |
| ETHUSDT | 4 | `mass_high_at_h` | one_head_filter_pi_star | 113 | 9.2458 | 1.7834 | 0.6814 | 2.8919 | 0.0266 | 0.4425 | EBR>35% | RAN |
| ETHUSDT | 4 | `mass_cross_up_27` | one_head_filter_pi_star | 68 | 5.7121 | 1.5669 | 0.6471 | 1.7341 | 0.0234 | 0.3676 | EBR>35% | RAN |
| BTCUSDT | 8 | `mass_high_at_h` | one_head_filter_pi_star | 23 | 1.9572 | 1.2025 | 0.4783 | 0.3453 | 0.0228 | 0.1304 | TPM<MIN | RAN |
| BTCUSDT | 4 | `mass_high_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 1.1480 | 0.4286 | 0.2584 | 0.0192 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `mass_high_at_h` | one_head_filter_pi_star | 95 | 7.7724 | 1.9868 | 0.6947 | 2.8167 | 0.0149 | 0.4947 | EBR>35% | RAN |
| SOLUSDT | 4 | `mass_cross_up_27` | one_head_filter_pi_star | 30 | 2.5254 | 1.8650 | 0.6667 | 1.4867 | 0.0143 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 8 | `mass_high_at_h` | one_head_filter_pi_star | 99 | 8.0996 | 1.5920 | 0.6566 | 2.0028 | 0.0112 | 0.4747 | EBR>35% | RAN |
| SOLUSDT | 8 | `mass_cross_up_27` | one_head_filter_pi_star | 117 | 9.6170 | 1.5161 | 0.6667 | 1.8806 | 0.0103 | 0.3932 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `mass_low_at_h` | one_head_filter_pi_star | 217 | 17.7418 | 1.5826 | 0.6129 | 2.8910 | 0.0083 | 0.2258 | ok | RAN |
| ETHUSDT | 4 | `mass_low_at_h` | one_head_filter_pi_star | 215 | 17.6802 | 1.2715 | 0.5953 | 1.4880 | 0.0080 | 0.2279 | ok | RAN |
| SOLUSDT | 8 | `mass_low_at_h` | one_head_filter_pi_star | 182 | 14.9779 | 1.5192 | 0.6209 | 2.3903 | 0.0073 | 0.2198 | ok | RAN |
| ETHUSDT | 8 | `mass_low_at_h` | one_head_filter_pi_star | 159 | 13.0773 | 1.1258 | 0.5660 | 0.6440 | 0.0035 | 0.2075 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `mass_cross_up_27` | one_head_filter_pi_star | 14 | 1.1914 | 0.8128 | 0.3571 | -0.3126 | -0.0252 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `mass_cross_up_27` | one_head_filter_pi_star | 16 | 1.3616 | 0.6096 | 0.3125 | -0.7519 | -0.0468 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 4 | `mass_cross_down_27` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `mass_cross_down_27` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `mass_cross_down_27` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `mass_cross_down_27` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `mass_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `mass_cross_down_27` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mass_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mass_cross_down_27` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
