# Autonomy public-indicator hunt gen 371

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T193020Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma148_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8703 | 0.6842 | 4.0333 | 0.0215 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma148_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8622 | 0.6769 | 4.1640 | 0.0209 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma148_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2447 | 0.6944 | 4.3666 | 0.0173 | 0.3667 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma148_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1113 | 0.6882 | 3.9609 | 0.0161 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma148_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.2518 | 0.6077 | 1.2459 | 0.0084 | 0.2210 | ok | RAN |
| ETHUSDT | 8 | `sma148_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2325 | 0.6064 | 1.1546 | 0.0081 | 0.2287 | ok | RAN |
| SOLUSDT | 8 | `sma148_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3887 | 0.6020 | 1.9700 | 0.0061 | 0.2704 | ok | RAN |
| SOLUSDT | 4 | `sma148_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.2933 | 0.5867 | 1.5403 | 0.0047 | 0.2602 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma148_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma148_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma148_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma148_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma148_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma148_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma148_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma148_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma148_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma148_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma148_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma148_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma148_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma148_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma148_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma148_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
