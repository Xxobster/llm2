# Autonomy public-indicator hunt gen 761

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T113856Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1460_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1460_below_at_h` | one_head_filter_pi_star | 285 | 23.2819 | 1.7596 | 0.6561 | 4.0353 | 0.0182 | 0.3228 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1460_below_at_h` | one_head_filter_pi_star | 291 | 23.7720 | 1.7257 | 0.6564 | 3.8249 | 0.0177 | 0.3196 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema1460_above_at_h` | one_head_filter_pi_star | 66 | 5.6161 | 1.3272 | 0.6061 | 0.9795 | 0.0128 | 0.2727 | ok | RAN |
| SOLUSDT | 8 | `ema1460_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.7578 | 0.6453 | 3.8226 | 0.0122 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1460_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.6803 | 0.6316 | 3.7337 | 0.0110 | 0.3228 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1460_above_at_h` | one_head_filter_pi_star | 44 | 3.8196 | 1.2614 | 0.6136 | 0.6740 | 0.0103 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1460_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.5783 | 0.6415 | 1.8977 | 0.0085 | 0.2736 | ok | RAN |
| SOLUSDT | 8 | `ema1460_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.4893 | 0.6286 | 1.7277 | 0.0075 | 0.2571 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1460_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1460_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
