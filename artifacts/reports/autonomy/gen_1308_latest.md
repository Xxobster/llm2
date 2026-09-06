# Autonomy public-indicator hunt gen 1308

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T210755Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema944_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 2.1145 | 0.6827 | 4.5452 | 0.0227 | 0.3654 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema944_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.8651 | 0.6711 | 3.9714 | 0.0203 | 0.3556 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema944_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7015 | 0.6457 | 3.5712 | 0.0114 | 0.3110 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema944_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.6854 | 0.6350 | 3.5638 | 0.0111 | 0.3042 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema944_above_at_h` | one_head_filter_pi_star | 130 | 10.6849 | 1.7262 | 0.6462 | 2.6233 | 0.0108 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema944_above_at_h` | one_head_filter_pi_star | 126 | 10.2741 | 1.7422 | 0.6587 | 2.5499 | 0.0106 | 0.3095 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema944_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 1.1624 | 0.5868 | 0.7013 | 0.0062 | 0.2149 | ok | RAN |
| ETHUSDT | 4 | `ema944_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.1383 | 0.5870 | 0.6505 | 0.0052 | 0.1957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema944_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema944_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema944_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema944_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema944_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema944_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema944_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema944_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema944_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema944_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema944_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema944_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema944_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema944_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema944_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema944_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
