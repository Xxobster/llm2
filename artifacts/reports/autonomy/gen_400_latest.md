# Autonomy public-indicator hunt gen 400

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T021640Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma600_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0804 | 0.6927 | 4.5198 | 0.0243 | 0.3854 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma600_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9605 | 0.6788 | 4.1991 | 0.0224 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma600_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7911 | 0.6649 | 3.4831 | 0.0124 | 0.3299 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma600_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.7967 | 0.6667 | 3.4856 | 0.0119 | 0.3182 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma600_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.6180 | 0.6333 | 2.4829 | 0.0093 | 0.3267 | ok | RAN |
| SOLUSDT | 4 | `sma600_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5782 | 0.6164 | 2.2916 | 0.0091 | 0.3288 | ok | RAN |
| ETHUSDT | 8 | `sma600_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2038 | 0.6047 | 1.0458 | 0.0073 | 0.2326 | ok | RAN |
| ETHUSDT | 4 | `sma600_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1756 | 0.5990 | 0.9479 | 0.0064 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma600_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma600_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
