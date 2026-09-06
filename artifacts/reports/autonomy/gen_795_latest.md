# Autonomy public-indicator hunt gen 795

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T151327Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma502_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1873 | 0.7128 | 4.8421 | 0.0253 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma502_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.1015 | 0.6949 | 4.5480 | 0.0253 | 0.3898 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma502_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.8793 | 0.6720 | 3.5803 | 0.0132 | 0.3441 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma502_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8013 | 0.6649 | 3.4199 | 0.0124 | 0.3455 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma502_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.2876 | 0.6071 | 1.3636 | 0.0099 | 0.2202 | ok | RAN |
| SOLUSDT | 4 | `sma502_above_at_h` | one_head_filter_pi_star | 188 | 15.4169 | 1.5178 | 0.6064 | 2.4463 | 0.0082 | 0.2926 | ok | RAN |
| SOLUSDT | 8 | `sma502_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.5049 | 0.6144 | 2.1379 | 0.0078 | 0.2876 | ok | RAN |
| ETHUSDT | 4 | `sma502_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2007 | 0.5944 | 1.0101 | 0.0073 | 0.2278 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma502_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma502_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma502_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma502_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
