# Autonomy public-indicator hunt gen 1521

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T044342Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema3360_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 1.5902 | 0.6416 | 3.6360 | 0.0157 | 0.2977 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema3360_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.5473 | 0.6390 | 3.5356 | 0.0149 | 0.3009 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3360_above_at_h` | one_head_filter_pi_star | 76 | 6.2476 | 2.1759 | 0.6842 | 2.5877 | 0.0142 | 0.2500 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3360_below_at_h` | one_head_filter_pi_star | 295 | 24.1224 | 1.8818 | 0.6508 | 4.5169 | 0.0132 | 0.3220 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3360_above_at_h` | one_head_filter_pi_star | 96 | 7.8738 | 1.9928 | 0.6771 | 2.6284 | 0.0122 | 0.2188 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3360_below_at_h` | one_head_filter_pi_star | 288 | 23.5500 | 1.7837 | 0.6424 | 4.0585 | 0.0121 | 0.3299 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3360_above_at_h` | one_head_filter_pi_star | 34 | 3.9953 | 0.8992 | 0.5000 | -0.3014 | -0.0050 | 0.2647 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
