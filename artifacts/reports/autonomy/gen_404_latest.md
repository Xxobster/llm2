# Autonomy public-indicator hunt gen 404

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T030920Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema265_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0558 | 0.6943 | 4.5373 | 0.0242 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema265_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9921 | 0.6959 | 4.3847 | 0.0229 | 0.3763 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema265_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.2569 | 0.6978 | 4.5313 | 0.0174 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema265_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 2.0255 | 0.6667 | 4.2030 | 0.0151 | 0.3582 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema265_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2630 | 0.6150 | 1.3581 | 0.0089 | 0.2246 | ok | RAN |
| SOLUSDT | 4 | `ema265_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4754 | 0.6022 | 2.2262 | 0.0075 | 0.2762 | ok | RAN |
| ETHUSDT | 4 | `ema265_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2066 | 0.6022 | 1.1028 | 0.0072 | 0.2151 | ok | RAN |
| SOLUSDT | 8 | `ema265_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3856 | 0.5947 | 1.9496 | 0.0060 | 0.2632 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema265_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema265_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema265_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema265_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
