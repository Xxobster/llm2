# Autonomy public-indicator hunt gen 1161

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T062147Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2460_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0799 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2460_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.5848 | 0.6418 | 3.5969 | 0.0156 | 0.2980 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2460_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 1.5750 | 0.6416 | 3.5328 | 0.0155 | 0.3035 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2460_below_at_h` | one_head_filter_pi_star | 271 | 22.0464 | 1.8982 | 0.6568 | 4.3347 | 0.0131 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2460_below_at_h` | one_head_filter_pi_star | 279 | 22.6972 | 1.8175 | 0.6416 | 4.0836 | 0.0123 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2460_above_at_h` | one_head_filter_pi_star | 104 | 8.6437 | 1.5972 | 0.6346 | 2.0190 | 0.0091 | 0.2692 | ok | RAN |
| SOLUSDT | 4 | `ema2460_above_at_h` | one_head_filter_pi_star | 114 | 9.3699 | 1.5137 | 0.6316 | 1.9022 | 0.0082 | 0.2719 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2460_above_at_h` | one_head_filter_pi_star | 26 | 3.0553 | 0.9546 | 0.5000 | -0.1213 | -0.0023 | 0.2692 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2460_above_at_h` | one_head_filter_pi_star | 12 | 1.4101 | 0.8159 | 0.4167 | -0.3873 | -0.0130 | 0.5000 | EBR>35% | RAN |
| BTCUSDT | 4 | `ema2460_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0284 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2460_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0435 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
