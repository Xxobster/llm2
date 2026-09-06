# Autonomy public-indicator hunt gen 1395

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T051359Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma658_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9525 | 0.6755 | 4.1808 | 0.0222 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma658_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8011 | 0.6650 | 3.8011 | 0.0199 | 0.3596 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma658_below_at_h` | one_head_filter_pi_star | 198 | 16.1077 | 1.9044 | 0.6818 | 3.7622 | 0.0130 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma658_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.6981 | 0.6550 | 3.2047 | 0.0111 | 0.3100 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma658_above_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.5938 | 0.6197 | 2.3687 | 0.0092 | 0.3099 | ok | RAN |
| SOLUSDT | 4 | `sma658_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.4940 | 0.5942 | 1.9717 | 0.0079 | 0.3261 | ok | RAN |
| ETHUSDT | 4 | `sma658_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.2253 | 0.6159 | 1.0785 | 0.0079 | 0.2252 | ok | RAN |
| ETHUSDT | 8 | `sma658_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1148 | 0.5901 | 0.5893 | 0.0044 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma658_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma658_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma658_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma658_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma658_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma658_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma658_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma658_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma658_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma658_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma658_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma658_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma658_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma658_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma658_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma658_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
