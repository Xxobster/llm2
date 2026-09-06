# Autonomy public-indicator hunt gen 1076

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T195850Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema910_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 2.1225 | 0.6915 | 4.3562 | 0.0234 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema910_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.7524 | 0.6594 | 3.7699 | 0.0191 | 0.3624 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema910_below_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.7897 | 0.6507 | 3.6827 | 0.0125 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema910_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7185 | 0.6420 | 3.5154 | 0.0115 | 0.3128 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema910_above_at_h` | one_head_filter_pi_star | 125 | 10.3891 | 1.6358 | 0.6400 | 2.3533 | 0.0096 | 0.3280 | ok | RAN |
| SOLUSDT | 8 | `ema910_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.6647 | 0.6308 | 2.4389 | 0.0095 | 0.3077 | ok | RAN |
| ETHUSDT | 8 | `ema910_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.1625 | 0.5940 | 0.7563 | 0.0064 | 0.2256 | ok | RAN |
| ETHUSDT | 4 | `ema910_above_at_h` | one_head_filter_pi_star | 121 | 9.9460 | 1.1474 | 0.5950 | 0.6451 | 0.0060 | 0.2314 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema910_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema910_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema910_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema910_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema910_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema910_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema910_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema910_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema910_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema910_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema910_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema910_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema910_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema910_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema910_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema910_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
