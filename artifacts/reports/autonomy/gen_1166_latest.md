# Autonomy public-indicator hunt gen 1166

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T065616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma635_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0614 | 0.6984 | 4.5237 | 0.0241 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma635_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9056 | 0.6754 | 4.1415 | 0.0220 | 0.3613 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma635_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8968 | 0.6650 | 3.8236 | 0.0137 | 0.3550 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma635_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.9433 | 0.6740 | 3.7274 | 0.0137 | 0.3536 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma635_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.5311 | 0.6077 | 2.4344 | 0.0085 | 0.2707 | ok | RAN |
| SOLUSDT | 4 | `wma635_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5248 | 0.6054 | 2.4107 | 0.0084 | 0.2757 | ok | RAN |
| ETHUSDT | 8 | `wma635_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2315 | 0.6034 | 1.1783 | 0.0083 | 0.2241 | ok | RAN |
| ETHUSDT | 4 | `wma635_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.1883 | 0.5955 | 0.9934 | 0.0071 | 0.2191 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma635_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma635_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma635_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma635_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
