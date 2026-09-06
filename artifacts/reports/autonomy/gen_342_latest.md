# Autonomy public-indicator hunt gen 342

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T134429Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma120_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8535 | 0.6816 | 4.1463 | 0.0216 | 0.3632 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma120_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8259 | 0.6800 | 3.9411 | 0.0213 | 0.3600 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma120_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2494 | 0.6928 | 4.2637 | 0.0185 | 0.4096 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma120_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2464 | 0.6928 | 4.2377 | 0.0183 | 0.4096 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma120_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.3082 | 0.6105 | 1.3932 | 0.0096 | 0.2209 | ok | RAN |
| ETHUSDT | 4 | `wma120_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2686 | 0.6056 | 1.2843 | 0.0085 | 0.2333 | ok | RAN |
| SOLUSDT | 8 | `wma120_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3210 | 0.5915 | 1.7123 | 0.0048 | 0.2535 | ok | RAN |
| SOLUSDT | 4 | `wma120_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.2805 | 0.5877 | 1.5384 | 0.0042 | 0.2464 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma120_cross_up` | one_head_filter_pi_star | 17 | 1.7496 | 0.5490 | 0.4118 | -1.1703 | -0.0206 | 0.1765 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma120_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma120_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
