# Autonomy public-indicator hunt gen 320

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T072245Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma400_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9927 | 0.6915 | 4.3810 | 0.0234 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma400_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9658 | 0.6940 | 4.2683 | 0.0230 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma400_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9547 | 0.6736 | 3.9187 | 0.0140 | 0.3575 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma400_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9269 | 0.6578 | 3.6868 | 0.0137 | 0.3583 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma400_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2704 | 0.6000 | 1.3915 | 0.0091 | 0.2205 | ok | RAN |
| ETHUSDT | 4 | `sma400_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2564 | 0.5979 | 1.3427 | 0.0088 | 0.2268 | ok | RAN |
| SOLUSDT | 8 | `sma400_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5394 | 0.6108 | 2.4676 | 0.0084 | 0.2595 | ok | RAN |
| SOLUSDT | 4 | `sma400_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.4247 | 0.6061 | 2.1110 | 0.0070 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma400_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma400_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
