# Autonomy public-indicator hunt gen 684

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T060241Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema615_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.9047 | 0.6698 | 4.2740 | 0.0215 | 0.3726 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema615_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.7963 | 0.6683 | 3.6129 | 0.0192 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema615_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.8567 | 0.6651 | 3.8138 | 0.0130 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema615_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 1.8010 | 0.6560 | 3.6426 | 0.0125 | 0.3119 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema615_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5611 | 0.6187 | 2.2112 | 0.0087 | 0.3165 | ok | RAN |
| SOLUSDT | 8 | `ema615_above_at_h` | one_head_filter_pi_star | 131 | 10.8878 | 1.5375 | 0.6183 | 2.1698 | 0.0084 | 0.3053 | ok | RAN |
| ETHUSDT | 4 | `ema615_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.1605 | 0.6026 | 0.7657 | 0.0059 | 0.1987 | ok | RAN |
| ETHUSDT | 8 | `ema615_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 1.1247 | 0.5939 | 0.6149 | 0.0045 | 0.1939 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema615_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema615_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema615_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema615_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
