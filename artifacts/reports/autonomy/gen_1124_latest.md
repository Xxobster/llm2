# Autonomy public-indicator hunt gen 1124

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T015251Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema917_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema917_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.8383 | 0.6695 | 4.1178 | 0.0203 | 0.3473 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema917_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 1.8008 | 0.6580 | 3.7376 | 0.0192 | 0.3420 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema917_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.8927 | 0.6584 | 4.1766 | 0.0134 | 0.3128 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema917_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.7784 | 0.6468 | 3.6913 | 0.0120 | 0.3021 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema917_above_at_h` | one_head_filter_pi_star | 123 | 10.2229 | 1.5892 | 0.6341 | 2.2055 | 0.0092 | 0.3171 | ok | RAN |
| ETHUSDT | 8 | `ema917_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 1.2367 | 0.5985 | 1.0651 | 0.0090 | 0.2263 | ok | RAN |
| SOLUSDT | 8 | `ema917_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.5664 | 0.6250 | 2.1399 | 0.0087 | 0.3125 | ok | RAN |
| ETHUSDT | 4 | `ema917_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.1622 | 0.5797 | 0.7646 | 0.0062 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema917_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema917_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0590 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema917_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema917_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema917_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema917_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema917_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema917_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema917_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema917_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema917_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema917_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema917_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema917_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema917_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
