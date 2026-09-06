# Autonomy public-indicator hunt gen 136

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T182500Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma80_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9086 | 0.6907 | 4.1808 | 0.0223 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma80_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8695 | 0.6950 | 4.1086 | 0.0220 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma80_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.3031 | 0.6946 | 4.4094 | 0.0189 | 0.4012 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma80_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1777 | 0.6894 | 4.0495 | 0.0178 | 0.4037 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma80_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.3460 | 0.6124 | 1.5883 | 0.0102 | 0.2191 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma80_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2365 | 0.6000 | 1.1868 | 0.0076 | 0.2324 | ok | RAN |
| SOLUSDT | 8 | `sma80_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3317 | 0.5962 | 1.7645 | 0.0049 | 0.2582 | ok | RAN |
| SOLUSDT | 4 | `sma80_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3170 | 0.5907 | 1.7059 | 0.0048 | 0.2512 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma80_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma80_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `sma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `sma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma80_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma80_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
