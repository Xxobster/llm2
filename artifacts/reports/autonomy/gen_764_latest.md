# Autonomy public-indicator hunt gen 764

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T120319Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema715_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.1213 | 0.6919 | 4.5779 | 0.0242 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema715_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9130 | 0.6771 | 3.7980 | 0.0216 | 0.3854 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema715_below_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 1.8574 | 0.6711 | 3.8836 | 0.0129 | 0.3244 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema715_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.7511 | 0.6573 | 3.3875 | 0.0115 | 0.3239 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema715_above_at_h` | one_head_filter_pi_star | 154 | 12.7083 | 1.2576 | 0.6104 | 1.2094 | 0.0089 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `ema715_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.5429 | 0.6176 | 2.1219 | 0.0086 | 0.3235 | ok | RAN |
| SOLUSDT | 8 | `ema715_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.5235 | 0.6357 | 2.0664 | 0.0082 | 0.3411 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema715_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.0300 | 0.5705 | 0.1508 | 0.0012 | 0.2081 | ok | RAN |
| BTCUSDT | 8 | `ema715_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema715_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema715_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema715_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
