# Autonomy public-indicator hunt gen 288

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T043801Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma320_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9371 | 0.6878 | 4.2819 | 0.0232 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma320_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8676 | 0.6823 | 4.1127 | 0.0221 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma320_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1390 | 0.6848 | 4.2297 | 0.0161 | 0.3696 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma320_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.0074 | 0.6765 | 3.7877 | 0.0153 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma320_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.5064 | 0.6146 | 2.3382 | 0.0075 | 0.2656 | ok | RAN |
| ETHUSDT | 8 | `sma320_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1983 | 0.5916 | 1.0676 | 0.0068 | 0.2094 | ok | RAN |
| ETHUSDT | 4 | `sma320_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.1775 | 0.5806 | 0.9431 | 0.0064 | 0.2204 | ok | RAN |
| SOLUSDT | 4 | `sma320_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3484 | 0.5895 | 1.7491 | 0.0058 | 0.2684 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma320_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma320_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
