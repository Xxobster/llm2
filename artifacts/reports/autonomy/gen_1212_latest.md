# Autonomy public-indicator hunt gen 1212

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T113050Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema930_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 1.7712 | 0.6529 | 3.8100 | 0.0186 | 0.3388 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema930_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.6823 | 0.6524 | 3.3384 | 0.0171 | 0.3519 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema930_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.7808 | 0.6490 | 3.8016 | 0.0123 | 0.2980 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema930_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.6913 | 0.6434 | 3.5460 | 0.0111 | 0.3101 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema930_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 1.2832 | 0.6074 | 1.2501 | 0.0105 | 0.2296 | ok | RAN |
| SOLUSDT | 8 | `ema930_above_at_h` | one_head_filter_pi_star | 112 | 9.2060 | 1.6861 | 0.6518 | 2.3285 | 0.0100 | 0.3214 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema930_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.5272 | 0.6148 | 1.9777 | 0.0082 | 0.3197 | ok | RAN |
| ETHUSDT | 4 | `ema930_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.1770 | 0.6000 | 0.8344 | 0.0068 | 0.2214 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema930_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema930_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema930_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema930_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema930_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema930_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema930_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema930_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema930_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema930_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema930_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema930_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema930_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema930_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema930_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema930_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
