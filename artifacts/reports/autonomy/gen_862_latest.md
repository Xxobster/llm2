# Autonomy public-indicator hunt gen 862

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T213605Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma445_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0462 | 0.7037 | 4.4814 | 0.0246 | 0.3915 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma445_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0585 | 0.7016 | 4.6056 | 0.0243 | 0.3874 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma445_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2537 | 0.6932 | 4.4389 | 0.0172 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma445_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2390 | 0.6966 | 4.4536 | 0.0168 | 0.3820 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma445_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2620 | 0.6000 | 1.3612 | 0.0088 | 0.2211 | ok | RAN |
| ETHUSDT | 8 | `wma445_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2144 | 0.6022 | 1.1267 | 0.0075 | 0.2204 | ok | RAN |
| SOLUSDT | 8 | `wma445_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.4267 | 0.6000 | 2.0396 | 0.0067 | 0.2611 | ok | RAN |
| SOLUSDT | 4 | `wma445_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3702 | 0.6010 | 1.9383 | 0.0058 | 0.2644 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma445_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma445_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma445_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma445_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
