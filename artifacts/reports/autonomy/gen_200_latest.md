# Autonomy public-indicator hunt gen 200

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T223528Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma95_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9186 | 0.6881 | 4.1713 | 0.0229 | 0.3614 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma95_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8627 | 0.6863 | 4.1663 | 0.0219 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma95_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2815 | 0.6901 | 4.3968 | 0.0186 | 0.3977 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma95_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2200 | 0.6928 | 4.2082 | 0.0178 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma95_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.3734 | 0.6127 | 1.6794 | 0.0112 | 0.2254 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma95_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.3002 | 0.6044 | 1.4451 | 0.0094 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `sma95_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3317 | 0.5962 | 1.7607 | 0.0050 | 0.2582 | ok | RAN |
| SOLUSDT | 4 | `sma95_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3016 | 0.5933 | 1.6039 | 0.0046 | 0.2584 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma95_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma95_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma95_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma95_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
