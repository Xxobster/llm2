# Autonomy public-indicator hunt gen 352

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T152847Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma480_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0483 | 0.6968 | 4.4639 | 0.0242 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma480_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0660 | 0.6957 | 4.4810 | 0.0240 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma480_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0025 | 0.6774 | 4.0125 | 0.0145 | 0.3548 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma480_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.9874 | 0.6837 | 4.0306 | 0.0142 | 0.3520 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma480_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.7460 | 0.6368 | 3.1778 | 0.0110 | 0.2684 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma480_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.2383 | 0.6026 | 1.1312 | 0.0084 | 0.2119 | ok | RAN |
| ETHUSDT | 4 | `sma480_above_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2387 | 0.5906 | 1.1962 | 0.0083 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `sma480_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.5037 | 0.5930 | 2.2633 | 0.0081 | 0.2791 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma480_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0409 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
