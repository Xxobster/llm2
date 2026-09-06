# Autonomy public-indicator hunt gen 1513

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T035907Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema3340_below_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 1.6060 | 0.6467 | 3.7406 | 0.0162 | 0.2991 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema3340_below_at_h` | one_head_filter_pi_star | 355 | 28.8799 | 1.5768 | 0.6423 | 3.6555 | 0.0155 | 0.2986 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema3340_below_at_h` | one_head_filter_pi_star | 295 | 24.1224 | 1.8713 | 0.6508 | 4.4570 | 0.0128 | 0.3356 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3340_above_at_h` | one_head_filter_pi_star | 89 | 7.3983 | 1.9274 | 0.6742 | 2.4965 | 0.0123 | 0.2472 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3340_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 1.7950 | 0.6421 | 4.2215 | 0.0122 | 0.3244 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema3340_above_at_h` | one_head_filter_pi_star | 77 | 6.3154 | 1.6263 | 0.6234 | 1.6569 | 0.0089 | 0.2208 | ok | RAN |
| ETHUSDT | 8 | `ema3340_above_at_h` | one_head_filter_pi_star | 32 | 3.7603 | 1.1560 | 0.5312 | 0.3917 | 0.0067 | 0.2812 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
