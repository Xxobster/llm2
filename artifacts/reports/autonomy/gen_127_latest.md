# Autonomy public-indicator hunt gen 127

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T174839Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema100_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0316 | 0.6995 | 4.5438 | 0.0241 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema100_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8598 | 0.6800 | 4.1142 | 0.0211 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema100_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2375 | 0.6905 | 4.2938 | 0.0180 | 0.3929 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema100_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2485 | 0.6954 | 4.3822 | 0.0180 | 0.3851 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema100_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.2619 | 0.6045 | 1.2468 | 0.0083 | 0.2090 | ok | RAN |
| ETHUSDT | 8 | `ema100_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.2118 | 0.5978 | 1.0442 | 0.0069 | 0.2067 | ok | RAN |
| SOLUSDT | 8 | `ema100_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.4107 | 0.6055 | 2.1414 | 0.0061 | 0.2615 | ok | RAN |
| SOLUSDT | 4 | `ema100_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2801 | 0.5854 | 1.5146 | 0.0043 | 0.2537 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
