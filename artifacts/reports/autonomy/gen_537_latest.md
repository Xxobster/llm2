# Autonomy public-indicator hunt gen 537

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T202418Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema900_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema900_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9489 | 0.6786 | 4.0037 | 0.0211 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema900_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7296 | 0.6606 | 3.5197 | 0.0181 | 0.3529 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema900_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.8649 | 0.6559 | 4.0793 | 0.0130 | 0.3117 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema900_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7527 | 0.6457 | 3.7393 | 0.0117 | 0.3150 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema900_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.2818 | 0.6071 | 1.3002 | 0.0101 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema900_above_at_h` | one_head_filter_pi_star | 122 | 10.1398 | 1.6135 | 0.6311 | 2.2645 | 0.0092 | 0.3279 | ok | RAN |
| SOLUSDT | 8 | `ema900_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.5789 | 0.6271 | 2.1077 | 0.0087 | 0.3136 | ok | RAN |
| ETHUSDT | 8 | `ema900_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1747 | 0.5813 | 0.8818 | 0.0068 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema900_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema900_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0542 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
