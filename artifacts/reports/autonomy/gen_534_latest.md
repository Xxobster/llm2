# Autonomy public-indicator hunt gen 534

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T201224Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma240_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0120 | 0.7005 | 4.4910 | 0.0236 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma240_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9726 | 0.6902 | 4.3557 | 0.0224 | 0.3696 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma240_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2477 | 0.7006 | 4.3763 | 0.0178 | 0.3785 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma240_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1193 | 0.6867 | 3.9321 | 0.0163 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma240_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2609 | 0.6071 | 1.3198 | 0.0089 | 0.2347 | ok | RAN |
| ETHUSDT | 8 | `wma240_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2382 | 0.5979 | 1.1621 | 0.0083 | 0.2328 | ok | RAN |
| SOLUSDT | 8 | `wma240_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3263 | 0.5874 | 1.7196 | 0.0051 | 0.2670 | ok | RAN |
| SOLUSDT | 4 | `wma240_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2652 | 0.5829 | 1.4161 | 0.0042 | 0.2613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma240_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma240_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
