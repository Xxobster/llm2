# Autonomy public-indicator hunt gen 1467

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T234347Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma669_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0852 | 0.6865 | 4.4145 | 0.0246 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma669_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9996 | 0.6740 | 4.1073 | 0.0231 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma669_below_at_h` | one_head_filter_pi_star | 195 | 15.8636 | 1.7350 | 0.6615 | 3.2571 | 0.0117 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma669_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 1.7114 | 0.6569 | 3.2447 | 0.0113 | 0.3088 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma669_above_at_h` | one_head_filter_pi_star | 114 | 9.3486 | 1.6599 | 0.6316 | 2.3551 | 0.0097 | 0.3246 | ok | RAN |
| ETHUSDT | 8 | `sma669_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2479 | 0.6049 | 1.2372 | 0.0089 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `sma669_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5298 | 0.6081 | 2.1847 | 0.0085 | 0.3108 | ok | RAN |
| ETHUSDT | 4 | `sma669_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.2135 | 0.6118 | 1.0298 | 0.0077 | 0.2039 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma669_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0402 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma669_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma669_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma669_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma669_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma669_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma669_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma669_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma669_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma669_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma669_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma669_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma669_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma669_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma669_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma669_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
