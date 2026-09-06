# Autonomy public-indicator hunt gen 585

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T233259Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1020_below_at_h` | one_head_filter_pi_star | 11 | 1.3908 | 1.7770 | 0.6364 | 1.0291 | 0.0814 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1020_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.8549 | 0.6638 | 4.0081 | 0.0198 | 0.3405 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1020_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 1.6448 | 0.6488 | 3.4386 | 0.0165 | 0.3388 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1020_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.7959 | 0.6448 | 3.9727 | 0.0120 | 0.3050 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1020_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 1.6656 | 0.6360 | 3.5110 | 0.0107 | 0.2989 | ok | RAN |
| SOLUSDT | 4 | `ema1020_above_at_h` | one_head_filter_pi_star | 114 | 9.3699 | 1.7316 | 0.6667 | 2.4819 | 0.0103 | 0.3070 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema1020_above_at_h` | one_head_filter_pi_star | 135 | 11.1413 | 1.2443 | 0.6000 | 1.0668 | 0.0095 | 0.2296 | ok | RAN |
| SOLUSDT | 8 | `ema1020_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.5833 | 0.6339 | 2.0735 | 0.0090 | 0.2857 | ok | RAN |
| ETHUSDT | 8 | `ema1020_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 1.1853 | 0.5854 | 0.7998 | 0.0070 | 0.2195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1020_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1020_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
