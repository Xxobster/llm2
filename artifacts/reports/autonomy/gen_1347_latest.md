# Autonomy public-indicator hunt gen 1347

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T004340Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma651_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0480 | 0.6788 | 4.4024 | 0.0240 | 0.3834 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma651_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.8757 | 0.6685 | 3.8543 | 0.0216 | 0.3876 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma651_below_at_h` | one_head_filter_pi_star | 207 | 16.8399 | 1.7728 | 0.6667 | 3.3709 | 0.0120 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma651_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7482 | 0.6585 | 3.3473 | 0.0116 | 0.3220 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma651_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.6654 | 0.6276 | 2.6033 | 0.0103 | 0.3241 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma651_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.6022 | 0.6129 | 2.4261 | 0.0094 | 0.3161 | ok | RAN |
| ETHUSDT | 4 | `sma651_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.2003 | 0.5987 | 0.9816 | 0.0076 | 0.2229 | ok | RAN |
| ETHUSDT | 8 | `sma651_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1934 | 0.6000 | 0.9557 | 0.0072 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma651_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma651_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5735 | 0.2632 | -0.9106 | -0.0438 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma651_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma651_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma651_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma651_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma651_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma651_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma651_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma651_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma651_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma651_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma651_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma651_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma651_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma651_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
