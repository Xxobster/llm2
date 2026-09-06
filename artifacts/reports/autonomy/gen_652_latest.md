# Autonomy public-indicator hunt gen 652

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T035216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema575_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0645 | 0.6911 | 4.4630 | 0.0242 | 0.3979 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema575_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.9274 | 0.6746 | 4.1042 | 0.0222 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema575_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.9354 | 0.6698 | 4.0198 | 0.0136 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema575_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.7868 | 0.6522 | 3.4777 | 0.0118 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema575_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.6337 | 0.6277 | 2.4429 | 0.0095 | 0.3212 | ok | RAN |
| SOLUSDT | 4 | `ema575_above_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.6036 | 0.6118 | 2.5852 | 0.0091 | 0.3000 | ok | RAN |
| ETHUSDT | 4 | `ema575_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1785 | 0.6025 | 0.8677 | 0.0066 | 0.1863 | ok | RAN |
| ETHUSDT | 8 | `ema575_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1330 | 0.5976 | 0.6486 | 0.0049 | 0.1951 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema575_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema575_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema575_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema575_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
