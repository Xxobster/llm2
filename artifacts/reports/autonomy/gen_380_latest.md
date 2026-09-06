# Autonomy public-indicator hunt gen 380

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T214421Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema235_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9948 | 0.6931 | 4.3730 | 0.0235 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema235_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0102 | 0.6990 | 4.4526 | 0.0235 | 0.3827 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema235_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2543 | 0.6994 | 4.3876 | 0.0176 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema235_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1529 | 0.6848 | 4.2736 | 0.0162 | 0.3696 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema235_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2424 | 0.6033 | 1.2604 | 0.0084 | 0.2174 | ok | RAN |
| ETHUSDT | 8 | `ema235_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2250 | 0.6075 | 1.1443 | 0.0076 | 0.2258 | ok | RAN |
| SOLUSDT | 4 | `ema235_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4486 | 0.6162 | 2.1356 | 0.0068 | 0.2703 | ok | RAN |
| SOLUSDT | 8 | `ema235_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3611 | 0.5949 | 1.8518 | 0.0056 | 0.2564 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema235_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema235_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema235_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema235_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
