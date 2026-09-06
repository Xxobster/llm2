# Autonomy public-indicator hunt gen 726

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T090315Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma360_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0483 | 0.6989 | 4.4864 | 0.0242 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma360_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8687 | 0.6839 | 4.0228 | 0.0216 | 0.3834 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma360_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1425 | 0.6886 | 3.9770 | 0.0161 | 0.3713 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma360_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.0433 | 0.6750 | 3.6982 | 0.0154 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma360_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2754 | 0.6051 | 1.4408 | 0.0093 | 0.2256 | ok | RAN |
| ETHUSDT | 4 | `wma360_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2287 | 0.5934 | 1.1772 | 0.0079 | 0.2198 | ok | RAN |
| SOLUSDT | 8 | `wma360_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3345 | 0.5911 | 1.7619 | 0.0053 | 0.2562 | ok | RAN |
| SOLUSDT | 4 | `wma360_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3166 | 0.5874 | 1.6861 | 0.0050 | 0.2621 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
