# Autonomy public-indicator hunt gen 926

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T042017Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma485_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9692 | 0.6923 | 4.3718 | 0.0227 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma485_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9591 | 0.6895 | 4.2752 | 0.0227 | 0.3789 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma485_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.0590 | 0.6793 | 4.0984 | 0.0153 | 0.3696 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma485_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.0105 | 0.6755 | 4.0361 | 0.0148 | 0.3617 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma485_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4926 | 0.6062 | 2.3825 | 0.0075 | 0.2591 | ok | RAN |
| ETHUSDT | 4 | `wma485_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2085 | 0.6010 | 1.1300 | 0.0072 | 0.2172 | ok | RAN |
| SOLUSDT | 8 | `wma485_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4224 | 0.5912 | 2.0583 | 0.0067 | 0.2597 | ok | RAN |
| ETHUSDT | 8 | `wma485_above_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.1462 | 0.5980 | 0.8052 | 0.0053 | 0.2111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma485_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma485_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma485_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma485_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
