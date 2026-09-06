# Autonomy public-indicator hunt gen 297

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T051637Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema300_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9221 | 0.6853 | 4.2628 | 0.0222 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema300_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9262 | 0.6832 | 4.1855 | 0.0222 | 0.3713 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema300_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 2.0405 | 0.6804 | 4.1728 | 0.0153 | 0.3608 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema300_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9145 | 0.6632 | 3.7862 | 0.0144 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema300_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.3168 | 0.6183 | 1.5753 | 0.0104 | 0.2097 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema300_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.5134 | 0.6124 | 2.3547 | 0.0078 | 0.2809 | ok | RAN |
| SOLUSDT | 8 | `ema300_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4625 | 0.6053 | 2.2705 | 0.0070 | 0.2632 | ok | RAN |
| ETHUSDT | 4 | `ema300_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.1718 | 0.5934 | 0.9207 | 0.0062 | 0.2088 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema300_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema300_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
