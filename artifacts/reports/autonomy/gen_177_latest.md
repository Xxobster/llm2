# Autonomy public-indicator hunt gen 177

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T210527Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema15_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8214 | 0.6786 | 3.9995 | 0.0210 | 0.3705 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema15_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema15_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1827 | 0.6975 | 4.0366 | 0.0179 | 0.4198 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema15_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema15_cross_down` | one_head_filter_pi_star | 26 | 2.2014 | 3.0123 | 0.6923 | 2.1120 | 0.0176 | 0.1154 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema15_cross_up` | one_head_filter_pi_star | 45 | 3.7029 | 1.2729 | 0.5556 | 0.6902 | 0.0109 | 0.2222 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema15_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2386 | 0.5951 | 1.0952 | 0.0076 | 0.2025 | ok | RAN |
| ETHUSDT | 8 | `ema15_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2025 | 0.5938 | 0.9322 | 0.0066 | 0.2062 | ok | RAN |
| SOLUSDT | 8 | `ema15_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3678 | 0.5915 | 1.9926 | 0.0055 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `ema15_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3690 | 0.5953 | 2.0075 | 0.0054 | 0.2465 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema15_cross_down` | one_head_filter_pi_star | 37 | 3.4166 | 0.9479 | 0.5135 | -0.1379 | -0.0016 | 0.1081 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema15_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema15_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema15_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema15_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
