# Autonomy public-indicator hunt gen 1088

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T213338Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2320_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5520 | 0.6366 | 3.4468 | 0.0149 | 0.3063 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2320_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5123 | 0.6334 | 3.3067 | 0.0142 | 0.3079 | ok | RAN |
| ETHUSDT | 4 | `sma2320_above_at_h` | one_head_filter_pi_star | 53 | 4.7943 | 1.3854 | 0.6226 | 1.1264 | 0.0140 | 0.2453 | ok | RAN |
| ETHUSDT | 8 | `sma2320_above_at_h` | one_head_filter_pi_star | 48 | 4.3420 | 1.3396 | 0.5833 | 0.9281 | 0.0134 | 0.2292 | ok | RAN |
| SOLUSDT | 4 | `sma2320_below_at_h` | one_head_filter_pi_star | 303 | 24.6496 | 1.7759 | 0.6403 | 4.1092 | 0.0117 | 0.3267 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2320_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.7296 | 0.6391 | 3.8503 | 0.0114 | 0.3278 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2320_above_at_h` | one_head_filter_pi_star | 55 | 4.5720 | 1.6375 | 0.6364 | 1.5486 | 0.0094 | 0.2909 | ok | RAN |
| SOLUSDT | 4 | `sma2320_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.5702 | 0.6406 | 1.4430 | 0.0085 | 0.2656 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2320_above_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3638 | 0.2727 | -1.8830 | -0.0996 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2320_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
