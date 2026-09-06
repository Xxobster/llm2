# Autonomy public-indicator hunt gen 641

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T030830Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1160_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1160_below_at_h` | one_head_filter_pi_star | 253 | 20.6678 | 1.7485 | 0.6522 | 3.6951 | 0.0181 | 0.3399 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1160_below_at_h` | one_head_filter_pi_star | 264 | 21.5664 | 1.7187 | 0.6515 | 3.7194 | 0.0180 | 0.3295 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1160_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.5982 | 0.6217 | 3.2721 | 0.0101 | 0.3071 | ok | RAN |
| SOLUSDT | 4 | `ema1160_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.6040 | 0.6327 | 3.3448 | 0.0100 | 0.3091 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1160_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.6026 | 0.6396 | 2.0992 | 0.0089 | 0.2973 | ok | RAN |
| SOLUSDT | 8 | `ema1160_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.4549 | 0.6250 | 1.6688 | 0.0072 | 0.2768 | ok | RAN |
| ETHUSDT | 4 | `ema1160_above_at_h` | one_head_filter_pi_star | 101 | 8.3354 | 1.1801 | 0.5842 | 0.7055 | 0.0068 | 0.2079 | ok | RAN |
| ETHUSDT | 8 | `ema1160_above_at_h` | one_head_filter_pi_star | 87 | 7.1800 | 1.0766 | 0.5632 | 0.3035 | 0.0032 | 0.2184 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1160_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1160_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
