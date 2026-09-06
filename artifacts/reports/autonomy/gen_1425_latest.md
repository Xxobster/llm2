# Autonomy public-indicator hunt gen 1425

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T115712Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema3120_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3120_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.5892 | 0.6447 | 3.6569 | 0.0158 | 0.3009 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema3120_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 1.5613 | 0.6400 | 3.5530 | 0.0152 | 0.2971 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3120_below_at_h` | one_head_filter_pi_star | 293 | 23.9589 | 1.8796 | 0.6553 | 4.4800 | 0.0128 | 0.3276 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3120_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 1.8329 | 0.6503 | 4.3780 | 0.0126 | 0.3235 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3120_above_at_h` | one_head_filter_pi_star | 81 | 6.6590 | 1.8206 | 0.6914 | 2.1175 | 0.0114 | 0.2469 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3120_above_at_h` | one_head_filter_pi_star | 104 | 8.5285 | 1.7195 | 0.6635 | 2.1759 | 0.0100 | 0.2212 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3120_above_at_h` | one_head_filter_pi_star | 31 | 9.1469 | 0.8459 | 0.4839 | -0.6880 | -0.0069 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `ema3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
