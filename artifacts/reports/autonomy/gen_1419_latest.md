# Autonomy public-indicator hunt gen 1419

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T084557Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma662_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.1120 | 0.6927 | 4.4792 | 0.0247 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma662_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9652 | 0.6821 | 4.2248 | 0.0225 | 0.3641 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma662_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8115 | 0.6700 | 3.4949 | 0.0124 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma662_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8050 | 0.6684 | 3.4643 | 0.0123 | 0.3316 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma662_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.3278 | 0.6242 | 1.4859 | 0.0113 | 0.2081 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma662_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.5281 | 0.6063 | 2.0184 | 0.0083 | 0.3228 | ok | RAN |
| SOLUSDT | 8 | `sma662_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.4954 | 0.6107 | 1.9284 | 0.0080 | 0.3206 | ok | RAN |
| ETHUSDT | 8 | `sma662_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1990 | 0.6087 | 0.9854 | 0.0073 | 0.2298 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma662_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma662_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma662_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma662_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma662_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma662_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma662_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma662_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma662_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma662_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma662_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma662_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma662_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma662_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma662_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma662_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
