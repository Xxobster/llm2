# Autonomy public-indicator hunt gen 667

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T045223Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma394_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9679 | 0.7010 | 4.3875 | 0.0229 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma394_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9092 | 0.6856 | 4.2441 | 0.0215 | 0.3660 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma394_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0199 | 0.6774 | 4.0836 | 0.0145 | 0.3602 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma394_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.9310 | 0.6582 | 3.8853 | 0.0137 | 0.3622 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma394_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.6870 | 0.6277 | 3.0388 | 0.0104 | 0.2660 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma394_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2880 | 0.6051 | 1.4665 | 0.0099 | 0.2205 | ok | RAN |
| ETHUSDT | 4 | `sma394_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2455 | 0.5926 | 1.2651 | 0.0086 | 0.2275 | ok | RAN |
| SOLUSDT | 4 | `sma394_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4043 | 0.5989 | 1.9673 | 0.0066 | 0.2674 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma394_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma394_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma394_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma394_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma394_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma394_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma394_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma394_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma394_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma394_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma394_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma394_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma394_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma394_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma394_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma394_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
