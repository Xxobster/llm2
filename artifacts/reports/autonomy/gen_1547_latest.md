# Autonomy public-indicator hunt gen 1547

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T071232Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma681_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0942 | 0.6927 | 4.3581 | 0.0248 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma681_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0305 | 0.6862 | 4.2811 | 0.0234 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma681_below_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 1.8174 | 0.6667 | 3.5902 | 0.0123 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma681_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.6615 | 0.6552 | 3.0540 | 0.0109 | 0.3202 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma681_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.6312 | 0.6303 | 2.6903 | 0.0098 | 0.3091 | ok | RAN |
| SOLUSDT | 8 | `sma681_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.4432 | 0.6015 | 1.8830 | 0.0074 | 0.3308 | ok | RAN |
| ETHUSDT | 8 | `sma681_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.1871 | 0.6012 | 0.9223 | 0.0068 | 0.2202 | ok | RAN |
| ETHUSDT | 4 | `sma681_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.0810 | 0.5920 | 0.4198 | 0.0030 | 0.2069 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma681_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma681_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma681_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma681_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma681_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma681_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma681_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma681_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma681_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma681_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma681_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma681_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma681_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma681_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma681_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma681_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
