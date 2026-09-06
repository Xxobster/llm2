# Autonomy public-indicator hunt gen 545

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T205546Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema920_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.9290 | 0.6681 | 4.0414 | 0.0207 | 0.3496 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema920_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.7275 | 0.6525 | 3.5562 | 0.0181 | 0.3432 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema920_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.8408 | 0.6596 | 3.8656 | 0.0125 | 0.3106 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema920_above_at_h` | one_head_filter_pi_star | 128 | 10.6385 | 1.7868 | 0.6484 | 2.8137 | 0.0115 | 0.3047 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema920_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.7193 | 0.6441 | 3.5195 | 0.0114 | 0.3008 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema920_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.2839 | 0.5933 | 1.3006 | 0.0105 | 0.2267 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema920_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.6310 | 0.6364 | 2.2696 | 0.0094 | 0.3140 | ok | RAN |
| ETHUSDT | 4 | `ema920_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.1741 | 0.5971 | 0.8249 | 0.0065 | 0.2302 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema920_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema920_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
