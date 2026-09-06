# Autonomy public-indicator hunt gen 1462

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T231144Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma406_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9687 | 0.6961 | 4.2591 | 0.0228 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma406_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8896 | 0.6907 | 4.1869 | 0.0222 | 0.3918 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma406_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1335 | 0.6860 | 4.1662 | 0.0164 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma406_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1535 | 0.6893 | 4.1869 | 0.0161 | 0.3672 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma406_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2386 | 0.5947 | 1.2343 | 0.0082 | 0.2211 | ok | RAN |
| ETHUSDT | 4 | `wma406_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2075 | 0.5895 | 1.0910 | 0.0073 | 0.2211 | ok | RAN |
| SOLUSDT | 8 | `wma406_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4358 | 0.6105 | 2.1379 | 0.0068 | 0.2579 | ok | RAN |
| SOLUSDT | 4 | `wma406_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2926 | 0.5879 | 1.5511 | 0.0047 | 0.2613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma406_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma406_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma406_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma406_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
