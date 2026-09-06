# Autonomy public-indicator hunt gen 1497

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T023123Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema3300_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0833 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3300_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.6560 | 0.6476 | 3.9038 | 0.0172 | 0.3066 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema3300_below_at_h` | one_head_filter_pi_star | 356 | 28.9613 | 1.5527 | 0.6404 | 3.5919 | 0.0152 | 0.2978 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3300_below_at_h` | one_head_filter_pi_star | 286 | 23.3865 | 1.8592 | 0.6538 | 4.3384 | 0.0129 | 0.3392 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3300_above_at_h` | one_head_filter_pi_star | 88 | 7.2341 | 2.0192 | 0.6932 | 2.5390 | 0.0126 | 0.2500 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3300_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 1.8378 | 0.6486 | 4.2862 | 0.0125 | 0.3311 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3300_above_at_h` | one_head_filter_pi_star | 99 | 8.1370 | 1.9158 | 0.6768 | 2.5961 | 0.0114 | 0.2222 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
