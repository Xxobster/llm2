# Autonomy public-indicator hunt gen 884

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T234956Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema865_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8351 | 0.6682 | 3.7454 | 0.0202 | 0.3779 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema865_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8249 | 0.6652 | 3.7709 | 0.0195 | 0.3616 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema865_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.8526 | 0.6480 | 4.0416 | 0.0128 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema865_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7379 | 0.6414 | 3.6891 | 0.0115 | 0.3028 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema865_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.2765 | 0.6000 | 1.2559 | 0.0102 | 0.2258 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema865_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.6205 | 0.6364 | 2.2359 | 0.0094 | 0.3306 | ok | RAN |
| SOLUSDT | 8 | `ema865_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.5726 | 0.6239 | 2.1120 | 0.0088 | 0.3248 | ok | RAN |
| ETHUSDT | 4 | `ema865_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.0583 | 0.5781 | 0.2772 | 0.0024 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema865_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema865_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema865_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema865_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema865_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema865_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema865_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema865_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema865_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema865_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema865_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema865_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema865_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema865_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema865_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema865_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
