# Autonomy public-indicator hunt gen 387

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T232156Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma166_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8982 | 0.6839 | 4.1818 | 0.0223 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma166_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7296 | 0.6701 | 3.5934 | 0.0186 | 0.3557 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma166_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2689 | 0.6977 | 4.3512 | 0.0175 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma166_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1682 | 0.6901 | 4.0937 | 0.0171 | 0.3801 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma166_above_at_h` | one_head_filter_pi_star | 197 | 16.2567 | 1.3593 | 0.6193 | 1.7622 | 0.0116 | 0.2335 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma166_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2681 | 0.6056 | 1.3102 | 0.0090 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `sma166_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3551 | 0.5950 | 1.8396 | 0.0056 | 0.2600 | ok | RAN |
| SOLUSDT | 8 | `sma166_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3107 | 0.5854 | 1.6605 | 0.0050 | 0.2634 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma166_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma166_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma166_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma166_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma166_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma166_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma166_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma166_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma166_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma166_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma166_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma166_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma166_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma166_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma166_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma166_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
