# Autonomy public-indicator hunt gen 657

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T041235Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1200_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1200_below_at_h` | one_head_filter_pi_star | 260 | 21.2396 | 1.6743 | 0.6462 | 3.5808 | 0.0168 | 0.3346 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1200_below_at_h` | one_head_filter_pi_star | 260 | 21.2396 | 1.6807 | 0.6462 | 3.5576 | 0.0167 | 0.3308 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1200_above_at_h` | one_head_filter_pi_star | 98 | 7.9910 | 1.8213 | 0.6633 | 2.4946 | 0.0112 | 0.2857 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1200_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 1.6290 | 0.6269 | 3.3934 | 0.0107 | 0.3134 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1200_above_at_h` | one_head_filter_pi_star | 102 | 8.3836 | 1.6481 | 0.6471 | 2.1824 | 0.0098 | 0.2941 | ok | RAN |
| SOLUSDT | 4 | `ema1200_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.5523 | 0.6217 | 3.0501 | 0.0093 | 0.3071 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1200_above_at_h` | one_head_filter_pi_star | 89 | 7.3450 | 1.0256 | 0.5506 | 0.1068 | 0.0011 | 0.2135 | ok | RAN |
| ETHUSDT | 4 | `ema1200_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 1.0032 | 0.5536 | 0.0141 | 0.0001 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `ema1200_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1200_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
