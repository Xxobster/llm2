# Autonomy public-indicator hunt gen 521

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T191913Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema860_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 2.0494 | 0.6905 | 4.2793 | 0.0229 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema860_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.9023 | 0.6728 | 4.0203 | 0.0213 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema860_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7686 | 0.6494 | 3.7912 | 0.0120 | 0.3068 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema860_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.7331 | 0.6429 | 3.5052 | 0.0115 | 0.3067 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema860_above_at_h` | one_head_filter_pi_star | 118 | 9.8073 | 1.6590 | 0.6441 | 2.3749 | 0.0096 | 0.3305 | ok | RAN |
| SOLUSDT | 8 | `ema860_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.6573 | 0.6288 | 2.3629 | 0.0094 | 0.3106 | ok | RAN |
| ETHUSDT | 4 | `ema860_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.2397 | 0.5933 | 1.1238 | 0.0086 | 0.2133 | ok | RAN |
| ETHUSDT | 8 | `ema860_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.1238 | 0.5804 | 0.5899 | 0.0049 | 0.2098 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema860_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema860_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
