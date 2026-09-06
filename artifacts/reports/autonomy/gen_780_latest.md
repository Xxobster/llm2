# Autonomy public-indicator hunt gen 780

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T134524Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema735_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 2.1217 | 0.6878 | 4.4762 | 0.0243 | 0.3902 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema735_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.9022 | 0.6759 | 4.0446 | 0.0216 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema735_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.8689 | 0.6498 | 3.9750 | 0.0127 | 0.3038 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema735_below_at_h` | one_head_filter_pi_star | 227 | 18.5620 | 1.8350 | 0.6652 | 3.8042 | 0.0124 | 0.3260 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema735_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.5871 | 0.6214 | 2.2977 | 0.0090 | 0.3143 | ok | RAN |
| SOLUSDT | 8 | `ema735_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.5913 | 0.6131 | 2.2628 | 0.0088 | 0.3139 | ok | RAN |
| ETHUSDT | 8 | `ema735_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2086 | 0.5833 | 0.9639 | 0.0076 | 0.2051 | ok | RAN |
| ETHUSDT | 4 | `ema735_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1170 | 0.5928 | 0.5994 | 0.0044 | 0.2156 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema735_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6154 | 0.3500 | -0.7982 | -0.0391 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema735_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema735_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema735_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
