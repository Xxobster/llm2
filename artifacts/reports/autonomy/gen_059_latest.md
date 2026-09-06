# Autonomy public-indicator hunt gen 059

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T132723Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `rngpos_high_at_h` | one_head_filter_pi_star | 23 | 2.0806 | 6.7613 | 0.8261 | 3.0740 | 0.0592 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 4 | `rngpos_low_at_h` | one_head_filter_pi_star | 22 | 3.0912 | 2.4277 | 0.7273 | 2.6489 | 0.0439 | 0.4091 | EBR>35% | RAN |
| SOLUSDT | 4 | `rngpos_cross_up_08` | one_head_filter_pi_star | 18 | 1.6691 | 4.3615 | 0.7778 | 2.2945 | 0.0300 | 0.0556 | TPM<MIN | RAN |
| SOLUSDT | 4 | `rngpos_low_at_h` | one_head_filter_pi_star | 11 | 1.8541 | 4.0471 | 0.8182 | 2.9768 | 0.0274 | 0.5455 | EBR>35% | RAN |
| SOLUSDT | 8 | `rngpos_high_at_h` | one_head_filter_pi_star | 13 | 1.3983 | 2.1407 | 0.6923 | 1.5821 | 0.0211 | 0.5385 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `rngpos_cross_down_02` | one_head_filter_pi_star | 70 | 5.7240 | 1.7630 | 0.6143 | 1.9949 | 0.0138 | 0.3286 | GATE_CAND | RAN |
| ETHUSDT | 8 | `rngpos_cross_down_02` | one_head_filter_pi_star | 64 | 5.4761 | 1.3187 | 0.6406 | 0.9710 | 0.0118 | 0.2656 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `rngpos_cross_up_08` | one_head_filter_pi_star | 65 | 5.3431 | 1.6055 | 0.6154 | 1.7296 | 0.0086 | 0.1692 | ok | RAN |
| ETHUSDT | 4 | `rngpos_cross_up_08` | one_head_filter_pi_star | 14 | 1.4650 | 1.1363 | 0.5000 | 0.2241 | 0.0059 | 0.4286 | EBR>35% | RAN |
| SOLUSDT | 4 | `rngpos_high_at_h` | one_head_filter_pi_star | 24 | 2.1477 | 1.0614 | 0.5417 | 0.1618 | 0.0015 | 0.4167 | EBR>35% | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rngpos_cross_up_08` | one_head_filter_pi_star | 27 | 2.8253 | 1.0125 | 0.4815 | 0.0326 | 0.0006 | 0.2593 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rngpos_cross_down_02` | one_head_filter_pi_star | 21 | 1.8797 | 0.8464 | 0.5238 | -0.3318 | -0.0087 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rngpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `rngpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `rngpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `rngpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rngpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rngpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rngpos_cross_up_08` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rngpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rngpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rngpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rngpos_cross_up_08` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rngpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
