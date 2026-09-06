# Autonomy public-indicator hunt gen 483

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T164824Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma244_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9713 | 0.6968 | 4.4240 | 0.0235 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma244_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.9886 | 0.6944 | 4.3309 | 0.0233 | 0.3889 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma244_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2564 | 0.6959 | 4.3058 | 0.0174 | 0.3977 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma244_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1702 | 0.6871 | 4.0141 | 0.0169 | 0.3742 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma244_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.2600 | 0.5989 | 1.3071 | 0.0088 | 0.2246 | ok | RAN |
| ETHUSDT | 8 | `sma244_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2117 | 0.5949 | 1.1526 | 0.0073 | 0.2256 | ok | RAN |
| SOLUSDT | 4 | `sma244_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3619 | 0.5941 | 1.8546 | 0.0059 | 0.2673 | ok | RAN |
| SOLUSDT | 8 | `sma244_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3506 | 0.5990 | 1.8303 | 0.0056 | 0.2525 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma244_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma244_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma244_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma244_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma244_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma244_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma244_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma244_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma244_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma244_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma244_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma244_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma244_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma244_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma244_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma244_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
