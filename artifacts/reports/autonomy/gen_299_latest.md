# Autonomy public-indicator hunt gen 299

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T052502Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma98_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9498 | 0.6869 | 4.4500 | 0.0231 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma98_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9183 | 0.6950 | 4.2502 | 0.0229 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma98_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2729 | 0.6923 | 4.3641 | 0.0187 | 0.3964 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma98_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2383 | 0.6864 | 4.2689 | 0.0179 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma98_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.4107 | 0.6236 | 1.8356 | 0.0122 | 0.2247 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma98_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.2962 | 0.6077 | 1.4189 | 0.0092 | 0.2320 | ok | RAN |
| SOLUSDT | 8 | `sma98_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.2840 | 0.5885 | 1.5239 | 0.0043 | 0.2536 | ok | RAN |
| SOLUSDT | 4 | `sma98_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2619 | 0.5833 | 1.4246 | 0.0041 | 0.2549 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma98_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma98_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma98_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma98_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma98_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma98_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma98_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma98_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma98_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma98_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma98_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma98_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma98_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma98_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma98_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma98_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
