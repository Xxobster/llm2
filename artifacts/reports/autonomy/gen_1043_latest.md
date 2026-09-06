# Autonomy public-indicator hunt gen 1043

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T154725Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma603_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.1615 | 0.6959 | 4.4695 | 0.0255 | 0.4211 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma603_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.0843 | 0.6950 | 4.6698 | 0.0244 | 0.3650 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma603_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8776 | 0.6700 | 3.7968 | 0.0127 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma603_below_at_h` | one_head_filter_pi_star | 198 | 16.1077 | 1.8245 | 0.6717 | 3.6570 | 0.0123 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma603_above_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.6033 | 0.6218 | 2.4404 | 0.0095 | 0.3141 | ok | RAN |
| SOLUSDT | 8 | `sma603_above_at_h` | one_head_filter_pi_star | 154 | 12.5572 | 1.5128 | 0.6039 | 2.1628 | 0.0083 | 0.3052 | ok | RAN |
| ETHUSDT | 8 | `sma603_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2012 | 0.5965 | 1.0332 | 0.0072 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `sma603_above_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2022 | 0.5965 | 1.0232 | 0.0072 | 0.2047 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma603_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma603_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma603_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma603_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma603_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma603_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma603_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma603_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma603_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma603_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma603_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma603_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma603_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma603_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma603_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma603_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
