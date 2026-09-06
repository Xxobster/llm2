# Autonomy public-indicator hunt gen 1228

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T125842Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema932_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.9736 | 0.6740 | 4.3156 | 0.0217 | 0.3436 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema932_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.8604 | 0.6711 | 3.8900 | 0.0201 | 0.3600 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema932_above_at_h` | one_head_filter_pi_star | 134 | 11.0588 | 1.3714 | 0.6045 | 1.6314 | 0.0135 | 0.2388 | ok | RAN |
| SOLUSDT | 8 | `ema932_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.7534 | 0.6481 | 3.6045 | 0.0118 | 0.3090 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema932_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.6853 | 0.6387 | 3.4156 | 0.0110 | 0.3025 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema932_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.6525 | 0.6336 | 2.4108 | 0.0098 | 0.3206 | ok | RAN |
| SOLUSDT | 4 | `ema932_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.5657 | 0.6328 | 2.1590 | 0.0088 | 0.3125 | ok | RAN |
| ETHUSDT | 4 | `ema932_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.1402 | 0.5827 | 0.6375 | 0.0055 | 0.2362 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema932_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0314 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema932_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0521 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema932_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema932_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema932_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema932_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema932_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema932_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema932_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema932_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema932_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema932_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema932_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema932_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema932_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema932_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
