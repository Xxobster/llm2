# Autonomy public-indicator hunt gen 745

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T102608Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1420_below_at_h` | one_head_filter_pi_star | 292 | 23.8537 | 1.6911 | 0.6507 | 3.7796 | 0.0172 | 0.3219 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1420_below_at_h` | one_head_filter_pi_star | 305 | 24.9157 | 1.6651 | 0.6492 | 3.7572 | 0.0168 | 0.3180 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1420_above_at_h` | one_head_filter_pi_star | 68 | 5.6119 | 1.4090 | 0.6176 | 1.2126 | 0.0158 | 0.2647 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1420_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 1.7226 | 0.6343 | 3.7442 | 0.0118 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1420_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.7399 | 0.6416 | 3.8921 | 0.0118 | 0.3226 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1420_above_at_h` | one_head_filter_pi_star | 66 | 5.6161 | 1.2837 | 0.6061 | 0.8693 | 0.0111 | 0.2727 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1420_above_at_h` | one_head_filter_pi_star | 102 | 8.3171 | 1.7066 | 0.6863 | 2.2022 | 0.0098 | 0.2549 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1420_above_at_h` | one_head_filter_pi_star | 100 | 8.1540 | 1.4151 | 0.6300 | 1.4486 | 0.0062 | 0.2700 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1420_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1420_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
