# Autonomy public-indicator hunt gen 1206

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T105716Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma660_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1257 | 0.7005 | 4.6485 | 0.0247 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma660_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9350 | 0.7010 | 4.1389 | 0.0218 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma660_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.9085 | 0.6769 | 3.7552 | 0.0135 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma660_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8401 | 0.6649 | 3.5391 | 0.0125 | 0.3508 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma660_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2546 | 0.6056 | 1.3080 | 0.0091 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `wma660_above_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 1.5168 | 0.6243 | 2.3610 | 0.0081 | 0.2762 | ok | RAN |
| SOLUSDT | 8 | `wma660_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4382 | 0.6066 | 2.0880 | 0.0073 | 0.2787 | ok | RAN |
| ETHUSDT | 4 | `wma660_above_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.1780 | 0.5882 | 0.9322 | 0.0064 | 0.2059 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma660_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma660_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
