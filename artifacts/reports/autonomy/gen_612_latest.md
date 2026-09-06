# Autonomy public-indicator hunt gen 612

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T011744Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema525_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.2214 | 0.7083 | 4.8525 | 0.0259 | 0.3958 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema525_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9810 | 0.6939 | 4.2964 | 0.0228 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema525_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.9182 | 0.6701 | 3.8622 | 0.0138 | 0.3452 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema525_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.8618 | 0.6535 | 3.6838 | 0.0127 | 0.3416 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema525_above_at_h` | one_head_filter_pi_star | 158 | 12.8834 | 1.5601 | 0.6013 | 2.3188 | 0.0086 | 0.2911 | ok | RAN |
| SOLUSDT | 8 | `ema525_above_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.5451 | 0.6074 | 2.3494 | 0.0085 | 0.2883 | ok | RAN |
| ETHUSDT | 4 | `ema525_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.2287 | 0.6040 | 1.0636 | 0.0081 | 0.2013 | ok | RAN |
| ETHUSDT | 8 | `ema525_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1291 | 0.5882 | 0.6634 | 0.0049 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema525_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema525_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema525_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema525_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
