# Autonomy public-indicator hunt gen 740

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T100505Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema685_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.9909 | 0.6814 | 4.2136 | 0.0225 | 0.3775 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema685_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8871 | 0.6683 | 3.9832 | 0.0210 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema685_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.7900 | 0.6635 | 3.5535 | 0.0123 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema685_below_at_h` | one_head_filter_pi_star | 219 | 17.9078 | 1.7881 | 0.6530 | 3.5854 | 0.0119 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema685_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.6139 | 0.6204 | 2.4195 | 0.0091 | 0.3139 | ok | RAN |
| SOLUSDT | 4 | `ema685_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.5304 | 0.6290 | 1.9982 | 0.0082 | 0.3226 | ok | RAN |
| ETHUSDT | 4 | `ema685_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.1700 | 0.5949 | 0.8367 | 0.0062 | 0.2025 | ok | RAN |
| ETHUSDT | 8 | `ema685_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.1419 | 0.5871 | 0.6930 | 0.0053 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema685_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema685_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema685_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema685_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
