# Autonomy public-indicator hunt gen 812

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T164938Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema775_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0037 | 0.6782 | 4.1591 | 0.0226 | 0.3861 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema775_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8675 | 0.6667 | 3.8510 | 0.0203 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema775_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.8553 | 0.6623 | 3.9006 | 0.0127 | 0.3160 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema775_below_at_h` | one_head_filter_pi_star | 227 | 18.5620 | 1.7497 | 0.6520 | 3.4580 | 0.0119 | 0.3260 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema775_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.7120 | 0.6541 | 2.5753 | 0.0103 | 0.3308 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema775_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.6822 | 0.6364 | 2.4909 | 0.0098 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema775_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.2465 | 0.5986 | 1.0809 | 0.0090 | 0.2042 | ok | RAN |
| ETHUSDT | 4 | `ema775_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.1590 | 0.5839 | 0.7580 | 0.0057 | 0.2148 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema775_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0408 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema775_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema775_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema775_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
