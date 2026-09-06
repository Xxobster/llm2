# Autonomy public-indicator hunt gen 1024

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T133553Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma2160_above_at_h` | one_head_filter_pi_star | 44 | 3.6576 | 2.5607 | 0.7273 | 2.3757 | 0.0170 | 0.3182 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma2160_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.6324 | 0.6448 | 3.7959 | 0.0167 | 0.3164 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2160_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5928 | 0.6399 | 3.6357 | 0.0160 | 0.3065 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2160_above_at_h` | one_head_filter_pi_star | 45 | 4.0706 | 1.3879 | 0.6000 | 0.9357 | 0.0156 | 0.2444 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2160_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 1.7782 | 0.6399 | 4.2083 | 0.0115 | 0.3151 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2160_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.7772 | 0.6875 | 1.8688 | 0.0109 | 0.2812 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2160_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.6970 | 0.6327 | 3.9005 | 0.0106 | 0.3210 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma2160_above_at_h` | one_head_filter_pi_star | 56 | 4.9037 | 1.2423 | 0.5714 | 0.6770 | 0.0091 | 0.2321 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2160_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2160_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
