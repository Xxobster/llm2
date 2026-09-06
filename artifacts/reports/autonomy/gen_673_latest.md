# Autonomy public-indicator hunt gen 673

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T051636Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1240_below_at_h` | one_head_filter_pi_star | 251 | 20.5044 | 1.7426 | 0.6534 | 3.7237 | 0.0177 | 0.3386 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1240_below_at_h` | one_head_filter_pi_star | 260 | 21.2396 | 1.7049 | 0.6462 | 3.6769 | 0.0170 | 0.3346 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1240_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 1.6398 | 0.6276 | 3.5570 | 0.0105 | 0.3103 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1240_below_at_h` | one_head_filter_pi_star | 282 | 23.0594 | 1.5311 | 0.6170 | 3.0464 | 0.0090 | 0.2943 | ok | RAN |
| ETHUSDT | 8 | `ema1240_above_at_h` | one_head_filter_pi_star | 81 | 6.6848 | 1.2012 | 0.5926 | 0.7447 | 0.0086 | 0.2346 | ok | RAN |
| SOLUSDT | 8 | `ema1240_above_at_h` | one_head_filter_pi_star | 107 | 8.7248 | 1.5912 | 0.6542 | 1.9826 | 0.0084 | 0.2710 | ok | RAN |
| SOLUSDT | 4 | `ema1240_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.5020 | 0.6147 | 1.7732 | 0.0077 | 0.2844 | ok | RAN |
| ETHUSDT | 4 | `ema1240_above_at_h` | one_head_filter_pi_star | 87 | 7.1800 | 1.1175 | 0.5632 | 0.4573 | 0.0047 | 0.2184 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1240_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1240_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5000 | 0.3529 | -1.0638 | -0.0557 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
