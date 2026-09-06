# Autonomy public-indicator hunt gen 1478

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T004519Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma408_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0055 | 0.6911 | 4.4450 | 0.0233 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma408_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9449 | 0.6939 | 4.2835 | 0.0219 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma408_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2770 | 0.6949 | 4.4388 | 0.0176 | 0.3842 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma408_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2102 | 0.6970 | 4.1461 | 0.0168 | 0.3818 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma408_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2678 | 0.6053 | 1.3756 | 0.0091 | 0.2263 | ok | RAN |
| ETHUSDT | 8 | `wma408_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2460 | 0.6064 | 1.2918 | 0.0085 | 0.2234 | ok | RAN |
| SOLUSDT | 8 | `wma408_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.4250 | 0.6030 | 2.1378 | 0.0066 | 0.2513 | ok | RAN |
| SOLUSDT | 4 | `wma408_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3585 | 0.5990 | 1.8677 | 0.0058 | 0.2574 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma408_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma408_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma408_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma408_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma408_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma408_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma408_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma408_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma408_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma408_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma408_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma408_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma408_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma408_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma408_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma408_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
